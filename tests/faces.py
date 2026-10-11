# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""Tiny OpenType faces for the tests: a table directory and a character map, no glyphs."""

from __future__ import annotations

import struct
from pathlib import Path

from tools import fonts


def cmap_format_12(ranges: list[tuple[int, int]]) -> bytes:
    """A format 12 subtable mapping each range to glyphs from 1 up."""
    groups = b""
    glyph = 1
    for first, last in ranges:
        groups += struct.pack(">III", first, last, glyph)
        glyph += last - first + 1
    length = 16 + len(groups)
    return struct.pack(">HHIII", 12, 0, length, 0, len(ranges)) + groups


def cmap_format_4(ranges: list[tuple[int, int]]) -> bytes:
    """A format 4 subtable mapping each range of the first plane to glyphs from 1 up."""
    segments = [*ranges, (0xFFFF, 0xFFFF)]
    ends = b"".join(struct.pack(">H", last) for _first, last in segments)
    starts = b"".join(struct.pack(">H", first) for first, _last in segments)
    deltas = b""
    glyph = 1
    for first, last in ranges:
        deltas += struct.pack(">h", ((glyph - first + 0x8000) & 0xFFFF) - 0x8000)
        glyph += last - first + 1
    deltas += struct.pack(">h", 1)
    offsets = b"\0\0" * len(segments)
    body = ends + b"\0\0" + starts + deltas + offsets
    length = 14 + len(body)
    return struct.pack(">HHHHHHH", 4, length, 0, 2 * len(segments), 0, 0, 0) + body


def face(ranges: list[tuple[int, int]], form: int = 12) -> bytes:
    """An OpenType face whose only table is a character map of the ranges."""
    if form == 12:
        subtable, encoding = cmap_format_12(ranges), 10
    else:
        subtable, encoding = cmap_format_4(ranges), 1
    cmap = struct.pack(">HH", 0, 1) + struct.pack(">HHI", 3, encoding, 12) + subtable
    directory = struct.pack(">IHHHH", 0x4F54544F, 1, 16, 0, 0)
    record = struct.pack(">4sIII", b"cmap", 0, 12 + 16, len(cmap))
    return directory + record + cmap


def write_face(path: Path, ranges: list[tuple[int, int]], form: int = 12) -> Path:
    """Write face(ranges, form) to path and return it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(face(ranges, form))
    return path


def ranges_of(codes: set[int]) -> list[tuple[int, int]]:
    """The code points as the fewest runs of consecutive ones."""
    runs: list[tuple[int, int]] = []
    for code in sorted(codes):
        if runs and runs[-1][1] == code - 1:
            runs[-1] = (runs[-1][0], code)
        else:
            runs.append((code, code))
    return runs


def pack_characters(pack: Path) -> set[int]:
    """The characters of a pack's text, outside its manifest, that only a CJK face draws."""
    found = set()
    for path in pack.rglob("*"):
        if path.is_file() and path.name != "language.yaml" and "fonts" not in path.relative_to(pack).parts:
            text = path.read_text(encoding="utf-8")
            found |= {ord(c) for c in text if fonts.cjk_block(ord(c))}
    return found
