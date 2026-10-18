#!/usr/bin/env python3
# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""Translate a new language pack from an existing one (docs/new-language.md).

    python3 tools/translate.py prepare TAG --work DIR --game-dir DIR [--oa-tool PATH]
                                         [--template uk] [--references zh-Hans,uk,ko]
    python3 tools/translate.py validate --work DIR CHUNK
    python3 tools/translate.py status --work DIR
    python3 tools/translate.py merge --work DIR [--allow-missing]
    python3 tools/translate.py warmup TAG [--bytes N]

`prepare` reads the template pack's tables, the reference packs' translations
and the English of the missions' names and briefings from the game folder,
and writes the translators' chunks under DIR/in. A translator writes each
chunk's translation to DIR/out/<chunk>.tsv (an id, a tab, the translation)
and each briefing to DIR/out/briefs/<name>. `validate` checks one chunk,
`status` lists every chunk's state, and `merge` writes the pack's tables and
briefings into TAG/, laid out as the template's. `warmup` writes the pack's
warmup.txt from the characters its text uses most.

The new pack's language.yaml must exist before `prepare`: its tag, word and
text needs decide the briefings' folder, the tables' keys and the
characters `validate` allows.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check  # noqa: E402
import oamod_yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
TABLES = ("interface.tdf", "translate.tdf", "units.tdf", "missions.tdf")
PARTS = {"interface.tdf": 5, "translate.tdf": 3, "units.tdf": 1, "missions.tdf": 1}
PREFIX = {"interface.tdf": "I", "translate.tdf": "T", "units.tdf": "U", "missions.tdf": "M"}
CHUNK = {"interface.tdf": "interface", "translate.tdf": "translate", "units.tdf": "units",
         "missions.tdf": "missions"}
BRIEF_PARTS = 5
PRINTF = re.compile(r"%(?:\d+\$)?[-+#0]*\d*(?:\.\d+)?(?:hh|h|ll|l|z)?[diuxXfFeEgGcsp%]")

# The characters every pack may write besides its own script's: Latin with
# its accents (names, keys, ARM and CORE), and the punctuation and signs the
# English itself uses.
COMMON = (
    (0x0020, 0x007E), (0x00A0, 0x024F), (0x02B0, 0x02FF), (0x2000, 0x206F),
    (0x20A0, 0x20CF), (0x2100, 0x214F), (0x2190, 0x21FF), (0x2200, 0x22FF),
    (0x2500, 0x25FF), (0x2600, 0x27BF),
)
# Each script a pack may write, by the tag's language subtag, the letters a
# briefing must hold at least one of, and the letters of a neighbouring
# language written in the same script that this one never uses.
SCRIPTS = {
    "ru": {"allow": ((0x0400, 0x052F),), "letters": ((0x0400, 0x04FF),),
           "forbid": "ІіЇїЄєҐґ"},
    "uk": {"allow": ((0x0400, 0x052F),), "letters": ((0x0400, 0x04FF),),
           "forbid": "ЫыЭэЪъЁё"},
    "ja": {"allow": ((0x3000, 0x30FF), (0x31F0, 0x31FF), (0x3400, 0x4DBF), (0x4E00, 0x9FFF),
                     (0xF900, 0xFAFF), (0xFF00, 0xFFEF)),
           "letters": ((0x3040, 0x30FF), (0x4E00, 0x9FFF))},
    "ko": {"allow": ((0x1100, 0x11FF), (0x3130, 0x318F), (0xAC00, 0xD7AF)),
           "letters": ((0xAC00, 0xD7AF),)},
    "zh": {"allow": ((0x3000, 0x303F), (0x3400, 0x4DBF), (0x4E00, 0x9FFF), (0xFF00, 0xFFEF)),
           "letters": ((0x4E00, 0x9FFF),)},
}


def within(code: int, ranges) -> bool:
    return any(low <= code <= high for low, high in ranges)


