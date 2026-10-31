# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""The pack checker accepts the zh-Hans source and refuses broken fixtures."""

from __future__ import annotations

import contextlib
import io
import shutil
import tempfile
import unittest
from pathlib import Path

from tests.faces import pack_characters, ranges_of, write_face
from tools import check

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"
FACE = "NotoSansCJKsc-Bold.otf"
KOREAN_FACE = "NotoSansCJKkr-Bold.otf"
JAPANESE_FACE = "NotoSansCJKjp-Bold.otf"


def run(args: list[str]) -> tuple[int, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = check.main(args)
    return code, buffer.getvalue()


class CheckTests(unittest.TestCase):
    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.empty = Path(self.folder.name) / "empty"
        self.empty.mkdir()

    def test_zh_hans_source_is_clean(self) -> None:
        # With no face built and no Unihan archive, the check keeps the pack
        # to the cut's code pages.
        code, output = run([str(ROOT / "zh-Hans"), "--source", "--fonts", str(self.empty),
                            "--deps", str(self.empty)])
        self.assertEqual(code, 0, output)
        self.assertIn("checked against the cut's code pages only", output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_zh_hans_without_source_misses_its_font(self) -> None:
        code, output = run([str(ROOT / "zh-Hans"), "--fonts", str(self.empty)])
        self.assertEqual(code, 1, output)
        self.assertIn("fonts/NotoSansCJKsc-Bold.otf is not a file", output)

    def test_zh_hans_with_its_face_built_is_clean(self) -> None:
        faces = Path(self.folder.name) / "faces"
        write_face(faces / FACE, ranges_of(pack_characters(ROOT / "zh-Hans")))
        code, output = run([str(ROOT / "zh-Hans"), "--fonts", str(faces)])
        self.assertEqual(code, 0, output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_a_character_the_built_face_lacks_fails(self) -> None:
        faces = Path(self.folder.name) / "faces"
        held = pack_characters(ROOT / "zh-Hans") - {ord("模")}
        write_face(faces / FACE, ranges_of(held))
        code, output = run([str(ROOT / "zh-Hans"), "--fonts", str(faces)])
        self.assertEqual(code, 1, output)
        self.assertIn("interface.tdf uses 1 character the pack's fonts lack: 模 (U+6A21, line", output)

    def test_all_source_is_clean(self) -> None:
        code, output = run(["--all", "--source", "--fonts", str(self.empty), "--deps", str(self.empty)])
        self.assertEqual(code, 0, output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_a_character_outside_the_packs_face_fails(self) -> None:
        pack = Path(self.folder.name) / "outside-cut"
        shutil.copytree(FIXTURES / "outside-cut", pack)
        write_face(pack / "fonts" / "Fixture.otf", ranges_of({ord("中"), ord("文")}), form=4)
        code, output = run([str(pack)])
        self.assertEqual(code, 1, output)
        self.assertIn("interface.tdf uses 1 character the pack's fonts lack: 𠀀 (U+20000, line 6)", output)
        write_face(pack / "fonts" / "Fixture.otf", ranges_of({ord("中"), ord("文"), 0x20000}))
        code, output = run([str(pack)])
        self.assertEqual(code, 0, output)

    def test_a_character_outside_the_recipe_fails(self) -> None:
        code, output = run([str(FIXTURES / "outside-cut"), "--deps", str(self.empty)])
        self.assertEqual(code, 1, output)
        self.assertIn("fonts/Fixture.otf is not a file", output)
        self.assertIn("checked against the cut's code pages only", output)
        self.assertIn("𠀀 (U+20000, line 6)", output)
        self.assertNotIn("中 (U+4E2D", output)

    def test_a_face_that_cannot_be_read_fails(self) -> None:
        pack = Path(self.folder.name) / "outside-cut"
        shutil.copytree(FIXTURES / "outside-cut", pack)
        (pack / "fonts").mkdir()
        (pack / "fonts" / "Fixture.otf").write_bytes(b"otf")
        code, output = run([str(pack)])
        self.assertEqual(code, 1, output)
        self.assertIn("fonts/Fixture.otf cannot be read", output)

    def test_a_dropped_place_or_number_fails(self) -> None:
        code, output = run([str(FIXTURES / "dropped-place")])
        self.assertEqual(code, 1, output)
        self.assertIn("[Needs {size} free] dropped-place drops {size}", output)
        self.assertIn("[In to 2x normal size at most.] dropped-place drops the number 2", output)
        self.assertIn("[Downloading %s] dropped-place adds %d", output)
        self.assertNotIn("[{done} of {total}]", output)

    def test_patterns(self) -> None:
        self.assertEqual(check.pattern_problems("{n} min ago", "{n}分钟前"), [])
        self.assertEqual(check.pattern_problems("Out to 1/32 of normal size", "缩小到1/32"), [])
        self.assertEqual(check.pattern_problems("about a minute left", "还剩约1分钟"), [])
        self.assertEqual(check.pattern_problems("{a}, {b}", "{a}、{a}"), ["drops {b}", "adds {a}"])
        self.assertEqual(check.pattern_problems("50% done: %s", "完成50%：%s"), [])
        self.assertEqual(check.pattern_problems("16x16 samples", "16x采样"), ["drops the number 16"])

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

    def test_uk_source_is_clean(self) -> None:
        # Ukrainian brings no font: the engine's own faces draw its Cyrillic.
        code, output = run([str(ROOT / "uk"), "--source", "--fonts", str(self.empty),
                            "--deps", str(self.empty)])
        self.assertEqual(code, 0, output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_ko_source_is_clean(self) -> None:
        # With no face built, the Korean text is kept to the Hangul cut's
        # recipe, which needs no download.
        code, output = run([str(ROOT / "ko"), "--source", "--fonts", str(self.empty),
                            "--deps", str(self.empty)])
        self.assertEqual(code, 0, output)
        self.assertIn("the Korean face is not built: characters are checked against its recipe", output)
        self.assertNotIn("Unihan", output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_ko_with_its_face_built_is_clean(self) -> None:
        faces = Path(self.folder.name) / "faces"
        write_face(faces / KOREAN_FACE, ranges_of(pack_characters(ROOT / "ko")))
        code, output = run([str(ROOT / "ko"), "--fonts", str(faces)])
        self.assertEqual(code, 0, output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_a_syllable_the_korean_face_lacks_fails(self) -> None:
        faces = Path(self.folder.name) / "faces"
        write_face(faces / KOREAN_FACE, ranges_of(pack_characters(ROOT / "ko") - {ord("한")}))
        code, output = run([str(ROOT / "ko"), "--fonts", str(faces)])
        self.assertEqual(code, 1, output)
        self.assertIn("character the pack's fonts lack: 한 (U+D55C, line", output)

    def test_ja_source_is_clean(self) -> None:
        # With no face built and no Unihan archive, the Japanese text is kept
        # to JIS X 0208's characters, which hold every kanji the pack uses.
        code, output = run([str(ROOT / "ja"), "--source", "--fonts", str(self.empty),
                            "--deps", str(self.empty)])
        self.assertEqual(code, 0, output)
        self.assertIn("the Japanese face is not built and the Unihan archive is not in --deps: "
                      "characters are checked against JIS X 0208 only", output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_ja_with_its_face_built_is_clean(self) -> None:
        faces = Path(self.folder.name) / "faces"
        write_face(faces / JAPANESE_FACE, ranges_of(pack_characters(ROOT / "ja")))
        code, output = run([str(ROOT / "ja"), "--fonts", str(faces)])
        self.assertEqual(code, 0, output)
        self.assertTrue(output.rstrip().endswith("clean"), output)

    def test_a_kana_the_japanese_face_lacks_fails(self) -> None:
        faces = Path(self.folder.name) / "faces"
        write_face(faces / JAPANESE_FACE, ranges_of(pack_characters(ROOT / "ja") - {ord("ボ")}))
        code, output = run([str(ROOT / "ja"), "--fonts", str(faces)])
        self.assertEqual(code, 1, output)
        self.assertIn("character the pack's fonts lack: ボ (U+30DC, line", output)

    def test_hanja_outside_the_hangul_recipe_fails(self) -> None:
        code, output = run([str(FIXTURES / "hanja"), "--source", "--fonts", str(self.empty),
                            "--deps", str(self.empty)])
        self.assertEqual(code, 1, output)
        self.assertIn("interface.tdf uses 2 characters the pack's fonts lack: "
                      "韓 (U+97D3, line 10), 國 (U+570B, line 10)", output)
        self.assertNotIn("한", output)

    def test_hanzi_outside_the_japanese_recipe_fails(self) -> None:
        # With no face built and no Unihan archive, the Japanese text is kept
        # to JIS X 0208's characters and the kana and punctuation blocks.
        code, output = run([str(FIXTURES / "hanzi"), "--source", "--fonts", str(self.empty),
                            "--deps", str(self.empty)])
        self.assertEqual(code, 1, output)
        self.assertIn("the Japanese face is not built and the Unihan archive is not in --deps: "
                      "characters are checked against JIS X 0208 only", output)
        self.assertIn("interface.tdf uses 2 characters the pack's fonts lack: "
                      "简 (U+7B80, line 10), 们 (U+4EEC, line 10)", output)
        self.assertNotIn("日 (U+65E5", output)
        self.assertNotIn("ー (U+30FC", output)

    def test_cyrillic_is_drawn_by_the_recorded_engine_faces(self) -> None:
        code, output = run([str(FIXTURES / "cyrillic")])
        self.assertEqual(code, 0, output)
        self.assertNotIn("lack", output)

    def engine_fonts(self, codes: set[int], bold: set[int] = frozenset()) -> Path:
        """An engine fonts folder whose faces hold codes in every weight and bold in bold only."""
        folder = Path(self.folder.name) / "engine-fonts"
        write_face(folder / "DejaVuSans-Bold.ttf", ranges_of(set(codes) | set(bold)))
        write_face(folder / "DejaVuSans.ttf", ranges_of(set(codes)))
        write_face(folder / "NotoSansCJKsc-Bold-Endonyms.otf", ranges_of({ord("中")}))
        write_face(folder / "NotoEmoji.ttf", ranges_of({0x1F600}))
        return folder

    def fixture_characters(self) -> set[int]:
        text = (FIXTURES / "cyrillic" / "interface.tdf").read_text(encoding="utf-8")
        return {ord(character) for character in text}

    def test_a_character_the_engine_faces_lack_fails(self) -> None:
        folder = self.engine_fonts(self.fixture_characters() - {ord("ї")})
        code, output = run([str(FIXTURES / "cyrillic"), "--engine-fonts", str(folder)])
        self.assertEqual(code, 1, output)
        self.assertIn(
            "interface.tdf uses 1 character the engine's faces and the pack's fonts lack: "
            "ї (U+0457, line 11)", output)

    def test_a_character_only_bold_draws_fails(self) -> None:
        folder = self.engine_fonts(self.fixture_characters() - {ord("ґ")}, {ord("ґ")})
        code, output = run([str(FIXTURES / "cyrillic"), "--engine-fonts", str(folder)])
        self.assertEqual(code, 1, output)
        self.assertIn("ґ (U+0491, line 11)", output)

    def test_engine_fonts_that_hold_every_character_are_clean(self) -> None:
        folder = self.engine_fonts(self.fixture_characters())
        code, output = run([str(FIXTURES / "cyrillic"), "--engine-fonts", str(folder)])
        self.assertEqual(code, 0, output)

    def test_a_letters_face_draws_what_the_engine_lacks(self) -> None:
        pack = Path(self.folder.name) / "cyrillic"
        shutil.copytree(FIXTURES / "cyrillic", pack)
        manifest = pack / "language.yaml"
        manifest.write_text(
            manifest.read_text(encoding="utf-8")
            + "fonts: [{file: Letters.otf, role: letters}]\n", encoding="utf-8")
        write_face(pack / "fonts" / "Letters.otf", ranges_of({ord("ї")}))
        folder = self.engine_fonts(self.fixture_characters() - {ord("ї")})
        code, output = run([str(pack), "--engine-fonts", str(folder)])
        self.assertEqual(code, 0, output)

    def test_engine_fonts_that_cannot_be_read_fail(self) -> None:
        code, output = run([str(FIXTURES / "cyrillic"), "--engine-fonts", str(self.empty)])
        self.assertEqual(code, 1, output)
        self.assertIn("the engine's faces cannot be read from", output)

    def test_cyrillic_in_the_game_fonts_fails(self) -> None:
        pack = Path(self.folder.name) / "cyrillic"
        shutil.copytree(FIXTURES / "cyrillic", pack)
        manifest = pack / "language.yaml"
        manifest.write_text(
            manifest.read_text(encoding="utf-8").replace("modern-fonts", "game-fonts"),
            encoding="utf-8")
        code, output = run([str(pack)])
        self.assertEqual(code, 1, output)
        self.assertIn("interface.tdf uses 21 characters the game's fonts (Windows-1252) lack: "
                      "М (U+041C, line 6)", output)
        self.assertNotIn("«", output)  # Windows-1252 holds the guillemets and the dash
        self.assertNotIn("does not set unicode: true", output)

    def test_the_game_fonts_without_unicode_fail(self) -> None:
        pack = Path(self.folder.name) / "cyrillic"
        shutil.copytree(FIXTURES / "cyrillic", pack)
        manifest = pack / "language.yaml"
        manifest.write_text(
            manifest.read_text(encoding="utf-8")
            .replace("modern-fonts", "game-fonts").replace("unicode: true\n", ""),
            encoding="utf-8")
        code, output = run([str(pack)])
        self.assertEqual(code, 1, output)
        self.assertEqual(output.count("does not set unicode: true"), 1, output)
        self.assertIn("interface.tdf holds М (U+041C, line 6), which would show garbled", output)

    def test_missing_pack_is_skipped(self) -> None:
        code, output = run([str(FIXTURES / "not-a-pack")])
        self.assertEqual(code, 77, output)
        self.assertIn("SKIP", output)


if __name__ == "__main__":
    unittest.main()
