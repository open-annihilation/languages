# Add a language

This is the whole way from nothing to a published pack, in order. Each step
says what to run, what it writes and what must be true before the next
step. The Korean pack was made this way; `docs/glossaries/ko.md` is its
glossary.

A pack is a folder named by its tag (`ja/`, `pt-BR/`) beside `zh-Hans/`,
`uk/` and `ko/`. The engine's [languages page](https://github.com/open-annihilation/open-annihilation/blob/main/docs/languages.md)
is the authority on what a pack may hold. This page is how this repository
makes one.

## What you need

- An engine build of the current release: its `oa-tool`, and the game
  itself (`open-annihilation.app/Contents/MacOS/open-annihilation` on
  macOS, `open-annihilation` elsewhere). The tools take them as `--oa-tool`
  and `--engine`, or `OA_TOOL` for the first.
- A Total Annihilation 3.1c install with both expansions, The Core
  Contingency and Battle Tactics: the missions' names and the briefings'
  English are read from it. Nothing is copied from it into this repository.
- Python 3.11 or later. A pack that needs a font of its own also needs the
  fontTools environment `tools/fonts.py` makes.

Keep scratch work under `local/` (for example `local/work/<tag>`): it is
never committed.

## 1. Decide how the text is drawn

The game draws text two ways, and the pack's manifest says which it needs.

