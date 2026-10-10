#!/usr/bin/env python3
# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""Build the CJK font a language pack ships, from the pins in fonts/fonts.json.

    fonts.py [--deps DIR] [--out DIR]

--deps is the folder of pinned downloads (default local/deps). A file that
is already there is used when its SHA-256 matches, and fetched otherwise.
--out is where the cut faces are written (default local/fonts). Each face
is one line: its path, its size in bytes and its SHA-256.

The cut is Noto Sans CJK SC Bold (face 2 of the Bold collection) kept to
the common CJK characters. fontTools 4.66.1, pinned by hash in
fonts/requirements.txt, runs in local/fonttools-venv. --self-test checks
the pins and the character set and downloads nothing.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import urllib.request
import venv
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
PINS = ROOT / "fonts" / "fonts.json"
REQUIREMENTS = ROOT / "fonts" / "requirements.txt"
UNIHAN_GENERAL_STANDARD_FILE = "Unihan_OtherMappings.txt"
GENERAL_STANDARD_CHARACTERS = 8105
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def general_standard_characters(unihan):
    """The code points of the Table of General Standard Chinese Characters.

    They are the characters the Unihan archive's kTGH field gives a
    position in the table of 2013; the archive must list all 8,105.
    """
    found = set()
    with zipfile.ZipFile(unihan) as archive:
        for line in archive.read(UNIHAN_GENERAL_STANDARD_FILE).decode("utf-8").splitlines():
            fields = line.split("\t")
            if len(fields) == 3 and fields[1] == "kTGH" and fields[0].startswith("U+"):
                found.add(int(fields[0][2:], 16))
    if len(found) != GENERAL_STANDARD_CHARACTERS:
        raise RuntimeError(
            f"{unihan} lists {len(found)} general standard characters, "
            f"not {GENERAL_STANDARD_CHARACTERS}"
        )
    return found


def cjk_characters(general_standard=()):
    """The characters the cut-down CJK font keeps, as a sorted list of code points.

    The two-byte characters of GB 2312, of Big5's symbols and level-1 hanzi
    (lead bytes 0xA1-0xC6), of JIS X 0208 (EUC-JP rows 1-84), and of KS X
    1001's symbol and Hangul rows (lead bytes 0xA1-0xAC and 0xB0-0xC8, the
    hanja left out), as Python's codecs map them, the blocks of CJK
    punctuation, kana, bopomofo, Hangul compatibility jamo and half- and
    full-width forms, and the code points of general_standard, the Table of
    General Standard Chinese Characters (general_standard_characters).
    """
    def two_byte(codec, leads, trails):
        found = set()
        for lead in leads:
            for trail in trails:
                try:
                    text = bytes((lead, trail)).decode(codec)
                except UnicodeDecodeError:
                    continue
                if len(text) == 1:
                    found.add(ord(text))
        return found

    characters = set()
    characters |= two_byte("gb2312", range(0xA1, 0xF8), range(0xA1, 0xFF))
    characters |= two_byte("big5", range(0xA1, 0xC7), [*range(0x40, 0x7F), *range(0xA1, 0xFF)])
    characters |= two_byte("euc_jp", range(0xA1, 0xF5), range(0xA1, 0xFF))
    characters |= two_byte("euc_kr", [*range(0xA1, 0xAD), *range(0xB0, 0xC9)], range(0xA1, 0xFF))
    for first, last in ((0x3000, 0x30FF), (0x3100, 0x312F), (0x3130, 0x318F), (0xFF00, 0xFFEF)):
        characters |= set(range(first, last + 1))
    characters |= set(general_standard)
    return sorted(characters)


def load_pins(path=None):
    """The fonts/fonts.json document."""
    return json.loads((path or PINS).read_text(encoding="utf-8"))