class Pack:
    """A pack's manifest values, as the tables and briefings need them."""

    def __init__(self, tag: str) -> None:
        self.tag = tag
        self.folder = ROOT / tag
        manifest = self.folder / "language.yaml"
        if not manifest.is_file():
            raise SystemExit(f"{manifest} does not exist: write the pack's language.yaml first")
        values = oamod_yaml.loads(manifest.read_bytes())
        self.word = values["word"]
        self.english_name = values["english-name"]
        self.modern = check.modern_fonts(values)
        self.script = SCRIPTS.get(tag.split("-")[0].lower())

    @property
    def briefs(self) -> Path:
        return self.folder / "files" / "camps" / f"briefs-{self.word}"


def value_line(table: str, pack: Pack) -> re.Pattern[str]:
    """The line of a table that holds a translated value, in the pack's shape."""
    if table == "interface.tdf":
        return re.compile(r"^\t" + re.escape(pack.tag) + r"=(.*);$")
    if table == "translate.tdf":
        return re.compile(r"^\t" + re.escape(pack.word) + r"=(.*);$")
    if table == "units.tdf":
        return re.compile(r"^\t(name|description)=(.*);$")
    return re.compile(r"^\tmissionname=(.*);$")


def section_key(table: str, section: str) -> str:
    return section if table in ("interface.tdf", "translate.tdf") else section.lower()


def reference_values(table: str, pack: Pack) -> dict:
    """A reference pack's translation of each section, by its section key."""
    path = pack.folder / table
    if not path.is_file():
        return {}
    key = {"interface.tdf": pack.tag.lower(), "translate.tdf": pack.word.lower()}.get(table)
    values = {}
    for name, fields, _children in check.parse_tdf(path.read_text(encoding="utf-8")):
        if table == "units.tdf":
            values[section_key(table, name)] = fields
        else:
            values[section_key(table, name)] = fields.get(key or "missionname", "")
    return values


def slots(table: str, template: Pack, references: list[Pack]) -> list[dict]:
    """Each value line of the template's table, with its English and the references."""
    lines = (template.folder / table).read_text(encoding="utf-8").split("\n")
    own = {section_key(table, s[0]): s[1]
           for s in check.parse_tdf((template.folder / table).read_text(encoding="utf-8"))}
    refs = [(p, reference_values(table, p)) for p in references]
    pattern = value_line(table, template)
    items = []
    section = None
    heading = ""
    for number, line in enumerate(lines):
        if line.startswith("//") and number > 6:
            heading = line[2:].strip()
            continue
        match = re.match(r"^\[(.*)\]$", line)
        if match:
            section = match.group(1)
            continue
        match = pattern.match(line)
        if not match or section is None:
            continue
        key = section_key(table, section)
        field = None
        if table == "units.tdf":
            field = match.group(1)
            english = own[key].get(field + "-from", "")
        elif table == "missions.tdf":
            english = None
        else:
            english = section
        item = {"line": number, "section": section, "field": field, "en": english,
                "heading": heading, "refs": {}}
        for ref, values in refs:
            value = values.get(key, "")
            if table == "units.tdf":
                value = value.get(field, "") if isinstance(value, dict) else ""
            item["refs"][ref.tag] = value
        items.append(item)
    return items


def balanced(items: list, parts: int, weight) -> list[list]:
    total = sum(weight(i) for i in items) or 1
    chunks, current, acc = [], [], 0
    for item in items:
        current.append(item)
        acc += weight(item)
        if acc >= total * (len(chunks) + 1) / parts and len(chunks) < parts - 1:
            chunks.append(current)
            current = []
    chunks.append(current)
    return [c for c in chunks if c]