- **The game's own fonts.** A language whose letters are all in Windows-1252
  can in principle be drawn as 3.1c draws English, German, French, Spanish
  and Italian: no `text` key, and every character of the pack within
  Windows-1252 (`tools/check.py` fails any other; `tools/translate.py
  validate` then refuses the English's own ✓, ✕ and →). Two things stand in
  the way today. A pack's tables are UTF-8, and this engine reads them as
  UTF-8 only while `unicode: true` or the modern fonts are on, so a pack in
  the game's fonts needs `unicode: true` too, or every accented letter
  shows garbled. And 3.1c's menu fonts (`hattfont11.gaf`, `hattfont12.gaf`)
  hold a box, not a letter, for ã, õ, Ã, Õ, Ç, Â, Ê, Ô and À, which this
  engine draws as it finds it; their other fonts hold every letter of the
  code page. Portuguese needs those letters, so its pack uses the modern
  fonts, and its menu captions still show the boxes until the engine draws
  them in the modern fonts instead.

  Decide with a probe before translating: a manifest, a `translate.tdf`
  with a few of the main menu's and the single-player menu's captions
  holding every accented letter the language uses, capitals included, and
  one briefing with the same letters. Build it and take its pictures (step
  9); every letter must show, not as a gap, a box or two wrong characters.
- **The modern fonts.** Any other language: `text: {needs: modern-fonts}`
  and `unicode: true`. The sans faces that travel with the engine draw
  Latin, Greek and Cyrillic, so a Russian or Ukrainian pack brings no
  font. Chinese, Japanese and Korean need a face of their own (step 7).
  `fonts/engine-faces.json` lists every character the engine's faces draw.

| Pack | Drawn with | Font in the pack |
|---|---|---|
| `zh-Hans` | modern fonts | `NotoSansCJKsc-Bold.otf` |
| `uk` | modern fonts | none |
| `ko` | modern fonts | `NotoSansCJKkr-Bold.otf` |
| `ja` | modern fonts | `NotoSansCJKjp-Bold.otf` |
| `ru` | modern fonts | none |
| `pt-BR` | modern fonts (3.1c's menu fonts lack some of its letters) | none |
| `pt-PT` | modern fonts (as `pt-BR`) | none |

## 2. Write the manifest

`<tag>/language.yaml` comes first: the other tools read its tag, word and
drawing needs. Copy the nearest pack's manifest and change every value:

```yaml
# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

# Russian, built by tools/build.py (README.md).
oalang: 1
tag: ru
name: Русский
english-name: Russian
word: Russian
version: "1"
locales: [ru, ru-RU, ru-BY, ru-KZ, ru-KG]
fallbacks: []
text: {needs: modern-fonts}
unicode: true
warmup: warmup.txt
packaging: {revision: 1, date: 2026-10-18, packager: open-annihilation/languages tools/build.py}
homepage: https://github.com/open-annihilation/languages
requires: {engine: ">= 0.8.0"}
```

- `tag` is the BCP 47 tag. `name` is the language's name in itself, as
  Settings › Language lists it. `english-name` is its name in English.
  First start's language card at 640x480 holds about 14 characters of the
  name: `Português (Brasil)` (18) fails the text-fit check and
  `Português (BR)` passes. Check the name with step 9 early.
- `word` is the English name the game data knows the language by: it keys
  `translate.tdf` (`Russian=…;`) and names the briefings' folder
  (`files/camps/briefs-Russian`).
- `locales` are the system locales that choose the language at first start.
- `requires.engine` is the oldest engine the pack's words are written for.
- `fonts` names a face in the pack's `fonts/` folder, with `role:
  ideographs` for a CJK face. Leave it out when the pack brings none.
- `packaging.revision` starts at 1. A revision is published once: the
  published ones are this repository's tags, `<tag>-r<revision>`.

The language's name is drawn before its pack is installed, in Settings ›
Language under AVAILABLE TO DOWNLOAD. Latin, Greek and Cyrillic names are
drawn by the sans faces. A CJK name must be in the engine's endonym face,
`NotoSansCJKsc-Bold-Endonyms.otf` in `fonts/engine-faces.json`. If a
character is not, the engine needs it added to its endonym list
(`tools/text-fonts/endonyms.txt` in the engine) before the pack is
published; say so in the pack's commit.

## 3. Prepare the work

```sh
python3 tools/translate.py prepare ru --work local/work/ru \
    --game-dir /path/to/totala --oa-tool /path/to/oa-tool
```

This reads the template pack (`--template`, Ukrainian by default) and the
reference packs (`--references`, `zh-Hans,uk,ko` by default), and writes
the work folder:

```
local/work/ru/
  work.json            the tag, template and references
  in/interface-1.txt … interface-5.txt   Open Annihilation's own words
  in/translate-1.txt … translate-3.txt   3.1c's own texts
  in/units.txt         the units' names and descriptions
  in/missions.txt      the missions' names
  in/briefs-1.list … briefs-5.list       the briefings, by name
  in/manifest.json     where each item goes in the tables
  en-briefs/           each briefing's English, as UTF-8 with LF line ends
  out/                 where the translations go
```

The template decides the new pack's layout: its tables' order, comments and
sections, and its set of briefings. Ukrainian is the template because it
stays closest to the English and its captions were already shortened where
3.1c's fixed-size buttons needed it.

A chunk lists its items, grouped under the template's comments:

```
## The order buttons' captions
@I0123
UNIT: ARMCOM name            (units and missions only: which unit or mission, and field)
EN: the English to translate
ZH-HANS: the Chinese pack's translation
UK: the Ukrainian pack's translation
KO: the Korean pack's translation
```

## 4. Write the glossary first

Before any chunk is translated, write `docs/glossaries/<tag>.md`, and keep
to it for every chunk. It is what keeps a pack written by several people,
or several sittings, in one voice, and what the next revision follows.
Model it on `docs/glossaries/ko.md`:

1. **Voice and grammar.** The register of statements, hints, instructions,
   questions, labels and status words; how the player is addressed; the
   briefings' military voice. The model is how the best-known RTS games
   of the era were localized for that language's players.
2. **Placeholders and numbers.** The hard rules of step 5, in the
   language's own terms (word order around `{name}`, grammatical endings
   after a value whose form is unknown).
3. **Names kept as written.** ARM and CORE in Latin capitals; Open
   Annihilation, Core Prime, Total Annihilation and its expansions, Cavedog,
   file names, keys and versions.
4. **Places and names of the fiction.** Transliterated or translated, once
   each (the planets, the Galactic Gate, the campaigns' places).
5. **Game terms.** Commander, Kbot, metal, energy, reclaim, patrol, guard,
   line of sight, and the rest.
6. **Menus and modes.** Skirmish, campaign, battle room, the difficulty
   and option names.
7. **Open Annihilation's interface.** The Library, Settings, mods, map
   packs, downloads, the game files.
8. **Unit names.** Every unit's name, once, from `in/units.txt`: generic
   names translated, proper names transliterated.
9. **Width.** How long a caption on one of 3.1c's fixed-size buttons may
   be, compared with the Ukrainian and Chinese.

## 5. Translate the chunks

Translate each chunk's `EN` into the language. The English is the source;
the references are for meaning, context and length. Ukrainian stays close
to the English and shows where a caption had to be shortened; Chinese is
freer, so do not copy what it adds. Neighbouring items often belong to one
screen, and some are pieces the engine joins into one line (`{a}, {b}`):
read the neighbours so the pieces read naturally together.

Write `out/<chunk>.tsv`: one line per item, the id, a tab, the translation.
Every id of the chunk once, in any order. Parts may be written as
`out/<chunk>.part1.tsv` and joined with `cat`; `merge` ignores the parts.

These rules are hard, because the engine fills or parses the text:

- Every placeholder stays exactly as written: `{name}`, `{size}`, `%s`,
  `%d`, `%.1f`, `%%`. `{name}` places may move; printf conversions (`%s`,
  `%d`) stay in the English's order, since they are filled in that order.
- Every number written in digits stays (`3.1c`, `16x16`, `9 x 21`).
- Staged captions keep their `|` stages, in order (`Easy|Medium|Hard`).
- A value never holds `;` (it ends a table value), `//` (the rest of the
  line is read as a comment) or a tab. Write a full stop, a comma or a
  dash instead of a semicolon.
- Only the pack's own script, Latin and common punctuation. A pack drawn
  in the game's fonts keeps to Windows-1252.

Each table has its own conventions:

- **interface**: Open Annihilation's own interface (settings, the Library,
  notices, dialogs, setup, touch and controller controls). Labels are noun
  phrases; hints are sentences.
