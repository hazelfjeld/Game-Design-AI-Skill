# DES-7 — Feeding preference observation plan

**Status:** Plan prepared for producer review. **Human sessions completed: 0.** No participant behavior, quotations, comprehension results, or enjoyment findings have been collected. The experience hypothesis remains unvalidated.

## Decision and scope

Can a player new to Harbor infer a ray's food preference from its response, and distinguish that information from hunger being satisfied? Use the next observations to decide whether to retain the current feedback, clarify the preference signal, or investigate hunger feedback first. Preserve the calm sanctuary tone, simple mouse controls, two rays, and two foods; stopping carries no penalty. This task adds no mechanics, food types, or success pressure.

The intended experience and available content come from [GAME_BRIEF.md](../GAME_BRIEF.md). [Decision 001](decision-001.md) makes preference recognition a hypothesis and requires hunger satisfaction to be distinguished from preference. **Design hypothesis:** a player who understands the response can anticipate a particular ray's response to a food and explain the cue without treating every hunger improvement as a preference.

## Current evidence and dependency

**Build observation — source inspection only, 2026-11-23:** on branch `main`, base commit `bc2df9d0aa46bd3b085ca034e635e8c02a946ddc`, [game/feeding.gd](../game/feeding.gd) sets `preferred_food` to `kelp` and returns `happy` for a match and `neutral` otherwise. Its working copy also contains the engineer's unfinished-work comment. This shows a source-level distinction; it does not establish visible reactions, per-ray configuration, hunger behavior, or player understanding. No runnable project manifest, scene, or launch instructions were present in the inspected repository.