def write_chunk(work: Path, name: str, items: list[dict]) -> None:
    lines = []
    last = None
    for item in items:
        if item.get("heading") and item["heading"] != last:
            lines.append(f"## {item['heading']}")
            last = item["heading"]
        lines.append(f"@{item['id']}")
        if item.get("label"):
            lines.append(f"UNIT: {item['label']}")
        lines.append(f"EN: {item['en']}")
        for tag, value in item["refs"].items():
            lines.append(f"{tag.upper()}: {value}")
        lines.append("")
    (work / "in" / f"{name}.txt").write_text("\n".join(lines), encoding="utf-8")
    print(f"{name}: {len(items)} items")


def game_entries(game_dir: Path, tool: Path) -> dict[str, tuple[Path | None, str]]:
    """The campaigns' files the game reads, each from the archive or folder that wins."""
    entries: dict[str, tuple[Path | None, str]] = {}

    def wanted(folded: str) -> bool:
        parts = folded.split("/")
        return (len(parts) == 2 and parts[0] == "camps" and parts[1].endswith(".tdf")) or (
            len(parts) == 3 and parts[:2] == ["camps", "briefs"] and parts[2].endswith(".txt"))

    for archive in check.archives(game_dir):
        listing = subprocess.run([str(tool), "list", str(archive)], capture_output=True,
                                 text=True, errors="replace")
        for line in listing.stdout.splitlines():
            entry = line.split("\t", 1)[0].replace("\\", "/")
            if wanted(entry.lower()):
                entries[entry.lower()] = (archive, entry)
    camps = game_dir / "camps"
    if camps.is_dir():
        for path in camps.rglob("*"):
            entry = path.relative_to(game_dir).as_posix()
            if path.is_file() and wanted(entry.lower()):
                entries[entry.lower()] = (None, str(path))
    return entries


def read_entry(tool: Path, source: tuple[Path | None, str]) -> str:
    archive, entry = source
    if archive is None:
        data = Path(entry).read_bytes()
    else:
        with tempfile.TemporaryDirectory() as scratch:
            output = Path(scratch) / "entry"
            subprocess.run([str(tool), "extract", str(archive), entry, str(output)],
                           check=True, capture_output=True)
            data = output.read_bytes()
    return data.decode("cp1252").replace("\r\n", "\n")


def prepare(args) -> int:
    pack = Pack(args.tag)
    template = Pack(args.template)
    references = [Pack(t) for t in args.references.split(",") if t]
    work = Path(args.work).resolve()
    tool = Path(args.oa_tool or os.environ.get("OA_TOOL", "oa-tool"))
    game_dir = Path(args.game_dir).expanduser()
    for sub in ("in", "out", "out/briefs", "en-briefs"):
        (work / sub).mkdir(parents=True, exist_ok=True)

    entries = game_entries(game_dir, tool)
    names = {}
    for folded, source in sorted(entries.items()):
        if folded.count("/") != 1:
            continue
        for _name, fields, _children in check.parse_tdf(read_entry(tool, source)):
            if "missionfile" in fields and "missionname" in fields:
                campaign = Path(source[1]).stem.strip()
                names.setdefault(fields["missionfile"].lower(), (fields["missionname"], campaign))

    manifest = {}
    for table in TABLES:
        items = slots(table, template, [r for r in references if r.tag != pack.tag])
        for number, item in enumerate(items):
            item["id"] = f"{PREFIX[table]}{number:04d}"
            if table == "units.tdf":
                item["label"] = f"{item['section']} {item['field']}"
                item["heading"] = ""
            if table == "missions.tdf":
                found = names.get(item["section"].lower())
                if found is None:
                    raise SystemExit(f"no campaign names the mission {item['section']}")
                item["en"], item["heading"] = found
                item["label"] = item["section"]
        parts = PARTS[table]
        chunks = balanced(items, parts, lambda i: len(i["en"] or "") + 25)
        for number, chunk in enumerate(chunks, 1):
            name = CHUNK[table] if len(chunks) == 1 else f"{CHUNK[table]}-{number}"
            write_chunk(work, name, chunk)
        manifest[table] = items

    briefs = sorted(p.name for p in template.briefs.iterdir())
    sizes = []
    for name in briefs:
        source = entries.get(f"camps/briefs/{name.lower()}")
        if source is None:
            raise SystemExit(f"the game folder holds no camps/briefs/{name}")
        text = read_entry(tool, source)
        (work / "en-briefs" / name).write_text(text, encoding="utf-8")
        sizes.append((name, len(text)))
    for number, batch in enumerate(balanced(sizes, BRIEF_PARTS, lambda s: s[1]), 1):
        (work / "in" / f"briefs-{number}.list").write_text(
            "\n".join(n for n, _ in batch) + "\n", encoding="utf-8")
        print(f"briefs-{number}: {len(batch)} briefings")

    (work / "in" / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=0), encoding="utf-8")
    (work / "work.json").write_text(json.dumps({
        "tag": pack.tag, "template": template.tag,
        "references": [r.tag for r in references if r.tag != pack.tag],
        "game_dir": str(game_dir),
    }, indent=1) + "\n", encoding="utf-8")
    print(f"prepared {work} for {pack.tag} from {template.tag}")
    return 0


