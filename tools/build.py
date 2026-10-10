#!/usr/bin/env python3
# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""Build a language pack with oa-tool and write the build info beside it.

    build.py [TAG ...] --oa-tool PATH [--fonts DIR] [--out DIR]

With no TAG, every pack in this repository is built. The source is checked
with check.py --source, staged under local/stage/<tag>/ with the fonts and
their licence, checked again, and packed:

    oa-tool pack local/stage/<tag> --out <out>/<tag>.oalang --force

<out>/<tag>.oalang.json records tag, revision, commit, dirty, size and
sha256 for the content library's publish script. One line is printed:
<out>/<tag>.oalang <size> <sha256>.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check  # noqa: E402
import oamod_yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MISSING_FONT = "run python3 tools/fonts.py first"


def worktree_dirty(root: Path) -> bool:
    """True when `git status --porcelain` in root printed anything."""
    result = subprocess.run(
        ["git", "status", "--porcelain"], cwd=root, check=True, capture_output=True, text=True
    )
    return bool(result.stdout)


def worktree_commit(root: Path) -> str:
    """The current commit of root."""
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def font_licence(name: str) -> str:
    """The licence file fonts/fonts.json names for a built font."""
    path = ROOT / "fonts" / "fonts.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    spec = data.get("fonts", {}).get(name)
    if not isinstance(spec, dict) or not isinstance(spec.get("licence"), str):
        raise RuntimeError(f"fonts/fonts.json names no licence for {name}")
    return spec["licence"]


def stage_pack(source: Path, stage: Path, fonts: Path) -> None:
    """Copy the source into stage, then each listed font and its licence."""
    if stage.exists():
        shutil.rmtree(stage)
    stage.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, stage)
    values = oamod_yaml.loads((source / "language.yaml").read_bytes())
    listed = values.get("fonts") or []
    if not listed:
        return
    destination = stage / "fonts"
    destination.mkdir(parents=True, exist_ok=True)
    copied: set[str] = set()
    for item in listed:
        name = item.get("file") if isinstance(item, dict) else None
        if not isinstance(name, str):
            continue
        font = fonts / name
        if not font.is_file():
            print(MISSING_FONT, file=sys.stderr)
            raise SystemExit(1)
        shutil.copyfile(font, destination / name)
        licence = font_licence(name)
        if licence not in copied:
            shutil.copyfile(ROOT / "fonts" / licence, destination / licence)
            copied.add(licence)


def write_info(package: Path, tag: str, revision: int, info_path: Path) -> None:
    """Write the six build-info fields the publish script reads."""
    payload = package.read_bytes()
    info = {
        "commit": worktree_commit(ROOT),
        "dirty": worktree_dirty(ROOT),
        "revision": revision,
        "sha256": hashlib.sha256(payload).hexdigest(),
        "size": len(payload),
        "tag": tag,
    }
    info_path.write_text(json.dumps(info, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_one(folder: Path, tool: Path, fonts: Path, out: Path) -> None:
    """Check, stage, pack and describe one pack. The last line is the package."""
    values = oamod_yaml.loads((folder / "language.yaml").read_bytes())
    tag = values.get("tag")
    if tag != folder.name:
        print(f"{folder.name} is not the manifest tag {tag}", file=sys.stderr)
        raise SystemExit(1)
    packaging = values.get("packaging")
    if not isinstance(packaging, dict):
        print(f"{tag} names no packaging", file=sys.stderr)
        raise SystemExit(1)
    revision = packaging.get("revision")
    if isinstance(revision, bool) or not isinstance(revision, int):
        print(f"{tag} packaging.revision is not an integer", file=sys.stderr)
        raise SystemExit(1)
    if check.main([str(folder), "--source"]) != 0:
        raise SystemExit(1)
    stage = ROOT / "local" / "stage" / tag
    stage_pack(folder, stage, fonts)
    if check.main([str(stage)]) != 0:
        raise SystemExit(1)
    out.mkdir(parents=True, exist_ok=True)
    package = out / f"{tag}.oalang"
    relative_stage = stage.relative_to(ROOT)
    relative_package = package.relative_to(ROOT) if package.is_relative_to(ROOT) else package
    result = subprocess.run(
        [str(tool), "pack", relative_stage.as_posix(), "--out", relative_package.as_posix(), "--force"],
        cwd=ROOT,
    )
    if result.returncode != 0:
        raise SystemExit(result.returncode)
    info_path = package.with_name(package.name + ".json")
    write_info(package, tag, revision, info_path)
    payload = package.read_bytes()
    print(f"{relative_package.as_posix()} {len(payload)} {hashlib.sha256(payload).hexdigest()}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("tags", nargs="*", help="packs to build (default: every pack)")
    parser.add_argument("--oa-tool", type=Path, default=os.environ.get("OA_TOOL") and Path(os.environ["OA_TOOL"]))
    parser.add_argument("--fonts", type=Path, default=Path("local") / "fonts")
    parser.add_argument("--out", type=Path, default=Path("dist"))
    options = parser.parse_args(argv)
    if options.oa_tool is None:
        parser.error("pass --oa-tool or set OA_TOOL")
    tool = options.oa_tool if options.oa_tool.is_absolute() else Path.cwd() / options.oa_tool
    if not os.access(tool, os.X_OK):
        print(f"{tool} is not executable", file=sys.stderr)
        return 1
    fonts = options.fonts if options.fonts.is_absolute() else Path.cwd() / options.fonts
    out = options.out if options.out.is_absolute() else Path.cwd() / options.out
    folders = check.pack_folders()
    if options.tags:
        selected = []
        by_name = {folder.name: folder for folder in folders}
        for tag in options.tags:
            if tag not in by_name:
                print(f"no pack {tag}", file=sys.stderr)
                return 1
            selected.append(by_name[tag])
    else:
        selected = folders
        if not selected:
            print("no pack", file=sys.stderr)
            return 1
    for folder in selected:
        build_one(folder, tool, fonts, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
