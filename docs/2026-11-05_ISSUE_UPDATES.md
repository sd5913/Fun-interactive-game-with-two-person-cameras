# GitHub Issues and Board update drafts — 05 Nov 2026

These are the evidence-based updates prepared for the GitHub Issues and Project Board. Before posting, the live repository was verified at main commit `ba51823942ed4fded6eb9ecf28b6569ced4f193b`: Issue #4 was open, Issues #5 and #6 were closed with empty descriptions, and all three Project items displayed **Todo**. Assignees were not inferred.

## Live update record

The following changes were applied after the branch and evidence were uploaded:

- [PR #7](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/pull/7) opened from `tutor-review-2026-11-05`.
- [Issue #4](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues/4) received the UI/evidence progress comment and moved from **Todo** to **In progress**; it remains open.
- [Issue #5](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues/5) received the playable keyboard-prototype evidence comment and its closed card moved from **Todo** to **Done**.
- [Issue #6](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues/6) received a camera-evidence limitation comment and its closed card moved from **Todo** to **Done**.
- [Issue #8](https://github.com/sd5913/Fun-interactive-game-with-two-person-cameras/issues/8) was created for real webcam, MediaPipe, two-hand, and pinch validation; it was added to the Project Board as **Todo**.
- [05 Nov Tutor Review card](https://github.com/orgs/sd5913/projects/8?pane=issue&itemId=286847119) was updated with live build, PR, report, screenshots, review record, blocker, and #8 links; status moved from **Todo** to **Review**.
- Tutor feedback and owners remain **Pending**. Project visibility was not changed.

## Existing Issue #4 — Design Game UI and Visual Assets

**Recommended action:** Add the following progress comment to Issue #4. Keep it open until the acceptance criteria are demonstrated; assign the person responsible for UI/art only after confirming team responsibilities.

### Suggested comment

> **Progress — 05 Nov Tutor Review**  
> Existing playable two-player game uses a split HUD, character colours, seagull sprites with cartoon eyebrows/beaks, three distinct harbours, fries/guard icons, carry and score feedback, and a shared camera-preview overlay.  
> **Next visual/UX acceptance criteria:** (1) both players' controls, score, carry and hit states are readable; (2) webcam status stays visible after the intro closes; (3) warning and collision feedback are recognisable; (4) collect two real playtester observations; (5) add before/after screenshots to the issue.  
> A draft HTML update, QA checklist and **headless Chromium smoke-test report** are prepared for review. Keyboard movement and auto-return/score were covered; not claiming final UI polish or real camera validation yet.

## Existing Issues #5 and #6 — duplicate-looking titles

Both are titled **Build a Playable Cooperative Prototype**, are closed, have empty descriptions, and display **Todo** on the Project Board. **Do not re-open/close or infer their original scope from the duplicate titles.**

Because neither issue records acceptance criteria, keep the historical titles and add evidence comments. Treat #5 as the playable keyboard-prototype record and #6 as the optional camera-path record only in the progress comments; do not claim that the original issue authors intended that split. Suggested future titles, if the team later confirms the scope, are:

- **#5 [if it concerns gameplay]:** `Implement local two-player keyboard gameplay loop`
- **#6 [if it concerns camera]:** `Integrate optional two-hand camera input and fallback`

Only use these titles **if they match the actual issue bodies**. If the issue is truly complete with evidence, update its Project Board status to Done. If not, add a follow-up issue for the missing acceptance test rather than silently changing historical completed work.

## New issue draft A — P0: Verify camera access and two-hand gesture tracking on the demo machine

**Title:** `P0 · Validate webcam permissions and two-hand gesture tracking`

**Description:**

### Goal
Ensure both players can start the same webcam, receive two independent hand inputs, and complete an input→response→feedback cycle without hidden errors.

### Tasks
- [ ] Verify HTTPS/localhost demo URL on Chrome and macOS camera permission.
- [ ] Confirm live video appears after permission approval.
- [ ] Confirm MediaPipe v0.10.21 JS, WASM and hand model load on the demo connection.
- [ ] Verify distinct P1/P2 hand regions and pinch responsiveness.
- [ ] Confirm visible status/error feedback after the intro overlay closes.
- [ ] Record screen capture + browser/OS + outcome and link them here.

### Definition of Done
A two-player video shows independent gesture movement plus a successful collection/return, or the blocker is documented with reproduction steps and keyboard fallback evidence.

**Labels suggestion:** `bug`, `camera`, `high-priority` (create labels only if needed).  
**Assignee:** confirm with teammate.  
**Target:** before 12 Nov review.

## New issue draft B — P0: Record first working interaction evidence and update README

**Title:** `P0 · Document and test the first working two-player interaction`

**Description:**

### Tasks
- [ ] Run the current main-branch HTML in a desktop browser.
- [ ] Capture one keyboard demo: P1 move → dive → pick up fries → release → auto-return → score increases.
- [ ] Demonstrate P2 independent controls and HUD.
- [ ] Record pass/fail results in `docs/QA_CHECKLIST.md`.
- [ ] Add an actual screenshot/video link and commit/PR to `docs/2026-11-05_TUTOR_REVIEW.md`.
- [ ] Confirm two-person roles / ownership and next goal with tutor.

### Definition of Done
A tutor can run the demo from README instructions, inspect evidence, and understand the input→response→feedback loop and known blocker.

**Assignee:** confirm with teammate.  
**Target:** 5 Nov initial review, follow-up next checkpoint 12 Nov.

## Existing Project Board — 05 Nov | Tutor review: first working interaction

Paste this progress update in the existing card:

> **Review focus:** Show a complete two-player input→response→feedback loop.  
> **Build:** `GIVE_ME_YOUR_FRIES_DUO_GESTURE.html` (keyboard demo available, optional shared-webcam tracking).  
> **Code changes prepared:** visible webcam status in game footer; stable fries tray IDs; keyboard nest-target reset after delivery; README/run instructions and QA checklist.  
> **Evidence:** local headless keyboard smoke test passed (`docs/QA_AUTOMATED_SMOKE_REPORT.md`); real classroom capture and pushed commit link still pending.  
> **Current blocker:** camera permissions / MediaPipe network loading vary by browser environment; keyboard fallback is the safe demonstration path.  
> **Tutor feedback and next owner:** add after meeting.  
> **Review notes:** `docs/2026-11-05_TUTOR_REVIEW.md` (link after pushing).

**Suggested board status:** `Todo` until you conduct the actual review; then set Done or status appropriate to the group's workflow. Assign the card owner(s) once confirmed.

## Recommended commit and PR

**Branch:** `tutor-review-2026-11-05`  
**Commit:** `docs: prepare Nov 5 interaction review and improve camera feedback`  
**PR:** `Prepare first working interaction for Nov 5 tutor review`

**PR description:**

> - Improve always-visible webcam feedback, including permission/model failure information.  
> - Assign stable identity to fries trays at creation instead of patching `setupRound`.  
> - Add project README with control mappings and demo instructions.  
> - Document review objective, evidence checklist, technical blocker and next steps.  
> - Keep optional camera mode separate from reliable keyboard demo.  
> **Validation:** Add actual browser test results and evidence before merging. Do not claim successful real webcam tests unless performed.
