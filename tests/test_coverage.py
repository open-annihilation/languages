# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""The coverage tool compares a pack's interface.tdf with an engine build's own listing."""

from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools import coverage

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"
PACK = FIXTURES / "coverage"
TOOL = FIXTURES / "bin" / "oa-tool"


def run(args: list[str]) -> tuple[int, str, str]:
    out = io.StringIO()
    err = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = coverage.main(args)
    return code, out.getvalue(), err.getvalue()


class CoverageTests(unittest.TestCase):
    def setUp(self) -> None:
        mode = TOOL.stat().st_mode
        if not mode & stat.S_IXUSR:
            TOOL.chmod(mode | stat.S_IXUSR)
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)

    def listing(self, words: object) -> Path:
        path = Path(self.folder.name) / "words.json"
        path.write_text(json.dumps(words, ensure_ascii=False), encoding="utf-8")
        return path

    def test_missing_and_left_over_words_are_listed(self) -> None:
        words = self.listing(["Library", "{count} min ago", "Install ID", "Registries"])
        code, output, _ = run([str(PACK), "--words", str(words)])
        self.assertEqual(code, 1, output)
        lines = output.splitlines()
        self.assertIn("missing: Install ID", lines)
        self.assertIn("missing: Registries", lines)
        self.assertIn("not in the engine: UNITS", lines)
        self.assertNotIn("missing: Library", lines)
        self.assertNotIn("missing: {count} min ago", lines)
        self.assertEqual(
            lines[-1],
            "coverage: zh-Hans translates 2 of the engine's 4 interface words; "
            "2 missing, 1 not in the engine, 0 cannot be a section",
        )

    def test_a_pack_that_covers_the_listing_is_clean(self) -> None:
        pack = Path(self.folder.name) / "coverage"
        shutil.copytree(PACK, pack)
        table = pack / "interface.tdf"
        table.write_text(table.read_text(encoding="utf-8").replace("zh-Hans=;", "zh-Hans=安装ID;"),
                         encoding="utf-8")
        words = self.listing({"words": ["Library", "{count} min ago", "UNITS", "Install ID"]})
        code, output, _ = run([str(pack), "--words", str(words)])
        self.assertEqual(code, 0, output)
        self.assertNotIn("missing:", output)
        self.assertTrue(output.rstrip().endswith("0 missing, 0 not in the engine, 0 cannot be a section"))

    def test_the_listing_comes_from_oa_tool(self) -> None:
        words = self.listing(["Library", "{count} min ago", "UNITS", "Downloads"])
        environment = dict(os.environ, OA_TOOL_FIXTURE_WORDS=str(words))
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "coverage.py"), str(PACK), "--oa-tool", str(TOOL)],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8", env=environment,
        )
        self.assertEqual(result.returncode, 1, result.stderr + result.stdout)
        self.assertEqual(result.stdout.splitlines()[0], "missing: Downloads")

    def test_a_build_without_the_listing_is_refused(self) -> None:
        environment = {key: value for key, value in os.environ.items() if key != "OA_TOOL_FIXTURE_WORDS"}
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "coverage.py"), str(PACK), "--oa-tool", str(TOOL)],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8", env=environment,
        )
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("does not list the interface words", result.stderr)
        self.assertIn("unknown command", result.stderr)

    def test_words_no_section_can_hold_are_told(self) -> None:
        words = self.listing(["Library", "{count} min ago", "UNITS", " · in use", "http://…", "a [b]", "x; y"])
        code, output, _ = run([str(PACK), "--words", str(words)])
        self.assertEqual(code, 1, output)
        self.assertIn("cannot be a section:  · in use (it starts or ends with a space)", output)
        self.assertIn("cannot be a section: http://… (it holds '//')", output)
        self.assertIn("cannot be a section: a [b] (it holds ']')", output)
        self.assertIn("missing: x; y", output)

    def test_a_listing_that_is_not_a_list_of_texts_is_refused(self) -> None:
        for document in ({"words": "Library"}, [1, 2], {"other": []}):
            code, _, error = run([str(PACK), "--words", str(self.listing(document))])
            self.assertEqual(code, 2, document)
            self.assertIn("not a list of texts", error)
        broken = Path(self.folder.name) / "broken.json"
        broken.write_text("[", encoding="utf-8")
        code, _, error = run([str(PACK), "--words", str(broken)])
        self.assertEqual(code, 2)
        self.assertIn("not JSON", error)

    def test_a_missing_pack_is_skipped(self) -> None:
        code, output, _ = run([str(FIXTURES / "not-a-pack"), "--words", str(self.listing([]))])
        self.assertEqual(code, 77, output)
        self.assertIn("SKIP", output)

    def test_words_print_on_one_line(self) -> None:
        self.assertEqual(coverage.shown("a\nb\tc"), "a\\nb\\tc")
        self.assertEqual(coverage.section_problem("Line one\nline two"), "it holds '\\n'")
        self.assertIsNone(coverage.section_problem("Settings › Downloads"))


if __name__ == "__main__":
    unittest.main()
