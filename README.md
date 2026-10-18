# Open Annihilation language packs

The sources of Open Annihilation's downloadable language packs (`.oalang`): Simplified Chinese, Ukrainian and Korean. Each pack is built and checked here, and published with the content library's publish script. That script also makes a GitHub release for each pack and revision, so a translation can ship without an engine release.

The five languages Total Annihilation 3.1c ships with (English, German, Spanish, French and Italian) need no pack: Open Annihilation reads them from the game's own data.

## Layout

- `zh-Hans/` holds the Simplified Chinese sources: `language.yaml`, the tables, `warmup.txt`, and the briefings under `files/`.
- `uk/` holds the Ukrainian sources, laid out the same way. Its text is drawn in the modern fonts, and the sans faces that travel with the game hold Cyrillic, so the pack brings no font of its own.
- `ko/` holds the Korean sources, laid out the same way. Its text is drawn in the modern fonts, its Hangul from the pack's own face, cut from the same collection as the Chinese one.
- `fonts/` holds the CJK fonts' recipes, their licence and the pinned fontTools requirements, and `engine-faces.json`, the record of the characters the engine's own faces draw. The built fonts are not stored here.
- `tools/check.py` checks a pack. `tools/coverage.py` lists the engine's interface words a pack does not translate. `tools/build.py` builds a `.oalang`. `tools/fonts.py` builds the fonts. `tools/translate.py` prepares, checks and merges a new pack's translation from an existing pack. `tools/screens.py` takes pictures of a built pack's screens with an engine build.
- `docs/` holds the guides: [adding a language](docs/new-language.md), [updating the packs for an engine release](docs/updating-a-pack.md), and each pack's glossary under `docs/glossaries/`.
- `dist/` receives the built pack and its build info. `local/` holds downloads, the fontTools environment and the build stage. Neither directory is committed.

## Add a language, or update the packs

[docs/new-language.md](docs/new-language.md) is the whole way from nothing to a published pack: how the text is drawn, the manifest, the translation work and its rules, a font of its own, the checks, the pictures and publishing. [docs/updating-a-pack.md](docs/updating-a-pack.md) brings the packs up to a new engine release.

## Make the fonts

Simplified Chinese, Korean and Japanese each ship a font, cut from the same Noto Sans CJK collection.

```sh
python3 tools/fonts.py
```

Downloads that are not already in `local/deps` are fetched and checked against the SHA-256 pins in `fonts/fonts.json`. Point `--deps` at a folder that already holds them:

```sh
python3 tools/fonts.py --deps /path/to/deps
```

The cut faces are written to `local/fonts/NotoSansCJKsc-Bold.otf`, `local/fonts/NotoSansCJKkr-Bold.otf` and `local/fonts/NotoSansCJKjp-Bold.otf`. `python3 tools/fonts.py --self-test` checks the pins and the character sets and downloads nothing. See `fonts/README.md` for the cut and the licence.

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

The check reads the built face from `local/fonts` (or `--fonts`) when the pack's own `fonts/` folder does not hold it, and fails on any character of the pack's text that only a CJK face draws and the face does not hold. Before the face is built, `--source` checks the characters against the cut's recipe: the Chinese face's with the general standard table when `--deps` holds the Unihan archive, the Japanese face's with the Jōyō and Jinmeiyō kanji from the same archive (and JIS X 0208 alone without it), and the Korean face's, Hangul, with no download. It also fails on an `interface.tdf` translation that drops a place (`{name}`, `%s`) or a number of its English.

Every other character must have a glyph where the game draws it. In a pack whose text needs the modern fonts (`text: {needs: modern-fonts}`), each visible character must be in the engine's own faces or the pack's fonts, in a face every weight looks in. The engine's faces are read from `fonts/engine-faces.json`, or from an engine build's fonts folder with `--engine-fonts`:

```sh
python3 tools/check.py uk --engine-fonts /path/to/open-annihilation.app/Contents/Resources/fonts
```

A pack drawn in the game's own fonts keeps to their code page, Windows-1252. When the engine's faces change, record them again from a build's fonts folder (the bundle's `Contents/Resources/fonts` on macOS, the `fonts` folder beside the game elsewhere):

```sh
python3 tools/fonts.py --record-engine-faces /path/to/fonts
```

## Coverage

```sh
python3 tools/coverage.py zh-Hans --oa-tool /path/to/oa-tool
```

This asks the engine build for its interface words (`oa-tool interface-words --json`) and prints each one the pack does not translate (`missing:`) and each section of the pack's `interface.tdf` the engine no longer has (`not in the engine:`). `--words FILE` reads a listing saved from that command instead. It exits 0 when the pack covers the build exactly.

## Build a pack

```sh
python3 tools/build.py zh-Hans --oa-tool /path/to/oa-tool
```

This checks the source, stages it with the font and the font licence, if it names one, checks the staged folder, and runs `oa-tool pack`. The pack is `dist/zh-Hans.oalang`. Beside it, `dist/zh-Hans.oalang.json` records the tag, revision, commit, whether the worktree was dirty, and the file's size and SHA-256. A second build of the same commit produces the same bytes. `OA_TOOL` names the tool when `--oa-tool` is omitted. Pass no tag to build every pack. A pack that names a CJK font, Simplified Chinese, Korean or Japanese, needs it built first (`python3 tools/fonts.py`); Ukrainian needs none:

```sh
python3 tools/build.py uk --oa-tool /path/to/oa-tool
```

## A new revision

Fix the translation, then bump `packaging.revision` and `packaging.date` in the pack's `language.yaml`. Commit and push to `main`. From that clean commit, build the pack. The maintainer publishes it with the content library's publish script, which reads the build info and makes the GitHub release for that pack and revision (for example `zh-Hans-r1`, `uk-r1` or `ko-r1`).

## Licences

The tables, briefings and tools are GPL-3.0-only, the same terms as the engine (`LICENSE`, `COPYRIGHT`). The CJK fonts are under the SIL Open Font License 1.1 (`fonts/NotoSansCJK-OFL.txt`). The Ukrainian pack carries no font.

## Tests

```sh
python3 -I -m unittest discover -s tests -t .
```

The tests use the standard library only. They do not need a network connection, game data or a real `oa-tool`.
