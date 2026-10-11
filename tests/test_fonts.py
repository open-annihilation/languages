# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""The font pins, the character set and a download whose SHA-256 does not match."""

from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from tests.faces import face as face_bytes
from tests.faces import write_face
from tools import fonts

COLLECTION = "faa5f3656a78b2e2d450d27fe8382c778bc2b6bb5ea29c986664a6a435056ceb"
LICENCE = "6a73f9541c2de74158c0e7cf6b0a58ef774f5a780bf191f2d7ec9cc53efe2bf2"
UNIHAN = "b8f000df69de7828d21326a2ffea462b04bc7560022989f7cc704f10521ef3e0"
CUT = "1bff16d425a0bc5048fddb7d33d2a59e08647d4a29380a348ccaabcbd89a29f2"


def unihan_zip(path: Path, count: int) -> None:
    lines = [f"U+{0x4E00 + index:04X}\tkTGH\t{index}\n" for index in range(count)]
    lines.append("# not a mapping\n")
    lines.append("U+4E00\tkDefinition\tignored\n")
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("Unihan_OtherMappings.txt", "".join(lines))


class FontTests(unittest.TestCase):
    def test_pins_are_well_formed(self) -> None:
        data = fonts.load_pins()
        self.assertEqual(fonts.pin_problems(data), [])
        downloads = {item["file"]: item for item in data["downloads"]}
        self.assertEqual(downloads["NotoSansCJK-Bold-2.004.ttc"]["sha256"], COLLECTION)
        self.assertEqual(downloads["NotoSansCJK-2.004-LICENSE"]["sha256"], LICENCE)
        self.assertEqual(downloads["Unihan-16.0.0.zip"]["sha256"], UNIHAN)
        for item in data["downloads"]:
            self.assertTrue(item["url"].startswith("https://"), item["url"])
            self.assertEqual(set(item), {"file", "url", "sha256"})
        face = data["fonts"]["NotoSansCJKsc-Bold.otf"]
        self.assertEqual(face["download"], "NotoSansCJK-Bold-2.004.ttc")
        self.assertEqual(face["face"], 2)
        self.assertEqual(face["characters"], "common-cjk")
        self.assertEqual(face["count"], 15309)
        self.assertEqual(face["sha256"], CUT)
        self.assertEqual(face["licence"], "NotoSansCJK-OFL.txt")
        self.assertEqual(fonts.self_test(), 0)

    def test_cjk_characters_hold_14066(self) -> None:
        characters = fonts.cjk_characters()
        self.assertEqual(len(characters), 14066)
        self.assertIn(ord("中"), characters)

    def test_general_standard_table_must_hold_8105(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            good = folder / "good.zip"
            short = folder / "short.zip"
            unihan_zip(good, 8105)
            unihan_zip(short, 8104)
            self.assertEqual(len(fonts.general_standard_characters(good)), 8105)
            with self.assertRaises(RuntimeError):
                fonts.general_standard_characters(short)

    def test_face_characters_read_formats_4_and_12(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            ranges = [(0x20, 0x7E), (0x4E00, 0x4E10), (0xFF01, 0xFF01)]
            for form in (4, 12):
                face = write_face(folder / f"face{form}.otf", ranges, form=form)
                held = fonts.face_characters(face)
                self.assertEqual(held, {c for first, last in ranges for c in range(first, last + 1)})
            wide = write_face(folder / "wide.otf", [(0x20000, 0x20002)])
            self.assertEqual(fonts.face_characters(wide), {0x20000, 0x20001, 0x20002})
            collection = folder / "collection.ttc"
            collection.write_bytes(b"ttcf" + bytes(60))
            with self.assertRaises(ValueError):
                fonts.face_characters(collection)
            short = folder / "short.otf"
            short.write_bytes(face_bytes([(0x4E00, 0x4E10)])[:40])
            with self.assertRaises(ValueError):
                fonts.face_characters(short)

    def test_cjk_blocks(self) -> None:
        for character in "中，。（「ア한𠀀":
            self.assertTrue(fonts.cjk_block(ord(character)), character)
        for character in "A›…—·✕é":
            self.assertFalse(fonts.cjk_block(ord(character)), character)

    def test_download_with_the_wrong_sha256_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            payload = folder / "payload"
            payload.write_bytes(b"not-the-font")
            destination = folder / "deps"
            destination.mkdir()
            url = "file://" + payload.resolve().as_posix()
            with self.assertRaises(RuntimeError):
                fonts.fetch_download(destination, {
                    "file": "payload",
                    "url": url,
                    "sha256": "0" * 64,
                })
            self.assertFalse((destination / "payload").exists())


if __name__ == "__main__":
    unittest.main()
