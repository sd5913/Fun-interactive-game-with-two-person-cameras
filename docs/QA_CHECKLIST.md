# QA checklist — first working interaction

Use this checklist on the intended demonstration computer. Record the browser, operating system, date, result, and a screenshot or short recording for each completed check.

## Keyboard baseline

- [ ] The page opens without a visible error.
- [ ] **Keyboard first** starts round 1.
- [ ] P1 moves with `W A S D`; P2 moves with the arrow keys.
- [ ] Holding `F` near fries lets P1 collect; releasing it returns P1 to the nest and increases the score.
- [ ] Holding `K` near fries lets P2 collect; releasing it returns P2 to the nest and increases the score.
- [ ] Carry, score, hit, round, and timer feedback remain readable for both players.
- [ ] The game advances through all three rounds and shows a final result.

## Optional webcam pathway

- [ ] Run from Chrome on `localhost` or HTTPS and allow camera access.
- [ ] Confirm the live preview appears.
- [ ] Wait for the MediaPipe status to confirm that the model loaded; a preview alone is not a pass.
- [ ] Confirm one hand in each half controls the corresponding player.
- [ ] Confirm a pinch produces a collect-and-return interaction for each player.
- [ ] Confirm permission, model-loading, and inference failures remain visible while keyboard fallback still works.

## Evidence still required

- [ ] Capture a 30–60 second real-device video showing two people and the complete input → response → feedback loop.
- [ ] Link the recording, browser/OS details, commit/PR, and relevant Issues in the tutor review record.
- [ ] Record tutor feedback and assign the agreed next goal.

The automated smoke test covers implementation behavior in headless Chromium. It does not replace the unchecked real-device and two-person checks above.
