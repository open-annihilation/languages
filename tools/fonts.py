#!/usr/bin/env python3
# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""Build the CJK fonts the language packs ship, from the pins in fonts/fonts.json.

    fonts.py [--deps DIR] [--out DIR]

--deps is the folder of pinned downloads (default local/deps). A file that
is already there is used when its SHA-256 matches, and fetched otherwise.
--out is where the cut faces are written (default local/fonts). Each face
is one line: its path, its size in bytes and its SHA-256.

Three faces are cut from the Bold collection: Noto Sans CJK SC Bold (face
2) kept to the common CJK characters, Noto Sans CJK KR Bold (face 1) kept
to Hangul, and Noto Sans CJK JP Bold (face 0) kept to Japanese. fontTools
4.66.1, pinned by hash in fonts/requirements.txt, runs in
local/fonttools-venv, which is made again when its Python no longer runs
it. --self-test checks the pins and the character sets and downloads
nothing.

    fonts.py --record-engine-faces FONTS

records the faces of an engine build's fonts folder (the bundle's
Contents/Resources/fonts on macOS, the fonts folder beside the game
elsewhere) in fonts/engine-faces.json: each face's SHA-256 and the code
points it draws. The pack check reads that record for the characters a
pack's text draws from the engine's own faces.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import shutil
import struct
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
UNIHAN_JAPANESE_FILE = "Unihan_OtherMappings.txt"
JAPANESE_KANJI_FIELDS = {"kJis0": 6356, "kJoyoKanji": 2140, "kJinmeiyoKanji": 863}
"""The Unihan fields the Japanese face's kanji are read from, each with the
code points it lists: JIS X 0208's ideographs (its 6,355 kanji and the 仝
of its symbol row), the 2,136 Jōyō kanji of 2010 and the 4 common forms
the table allows beside 𠮟, 剝, 塡 and 頰, and the 863 Jinmeiyō kanji.
"""
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


def japanese_kanji(unihan):
    """The kanji of JIS X 0208 and the Jōyō and Jinmeiyō kanji, 6,465 in Unihan 16.0.

    They are the code points the Unihan archive's kJis0, kJoyoKanji and
    kJinmeiyoKanji fields list; each field must list as many as
    JAPANESE_KANJI_FIELDS says.
    """
    found = {field: set() for field in JAPANESE_KANJI_FIELDS}
    with zipfile.ZipFile(unihan) as archive:
        for line in archive.read(UNIHAN_JAPANESE_FILE).decode("utf-8").splitlines():
            fields = line.split("\t")
            if len(fields) == 3 and fields[1] in found and fields[0].startswith("U+"):
                found[fields[1]].add(int(fields[0][2:], 16))
    for field, count in JAPANESE_KANJI_FIELDS.items():
        if len(found[field]) != count:
            raise RuntimeError(f"{unihan} lists {len(found[field])} {field} characters, not {count}")
    return set().union(*found.values())


def two_byte_characters(codec, leads, trails):
    """The characters a two-byte code page maps, as Python's codec decodes them."""
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
    characters = set()
    for codec, leads, trails in (
        ("gb2312", range(0xA1, 0xF8), range(0xA1, 0xFF)),
        ("big5", range(0xA1, 0xC7), [*range(0x40, 0x7F), *range(0xA1, 0xFF)]),
        ("euc_jp", range(0xA1, 0xF5), range(0xA1, 0xFF)),
        ("euc_kr", [*range(0xA1, 0xAD), *range(0xB0, 0xC9)], range(0xA1, 0xFF)),
    ):
        characters |= two_byte_characters(codec, leads, trails)
    for first, last in ((0x3000, 0x30FF), (0x3100, 0x312F), (0x3130, 0x318F), (0xFF00, 0xFFEF)):
        characters |= set(range(first, last + 1))
    characters |= set(general_standard)
    return sorted(characters)


HANGUL_SYLLABLES = (0xAC00, 0xD7A3)
"""The 11,172 precomposed Hangul syllables of modern Korean."""

HANGUL_COUNT = 12349
"""The characters hangul_characters() lists."""


