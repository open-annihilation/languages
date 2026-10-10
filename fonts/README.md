# Fonts

Simplified Chinese (`zh-Hans`) ships `NotoSansCJKsc-Bold.otf`.

The face is Noto Sans CJK SC Bold, face 2 of the Noto Sans CJK Bold 2.004 collection (`NotoSansCJK-Bold-2.004.ttc`). `tools/fonts.py` cuts it to the common CJK characters: the two-byte characters of GB 2312, of Big5's symbols and level-1 hanzi, of JIS X 0208, and of KS X 1001's symbol and Hangul rows (the hanja left out); the CJK punctuation, kana, bopomofo, Hangul compatibility jamo and half- and full-width forms; and the 8,105 characters of the Table of General Standard Chinese Characters (2013), read from the Unicode 16.0 Unihan file's `kTGH` field. The cut keeps 15,309 characters. Its SHA-256 is `1bff16d425a0bc5048fddb7d33d2a59e08647d4a29380a348ccaabcbd89a29f2`.

The collection, its licence and the Unihan archive are pinned in `fonts.json`, with their URLs and SHA-256s. The font's licence is the SIL Open Font License 1.1, in `NotoSansCJK-OFL.txt`. The downloaded licence must match that file.

The cut uses fontTools 4.66.1, pinned by hash in `requirements.txt`, installed into `local/fonttools-venv`. Nothing else in this repository needs it.

Make the font with `python3 tools/fonts.py`. When the downloads are already on disk, pass that folder with `--deps`. The face is written to `local/fonts`, or to `--out`. The font file is built when a pack is built and is not part of this repository.
