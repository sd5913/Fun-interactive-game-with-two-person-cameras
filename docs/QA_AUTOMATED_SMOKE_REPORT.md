# Automated smoke-test evidence — 05 November 2026

**Target:** `GIVE_ME_YOUR_FRIES_DUO_GESTURE.html` / identical `index.html` in this package.  
**Environment:** local Google Chrome in headless mode on macOS using Python Playwright.  
**Scope:** UI rendering, JavaScript execution, keyboard input, core gameplay state and **simulated** camera-permission failure. **Not** real-user testing or real-hand camera tracking.

## Results

| Check | Observation | Result |
| --- | --- | --- |
| Page loads with no uncaught JS errors | No `pageerror` events in the test | **PASS** |
| Start keyboard demo | Game enters `playing`; P1 and P2 appear with six food trays in round 1 | **PASS** |
| P1 WASD | Pressing W moves P1 upward | **PASS** |
| P2 arrow controls | Pressing Left moves P2 left | **PASS** |
| P1 grab and deliver | Using a test-only position helper and **real F key down/up**, carried fries increased to 1; after release score increased to 1; P1 remained at nest | **PASS** |
| P2 grab and deliver | Using a test-only position helper and **real K key down/up**, P2 score increased to 1; P2 remained at nest | **PASS** |
| Timer → next rounds | Test-only accelerated timer: game advances from round 1 → 2 → 3 with the correct round state | **PASS** |
| Camera errors visible outside modal | Test-only `getUserMedia` rejection with `NotAllowedError` produced a visible footer message; keyboard mode remained active | **PASS (simulated permission error)** |
| Real camera / hands / pinch | Not connected to real webcam in this test | **NOT TESTED** |
| Rival bump / tray drag | Functions are present in source, but were not exercised by this smoke test | **NOT TESTED** |
| Two people independently controlling real hands | Requires two players at a real camera | **NOT TESTED** |

For speed and repeatability, the automated scenario uses a **test-only positioning hook** to move the birds next to fries before triggering genuine F/K key events. The hook is injected into an in-memory testing copy and **is not included in the shipped playable HTML**. Therefore these results are implementation smoke tests, not evidence of completed natural user journeys.

## Screenshots

- [Before start](./evidence/01_before_start.png)
- [Keyboard game running](./evidence/02_keyboard_start.png)
- [P1 score after auto-return](./evidence/03_first_deposit.png)

## How to repeat

1. Install Python 3 and Playwright: `python3 -m pip install playwright`.
2. Ensure Google Chrome is installed in `/Applications/Google Chrome.app` (or update `executable_path` in the script for your system).
3. Run from project root: `python3 tests/smoke_test.py`.
4. Check the PASS output and generated `docs/evidence/` screenshots.

## Next evidence needed before marking camera as Done

Capture a **real** 30–60 second recording in Chrome on the presentation Mac showing both people in the camera preview, each controlling their own bird, plus a pinch-triggered collection and delivery. Record browser version, OS, time, whether CDN model loaded, and any permission blocker.
