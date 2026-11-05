# GIVE ME YOUR FRIES! 🕊️🍟

**A two-player, same-screen, hand-tracking seagull game** developed for **SD5913: Programming for Art and Design**.

Repository: [sd5913/Fun-interactive-game-with-two-person-cameras](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras)

> **Project status (5 November 2026): first working interaction / tutor review.** The prototype implements two-player keyboard interaction and contains optional webcam-based hand tracking. Webcam reliability and two-user device testing **still need verification**. This document describes the prototype; it does not claim that every feature has passed user testing.

## Game concept

Two seagulls compete to steal fries at a seaside dock. Players can cross the centre line, steal fries, fly home to bank them, physically bump into their rival, and move their rival's fries tray. There is **no separate summoned seagull**: each player controls their own character.

The current build includes **three rounds** with different harbour layouts: **Sunny L-shaped Pier**, **Sunset Fish Market**, and **Storm Harbour**. Scores accumulate across the rounds. Human guards threaten seagulls that dive too close.

## First working interaction: input → response → feedback

| Stage | What happens |
| --- | --- |
| **Input** | Player 1 moves with `W A S D`, Player 2 with arrow keys. Hold `F` (P1) or `K` (P2) to dive. Optional webcam mode tracks a hand in each camera half and uses thumb-index pinching to dive. |
| **Response** | A seagull moves toward the target; while diving next to fries, it picks up fries over time. Releasing the action makes a seagull carrying fries return automatically to its own nest. In keyboard mode, after depositing, the bird stays at the nest until the player moves again. |
| **Feedback** | Carry counter changes; HUD scores update after successful delivery; particles, floating actions, character animation, audio cues and status messages communicate actions. |
| **Outcome** | Players bank points, disrupt one another and compete across three timed rounds. |

**Tutor-demo script (60–90 seconds):** Open in Chrome → choose **Keyboard first** → move P1 to a fries tray with WASD → hold F near it → release F → wait for automatic return and score update → move P2 using arrow keys and hold K → show opposing controls. Explain that webcam pinch control is an **optional, device-dependent input pathway**, not a prerequisite for demonstrating the playable loop.

## How to play

| Action | Player 1 | Player 2 |
| --- | --- | --- |
| Move | W A S D | Arrow keys |
| Dive / steal | Hold F | Hold K |
| Release / return with fries | Release F | Release K |
| Webcam control (optional) | Hand in **left half** of the camera frame | Hand in **right half** of the camera frame |
| Webcam dive | Thumb + index finger pinch | Thumb + index finger pinch |

- A pinched/dive input near a fries tray gathers fries over time, up to **4** carried fries.
- Release while carrying to **auto-return to the nest** and bank points.
- Dive into your opponent to **bump and drop carried fries**.
- A tray may be **dragged** by gripping while moving it; taking a rival tray to your side can earn a bonus.
- Each round is timed (**65 / 75 / 85 seconds**); the player with the highest cumulative score wins after round 3.

**Important:** Camera mode uses **one shared webcam** with two designated halves; this build does **not** use two separate webcams. A fallback keyboard mode is provided.

## Running the game

### Option A — keyboard mode (no server required)

Open `index.html` or `GIVE_ME_YOUR_FRIES_DUO_GESTURE.html` in a modern desktop browser. Choose **⌨ Keyboard first**. Keyboard mode does not need a camera or AI model download.

### Option B — webcam mode (recommended: Chrome on localhost or HTTPS)

From the directory containing `index.html`, start a local HTTP server:

```bash
python3 -m http.server 8765
```

Visit `http://localhost:8765/` in **Google Chrome**, click **📷 Two-player camera start**, then allow camera access. Place one hand in each half of the camera view. On first use, a network connection is needed to load **MediaPipe Tasks Vision 0.10.21**, WASM, and its hand landmark model from CDN/Google Storage servers.

A video preview alone **does not prove hand tracking is ready**. Wait for the hand-tracking status message. If the model fails, **the browser can still use keyboard mode**; use the retry button to attempt another download.

**Camera troubleshooting:**

1. Use `localhost` or a standalone **HTTPS** deployment; embedded HTML previewers may block camera access.
2. Check Chrome site permissions and macOS **Privacy & Security → Camera**.
3. Close other applications currently using the webcam.
4. Confirm that the webcam video appears, then check whether MediaPipe reports successful two-hand tracking.
5. If it fails, demonstrate the full input→response→feedback flow using the keyboard and record the webcam failure as an open blocker.

The app processes webcam frames in the browser. Face images are loaded locally or captured from the webcam; this code does not intentionally upload frames to a server. External library/model requests still require an internet connection.

## Project structure

```text
index.html                          # identical playable HTML for easy local hosting / future GitHub Pages
GIVE_ME_YOUR_FRIES_DUO_GESTURE.html # existing filename retained for continuity
README.md                           # project and run instructions

docs/
  2026-11-05_TUTOR_REVIEW.md        # first working interaction review and evidence
  2026-11-05_ISSUE_UPDATES.md        # issue/comment drafts and project board instructions
  QA_CHECKLIST.md                   # repeatable test plan and known limitations
  QA_AUTOMATED_SMOKE_REPORT.md      # headless Chromium smoke test results
  evidence/                         # screenshots generated by smoke test

tests/
  smoke_test.py                     # optional automated checks
```

## Evidence and development process

- **Playable source:** [GIVE_ME_YOUR_FRIES_DUO_GESTURE.html](./GIVE_ME_YOUR_FRIES_DUO_GESTURE.html)
- **Tutor review (5 Nov):** [docs/2026-11-05_TUTOR_REVIEW.md](./docs/2026-11-05_TUTOR_REVIEW.md)
- **QA checklist:** [docs/QA_CHECKLIST.md](./docs/QA_CHECKLIST.md)
- **Automated smoke test report:** [docs/QA_AUTOMATED_SMOKE_REPORT.md](./docs/QA_AUTOMATED_SMOKE_REPORT.md)
- **Issues:** [GitHub Issues](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues)
- **GitHub Project Board:** [Fun Interactive Game – Team Board](https://github.com/orgs/sd5913/projects/8) (private to the organization; visibility is managed by organization owners)

The team should link completed issue work to commits or PRs and record who completed each task. Do **not** mark camera tracking fully tested until both players can use it on the intended hardware.

## Next milestone: 12 November 2026

Integrate and verify a stable two-player session, document a real-user playtest, and prepare an accessible demo link/build. Assign specific owners in GitHub Projects.

## Credits

SD5913 group project. Individual contributions should be taken from repository commits, issues and teammate confirmation; they have not been inferred or assigned in this README.