def work_pack(work: Path) -> tuple[dict, Pack]:
    info = json.loads((work / "work.json").read_text(encoding="utf-8"))
    return info, Pack(info["tag"])


def foreign(text: str, pack: Pack) -> list[str]:
    """The characters a pack's text may not hold: another script's, or past its code page."""
    found = []
    for character in text:
        code = ord(character)
        if not pack.modern:
            if not check.code_page_holds(character):
                found.append(character)
            continue
        allowed = COMMON + (pack.script["allow"] if pack.script else ())
        if not within(code, allowed) or (
                pack.script and character in pack.script.get("forbid", "")):
            found.append(character)
    return found


def read_chunk(path: Path) -> collections.OrderedDict:
    items = collections.OrderedDict()
    current = None
    for line in path.read_text(encoding="utf-8").split("\n"):
        if line.startswith("@"):
            current = line[1:].strip()
            items[current] = {}
        elif current and line.startswith("EN: "):
            items[current]["EN"] = line[4:]
    return items


def read_tsv(path: Path, problems: list[str] | None = None) -> dict[str, str]:
    got: dict[str, str] = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        if "\t" not in line:
            if problems is not None:
                problems.append(f"line {number}: no tab: {line[:60]!r}")
            continue
        key, value = line.split("\t", 1)
        key = key.strip()
        if problems is not None and key in got:
            problems.append(f"{key}: given twice")
        got[key] = value
    return got


def check_value(key: str, english: str, value: str, pack: Pack) -> list[str]:
    problems = []
    if not value.strip():
        return [f"{key}: empty"]
    if value != value.strip():
        problems.append(f"{key}: leading or trailing space")
    if ";" in value or "\t" in value:
        problems.append(f"{key}: holds ';' or a tab (a table value ends at ';')")
    if "//" in value:
        problems.append(f"{key}: holds '//' (a table reads the rest of the line as a comment)")
    for problem in check.pattern_problems(english, value):
        problems.append(f"{key}: {problem} (EN {english[:60]!r})")
    if PRINTF.findall(english) != PRINTF.findall(value):
        problems.append(f"{key}: printf conversions not in the English order: "
                        f"{PRINTF.findall(english)} vs {PRINTF.findall(value)}")
    if english.count("|") != value.count("|"):
        problems.append(f"{key}: {english.count('|')} '|' in the English, {value.count('|')} here")
    bad = foreign(value, pack)
    if bad:
        problems.append(f"{key}: characters this pack cannot hold: {''.join(sorted(set(bad)))}")
    return problems


