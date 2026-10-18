#!/usr/bin/env python3
# SPDX-FileCopyrightText: The Open Annihilation Authors; see COPYRIGHT
# SPDX-License-Identifier: GPL-3.0-only

"""Take pictures of a built pack's screens with an engine build (docs/new-language.md).

    python3 tools/screens.py TAG --engine PATH --game-dir DIR --out DIR [--resolution 640x480]

The pack is read from dist/TAG.oalang and installed into a scratch user
folder under --out, so the player's own folders are never touched. The
engine runs without a window, without sound and without its intro, and is
driven through its automation endpoint (`--fark`). The pictures:

    main-menu, single-player, new-campaign, briefing      the campaign's way in
    skirmish, battle, game-menu, help                     a skirmish's way in

A picture that cannot be reached is reported and the rest are still taken.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import time
import zipfile
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
F2 = (59, 1073741883)  # SDL scancode and keycode of F2, the in-game menu


def frame_bytes(message: dict) -> bytes:
    body = json.dumps(message).encode()
    return b"AUTO/1 - %d 0 %08x\n" % (len(body), zlib.crc32(body)) + body


class Game:
    """One engine run, driven through its automation endpoint."""

    def __init__(self, engine: Path, game_dir: Path, run: Path, language: str, resolution: str):
        for sub in ("data", "user"):
            (run / sub).mkdir(parents=True, exist_ok=True)
        prefs = run / "prefs.conf"
        prefs.write_text("open-annihilation-preferences 1\n"
                         f'"open-annihilation.language" "{language}"\n', encoding="utf-8")
        self.endpoint = run / "automation.json"
        if self.endpoint.exists():
            self.endpoint.unlink()
        env = dict(os.environ, SDL_VIDEO_DRIVER="dummy", SDL_AUDIO_DRIVER="dummy",
                   SDL_VIDEODRIVER="dummy", SDL_AUDIODRIVER="dummy")
        args = [str(engine), "--fark", "--fark-file", str(self.endpoint),
                "--preferences-file", str(prefs), "--data-dir", str(run / "data"),
                "--user-folder", str(run / "user"), "--game-dir", str(game_dir),
                "--skip-intro", "--mute", "--resolution", resolution]
        self.log = open(run / "game.log", "wb")
        self.proc = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=self.log,
                                     stderr=subprocess.STDOUT, env=env)
        for _ in range(900):
            if self.endpoint.exists():
                try:
                    info = json.loads(self.endpoint.read_text())
                    break
                except ValueError:
                    pass
            if self.proc.poll() is not None:
                raise RuntimeError(f"the game exited; see {run / 'game.log'}")
            time.sleep(0.1)
        else:
            raise RuntimeError("the game wrote no automation file")
        host, _, port = info["address"].rpartition(":")
        self.sock = socket.create_connection((host.strip("[]"), int(port)))
        self.sock.settimeout(60)
        self.next_id = 1
        self.request("hello", versions=[1], client="languages-screens", token=info["token"])

    def _read(self) -> tuple[dict, bytes]:
        header = b""
        while not header.endswith(b"\n"):
            chunk = self.sock.recv(1)
            if not chunk:
                raise EOFError
            header += chunk
        _, _, json_size, payload_size, _ = header.split()
        size = int(json_size) + int(payload_size)
        data = b""
        while len(data) < size:
            data += self.sock.recv(size - len(data))
        return json.loads(data[:int(json_size)]), data[int(json_size):]

    def request(self, op: str, **fields) -> dict:
        message = {"id": self.next_id, "op": op, **fields}
        self.next_id += 1
        self.sock.sendall(frame_bytes(message))
        while True:
            answer, payload = self._read()
            if answer.get("id") == message["id"]:
                answer["_payload"] = payload
                return answer

    def screen(self) -> str:
        return self.request("screen").get("screen", "")

    def find(self, name: str) -> dict | None:
        for control in self.request("controls").get("controls", []):
            if control["name"] == name and control.get("visible", True):
                return control
        return None

    def wait_screen(self, name: str, timeout: float = 60) -> None:
        end = time.time() + timeout
        while time.time() < end:
            if self.screen() == name:
                return
            time.sleep(0.25)
        raise RuntimeError(f"the screen {name} did not come; the game shows {self.screen()}")

    def wait_change(self, old: str, timeout: float = 60) -> str:
        end = time.time() + timeout
        while time.time() < end:
            now = self.screen()
            if now and now != old:
                return now
            time.sleep(0.25)
        raise RuntimeError(f"the screen stayed {old}")

    def click(self, name: str, timeout: float = 30) -> None:
        end = time.time() + timeout
        control = None
        while time.time() < end and control is None:
            control = self.find(name)
            if control is None:
                time.sleep(0.25)
        if control is None:
            raise RuntimeError(f"no control named {name} on {self.screen()}")
        space, rect = ("window", control["window_rect"]) if control.get("window_rect") else (
            "game", control["rect"])
        x, y = int(rect[0] + rect[2] // 2), int(rect[1] + rect[3] // 2)
        answer = self.request("input", events=[
            {"kind": "pointer_move", "x": x, "y": y, "space": space},
            {"kind": "button_down", "x": x, "y": y, "space": space, "button": "left"},
            {"kind": "button_up", "x": x, "y": y, "space": space, "button": "left"}])
        if not answer.get("ok"):
            raise RuntimeError(f"clicking {name}: {answer}")

    def key(self, scancode: int, keycode: int) -> None:
        event = {"scancode": scancode, "keycode": keycode}
        self.request("input", events=[{"kind": "key_down", **event}, {"kind": "key_up", **event}])

    def shot(self, path: Path) -> None:
        answer = self.request("frame", format="png", source="presented")
        if not answer.get("ok"):
            raise RuntimeError(f"no frame: {answer}")
        path.write_bytes(answer["_payload"])
        print(f"took {path}")

    def close(self) -> None:
        try:
            self.request("quit")
        except Exception:
            pass
        try:
            self.proc.wait(timeout=20)
        except subprocess.TimeoutExpired:
            self.proc.kill()
        self.log.close()


def campaign(game: Game, out: Path) -> None:
    game.wait_screen("main_menu", 120)
    time.sleep(1.5)
    game.shot(out / "main-menu.png")
    game.click("SINGLE")
    game.wait_screen("single_player")
    time.sleep(1)
    game.shot(out / "single-player.png")
    game.click("NewCamp")
    game.wait_screen("new_campaign")
    time.sleep(1)
    game.shot(out / "new-campaign.png")
    game.click("Start")
    game.wait_change("new_campaign")
    time.sleep(3)
    game.shot(out / "briefing.png")


def skirmish(game: Game, out: Path) -> None:
    game.wait_screen("main_menu", 120)
    time.sleep(1)
    game.click("SINGLE")
    game.wait_screen("single_player")
    game.click("Skirmish")
    game.wait_change("single_player")
    time.sleep(1.5)
    game.shot(out / "skirmish.png")
    game.click("Start")
    game.wait_screen("match", 120)
    time.sleep(5)
    game.shot(out / "battle.png")
    game.key(*F2)
    time.sleep(1.5)
    game.shot(out / "game-menu.png")
    game.click("HELP")
    time.sleep(1.5)
    game.shot(out / "help.png")


def install(tag: str, user: Path) -> None:
    built = ROOT / "dist" / f"{tag}.oalang"
    if not built.is_file():
        raise SystemExit(f"{built} does not exist: build the pack first (tools/build.py)")
    folder = user / "Languages" / tag
    shutil.rmtree(folder, ignore_errors=True)
    folder.mkdir(parents=True)
    with zipfile.ZipFile(built) as archive:
        archive.extractall(folder)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("tag")
    parser.add_argument("--engine", required=True, help="the engine build's executable")
    parser.add_argument("--game-dir", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--resolution", default="640x480")
    args = parser.parse_args(argv)
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    failed = 0
    for walk in (campaign, skirmish):
        run = out / f"run-{walk.__name__}"
        shutil.rmtree(run, ignore_errors=True)
        install(args.tag, run / "user")
        game = Game(Path(args.engine), Path(args.game_dir).expanduser(), run, args.tag,
                    args.resolution)
        try:
            walk(game, out)
        except (RuntimeError, OSError) as error:
            failed += 1
            print(f"{walk.__name__}: {error}")
        finally:
            game.close()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
