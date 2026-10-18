# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""The translation tool's checks catch what would break a table or a briefing."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools import translate


def pack(tag: str, modern: bool = True) -> translate.Pack:
    """A pack's values without its folder, for the character rules."""
    value = translate.Pack.__new__(translate.Pack)
    value.tag = tag
    value.word = "Word"
    value.english_name = "Word"
    value.modern = modern
    value.script = translate.SCRIPTS.get(tag.split("-")[0].lower())
    return value


class ValueTests(unittest.TestCase):
    def problems(self, english: str, value: str, tag: str = "ru", modern: bool = True) -> list[str]:
        return translate.check_value("I0001", english, value, pack(tag, modern))

    def test_a_good_value_passes(self) -> None:
        self.assertEqual(self.problems("{count} files differ", "Различаются файлы: {count}"), [])

    def test_a_semicolon_ends_the_value_early(self) -> None:
        self.assertTrue(any("';'" in p for p in self.problems("Saved", "Сохранено; готово")))

    def test_a_dropped_place_is_caught(self) -> None:
        self.assertTrue(any("drops {name}" in p for p in self.problems("Remove {name}?", "Удалить?")))

    def test_printf_order_is_kept(self) -> None:
        found = self.problems("%s has %d units", "%d юнитов у %s")
        self.assertTrue(any("printf" in p for p in found))

    def test_stages_are_kept(self) -> None:
        found = self.problems("Easy|Medium|Hard", "Легко|Сложно")
        self.assertTrue(any("'|'" in p for p in found))

    def test_another_script_is_caught(self) -> None:
        self.assertTrue(any("cannot hold" in p for p in self.problems("Off", "Выкл 关")))

    def test_russian_and_ukrainian_keep_their_own_letters(self) -> None:
        self.assertTrue(any("cannot hold" in p for p in self.problems("Units", "Підрозділи", "ru")))
        self.assertTrue(any("cannot hold" in p for p in self.problems("Units", "Юниты", "uk") if "ы" in p))
        self.assertEqual(self.problems("Units", "Юниты", "ru"), [])

    def test_japanese_keeps_its_own_punctuation(self) -> None:
        self.assertEqual(self.problems("Settings were not saved.", "設定を保存できませんでした。", "ja"), [])
        self.assertTrue(any("cannot hold" in p for p in self.problems("Off", "オフ 끔", "ja")))

    def test_a_code_page_pack_keeps_to_windows_1252(self) -> None:
        self.assertEqual(self.problems("Saved games", "Jogos salvos ação", "pt-BR", False), [])
        found = self.problems("Off", "Desligado ő", "pt-BR", False)
        self.assertTrue(any("cannot hold" in p for p in found))


class ChunkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scratch = tempfile.TemporaryDirectory()
        self.work = Path(self.scratch.name)
        for sub in ("in", "out/briefs", "en-briefs"):
            (self.work / sub).mkdir(parents=True)
        (self.work / "work.json").write_text(json.dumps({"tag": "uk", "template": "uk"}))

    def tearDown(self) -> None:
        self.scratch.cleanup()

    def test_every_id_once(self) -> None:
        (self.work / "in" / "units.txt").write_text(
            "@U0000\nUNIT: ARMCOM name\nEN: Commander\n\n@U0001\nEN: Kbot\n", encoding="utf-8")
        (self.work / "out" / "units.tsv").write_text(
            "U0000\tКомандир\nU0000\tКомандир\nU0002\tРобот\n", encoding="utf-8")
        problems, count = translate.validate_tsv(self.work, "units", pack("uk"))
        self.assertEqual(count, 2)
        self.assertIn("U0000: given twice", problems)
        self.assertTrue(any(p.startswith("U0001: missing") for p in problems))
        self.assertIn("U0002: not an id of this chunk", problems)

    def test_a_briefing_keeps_its_lines_marks_and_numbers(self) -> None:
        (self.work / "in" / "briefs-1.list").write_text("ArmCampaign1.txt\n", encoding="utf-8")
        english = "MISSION 1.0001ARME\n\n&RExpect 3 patrols.&\nEND\n"
        (self.work / "en-briefs" / "ArmCampaign1.txt").write_text(english, encoding="utf-8")
        (self.work / "out" / "briefs" / "ArmCampaign1.txt").write_text(
            "МІСІЯ 1.0001ARME\n&RЧекайте патрулів.\nКІНЕЦЬ\n", encoding="utf-8")
        problems, _count = translate.validate_briefs(self.work, "briefs-1", pack("uk"))
        self.assertTrue(any("4 lines in the English, 3 here" in p for p in problems))
        self.assertTrue(any("'&'" in p for p in problems))
        self.assertTrue(any("['3']" in p for p in problems))


if __name__ == "__main__":
    unittest.main()