def validate_tsv(work: Path, name: str, pack: Pack) -> tuple[list[str], int]:
    items = read_chunk(work / "in" / f"{name}.txt")
    path = work / "out" / f"{name}.tsv"
    if not path.is_file():
        return [f"{path} does not exist"], len(items)
    problems: list[str] = []
    got = read_tsv(path, problems)
    for key, item in items.items():
        if key not in got:
            problems.append(f"{key}: missing ({item.get('EN', '')[:50]!r})")
            continue
        problems.extend(check_value(key, item.get("EN", ""), got[key], pack))
    for key in got:
        if key not in items:
            problems.append(f"{key}: not an id of this chunk")
    return problems, len(items)


def validate_briefs(work: Path, name: str, pack: Pack) -> tuple[list[str], int]:
    problems = []
    names = [n for n in (work / "in" / f"{name}.list").read_text(encoding="utf-8").split("\n") if n]
    for n in names:
        english = (work / "en-briefs" / n).read_text(encoding="utf-8")
        path = work / "out" / "briefs" / n
        if not path.is_file():
            problems.append(f"{n}: missing")
            continue
        text = path.read_text(encoding="utf-8")
        if "\r" in text:
            problems.append(f"{n}: write LF line ends, not CRLF")
            text = text.replace("\r\n", "\n")
        english_lines = english.rstrip("\n").split("\n")
        lines = text.rstrip("\n").split("\n")
        if len(english_lines) != len(lines):
            problems.append(f"{n}: {len(english_lines)} lines in the English, {len(lines)} here")
        else:
            for number, (a, b) in enumerate(zip(english_lines, lines), 1):
                if (a.strip() == "") != (b.strip() == ""):
                    problems.append(f"{n}: line {number} blank in one and not the other")
        for mark in ("&", "*"):
            if english.count(mark) != text.count(mark):
                problems.append(f"{n}: {english.count(mark)} '{mark}' in the English, "
                                f"{text.count(mark)} here")
        lost = collections.Counter(re.findall(r"\d+", english)) - collections.Counter(
            re.findall(r"\d+", text))
        if lost:
            problems.append(f"{n}: numbers of the English not here: {sorted(lost)}")
        bad = foreign(text.replace("\n", " "), pack)
        if bad:
            problems.append(f"{n}: characters this pack cannot hold: {''.join(sorted(set(bad)))}")
        if pack.script and not any(within(ord(c), pack.script["letters"]) for c in text):
            problems.append(f"{n}: holds none of the language's letters")
        if text.strip() == english.strip():
            problems.append(f"{n}: the same as the English")
    return problems, len(names)


def chunk_names(work: Path) -> list[str]:
    names = [p.stem for p in sorted((work / "in").glob("*.txt"))]
    return names + [p.stem for p in sorted((work / "in").glob("briefs-*.list"))]


def validate(args) -> int:
    work = Path(args.work).resolve()
    _info, pack = work_pack(work)
    checker = validate_briefs if args.chunk.startswith("briefs") else validate_tsv
    problems, count = checker(work, args.chunk, pack)
    for problem in problems:
        print("PROBLEM", problem)
    print(f"{args.chunk}: {count} items, {len(problems)} problems")
    return 1 if problems else 0


def status(args) -> int:
    work = Path(args.work).resolve()
    _info, pack = work_pack(work)
    clean = True
    for name in chunk_names(work):
        checker = validate_briefs if name.startswith("briefs") else validate_tsv
        problems, count = checker(work, name, pack)
        clean = clean and not problems
        print(f"{name}: {count} items, {len(problems)} problems")
    return 0 if clean else 1


