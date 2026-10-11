# Open Annihilation language packs

The sources of Open Annihilation's downloadable language packs (`.oalang`), starting with Simplified Chinese. Each pack is built and checked here, and published with the content library's publish script. That script also makes a GitHub release for each pack and revision, so a translation can ship without an engine release.

The five languages Total Annihilation 3.1c ships with (English, German, Spanish, French and Italian) need no pack: Open Annihilation reads them from the game's own data.

## Layout

- `zh-Hans/` holds the Simplified Chinese sources: `language.yaml`, the tables, `warmup.txt`, and the briefings under `files/`.
- `fonts/` holds the CJK font's recipe, its licence and the pinned fontTools requirements. The built font is not stored here.
- `tools/check.py` checks a pack. `tools/coverage.py` lists the engine's interface words a pack does not translate. `tools/build.py` builds a `.oalang`. `tools/fonts.py` builds the font.
- `dist/` receives the built pack and its build info. `local/` holds downloads, the fontTools environment and the build stage. Neither directory is committed.

## Make the font

```sh
python3 tools/fonts.py
```

Downloads that are not already in `local/deps` are fetched and checked against the SHA-256 pins in `fonts/fonts.json`. Point `--deps` at a folder that already holds them:

```sh
python3 tools/fonts.py --deps /path/to/deps
```

The cut face is written to `local/fonts/NotoSansCJKsc-Bold.otf`. `python3 tools/fonts.py --self-test` checks the pins and the character set and downloads nothing. See `fonts/README.md` for the cut and the licence.

## Check a pack

```sh
python3 tools/check.py zh-Hans --source
python3 tools/check.py --all --source
```

`--source` allows the font named in `fonts/fonts.json` to be absent from the source tree. To compare a pack with a player's game data, pass the game folder and an `oa-tool` built from the engine:

```sh
python3 tools/check.py zh-Hans --game-dir /path/to/game --oa-tool /path/to/oa-tool
```

The check exits 0 when the pack is clean, 1 when it found failures, and 77 when there is no pack.

The check reads the built face from `local/fonts` (or `--fonts`) when the pack's own `fonts/` folder does not hold it, and fails on any character of the pack's text that only a CJK face draws and the face does not hold. Before the face is built, `--source` checks the characters against the cut's recipe, with the general standard table when `--deps` holds the Unihan archive. It also fails on an `interface.tdf` translation that drops a place (`{name}`, `%s`) or a number of its English.

## Coverage

```sh
python3 tools/coverage.py zh-Hans --oa-tool /path/to/oa-tool
```

This asks the engine build for its interface words (`oa-tool interface-words --json`) and prints each one the pack does not translate (`missing:`) and each section of the pack's `interface.tdf` the engine no longer has (`not in the engine:`). `--words FILE` reads a listing saved from that command instead. It exits 0 when the pack covers the build exactly.

## Build a pack

```sh
python3 tools/build.py zh-Hans --oa-tool /path/to/oa-tool
```

This checks the source, stages it with the font and the font licence, checks the staged folder, and runs `oa-tool pack`. The pack is `dist/zh-Hans.oalang`. Beside it, `dist/zh-Hans.oalang.json` records the tag, revision, commit, whether the worktree was dirty, and the file's size and SHA-256. A second build of the same commit produces the same bytes. `OA_TOOL` names the tool when `--oa-tool` is omitted. Pass no tag to build every pack. The font has to be built first (`python3 tools/fonts.py`).

## A new revision

Fix the translation, then bump `packaging.revision` and `packaging.date` in the pack's `language.yaml`. Commit and push to `main`. From that clean commit, build the pack. The maintainer publishes it with the content library's publish script, which reads the build info and makes the GitHub release for that pack and revision (for example `zh-Hans-r1`).

## Licences

The tables, briefings and tools are GPL-3.0-only, the same terms as the engine (`LICENSE`, `COPYRIGHT`). The CJK font is under the SIL Open Font License 1.1 (`fonts/NotoSansCJK-OFL.txt`).

## Tests

```sh
python3 -I -m unittest discover -s tests -t .
```

The tests use the standard library only. They do not need a network connection, game data or a real `oa-tool`.
