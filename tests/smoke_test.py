#!/usr/bin/env python3
"""Headless smoke checks for the keyboard gameplay loop and camera error UI.

The test instruments a temporary copy of the shipped HTML. The production files
are never modified by the test hook.
"""

from __future__ import annotations

import contextlib
import http.server
import socketserver
import tempfile
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "GIVE_ME_YOUR_FRIES_DUO_GESTURE.html"
EVIDENCE = ROOT / "docs" / "evidence"
HOOK_POINT = "window.addEventListener('beforeunload',()=>{if(cameraEnabled)closeCamera()});"
HOOK = """
window.__gameTest={
 state:()=>({phase,level,remain,food:food.map(f=>({x:f.x,y:f.y,count:f.count})),players:players.map(p=>({x:p.x,y:p.y,carry:p.carry,score:p.score,auto:p.auto})),nests:[nestXY(0),nestXY(1)],feedback:$('cameraFeedback').textContent}),
 position:(i,x,y)=>{const p=players[i];p.x=x;p.y=y;p.aimX=x;p.aimY=y;p.auto=false;},
 setRemain:(v)=>{remain=v;}
};
"""


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


@contextlib.contextmanager
def serve(directory: Path):
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(directory), **kwargs)
    with socketserver.TCPServer(("127.0.0.1", 0), handler) as server:
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield server.server_address[1]
        finally:
            server.shutdown()
            thread.join()


def wait_for(page, expression: str, timeout: int = 6000):
    page.wait_for_function(expression, timeout=timeout)


def run() -> None:
    html = SOURCE.read_text(encoding="utf-8")
    if HOOK_POINT not in html:
        raise AssertionError("test hook insertion point is missing")

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temp_name:
        temp = Path(temp_name)
        (temp / "index.html").write_text(html.replace(HOOK_POINT, HOOK + HOOK_POINT), encoding="utf-8")
        with serve(temp) as port, sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=True,
                executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                args=["--use-fake-ui-for-media-stream"],
            )
            page = browser.new_page(viewport={"width": 1440, "height": 1000})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(f"http://127.0.0.1:{port}/", wait_until="load")
            page.screenshot(path=str(EVIDENCE / "01_before_start.png"), full_page=True)

            page.click("#goKeyboard")
            wait_for(page, "() => window.__gameTest?.state().phase === 'playing'")
            state = page.evaluate("window.__gameTest.state()")
            assert len(state["players"]) == 2 and len(state["food"]) == 6
            page.screenshot(path=str(EVIDENCE / "02_keyboard_start.png"), full_page=True)

            before = state["players"][0]["y"]
            page.keyboard.down("w")
            page.wait_for_timeout(250)
            page.keyboard.up("w")
            assert page.evaluate("window.__gameTest.state().players[0].y") < before

            before = page.evaluate("window.__gameTest.state().players[1].x")
            page.keyboard.down("ArrowLeft")
            page.wait_for_timeout(250)
            page.keyboard.up("ArrowLeft")
            assert page.evaluate("window.__gameTest.state().players[1].x") < before

            for player, key, food_index in ((0, "f", 0), (1, "k", 3)):
                food = page.evaluate(f"window.__gameTest.state().food[{food_index}]")
                page.evaluate("([i,x,y])=>window.__gameTest.position(i,x,y)", [player, food["x"], food["y"]])
                page.keyboard.down(key)
                wait_for(page, f"() => window.__gameTest.state().players[{player}].carry > 0", 5000)
                page.keyboard.up(key)
                wait_for(page, f"() => window.__gameTest.state().players[{player}].score > 0", 6000)
                delivered = page.evaluate(f"window.__gameTest.state().players[{player}]")
                nest = page.evaluate(f"window.__gameTest.state().nests[{player}]")
                assert not delivered["auto"]
                assert abs(delivered["x"] - nest[0]) < 20 and abs(delivered["y"] - nest[1]) < 20

            page.screenshot(path=str(EVIDENCE / "03_first_deposit.png"), full_page=True)

            for expected_level in (1, 2):
                page.evaluate("window.__gameTest.setRemain(0.01)")
                wait_for(page, "() => window.__gameTest.state().phase === 'modal'")
                page.click("#goKeyboard")
                wait_for(page, f"() => window.__gameTest.state().phase === 'playing' && window.__gameTest.state().level === {expected_level}")

            page.evaluate("Object.defineProperty(navigator.mediaDevices,'getUserMedia',{configurable:true,value:async()=>{const e=new Error('denied');e.name='NotAllowedError';throw e;}})")
            page.click("#cameraBtn")
            wait_for(page, "() => window.__gameTest.state().feedback.includes('拒绝')")
            assert page.locator("#cameraFeedback").is_visible()
            assert not errors, errors
            browser.close()

    print("PASS page load, keyboard controls, P1/P2 deposit, round transitions, and visible simulated camera denial")


if __name__ == "__main__":
    run()
