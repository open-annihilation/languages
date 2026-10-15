# Fonts

Simplified Chinese (`zh-Hans`) ships `NotoSansCJKsc-Bold.otf`, and Korean (`ko`) ships `NotoSansCJKkr-Bold.otf`.

The face is Noto Sans CJK SC Bold, face 2 of the Noto Sans CJK Bold 2.004 collection (`NotoSansCJK-Bold-2.004.ttc`). `tools/fonts.py` cuts it to the common CJK characters: the two-byte characters of GB 2312, of Big5's symbols and level-1 hanzi, of JIS X 0208, and of KS X 1001's symbol and Hangul rows (the hanja left out); the CJK punctuation, kana, bopomofo, Hangul compatibility jamo and half- and full-width forms; and the 8,105 characters of the Table of General Standard Chinese Characters (2013), read from the Unicode 16.0 Unihan file's `kTGH` field. The cut keeps 15,309 characters. Its SHA-256 is `1bff16d425a0bc5048fddb7d33d2a59e08647d4a29380a348ccaabcbd89a29f2`.

The Korean face is Noto Sans CJK KR Bold, face 1 of the same collection. `tools/fonts.py` cuts it to Hangul: the 11,172 precomposed Hangul syllables, the Hangul compatibility jamo, CJK punctuation and half- and full-width forms, and the two-byte characters of KS X 1001's symbol rows; KS X 1001's hanja are left out, and the Korean pack's text uses none. The face holds 12,298 of those 12,349 characters. Its SHA-256 is `0f035ef4a3ce2cb1aee6c921fc550281ba4ee5fec43cf6febc2c3c3110de168f`. Before it is built, `tools/check.py --source` checks the Korean text against this recipe, which needs no download.

The collection, its licence and the Unihan archive are pinned in `fonts.json`, with their URLs and SHA-256s. Both faces' licence is the SIL Open Font License 1.1, in `NotoSansCJK-OFL.txt`. The downloaded licence must match that file.

The cut uses fontTools 4.66.1, pinned by hash in `requirements.txt`, installed into `local/fonttools-venv`. Nothing else in this repository needs it.

Make the fonts with `python3 tools/fonts.py`. When the downloads are already on disk, pass that folder with `--deps`. The faces are written to `local/fonts`, or to `--out`. The font files are built when a pack is built and are not part of this repository.

## The engine's own faces

Ukrainian (`uk`) ships no font. Its text needs the modern fonts, and the sans faces that travel with the game, DejaVu Sans Bold and DejaVu Sans 2.37, hold Cyrillic, Ukrainian's і, ї, є, ґ and the apostrophe ʼ among it.

`engine-faces.json` records the engine's four base faces, in the order its font stack opens them (DejaVu Sans Bold, DejaVu Sans, the endonym face and Noto Emoji): each one's SHA-256 and the code points its character map holds, as runs. `tools/check.py` reads it to tell that every character of a pack's text has a glyph: the bold weight looks in all four faces, the regular weight in all but DejaVu Sans Bold, so a character must be in one of the other three, or in the pack's own fonts. The record was made from Open Annihilation 0.8.0's fonts folder with `python3 tools/fonts.py --record-engine-faces FONTS`; make it again when the engine's faces change.