def hangul_characters():
    """The characters the cut-down Korean face keeps, as a sorted list of code points.

    Every precomposed Hangul syllable, the blocks of Hangul compatibility
    jamo, CJK punctuation and half- and full-width forms, and the two-byte
    characters of KS X 1001's symbol rows (lead bytes 0xA1-0xAC), as
    Python's codecs map them. KS X 1001's hanja are left out.
    """
    characters = set(range(HANGUL_SYLLABLES[0], HANGUL_SYLLABLES[1] + 1))
    characters |= two_byte_characters("euc_kr", range(0xA1, 0xAD), range(0xA1, 0xFF))
    for first, last in ((0x3000, 0x303F), (0x3130, 0x318F), (0xFF00, 0xFFEF)):
        characters |= set(range(first, last + 1))
    return sorted(characters)


JAPANESE_BLOCKS = (
    (0x3000, 0x303F),  # CJK symbols and punctuation
    (0x3040, 0x309F),  # Hiragana
    (0x30A0, 0x30FF),  # Katakana, the middle dot and the prolonged-sound mark among them
    (0x31F0, 0x31FF),  # Katakana phonetic extensions
    (0xFF00, 0xFFEF),  # Half- and full-width forms, half-width katakana among them
)
"""The blocks the Japanese face keeps whole."""

JAPANESE_COUNT = 7100
"""The characters japanese_characters() lists without the Unihan kanji."""


def japanese_characters(kanji=()):
    """The characters the cut-down Japanese face keeps, as a sorted list of code points.

    The two-byte characters of JIS X 0208 (EUC-JP rows 1-84: its symbols,
    Latin letters, digits, kana, Greek, Cyrillic and box drawing, and its
    6,355 kanji), as Python's codecs map them, the blocks of
    JAPANESE_BLOCKS, and the code points of kanji, the kanji of JIS X 0208
    and the Jōyō and Jinmeiyō kanji (japanese_kanji). Without kanji the
    set is the code page's alone, which lacks the Jōyō and Jinmeiyō kanji
    outside JIS X 0208.
    """
    characters = two_byte_characters("euc_jp", range(0xA1, 0xF5), range(0xA1, 0xFF))
    for first, last in JAPANESE_BLOCKS:
        characters |= set(range(first, last + 1))
    characters |= set(kanji)
    return sorted(characters)


RECIPES = ("common-cjk", "hangul", "japanese")
"""The character sets a face in fonts.json may be cut to.

common-cjk is cjk_characters() with the general standard table, hangul is
hangul_characters(), japanese is japanese_characters() with the kanji of
JIS X 0208 and the Jōyō and Jinmeiyō kanji.
"""


def unihan_characters(recipe, unihan):
    """The code points a recipe reads from the Unihan archive at unihan.

    The general standard table for common-cjk, the Japanese kanji for
    japanese, and none for hangul, which does not read the archive.
    """
    if recipe == "common-cjk":
        return general_standard_characters(unihan)
    if recipe == "japanese":
        return japanese_kanji(unihan)
    if recipe == "hangul":
        return set()
    raise ValueError(f"{recipe!r} is not a recipe")


def recipe_characters(recipe, from_unihan=()):
    """The code points a recipe keeps, with from_unihan, what it reads from the Unihan archive."""
    if recipe == "hangul":
        return hangul_characters()
    if recipe == "common-cjk":
        return cjk_characters(from_unihan)
    if recipe == "japanese":
        return japanese_characters(from_unihan)
    raise ValueError(f"{recipe!r} is not a recipe")


CJK_BLOCKS = (
    (0x1100, 0x11FF),    # Hangul Jamo
    (0x2E80, 0x2FFF),    # CJK and Kangxi radicals, ideographic description
    (0x3000, 0x303F),    # CJK symbols and punctuation
    (0x3040, 0x30FF),    # Hiragana and Katakana
    (0x3100, 0x318F),    # Bopomofo and Hangul compatibility jamo
    (0x3190, 0x31FF),    # Kanbun, Bopomofo extended, CJK strokes, Katakana extensions
    (0x3200, 0x33FF),    # Enclosed CJK letters and months, CJK compatibility
    (0x3400, 0x4DBF),    # CJK unified ideographs extension A
    (0x4E00, 0x9FFF),    # CJK unified ideographs
    (0xA960, 0xA97F),    # Hangul jamo extended A
    (0xAC00, 0xD7FF),    # Hangul syllables and jamo extended B
    (0xF900, 0xFAFF),    # CJK compatibility ideographs
    (0xFE10, 0xFE1F),    # Vertical forms
    (0xFE30, 0xFE6F),    # CJK compatibility forms and small form variants
    (0xFF00, 0xFFEF),    # Half- and full-width forms
    (0x20000, 0x3FFFF),  # The supplementary ideographic planes
)
"""The Unicode blocks whose characters only a CJK face draws.

The game's fonts and the engine's own faces draw the Latin letters,
punctuation and symbols outside them.
"""


