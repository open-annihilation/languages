# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""Every tracked text file carries the SPDX lines or a REUSE annotation."""

from __future__ import annotations

import re
import subprocess
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPYRIGHT = "SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT"
LICENCE = "SPDX-License-Identifier: GPL-3.0-only"


def reserved_pattern() -> re.Pattern[str]:
    """The names this repository does not use, built so the source does not spell them."""
    terms = (
        "bone" + "yards?",
        "ma" + "ia",
        "ro" + "ver",
        "net" + "play",
        "online " + "services?",
    )
    return re.compile(r"(?i)(?<![A-Za-z0-9_])(?:" + "|".join(terms) + r")(?![A-Za-z0-9_])")


def reuse_regex(pattern: str) -> re.Pattern[str]:
    """A REUSE path glob: '*' stays in one directory and '**' crosses directories."""
    parts: list[str] = []
    index = 0
    while index < len(pattern):
        if pattern.startswith("**", index):
            parts.append(".*")
            index += 2
        elif pattern[index] == "*":
            parts.append("[^/]*")
            index += 1
        elif pattern[index] == "?":
            parts.append("[^/]")
            index += 1
        else:
            parts.append(re.escape(pattern[index]))
            index += 1
    return re.compile("^" + "".join(parts) + "$")


def annotations() -> list[re.Pattern[str]]:
    with (ROOT / "REUSE.toml").open("rb") as handle:
        document = tomllib.load(handle)
    patterns = []
    for annotation in document["annotations"]:
        paths = annotation["path"]
        if isinstance(paths, str):
            paths = [paths]
        patterns.extend(reuse_regex(path) for path in paths)
    return patterns


def listed_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-co", "--exclude-standard"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


class RepositoryTests(unittest.TestCase):
    def test_headers_or_annotations_cover_every_text_file(self) -> None:
        patterns = annotations()
        missing = []
        reserved = []
        for relative in listed_files():
            path = ROOT / relative
            if not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = None
            covered = any(pattern.fullmatch(relative) for pattern in patterns)
            if text is not None and COPYRIGHT in text and LICENCE in text:
                covered = True
            if not covered:
                missing.append(relative)
            if text is not None:
                found = reserved_pattern().search(text)
                if found:
                    reserved.append(f"{relative}: {found.group(0)}")
        self.assertEqual(missing, [], "files without SPDX lines or a REUSE annotation")
        self.assertEqual(reserved, [], "reserved words")


if __name__ == "__main__":
    unittest.main()
