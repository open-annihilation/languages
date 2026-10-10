# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""The pack checker accepts the zh-Hans source and refuses broken fixtures."""

from __future__ import annotations

import contextlib
import io
import unittest
from pathlib import Path

from tools import check

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


def run(args: list[str]) -> tuple[int, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = check.main(args)
    return code, buffer.getvalue()


class CheckTests(unittest.TestCase):
    def test_zh_hans_source_is_clean(self) -> None:
        code, output = run([str(ROOT / "zh-Hans"), "--source"])
        self.assertEqual(code, 0, output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_zh_hans_without_source_misses_its_font(self) -> None:
        code, output = run([str(ROOT / "zh-Hans")])
        self.assertEqual(code, 1, output)
        self.assertIn("fonts/NotoSansCJKsc-Bold.otf is not a file", output)

    def test_all_source_is_clean(self) -> None:
        code, output = run(["--all", "--source"])
        self.assertEqual(code, 0, output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_unknown_key_fails(self) -> None:
        code, output = run([str(FIXTURES / "unknown-key")])
        self.assertEqual(code, 1, output)
        self.assertIn("has no key mystery", output)

    def test_missing_licence_header_fails(self) -> None:
        code, output = run([str(FIXTURES / "missing-header")])
        self.assertEqual(code, 1, output)
        self.assertIn("has no licence header", output)

    def test_fifth_font_fails(self) -> None:
        code, output = run([str(FIXTURES / "five-fonts")])
        self.assertEqual(code, 1, output)
        self.assertIn("more than 4", output)

    def test_long_warmup_fails(self) -> None:
        code, output = run([str(FIXTURES / "long-warmup")])
        self.assertEqual(code, 1, output)
        self.assertIn("larger than 4096", output)

    def test_duplicate_section_fails(self) -> None:
        code, output = run([str(FIXTURES / "duplicate-section")])
        self.assertEqual(code, 1, output)
        self.assertIn("names [Same] twice", output)

    def test_missing_pack_is_skipped(self) -> None:
        code, output = run([str(FIXTURES / "not-a-pack")])
        self.assertEqual(code, 77, output)
        self.assertIn("SKIP", output)


if __name__ == "__main__":
    unittest.main()
