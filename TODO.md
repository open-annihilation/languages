# To do

## Brazilian Portuguese (`pt-BR`)

The pack is complete and checks clean: every interface word, 3.1c's texts,
the units, the missions and the 175 briefings, fitting every screen the
text-fit check measures. It is not published yet. These are what is left,
most important first. `python3 tools/screens.py pt-BR …` (see
[adding a language, step 9](docs/new-language.md#9-look-at-it-in-the-game))
shows each problem on screen.

### 1. 3.1c's menu buttons draw a box for some Portuguese letters (engine)

**What the player sees.** On 3.1c's own buttons and labels, a box in place of
a letter: `Opç□es` on the single-player menu, `OP□□ES` on the in-game
menu, `Posiç□o` and `Linha de vis□o` in the skirmish setup, `Sem narraç□o`
on the briefing's narration button. A test pack showed the letters hit:
ã, õ, Ã, Õ, Ç, Â, Ê, Ô and À. The small â, ê, ô and à draw, as do á, é, í,
ó, ú, ç and their capitals Á, É, Í, Ó, Ú. Briefings, help and Open
Annihilation's own screens draw every letter.

**What is known.**

- 3.1c's menu fonts, `anims/hattfont12.GAF` and `anims/hattfont11.GAF` (in
  `totala1.hpi`, with later copies in `ccdata.ccx`, `btdata.ccx` and
  `rev31.gp3`), hold a placeholder box in those letters' Windows-1252
  slots. In every copy the box is the same picture as the font's frame 0:
  the same size, origin and pixels.
- The engine means to hand such a letter to the modern fonts. For a letter
  in the code page it asks the font, letter by letter, whether it has a
  real glyph: `present::FontCharacters::gui_font`, fed by
  `frontend_renderer::gui_font_characters`
  (`src/ui/frontend-renderer/src/game_text.cpp`) and gadget-render's
  `font_characters` (`src/ui/gadget-render/src/gadget_text.cpp`), each of
  which counts a frame as missing when `present::same_glyph` finds it equal
  to frame 0.
- At run time that check still takes the boxes for letters. The proof is
  Ç: the font holds a real Ç in its DOS slot, `0x80`, which
  `FontCharacters::gui_font` uses when the Windows-1252 slot `0xC7` is
  missing, yet the screen shows the box. Find why: whether frame 0 reaches
  the check as the same sprite (the gadget renderer's frames come through
  `frontend-dialogs/src/dialog_art.cpp`, which re-encodes compressed
  frames), whether the kept characters are worked out from another copy of
  the font, or whether these captions are drawn by a path that skips
  `split_text`.
- Korean, Japanese, Russian and Ukrainian are not hit: their letters are
  outside the code page, so their captions go to the modern fonts whole,
  without the per-letter check. Other Latin languages whose extra letters
  are outside the code page (Polish, Turkish) would not be hit either.

**Done when** the screens pictures show `Opções`, `OPÇÕES`, `Posição` and
`Linha de visão` whole, and an engine test covers a GUI font whose
placeholder frames equal frame 0. Then publish the pack (or publish it
before, with the boxes, if the maintainer chooses).

### 2. The pack's name on the first-start language card

The manifest's `name` is `Português (BR)`. `Português (Brasil)` wraps onto
a second line of first start's language card at 640x480 and runs over the
English name beneath it, and the text-fit check fails on it. One pack
serves Brazil and Portugal (its locales are `pt-BR`, `pt` and `pt-PT`), so
the simplest fix is `name: Português`, keeping `english-name: Portuguese
(Brazil)` so the card still says which Portuguese it is; that passes the
check. The other way is an engine change that lets the card take a longer
name.

### 3. The engine's languages page misstates what a Windows-1252 language needs (docs)

The engine's `docs/languages.md` ("Adding a language") says a language
whose letters are all in Windows-1252, "as Portuguese's or Dutch's are,
needs nothing more". Two things make that untrue today:

- A pack's tables are UTF-8, and the engine reads them as UTF-8 only while
  `unicode: true` or the modern fonts are on; a pack in the game's own
  fonts without `unicode: true` shows every accented letter as two wrong
  characters (`OpÃ§Ãµes`).
- 3.1c's menu fonts lack the letters in item 1.

Correct the page; `docs/new-language.md` here already says both. Also make
`tools/check.py` refuse a pack in the game's own fonts that does not set
`unicode: true`.

### 4. A native speaker's reading

The pack was translated in one pass with a glossary
(`docs/glossaries/pt-BR.md`) and has not been read by a Brazilian player.
The choices the translator was least sure of: `Briefing` kept as a
loanword, `Destróier`, `ABERTURA` for INTRO, `Sim`/`Não` for 3.1c's On/Off
(as its French and Italian do), `RECICLAR` for reclaim rather than
`RECUPERAR`, the Serpent and the Scorpion left in English in the
briefings, and every unit's proper name left in English (Peewee, Big
Bertha) while the generic names are translated.