def merge(args) -> int:
    work = Path(args.work).resolve()
    info, pack = work_pack(work)
    template = Pack(info["template"])
    manifest = json.loads((work / "in" / "manifest.json").read_text(encoding="utf-8"))
    values: dict[str, str] = {}
    for path in sorted((work / "out").glob("*.tsv")):
        if ".part" not in path.name:
            values.update(read_tsv(path))
    fixes = work / "fixes.tsv"
    if fixes.is_file():
        values.update(read_tsv(fixes))
    missing = []
    pack.folder.mkdir(exist_ok=True)
    for table, items in manifest.items():
        lines = (template.folder / table).read_text(encoding="utf-8").split("\n")
        for number in range(min(8, len(lines))):
            lines[number] = lines[number].replace(template.english_name, pack.english_name)
        old = value_line(table, template)
        for item in items:
            value = values.get(item["id"])
            if value is None:
                missing.append(item["id"])
                if not args.allow_missing:
                    continue
                value = item["en"] or ""
            number = item["line"]
            match = old.match(lines[number])
            if not match:
                raise SystemExit(f"{template.tag}/{table} line {number + 1} moved: prepare again")
            if table == "units.tdf":
                lines[number] = f"\t{item['field']}={value};"
            elif table == "interface.tdf":
                lines[number] = f"\t{pack.tag}={value};"
            elif table == "translate.tdf":
                lines[number] = f"\t{pack.word}={value};"
            else:
                lines[number] = f"\tmissionname={value};"
        (pack.folder / table).write_text("\n".join(lines), encoding="utf-8")
    pack.briefs.mkdir(parents=True, exist_ok=True)
    for path in sorted(template.briefs.iterdir()):
        source = work / "out" / "briefs" / path.name
        if not source.is_file():
            missing.append(path.name)
            continue
        text = source.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip("\n")
        ending = "\r\n" if path.read_bytes().endswith(b"\r\n") else ""
        (pack.briefs / path.name).write_bytes((text.replace("\n", "\r\n") + ending).encode("utf-8"))
    print(f"merged into {pack.folder}; {len(missing)} missing"
          + (f": {missing[:10]}" if missing else ""))
    return 0 if not missing or args.allow_missing else 1


def warmup(args) -> int:
    pack = Pack(args.tag)
    counts: collections.Counter[str] = collections.Counter()
    paths = [pack.folder / t for t in TABLES if (pack.folder / t).is_file()]
    if pack.briefs.is_dir():
        paths.extend(sorted(pack.briefs.iterdir()))
    for path in paths:
        for line in path.read_text(encoding="utf-8").split("\n"):
            if line.startswith("//") or line.startswith("["):
                continue
            if path.suffix == ".tdf":
                if "=" not in line or "-from=" in line:
                    continue
                line = line.split("=", 1)[1]
            counts.update(c for c in line if ord(c) > 0x7E and not c.isspace())
    text = ""
    for character, _count in counts.most_common():
        if len((text + character).encode("utf-8")) > args.bytes:
            break
        text += character
    (pack.folder / "warmup.txt").write_text(text + "\n", encoding="utf-8")
    print(f"{pack.folder / 'warmup.txt'}: {len(text)} characters, "
          f"{len(text.encode('utf-8'))} bytes, of {len(counts)} the pack uses")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("prepare", help="write the translators' chunks")
    p.add_argument("tag")
    p.add_argument("--work", required=True)
    p.add_argument("--game-dir", required=True)
    p.add_argument("--oa-tool")
    p.add_argument("--template", default="uk")
    p.add_argument("--references", default="zh-Hans,uk,ko")
    p.set_defaults(run=prepare)
    p = commands.add_parser("validate", help="check one chunk's translation")
    p.add_argument("--work", required=True)
    p.add_argument("chunk")
    p.set_defaults(run=validate)
    p = commands.add_parser("status", help="check every chunk")
    p.add_argument("--work", required=True)
    p.set_defaults(run=status)
    p = commands.add_parser("merge", help="write the pack's tables and briefings")
    p.add_argument("--work", required=True)
    p.add_argument("--allow-missing", action="store_true")
    p.set_defaults(run=merge)
    p = commands.add_parser("warmup", help="write the pack's warmup.txt")
    p.add_argument("tag")
    p.add_argument("--bytes", type=int, default=1200)
    p.set_defaults(run=warmup)
    args = parser.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
