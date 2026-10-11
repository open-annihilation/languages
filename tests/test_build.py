# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""build.py stages fonts, writes the build info, and stops when a font is missing."""

from __future__ import annotations

import hashlib
import json
import stat
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from tests.faces import pack_characters, ranges_of, write_face
from tools import oamod_yaml
from tools.build import worktree_dirty

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tests" / "fixtures" / "bin" / "oa-tool"
FIELDS = {"commit", "dirty", "revision", "sha256", "size", "tag"}


class BuildTests(unittest.TestCase):
    def setUp(self) -> None:
        mode = TOOL.stat().st_mode
        if not mode & stat.S_IXUSR:
            TOOL.chmod(mode | stat.S_IXUSR)

    def build(self, out: Path, fonts: Path, tag: str = "zh-Hans") -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / "tools" / "build.py"), tag,
             "--oa-tool", str(TOOL), "--fonts", str(fonts), "--out", str(out)],
            cwd=ROOT, capture_output=True, text=True,
        )

    def test_build_stages_fonts_and_writes_build_info(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            fonts = folder / "fonts"
            fonts.mkdir()
            write_face(fonts / "NotoSansCJKsc-Bold.otf", ranges_of(pack_characters(ROOT / "zh-Hans")))
            out = folder / "out"
            first = self.build(out, fonts)
            self.assertEqual(first.returncode, 0, first.stderr + first.stdout)
            second = self.build(out, fonts)
            self.assertEqual(second.returncode, 0, second.stderr + second.stdout)
            package = out / "zh-Hans.oalang"
            info = json.loads((out / "zh-Hans.oalang.json").read_text(encoding="utf-8"))
            self.assertEqual(set(info), FIELDS)
            self.assertIsInstance(info["tag"], str)
            self.assertIsInstance(info["commit"], str)
            self.assertIsInstance(info["dirty"], bool)
            self.assertIsInstance(info["revision"], int)
            self.assertIsInstance(info["size"], int)
            self.assertIsInstance(info["sha256"], str)
            self.assertEqual(info["tag"], "zh-Hans")
            manifest = oamod_yaml.loads((ROOT / "zh-Hans" / "language.yaml").read_bytes())
            self.assertEqual(info["revision"], manifest["packaging"]["revision"])
            self.assertEqual(info["size"], package.stat().st_size)
            self.assertEqual(info["sha256"], hashlib.sha256(package.read_bytes()).hexdigest())
            self.assertEqual(info["dirty"], worktree_dirty(ROOT))
            self.assertRegex(info["sha256"], r"^[0-9a-f]{64}$")
            self.assertEqual(info["commit"], subprocess.run(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True
            ).stdout.strip())
            line = first.stdout.strip().splitlines()[-1]
            self.assertEqual(line.split()[1:], [str(info["size"]), info["sha256"]])
            self.assertEqual(first.stdout.strip().splitlines()[-1].split()[-1],
                             second.stdout.strip().splitlines()[-1].split()[-1])
            staged = ROOT / "local" / "stage" / "zh-Hans" / "fonts"
            self.assertTrue((staged / "NotoSansCJKsc-Bold.otf").is_file())
            licence = staged / "NotoSansCJK-OFL.txt"
            self.assertEqual(licence.read_bytes(), (ROOT / "fonts" / "NotoSansCJK-OFL.txt").read_bytes())
            with zipfile.ZipFile(package) as archive:
                names = archive.namelist()
            self.assertIn("language.yaml", names)
            self.assertIn("fonts/NotoSansCJKsc-Bold.otf", names)
            self.assertIn("fonts/NotoSansCJK-OFL.txt", names)
            self.assertFalse(any(name.startswith("zh-Hans/") for name in names))

    def test_missing_font_stops(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            fonts = folder / "empty"
            fonts.mkdir()
            out = folder / "out"
            result = self.build(out, fonts)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("run python3 tools/fonts.py first", result.stderr)
            self.assertFalse((out / "zh-Hans.oalang").exists())

    def test_dirty_follows_a_change_in_a_repository(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            git = ["git", "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null"]
            subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "pack@example.com"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "Pack Test"], cwd=root, check=True)
            (root / "README").write_text("pack\n", encoding="utf-8")
            subprocess.run(["git", "add", "README"], cwd=root, check=True)
            subprocess.run([*git, "commit", "-m", "start"], cwd=root, check=True, capture_output=True)
            self.assertFalse(worktree_dirty(root))
            (root / "change").write_text("changed\n", encoding="utf-8")
            self.assertTrue(worktree_dirty(root))


if __name__ == "__main__":
    unittest.main()