- **translate**: 3.1c's own texts: menu and button captions, unit speech,
  help, errors, multiplayer messages, feature descriptions, map names and
  descriptions. Captions sit on fixed-size buttons: keep them short. A map
  description starts with its size, usually `5 x 8  ` with two spaces: keep
  the English's own prefix exactly, whatever its spacing (a few read
  `11 x 10 map.  `). Translate descriptive map names; transliterate
  invented ones.
- **units**: names from the glossary exactly; descriptions as short as the
  English, since they share the bottom bar's line.
- **missions**: the campaign lists' names. Keep a leading `N: ` exactly.

Some interface words are not shown alone but put into other sentences'
places: `device` and `the cloud` (`Uses {size} on this {device}.`,
`{size} is in {cloud} only…`), `the folder you chose`, `this part`, and the
sizes (`{n} KB`). In a language with cases, translate such a word in the
form every sentence it goes into needs, write that form in the glossary's
placeholder section, and word those sentences around it. To find where a
text goes, search the engine's `src/` for its English: each part's
`interface_words.hpp` lists its words, and the call sites show the
sentences (the game files' are in `src/ui/game-files/src/`). The same
search gives context to the first interface chunk's items, which have no
headings.

A briefing (`en-briefs/<name>` to `out/briefs/<name>`, UTF-8, LF):

- the same number of lines, blank where the English is blank, each line
  translating the same English line;
- `MISSION 1.0001ARME` keeps its code; `Mission T01: Air Assault` keeps
  `T01: `;
- colour codes stay around the words they colour: `&Y`, `&R` and `&G` open
  a coloured run and a lone `&` closes it (`&RExpect Core patrols.&`); `*`
  marks stay as the English has them;
- every number of the English stays; unit names and places are the
  glossary's.

Check each chunk until it reports no problems, then reread it start to
finish as a player would:

```sh
python3 tools/translate.py validate --work local/work/ru interface-1
python3 tools/translate.py validate --work local/work/ru briefs-2
python3 tools/translate.py status --work local/work/ru
```

When every chunk is done, read across them once for consistency: search
the outputs for each glossary term's likely variants and make them one.

## 6. Merge, pictures and warmup

```sh
python3 tools/translate.py merge --work local/work/ru
```

This writes `<tag>/interface.tdf`, `translate.tdf`, `units.tdf`,
`missions.tdf` and `files/camps/briefs-<Word>/`, each laid out as the
template's, with its header naming the new language. Later corrections go
in `local/work/<tag>/fixes.tsv` (an id, a tab, the value; it wins over the
chunks) before merging again, or straight into the pack once it is merged.

Two files are written by hand:

- **`pictures.tdf`**: the captions drawn over words in the game's pictures
  (the order buttons, the top bar). Copy the template's and translate each
  `text=`. A caption is drawn at the largest size that fits its button, so
  keep it to a word, abbreviated with a full stop if need be, and compare
  the order buttons in the battle picture: a caption drawn much smaller
  than its neighbours wants a shorter word, or an `area` as the Japanese
  pack's D-gun has. The Ukrainian captions are words alone; the Chinese,
  Korean and Japanese ones add the key in brackets (`攻撃(A)`), which suits
  a script whose captions are short.
- **`warmup.txt`**: `python3 tools/translate.py warmup <tag>` writes the
  characters the pack's text uses most (at most 4,096 bytes; 1,200 by
  default), drawn ahead so the first screen is quick.

## 7. A font of its own (CJK only)

Run `python3 tools/check.py <tag> --source`. A pack in the modern fonts
fails on any character neither the engine's faces nor the pack's own font
draws. Only a CJK language needs a face of its own; it is cut from the Noto
Sans CJK collection already pinned in `fonts/fonts.json`, whose faces are,
in order, Japanese (0), Korean (1), Simplified Chinese (2), Traditional
Chinese (3) and Hong Kong (4). A Chinese face draws Japanese and Traditional
Chinese characters in Chinese forms, so each needs its own cut.

A new face takes, in one commit:

- its recipe in `fonts/fonts.json` (file, face index, character set, count,
  licence, SHA-256);
- its character set in `tools/fonts.py`, documented there, and its self-test;
- `tools/check.py` checking the pack's characters against that set before
  the face is built, as it does for the Chinese, Korean and Japanese faces;