def cjk_block(code):
    """Whether a code point is in one of CJK_BLOCKS."""
    return any(first <= code <= last for first, last in CJK_BLOCKS)


def face_characters(path):
    """The code points a TrueType or OpenType face maps to a glyph.

    Reads the face's cmap table, its format 4 and format 12 subtables of
    the Unicode and Windows platforms, without fontTools. A code point
    mapped to glyph 0 is not held. Raises ValueError for a file that is not
    one face with a character map read here, such as a collection.
    """
    data = pathlib.Path(path).read_bytes()

    def unpack(form, offset):
        size = struct.calcsize(form)
        if offset < 0 or offset + size > len(data):
            raise ValueError(f"{pathlib.Path(path).name} ends inside its tables")
        return struct.unpack_from(form, data, offset)

    (version,) = unpack(">I", 0)
    if version not in (0x00010000, 0x4F54544F, 0x74727565):
        raise ValueError(f"{pathlib.Path(path).name} is not a TrueType or OpenType face")
    (tables,) = unpack(">H", 4)
    cmap = None
    for index in range(tables):
        tag, _checksum, offset, _length = unpack(">4sIII", 12 + 16 * index)
        if tag == b"cmap":
            cmap = offset
    if cmap is None:
        raise ValueError(f"{pathlib.Path(path).name} has no character map")
    _version, subtables = unpack(">HH", cmap)
    held = set()
    read = False
    for index in range(subtables):
        platform, encoding, offset = unpack(">HHI", cmap + 4 + 8 * index)
        if not (platform == 0 or (platform == 3 and encoding in (1, 10))):
            continue
        start = cmap + offset
        (form,) = unpack(">H", start)
        if form == 12:
            (groups,) = unpack(">I", start + 12)
            for group in range(groups):
                first, last, glyph = unpack(">III", start + 16 + 12 * group)
                if last < first or last > 0x10FFFF:
                    raise ValueError(f"{pathlib.Path(path).name} has a malformed character map")
                held.update(range(first if glyph else first + 1, last + 1))
            read = True
        elif form == 4:
            (doubled,) = unpack(">H", start + 6)
            segments = doubled // 2
            ends = unpack(f">{segments}H", start + 14)
            starts = unpack(f">{segments}H", start + 16 + doubled)
            deltas = unpack(f">{segments}h", start + 16 + 2 * doubled)
            ranges_at = start + 16 + 3 * doubled
            ranges = unpack(f">{segments}H", ranges_at)
            for segment in range(segments):
                for code in range(starts[segment], ends[segment] + 1):
                    if code == 0xFFFF:
                        continue
                    if ranges[segment] == 0:
                        glyph = (code + deltas[segment]) & 0xFFFF
                    else:
                        address = (ranges_at + 2 * segment + ranges[segment]
                                   + 2 * (code - starts[segment]))
                        (glyph,) = unpack(">H", address)
                        if glyph:
                            glyph = (glyph + deltas[segment]) & 0xFFFF
                    if glyph:
                        held.add(code)
            read = True
    if not read:
        raise ValueError(f"{pathlib.Path(path).name} has no Unicode character map")
    return held


ENGINE_FACES = ROOT / "fonts" / "engine-faces.json"
"""The record of the characters the engine's own faces draw."""

ENGINE_FACE_FILES = (
    "DejaVuSans-Bold.ttf",
    "DejaVuSans.ttf",
    "NotoSansCJKsc-Bold-Endonyms.otf",
    "NotoEmoji.ttf",
)
"""The engine's base faces, in the order its font stack opens them.

They are the files of the fonts folder beside the game (face_files in the
engine's oa/platform/text_font.hpp). The bold weight looks in all four; the
regular weight skips DejaVu Sans Bold.
"""

