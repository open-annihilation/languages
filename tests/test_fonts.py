# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""The font pins, the character set, the engine faces' record and a download whose SHA-256 does not match."""

from __future__ import annotations

import json
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
UKRAINIAN = (
    "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    "ʼ’«»—–…№"
)


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

    def test_engine_faces_record_is_well_formed(self) -> None:
        data = json.loads(fonts.ENGINE_FACES.read_text(encoding="utf-8"))
        self.assertEqual(fonts.engine_face_problems(data), [])
        self.assertEqual(list(data["faces"]), list(fonts.ENGINE_FACE_FILES))
        held = fonts.engine_characters()
        for character in UKRAINIAN:
            self.assertIn(ord(character), held, character)

    def test_engine_faces_are_recorded_and_read_back(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "fonts"
            write_face(folder / "DejaVuSans-Bold.ttf", [(0x20, 0x7E), (0x0400, 0x045F)])
            write_face(folder / "DejaVuSans.ttf", [(0x20, 0x7E), (0x0400, 0x044F)], form=4)
            write_face(folder / "NotoSansCJKsc-Bold-Endonyms.otf", [(0x4E2D, 0x4E2D)])
            write_face(folder / "NotoEmoji.ttf", [(0x1F600, 0x1F601)])
            data = fonts.record_engine_faces(folder)
            self.assertEqual(fonts.engine_face_problems(data), [])
            self.assertEqual(data["faces"]["DejaVuSans.ttf"]["characters"], ["0020-007E", "0400-044F"])
            record = Path(tmp) / "engine-faces.json"
            record.write_text(json.dumps(data), encoding="utf-8")
            expected = {*range(0x20, 0x7F), *range(0x0400, 0x0450), 0x4E2D, 0x1F600, 0x1F601}
            # U+0450-U+045F are in the bold face alone, so not in every weight.
            self.assertEqual(fonts.engine_characters(record=record), expected)
            self.assertEqual(fonts.engine_characters(folder), expected)
            (folder / "NotoEmoji.ttf").unlink()
            with self.assertRaises(OSError):
                fonts.record_engine_faces(folder)

    def test_engine_face_problems(self) -> None:
        self.assertEqual(fonts.engine_face_problems([]), ["the record holds no faces"])
        faces = {name: {"characters": ["0020-007E"], "sha256": "0" * 64}
                 for name in fonts.ENGINE_FACE_FILES}
        self.assertEqual(fonts.engine_face_problems({"faces": faces}), [])
        faces["NotoEmoji.ttf"] = {"characters": ["007E-0020"], "sha256": "0" * 64}
        self.assertEqual(fonts.engine_face_problems({"faces": faces}),
                         ["NotoEmoji.ttf: '007E-0020' is not a run of code points"])
        del faces["NotoEmoji.ttf"]
        self.assertIn("the record does not name the engine's four faces in their order",
                      fonts.engine_face_problems({"faces": faces}))

    def test_code_ranges(self) -> None:
        codes = {0x41, 0x42, 0x43, 0x4E2D, 0x1F600}
        runs = fonts.code_ranges(codes)
        self.assertEqual(runs, ["0041-0043", "4E2D", "1F600"])
        self.assertEqual(fonts.range_codes(runs), codes)
        for bad in ("41", "0041-", "zz00", 65):
            with self.assertRaises(ValueError):
                fonts.range_codes([bad])

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