def pin_problems(data):
    """What is wrong with a fonts.json document; empty when it is well formed."""
    problems = []
    if not isinstance(data, dict):
        return ["fonts.json is not an object"]
    downloads = data.get("downloads")
    fonts = data.get("fonts")
    if not isinstance(downloads, list) or not downloads:
        problems.append("downloads is not a list")
        downloads = []
    names = set()
    for item in downloads:
        if not isinstance(item, dict):
            problems.append("a download is not an object")
            continue
        for key in ("file", "url", "sha256"):
            if key not in item:
                problems.append(f"a download has no {key}")
        name = item.get("file")
        url = item.get("url")
        digest = item.get("sha256")
        if not isinstance(name, str) or not name or name != pathlib.PurePath(name).name:
            problems.append(f"a download file is not a file name: {name!r}")
        elif name in names:
            problems.append(f"{name} is listed twice")
        else:
            names.add(name)
        if not isinstance(url, str) or not url.startswith("https://"):
            problems.append(f"the url of {name} is not https")
        if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            problems.append(f"the sha256 of {name} is malformed")
    if not isinstance(fonts, dict) or not fonts:
        problems.append("fonts is not an object")
        fonts = {}
    for name, spec in fonts.items():
        if not isinstance(spec, dict):
            problems.append(f"{name} is not an object")
            continue
        for key in ("download", "face", "characters", "count", "sha256", "licence"):
            if key not in spec:
                problems.append(f"{name} has no {key}")
        download = spec.get("download")
        if download not in names:
            problems.append(f"{name} names no download")
        face = spec.get("face")
        if isinstance(face, bool) or not isinstance(face, int) or face < 0:
            problems.append(f"{name} has no face index")
        if spec.get("characters") != "common-cjk":
            problems.append(f"{name} is not cut to common-cjk")
        count = spec.get("count")
        if isinstance(count, bool) or not isinstance(count, int) or count < 1:
            problems.append(f"{name} has no character count")
        digest = spec.get("sha256")
        if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            problems.append(f"the sha256 of {name} is malformed")
        licence = spec.get("licence")
        if not isinstance(licence, str) or not licence or licence != pathlib.PurePath(licence).name:
            problems.append(f"the licence of {name} is not a file name")
        elif not (ROOT / "fonts" / licence).is_file():
            problems.append(f"the licence of {name} is missing")
    if not REQUIREMENTS.is_file():
        problems.append("fonts/requirements.txt is missing")
    return problems


def fetch_download(directory, item):
    """The path of one verified download under directory, fetched unless present.

    A file already there is kept when its SHA-256 matches and refused when
    it does not. A download whose bytes do not match is not written.
    """
    directory.mkdir(parents=True, exist_ok=True)
    destination = directory / item["file"]
    expected = item["sha256"]
    if destination.is_file():
        actual = hashlib.sha256(destination.read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"{destination.name} has SHA-256 {actual}, not {expected}")
        return destination
    with urllib.request.urlopen(item["url"], timeout=120) as response:
        payload = response.read()
    actual = hashlib.sha256(payload).hexdigest()
    if actual != expected:
        raise RuntimeError(f"{item['file']} has SHA-256 {actual}, not {expected}")
    destination.write_bytes(payload)
    return destination


def download_roles(data):
    """The collection, the Unihan archive and the licence download, by file name."""
    by_name = {item["file"]: item for item in data["downloads"]}
    collections = []
    archives = []
    for spec in data["fonts"].values():
        collections.append(by_name[spec["download"]])
    for item in data["downloads"]:
        if item["file"].endswith(".zip"):
            archives.append(item)
    licences = [
        item for item in data["downloads"]
        if item not in collections and item not in archives
    ]
    if len(collections) != 1 or len(archives) != 1 or len(licences) != 1:
        raise RuntimeError("fonts.json needs one collection, one Unihan archive and one licence")
    return collections[0], archives[0], licences[0]


def fonttools_python():
    """The Python of the virtual environment that holds the pinned fontTools."""
    environment = ROOT / "local" / "fonttools-venv"
    names = (pathlib.Path("bin") / "python", pathlib.Path("Scripts") / "python.exe")
    python = next((environment / name for name in names if (environment / name).is_file()), None)
    stamp = environment / "requirements.txt"
    if python is None or not stamp.is_file() or stamp.read_bytes() != REQUIREMENTS.read_bytes():
        print(f"Installing the pinned fontTools into {environment}", flush=True)
        venv.EnvBuilder(with_pip=True, clear=True).create(environment)
        python = next(environment / name for name in names if (environment / name).is_file())
        subprocess.run(
            [str(python), "-m", "pip", "install", "--disable-pip-version-check", "--quiet",
             "--require-hashes", "-r", str(REQUIREMENTS)],
            check=True,
        )
        shutil.copyfile(REQUIREMENTS, stamp)
    return python