[ENG-12's latest checkpoint](../runs/eng-12-checkpoint.md) records ongoing work to separate preference and hunger signals. A human session depends on the engineer and producer providing an identified playable build and a verified setup. Preparing this plan does not depend on completing that work. No human sessions or runtime checks were performed in this run.

## Session setup

Use a small first round of up to three willing people who are new to this prototype and interested in a calm PC creature-care experience. This is a provisional effort bound for qualitative discovery, not a validation threshold. Record prior prototype/genre familiarity, mouse setup, relevant access needs volunteered by the participant, and recruitment context. Repeat participants and developers must be identified separately because prior knowledge changes the question. Recruitment has not been arranged or conducted.

Allow roughly 8–10 minutes, with no visible countdown or requirement to finish. Use anonymous session IDs and written notes; recording is unnecessary. Obtain permission if recording is later proposed. Explain that the game is being examined and that the participant can pause or stop at any time. Retain withdrawals and their context in the record.

Before testing, the engineer or facilitator records the actual build/version, date, launch procedure, displayed ray/food names, the hidden preference mapping, and placeholders in presentation. Call the displayed identities Ray A/B and Food A/B only in facilitator notes. Do not assume that `kelp` is a displayed label, that the other food has a particular name, or that the two rays have different preferences.

The facilitator checks the following in the playable build without coaching a participant:

- Both foods can be offered to each ray, the rays can be reliably distinguished, and the response is observable. Record what is actually visible/audible rather than assuming `happy` and `neutral` are implemented animations.
- Record the hunger meter's units/direction, each food's hunger effect, and whether fullness or a clamp suppresses either the response or meter movement.
- Identify a repeatable, non-capped starting hunger state for comparisons. An existing reset/snapshot may be used only if it preserves ray identities and preference mappings. Verify the mapping after reset; do not introduce new reset code in this task.
- Record whether both foods produce the same hunger change in matched conditions. A different hunger change is a competing explanation for a food choice, not proof of preference recognition.

If a comparable state cannot be restored, record the actual state and continue only as exploratory observation. Do not claim that reaction and hunger effects have been isolated. If the build cannot be played or responses cannot be observed, record the specific readiness issue and defer the human session. If both rays share a preference, the session may test food-response comprehension, but cannot establish that players understand differences between individuals.

## Neutral session script and order

### 1. Natural exploration — up to about three minutes

Say: “This is a small creature sanctuary. Explore and care for the rays as you normally would. We are checking the game, and you can pause or stop whenever you want. I may stay quiet while you explore.”

Give only the minimum input instructions needed to start; record their exact wording. Do not mention favorites, preferred foods, distinct reactions, or where to look. Observe food choices, feeding events, attention to the screen, repeat attempts, pauses, spontaneous comments, and stopping. Do not praise a particular choice or ask for continuous commentary.

If the participant becomes blocked, first note what they attempted and ask, “What are you trying to do?” Provide only the assistance needed to continue. Record its time and wording. Later behavior affected by that help is assisted evidence. Do not count failure to encounter both foods as failed comprehension.

### 2. Capture the initial interpretation before teaching anything

Ask: “What do you think happened when you fed the rays?” Follow with “What made you think that?” and “What would you choose to do next, if anything?”

If they choose another feeding action, ask before its outcome: “What do you expect to happen, and what makes you expect that?” Record the selected ray/food, prediction, reason, and then the result. Ask once rather than repeating until the intended answer appears. Capture uncertainty as a valid response. This is an elicited report following natural play; distinguish it from something said spontaneously.

Close and preserve these initial notes before the next stage. A correct food choice by itself may be a guess, a habit, or an attempt to increase hunger satisfaction.

### 3. Separate, prompted comparison — only while the participant wishes to continue

Say: “For this next section, please try each of the two foods with each ray in the order I give you. Take your time.” This deliberately supplies comparison opportunities, so any new understanding belongs to the **prompted-comparison** stage. Do not combine it with unassisted discovery.

Use one of these facilitator orders, alternating across sessions if practical. These are planned order cards, not completed sessions. Substitute the actual displayed names without revealing the hidden mapping.

| Trial | Order A | Order B |
|---|---|---|
| 1 | Ray A, Food A | Ray B, Food A |
| 2 | Ray B, Food B | Ray A, Food B |
| 3 | Ray A, Food B | Ray B, Food B |
| 4 | Ray B, Food A | Ray A, Food A |

Return the relevant ray to the verified comparable starting state before every trial, and record both hunger values and the response. Explain any reset neutrally: “I am returning the scene to the same starting point.” If restoration changes another relevant condition, flag the trial as unmatched. Order variation reduces a simple order confound; this small round cannot establish an order effect statistically.

Repeat the neutral interpretation and next-action prediction questions from stage 2 once after the comparisons. Do not reveal whether a prediction is correct before the action. Record incomplete trials and the reason rather than pressing someone to finish.

### 4. Retrospective debrief

Ask: “What were you trying to do at [observed moment]?”, “What felt clear or unclear?”, and “What would you choose to do next, if anything?”

Only after the initial and comparison interpretations have been saved, ask the diagnostic questions: “What did the hunger display tell you, if anything?” and “What did the ray's response tell you, if anything?” These questions direct attention to specific signals; label answers as **diagnostically prompted reports**. They cannot retroactively establish spontaneous understanding. Accept “the same thing” or “I don't know” without correction. Offer an explanation after observation has ended if the participant wants one.

## Observation record

Create one dated, anonymous note per actual session in a path assigned by the producer. This run does not create fictional participant records. Copy the following fields into that note:

- **Context:** session ID; date; exact build and relevant local changes; device/input; prior exposure; observer; presentation placeholders; order card; permission/recording status.
- **Ground truth, facilitator only:** displayed identities; verified preference mapping; hunger units/direction; target starting state; actual food effects; reset method and stability check.
- **Event rows:** elapsed time in seconds; stage; ray; food; hunger immediately before/after; visible/audible response; selected next action; pre-action prediction and its stated basis; exact quotation or marked paraphrase; any help; matched/unmatched condition.
- **Opportunity:** which ray/food pairs were actually seen; whether both foods were encountered for each ray under comparable hunger conditions; capped results, blocked actions, and missing data.
- **Outcome and interpretation:** comprehension category below, cited event(s), alternative explanation, missing evidence, and the smallest next question. Keep these judgments separate from raw behavior and speech.

A session with no feedings remains an onboarding/access or voluntary-stopping observation. A session without comparable exposure remains insufficient evidence for the controlled preference question. Report those sessions rather than removing them from the account.

## Analysis and next decision

Treat behavior, participant reports, and designer interpretations as separate evidence. Classify each ray only where an actual observation supports it:

| Category | Evidence needed / limit |
|---|---|
| Preference comprehension supported in this session | The participant predicts a ray-food response consistent with the verified mapping, gives an observed cue as the reason, and distinguishes that cue from hunger movement when the two explanations can be separated. Record stage and assistance. A correct guess or food choice alone is insufficient. |
| Hunger interpretation only | The participant explains choices/results through hunger or meter changes and provides no supported food-response distinction. This may be sensible care behavior; it does not demonstrate the preference hypothesis. |
| Mixed or uncertain | The explanation links both signals, contradicts a prediction, or the build makes the two explanations inseparable. Preserve competing explanations. |
| Insufficient opportunity | Exposure, visibility, comparable states, participation, or logging did not permit the question to be evaluated. This is not a comprehension failure. |

Summarize the actual counts with denominators: all sessions started; sessions with comparable exposure for each ray; natural-stage, prompted-comparison, and assisted evidence separately. With no sessions the current result is **0 observed sessions; comprehension not assessed**. Do not estimate population success rates, enjoyment, retention, or accessibility from this small study.

Use the following provisional decision rules after real observations:

- If preference is inferred before comparison prompting and supported by the prediction/reason evidence, retain the feedback provisionally and check for conflicting cases. No fixed participant count makes it validated.
- If only the prompted comparison makes the cue understandable, investigate discoverability or opportunities to compare before redesigning the response itself.
- If comparable observations repeatedly yield hunger-only or confused explanations, propose the smallest preference/hunger feedback distinction and state its predicted effect before retesting. Do not add foods to solve an unclear signal.
- If presentation is missing, hunger effects differ, resets change mappings, or conditions are otherwise confounded, resolve that concrete build/setup issue or narrow the claim. Do not infer a player comprehension deficit from it.

**Next action:** the producer reviews this plan and resolves ENG-12's build/handoff readiness; the engineer supplies a playable version and verified signal/mapping details. A facilitator can then run the neutral sessions and bring raw notes back for a scoped design decision. Human observation remains pending and is not replaced by this document or by software checks.
