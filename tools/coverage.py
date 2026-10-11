#!/usr/bin/env python3
# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""List the engine's interface words a language pack does not translate.

    coverage.py PACK --oa-tool EXE
    coverage.py PACK --words FILE

The engine's own words are the English texts its interface looks up in the
interface catalogue (oa/data/languages/interface_text.hpp): the settings
dialog, the Library, the notices, the questions and the rest. An engine
build lists them itself:

    oa-tool interface-words --json

prints a JSON array of the texts, or an object whose "words" member holds
that array. --words reads a listing saved from it instead.

The pack's interface.tdf translates a word when the word's section gives
the pack's tag (language.yaml's tag, in any case) a value. Each word the
engine has and the pack does not translate is printed as "missing: WORD",
and each section the engine no longer has as "not in the engine: WORD". A
word the game's table reader cannot hold as a section name (one that starts
or ends with a space, or holds a line break, ']', '//' or '/*') is
printed as "cannot be a section: WORD", since no pack can translate it. A
line break or tab in a word is printed as \\n or \\t. The last line counts
them all.

The status is 0 when every word is translated and no section is left over,
1 when something is missing, left over or cannot be a section, 2 when the
listing cannot be had or read, and 77 when there is no pack.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check  # noqa: E402
import oamod_yaml  # noqa: E402

SKIPPED = 77
"""The status of a run with no pack."""

UNREADABLE = 2
"""The status of a run whose listing cannot be had or read."""

LISTING = ("interface-words", "--json")
"""The oa-tool command that lists the engine's interface words."""


class ListingError(RuntimeError):
    """A listing of the engine's words that cannot be had or read."""


def parse_listing(text: str) -> list[str]:
    """The words of a listing: a JSON array of strings, or an object holding one as "words"."""
    try:
        document = json.loads(text)
    except json.JSONDecodeError as error:
        raise ListingError(f"the listing is not JSON: {error}") from error
    if isinstance(document, dict):
        document = document.get("words")
    if not isinstance(document, list) or not all(isinstance(word, str) for word in document):
        raise ListingError("the listing is not a list of texts")
    return document


def engine_words(tool: Path) -> list[str]:
    """The interface words an engine build lists."""
    if not os.access(tool, os.X_OK):
        raise ListingError(f"{tool} is not an executable oa-tool")
    try:
        result = subprocess.run(
            [str(tool), *LISTING], capture_output=True, text=True, encoding="utf-8", errors="replace"
        )
    except OSError as error:
        raise ListingError(f"{tool} does not run: {error}") from error
    if result.returncode != 0:
        said = (result.stderr or result.stdout).strip().splitlines()
        reason = f": {said[0]}" if said else ""
        raise ListingError(
            f"{tool} does not list the interface words ('oa-tool {' '.join(LISTING)}' "
            f"exited with status {result.returncode}{reason})"
        )
    return parse_listing(result.stdout)


def folded_tag(tag: str) -> str:
    """A tag as the interface catalogue matches it: lower case, '_' read as '-'."""
    return tag.lower().replace("_", "-")


def pack_translations(pack: Path) -> tuple[str, dict[str, str]]:
    """The pack's tag and its interface.tdf's translations into it, by English text."""
    values = oamod_yaml.loads((pack / "language.yaml").read_bytes())
    tag = values.get("tag") if isinstance(values, dict) else None
    if not isinstance(tag, str) or not tag:
        raise ListingError(f"{pack / 'language.yaml'} names no tag")
    path = pack / "interface.tdf"
    if not path.is_file():
        return tag, {}
    sections = check.parse_tdf(path.read_bytes().decode("utf-8"))
    key = folded_tag(tag)
    translations: dict[str, str] = {}
    for name, fields, _children in sections:
        text = next((value for field, value in fields.items() if folded_tag(field) == key), "")
        translations[name] = text
    return tag, translations


def section_problem(word: str) -> str | None:
    """Why a word cannot be a table's section name, or None when it can be."""
    if word != word.strip(" \t\r\n"):
        return "it starts or ends with a space"
    for mark in ("\n", "\r", "]", "//", "/*"):
        if mark in word:
            return f"it holds {mark!r}"
    if not word:
        return "it is empty"
    return None


def shown(word: str) -> str:
    """A word on one line: a line break or tab written as \\n or \\t."""
    return word.replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")


def report(words: list[str], tag: str, translations: dict[str, str]) -> int:
    """Print what is missing, left over and unwritable; return the status."""
    listed = list(dict.fromkeys(words))
    unwritable = [(word, section_problem(word)) for word in listed if section_problem(word)]
    blocked = {word for word, _why in unwritable}
    missing = [word for word in listed if word not in blocked and not translations.get(word)]
    known = set(listed)
    left_over = [word for word in translations if word not in known]
    for word in missing:
        print(f"missing: {shown(word)}")
    for word in left_over:
        print(f"not in the engine: {shown(word)}")
    for word, why in unwritable:
        print(f"cannot be a section: {shown(word)} ({why})")
    translated = len(listed) - len(missing) - len(unwritable)
    print(
        f"coverage: {tag} translates {translated} of the engine's {len(listed)} interface words; "
        f"{len(missing)} missing, {len(left_over)} not in the engine, "
        f"{len(unwritable)} cannot be a section"
    )
    return 1 if missing or left_over or unwritable else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n\n", 1)[0], formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("pack", type=Path)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--oa-tool", type=Path, help="an oa-tool built from the engine")
    source.add_argument("--words", type=Path, help="a listing saved from oa-tool interface-words --json")
    options = parser.parse_args(argv)
    if not (options.pack / "language.yaml").is_file():
        print(f"SKIP no pack at {options.pack}")
        return SKIPPED
    try:
        if options.words is not None:
            try:
                words = parse_listing(options.words.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError) as error:
                raise ListingError(f"{options.words} cannot be read: {error}") from error
        else:
            words = engine_words(options.oa_tool)
        tag, translations = pack_translations(options.pack)
    except (ListingError, check.TdfError, oamod_yaml.OamodYamlError, ValueError) as error:
        print(f"coverage: {error}", file=sys.stderr)
        return UNREADABLE
    return report(words, tag, translations)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