def cut_cjk_face(collection, unihan, face, out, count):
    """Write one face of the CJK collection to out, cut to cjk_characters().

    Runs in the fontTools environment (--cut-face). Layout tables are
    dropped, since the engine shapes nothing, and the hinting kept; the
    font's modification time is left as it was, so the output depends only
    on its input.
    """
    from fontTools import subset
    from fontTools.ttLib import TTFont

    font = TTFont(collection, fontNumber=face, recalcTimestamp=False, lazy=False)
    options = subset.Options()
    options.layout_features = []
    options.name_IDs = ["*"]
    options.name_languages = ["*"]
    options.notdef_outline = True
    options.recalc_timestamp = False
    held = font.getBestCmap()
    kept = [c for c in cjk_characters(general_standard_characters(unihan)) if c in held]
    if len(kept) != count:
        raise RuntimeError(f"the face holds {len(kept)} of the characters, not {count}")
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=kept)
    subsetter.subset(font)
    font.save(out)


def self_test():
    """Check the pins and the character set. Return the exit status."""
    try:
        data = load_pins()
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        print(f"fonts self-test: fonts.json does not read: {error}")
        return 1
    problems = pin_problems(data)
    characters = cjk_characters()
    if len(characters) != 14066:
        problems.append(f"the CJK character set holds {len(characters)} characters, not 14066")
    for sample in ("中", "國", "日本", "한국어", "ア", "，"):
        if any(ord(character) not in characters for character in sample):
            problems.append(f"the CJK character set lacks {sample}")
    for problem in problems:
        print(f"fonts self-test: {problem}")
    if problems:
        return 1
    print(
        f"fonts self-test: {len(data['downloads'])} downloads, {len(data['fonts'])} fonts "
        f"and {len(characters)} CJK characters besides the general standard table, as expected"
    )
    return 0


def build(deps, out, shown):
    """Fetch, check the licence, cut each font and print its path, size and SHA-256."""
    data = load_pins()
    problems = pin_problems(data)
    if problems:
        raise RuntimeError("; ".join(problems))
    collection, unihan, licence = download_roles(data)
    collection_path = fetch_download(deps, collection)
    unihan_path = fetch_download(deps, unihan)
    licence_path = fetch_download(deps, licence)
    for spec in data["fonts"].values():
        notice = ROOT / "fonts" / spec["licence"]
        if licence_path.read_bytes() != notice.read_bytes():
            raise RuntimeError(f"{notice.name} differs from the downloaded licence")
    python = fonttools_python()
    out.mkdir(parents=True, exist_ok=True)
    for name, spec in data["fonts"].items():
        destination = out / name
        command = [
            str(python), str(pathlib.Path(__file__).resolve()),
            "--cut-face", str(collection_path), str(unihan_path), str(destination),
            "--face", str(spec["face"]), "--count", str(spec["count"]),
        ]
        subprocess.run(command, check=True)
        payload = destination.read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        if digest != spec["sha256"]:
            destination.unlink()
            raise RuntimeError(f"{name} has SHA-256 {digest}, not {spec['sha256']}")
        print(f"{(shown / name).as_posix()} {len(payload)} {digest}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--deps", type=pathlib.Path, default=pathlib.Path("local") / "deps",
                        help="pinned downloads (default: local/deps)")
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("local") / "fonts",
                        help="where to write the faces (default: local/fonts)")
    parser.add_argument("--self-test", action="store_true",
                        help="check the pins and the character set, and exit")
    parser.add_argument("--cut-face", nargs=3, metavar=("COLLECTION", "UNIHAN", "OUT"), help=argparse.SUPPRESS)
    parser.add_argument("--face", type=int, default=2, help=argparse.SUPPRESS)
    parser.add_argument("--count", type=int, default=15309, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.cut_face:
        cut_cjk_face(args.cut_face[0], args.cut_face[1], args.face, args.cut_face[2], args.count)
        return 0
    build(args.deps, args.out, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