- tests beside the Chinese, Korean and Japanese ones, `fonts/README.md` and
  this repository's README.

A set that reads the pinned Unihan archive (the Chinese and Japanese ones)
also needs one it falls back to without it, from Python's codecs alone:
`check.py --source` uses it when `--deps` lacks the archive, and so do the
tests, which download nothing. Every character of the pack must be in that
fallback too.

The count and the SHA-256 come from cutting the face once by hand. With the
fontTools environment made (`python3 tools/fonts.py` makes it before it
cuts), run

```sh
local/fonttools-venv/bin/python tools/fonts.py --cut-face \
    local/deps/NotoSansCJK-Bold-2.004.ttc local/deps/Unihan-16.0.0.zip \
    /tmp/face.otf --face 0 --characters japanese --count 1
```

with the new face's index and set: it fails naming how many of the set's
characters the face holds. Run it twice more with that count, check that
the two files are the same bytes, and pin their SHA-256.

Then `python3 tools/fonts.py` builds it into `local/fonts/`, and the
manifest names it under `fonts`.

## 8. Check, coverage and build

```sh
python3 tools/check.py ru --source
python3 tools/coverage.py ru --oa-tool /path/to/oa-tool
python3 tools/build.py ru --oa-tool /path/to/oa-tool
python3 -I -m unittest discover -s tests -t .
```

The check must report `check: clean`, the coverage `0 missing, 0 not in
the engine`, and the tests `OK`. The build writes `dist/<tag>.oalang` and
its build information. The tests check every pack folder in the tree, so
they pass only once each pack in it is whole (its tables, briefings and
`warmup.txt`); a pack still being made elsewhere in the same checkout fails
them. The build tests stage into `local/stage/<tag>`, so do not run them
in two checkouts that share `local/` at once.

## 9. Look at it in the game

Every screen must fit. Install the built pack in a scratch user folder and
run the engine's text-fit check; it opens every Open Annihilation screen at
640x480 and 1280x720 and names each text that does not fit:

```sh
mkdir -p local/fit/ru/user/Languages/ru
(cd local/fit/ru/user/Languages/ru && unzip -o ../../../../../../dist/ru.oalang)
printf 'open-annihilation-preferences 1\n"open-annihilation.language" "ru"\n' > local/fit/ru/prefs.conf
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy /path/to/open-annihilation \
    --game-dir /path/to/totala --preferences-file local/fit/ru/prefs.conf \
    --user-folder local/fit/ru/user --skip-intro --mute \
    --check-text-fit --check-language ru
```

Keep each language's run in its own folder (`local/fit/<tag>/`), so packs
checked at the same time do not share a preferences file. It must end with
`text-fit check: every screen fits in ru at 640x480 and 1280x720`. It names
at most 40 texts and then how many more there are, so shorten those, merge
or edit, build and run it again until it passes.

Then look at the game's own screens, which the text-fit check does not
measure:

```sh
python3 tools/screens.py ru --engine /path/to/open-annihilation \
    --game-dir /path/to/totala --out local/screens/ru
```

It takes fifteen pictures at 640x480: the main menu, the single-player
menu, the campaign menu, the first briefing, the skirmish menu, a battle,
the in-game menu, the help screen, the four pages of 3.1c's options, the
load dialog with and without its "no saved games" message, and the map
chooser. Open every picture: each letter drawn (no boxes or gaps), nothing
cut off at a button's edge or wrapped inside a word, the briefing reading
naturally. Map names in the map chooser and the skirmish menu, and the
`EXAMPLE` campaign, come from the game data and stay in English.

## 10. Commit

- Every table starts with the SPDX lines, as the template's do; the
  briefings, `warmup.txt` and Markdown are covered by `REUSE.toml`.
- The repository test refuses a few reserved words; it names any it finds.
- Add the pack to this repository's README (its first paragraph, Layout
  and, if it brings a face, the font sections), and the glossary under
  `docs/glossaries/`.
- One commit for a new face, one for the pack:
  `(feat) Add the Russian language pack`.

## 11. Publish

Publishing is public: the pack goes to every player's Library through the
Core Prime catalogue. It needs the maintainer's go-ahead. From the content
library's checkout (its README is the authority):

```sh
python3 -m publish add coreprime ../languages/dist/ru.oalang
```

Fill the new `packages/oalang/<tag>/package.toml`'s descriptive fields as
the other packs' are (`summary`, `notes`, `publisher` and `author` "OA team"),
commit it as `(chore) Add ru revision 1`, then:

```sh
python3 -m publish run coreprime --dry-run
python3 -m publish run coreprime
```

The run signs and uploads the next catalogue, pushes the content library
and makes this repository's release `<tag>-r<revision>` with the pack
attached.
