# Tutor Review — 05 November 2026

**Review:** First Working Interaction  
**Project:** GIVE ME YOUR FRIES! — Two-Player Seagull Gesture Game  
**Repository:** https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras  
**Meeting time:** Confirm with assigned tutor (5 November is the class-week review date).  
**Review status:** Prepared for demonstration; tutor feedback not yet recorded.

## Delivery focus

> Demonstrate one usable interaction from **start to response** and agree the **smallest next goal** with the tutor.

The smallest complete gameplay loop is:

1. **Input:** P1 moves with WASD and holds F to dive near a fries tray (or P2 moves with arrow keys and holds K).
2. **Program response:** The character moves and collects fries while the dive input is held.
3. **Feedback:** The carry counter and visual/audio effects update when fries are collected.
4. **Outcome:** Releasing the key automatically sends the bird to its nest; the stored score increases on arrival.

Camera mode maps one hand in each half of a shared webcam to the same input loop via MediaPipe; **this pathway still requires real-device verification**.

## Bring to the tutor

- [x] Working HTML prototype prepared in this package (`GIVE_ME_YOUR_FRIES_DUO_GESTURE.html`).
- [x] Local keyboard fallback available for demonstration.
- [x] README and repeatable QA checklist prepared.
- [x] Headless Chromium keyboard smoke checks completed and screenshots produced (see automated report).
- [ ] Open and run the demo on the actual classroom laptop; demonstrate one complete steal-and-return loop.
- [ ] Add actual test evidence (short screen recording / screenshot, tested browser/OS, date).
- [x] Files committed on `tutor-review-2026-11-05` and submitted in [PR #7](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/pull/7).
- [ ] Confirm issue / board links and owners.

## What changed / current evidence

**Implemented in the supplied game source:** two independent keyboard control sets; optional two-hand webcam detection; three separate maps; fries collection, bumping, tray dragging, return to nest, timed rounds and HUD feedback. The HTML also supports overlaying two players' photos on the seagull faces while retaining cartoon eyebrows and beaks.

**Documentation/refinement prepared for this review (local package; not yet pushed to GitHub):**

- README with setup instructions, control mapping, gameplay-loop explanation, known limitations and review link.
- Persistent, visible webcam status line beneath the game: permission or model errors can be read even after the start overlay closes.
- Stable tray identity allocated directly in `setupRound`, removing a late wrapper that patched `setupRound` at the end of the file.
- Keyboard players now remain at their nest after automatic delivery, rather than drifting back toward the previous input target.
- Review record and issue status update drafts.

**Automated check (not classroom proof):** Headless Chromium tests passed keyboard movement for P1/P2, grab/release with auto-deposit, accelerated round transitions and simulated permission-error visibility. Evidence and limitations are recorded in [`QA_AUTOMATED_SMOKE_REPORT.md`](./QA_AUTOMATED_SMOKE_REPORT.md). Real webcam and hand gesture testing remains pending.

**Difference from the previous tutor review:** not established from the available evidence. Add only changes you can connect to earlier commits/review notes.

## Evidence / links to add after running

| Evidence | Link or observation | Status |
| --- | --- | --- |
| Playable HTML | [`../GIVE_ME_YOUR_FRIES_DUO_GESTURE.html`](../GIVE_ME_YOUR_FRIES_DUO_GESTURE.html) | Submitted in PR #7 |
| README | [`../README.md`](../README.md) | Submitted in PR #7 |
| Headless keyboard smoke test | [`QA_AUTOMATED_SMOKE_REPORT.md`](./QA_AUTOMATED_SMOKE_REPORT.md) | Passed in local Google Chrome; real playtest pending |
| Keyboard gameplay recording | _Add your recording link_ | Pending real-device capture |
| P1 movement → collection → score update | _Record result, browser, OS, timestamp_ | Pending verification |
| P2 independent movement | _Record result_ | Pending verification |
| Webcam preview + two-hand pinch | _Record real-device result_ | Pending verification |
| PR / commit | [PR #7](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/pull/7) · [commit `55d840c`](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/commit/55d840c6afa2f16ada045947f79818e449492121) | Open for review |
| Project item / Issues | [05 Nov review card](https://github.com/orgs/sd5913/projects/8?pane=issue&itemId=286847119) · [#4](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues/4) · [#5](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues/5) · [#6](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues/6) · [#8 camera validation](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues/8) | Live links verified; owners still to be confirmed |

## Current blocker / question for the tutor

**Camera reliability and accessible deployment.** The browser's camera permission / secure-context requirements and MediaPipe CDN/model availability can interrupt two-person gesture input. We can demonstrate the gameplay with keyboard input, but need a repeatable HTTPS-hosted or local-server setup to verify the webcam mode reliably.

**Question:** For the 12 November integrated-core milestone, is it acceptable to treat keyboard control as the stable interactive baseline while we validate camera mode on the classroom hardware? What minimum evidence is expected for camera success?

## Tutor feedback — complete only after the meeting

- **What works (observed with tutor):** _Pending_ 
- **Tutor feedback:** _Pending_ 
- **Additional blockers:** _Pending_ 
- **Decision / agreed smallest next goal:** _Pending_ 
- **Next goal owner(s):** _Assign in GitHub Project after discussion_ 
- **Next checkpoint:** 12 November 2026 — integrated core experience.

## After the review

1. Record actual feedback and the agreed goal above, then commit this document.
2. Link this review from the README (already linked in the local draft).
3. Update your existing GitHub Project item **“05 Nov | Tutor review: first working interaction”** with links to this file, the playable build, test evidence and the next goal.
4. Verify that Issues #1–#6 and Project Board statuses match; do not create duplicates merely because the board says Todo.