BOLD_ONLY_FACES = ("DejaVuSans-Bold.ttf",)
"""The base faces only the bold weight looks in."""


def code_ranges(codes):
    """The code points as runs, each "XXXX" or "XXXX-YYYY" in hexadecimal."""
    runs = []
    for code in sorted(codes):
        if runs and runs[-1][1] == code - 1:
            runs[-1][1] = code
        else:
            runs.append([code, code])
    return [f"{first:04X}" if first == last else f"{first:04X}-{last:04X}" for first, last in runs]


def range_codes(runs):
    """The code points of runs written by code_ranges. Raises ValueError for a malformed run."""
    codes = set()
    for run in runs:
        if not isinstance(run, str) or not re.fullmatch(r"[0-9A-F]{4,6}(-[0-9A-F]{4,6})?", run):
            raise ValueError(f"{run!r} is not a run of code points")
        first, _, last = run.partition("-")
        start = int(first, 16)
        end = int(last, 16) if last else start
        if end < start or end > 0x10FFFF:
            raise ValueError(f"{run!r} is not a run of code points")
        codes.update(range(start, end + 1))
    return codes


def record_engine_faces(folder):
    """The record of the engine's base faces in a fonts folder.

    Each face's SHA-256 and the runs of the code points its character map
    holds. Raises OSError for a missing face and ValueError for one that
    cannot be read.
    """
    faces = {}
    for name in ENGINE_FACE_FILES:
        path = pathlib.Path(folder) / name
        faces[name] = {
            "characters": code_ranges(face_characters(path)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    return {"faces": faces}


def engine_face_problems(data):
    """What is wrong with a record of the engine's faces; empty when it is well formed."""
    if not isinstance(data, dict) or not isinstance(data.get("faces"), dict):
        return ["the record holds no faces"]
    problems = []
    faces = data["faces"]
    if list(faces) != list(ENGINE_FACE_FILES):
        problems.append("the record does not name the engine's four faces in their order")
    for name, face in faces.items():
        if not isinstance(face, dict) or set(face) != {"characters", "sha256"}:
            problems.append(f"{name} is not a face's record")
            continue
        if not isinstance(face["sha256"], str) or not SHA256_RE.fullmatch(face["sha256"]):
            problems.append(f"the sha256 of {name} is malformed")
        if not isinstance(face["characters"], list) or not face["characters"]:
            problems.append(f"{name} records no characters")
            continue
        try:
            range_codes(face["characters"])
        except ValueError as error:
            problems.append(f"{name}: {error}")
    return problems


def every_weight_characters(faces):
    """The code points every weight draws, from {face file: code points}."""
    held = set()
    for name, codes in faces.items():
        if name not in BOLD_ONLY_FACES:
            held |= codes
    return held


def engine_characters(folder=None, record=None):
    """The code points the engine's base faces draw in every weight.

    Read from the faces in folder, the engine's fonts folder, when it is
    given, and else from the record (default fonts/engine-faces.json).
    Raises OSError or ValueError when they cannot be read.
    """
    if folder is not None:
        return every_weight_characters(
            {name: face_characters(pathlib.Path(folder) / name) for name in ENGINE_FACE_FILES}
        )
    path = record or ENGINE_FACES
    try:
        data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"{pathlib.Path(path).name} is not JSON: {error}") from error
    problems = engine_face_problems(data)
    if problems:
        raise ValueError("; ".join(problems))
    return every_weight_characters(
        {name: range_codes(face["characters"]) for name, face in data["faces"].items()}
    )


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
        if spec.get("characters") not in RECIPES:
            problems.append(f"{name} is not cut to one of {', '.join(RECIPES)}")
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
        if by_name[spec["download"]] not in collections:
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


def runs_fonttools(python):
    """Whether python runs and imports fontTools.

    A virtual environment's Python stops running when the Python it was
    made from is upgraded or removed.
    """
    try:
        result = subprocess.run([str(python), "-I", "-c", "import fontTools"],
                                capture_output=True, timeout=120)
    except OSError:
        return False
    return result.returncode == 0


def fonttools_python():
    """The Python of the virtual environment that holds the pinned fontTools.

    The environment is made, or made again, when it is missing, was made
    from other requirements, or its Python no longer runs fontTools.
    """
    environment = ROOT / "local" / "fonttools-venv"
    names = (pathlib.Path("bin") / "python", pathlib.Path("Scripts") / "python.exe")
    python = next((environment / name for name in names if (environment / name).is_file()), None)
    stamp = environment / "requirements.txt"
    if (python is None or not stamp.is_file() or stamp.read_bytes() != REQUIREMENTS.read_bytes()
            or not runs_fonttools(python)):
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


def cut_cjk_face(collection, unihan, face, out, count, recipe="common-cjk"):
    """Write one face of the CJK collection to out, cut to its recipe's characters.

    The recipe is common-cjk, cjk_characters() with the general standard
    table read from unihan, japanese, japanese_characters() with the kanji
    read from unihan, or hangul, hangul_characters(), which does not read
    unihan. Runs in the fontTools environment (--cut-face). Layout tables
    are dropped, since the engine shapes nothing, and the hinting kept; the
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
    kept = [c for c in recipe_characters(recipe, unihan_characters(recipe, unihan)) if c in held]
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
    hangul = hangul_characters()
    if len(hangul) != HANGUL_COUNT:
        problems.append(f"the Hangul character set holds {len(hangul)} characters, not {HANGUL_COUNT}")
    for sample in ("한국어", "똠방각하", "ㅋㅎ", "「」", "，"):
        if any(ord(character) not in hangul for character in sample):
            problems.append(f"the Hangul character set lacks {sample}")
    if any(0x4E00 <= code <= 0x9FFF for code in hangul):
        problems.append("the Hangul character set holds hanja")
    japanese = japanese_characters()
    if len(japanese) != JAPANESE_COUNT:
        problems.append(
            f"the Japanese character set holds {len(japanese)} characters, not {JAPANESE_COUNT}"
        )
    for sample in ("日本語", "ひらがな", "カタカナー", "ヴ・ㇰㇷ", "「」、。〜", "！？（）", "ｱｲｳ"):
        if any(ord(character) not in japanese for character in sample):
            problems.append(f"the Japanese character set lacks {sample}")
    if any(0xAC00 <= code <= 0xD7A3 for code in japanese):
        problems.append("the Japanese character set holds Hangul")
    if any(ord(character) in japanese for character in "们这说"):
        problems.append("the Japanese character set holds simplified Chinese characters")
    for problem in problems:
        print(f"fonts self-test: {problem}")
    if problems:
        return 1
    print(
        f"fonts self-test: {len(data['downloads'])} downloads, {len(data['fonts'])} fonts, "
        f"{len(characters)} CJK characters besides the general standard table, "
        f"{len(hangul)} Hangul characters and {len(japanese)} Japanese characters "
        f"besides the Unihan kanji, as expected"
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
            "--characters", spec["characters"],
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
                        help="check the pins and the character sets, and exit")
    parser.add_argument("--record-engine-faces", type=pathlib.Path, metavar="FONTS",
                        help="record the faces of an engine build's fonts folder in "
                             "fonts/engine-faces.json, and exit")
    parser.add_argument("--cut-face", nargs=3, metavar=("COLLECTION", "UNIHAN", "OUT"), help=argparse.SUPPRESS)
    parser.add_argument("--face", type=int, default=2, help=argparse.SUPPRESS)
    parser.add_argument("--count", type=int, default=15309, help=argparse.SUPPRESS)
    parser.add_argument("--characters", choices=RECIPES, default="common-cjk", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.record_engine_faces:
        data = record_engine_faces(args.record_engine_faces)
        ENGINE_FACES.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
        held = every_weight_characters(
            {name: range_codes(face["characters"]) for name, face in data["faces"].items()}
        )
        print(f"{ENGINE_FACES.relative_to(ROOT).as_posix()}: {len(held)} characters in every weight")
        return 0
    if args.cut_face:
        cut_cjk_face(args.cut_face[0], args.cut_face[1], args.face, args.cut_face[2], args.count,
                     args.characters)
        return 0
    build(args.deps, args.out, args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
