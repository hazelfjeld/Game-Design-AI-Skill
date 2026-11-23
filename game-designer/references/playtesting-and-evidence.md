# Playtesting and Evidence

## Contents

- [Choose the decision](#choose-the-decision)
- [Label evidence accurately](#label-evidence-accurately)
- [Run a neutral session](#run-a-neutral-session)
- [Recruit and interpret carefully](#recruit-and-interpret-carefully)
- [Measure the relevant behavior](#measure-the-relevant-behavior)
- [Turn findings into revisions](#turn-findings-into-revisions)
- [Continue without human testers](#continue-without-human-testers)

Use this workflow to reduce a design uncertainty. Treat the developer accounts indexed as B7 and W3 in [sources.md](sources.md) as examples of situated decisions, not universal recipes. The procedures and examples below are original guidance; source access is documented separately.

## Choose the decision

Identify one decision the next session can inform. Replace “Is this fun?” with a question such as “Can a new player recognize the cost of keeping a second creature?” or “Does this attack communicate when the player can act again?” State the intended experience, current concern, smallest useful build, and what observation would change the design.

Use [playtest-plan.md](../assets/templates/playtest-plan.md) and [experiment-card.md](../assets/templates/experiment-card.md). Reuse existing project criteria instead of inventing a new approval gate. A rough prototype may be sufficient to test a tradeoff; visual appeal requires a representative presentation. Record which parts are placeholders so conclusions stay within what the build can demonstrate.

## Label evidence accurately

Maintain separate fields in [playtest-observation.md](../assets/templates/playtest-observation.md):

| Evidence type | Example | Permitted conclusion |
|---|---|---|
| Observed human behavior | P03 opened inventory four times before feeding | This behavior occurred in this session |
| Participant report | P03 said the food icon resembled a coin | This participant reported that interpretation |
| Designer interpretation | The icons may be visually confusable | A plausible explanation requiring examination |
| Design hypothesis | A bowl silhouette may improve recognition | A proposed change and prediction |
| Simulation | A scripted agent chose feeding in 91 of 100 runs | Behavior under the stated model and policy |
| Technical QA | A tool confirmed the button dispatches one event | The checked implementation behavior works |

Record build, task, device, relevant audience experience, assistance, and timestamp when available. Keep quoted speech distinct from paraphrase. Never invent participant identities, sessions, quotations, reactions, or measurements. Label an AI critique or persona walkthrough as a synthetic review. Neither simulation nor direct tool interaction establishes human enjoyment, comprehension, accessibility, or purchase intent.

## Run a neutral session

Use a short script and adapt it to the project:

> We are testing the game. You can stop whenever you want. Try this section as you normally would. I may stay quiet while you explore. If something is unclear, tell me what you are trying to do.

Give a goal without revealing the solution: “Keep both creatures fed until nightfall,” rather than “Open the backpack and drag the berries.” Avoid praising an intended action or describing a feature as exciting before it is played. Ask permission before recording a participant, and honor existing privacy and consent arrangements.

Observe before explaining. If someone becomes blocked, note the blockage and any assistance, then help enough to reach the next useful observation. Do not count assisted completion as independent success. Use retrospective questions for timing-sensitive actions; continuous commentary can change how someone plays.

Ask neutral follow-ups: “What did you expect?”, “What were you deciding between?”, “What made you stop?”, and “Which moment would you change?” Ask why after capturing behavior. Avoid “Did you like the improved combat?” or promising additions to obtain approval.

## Recruit and interpret carefully

Recruit for the question: new players for onboarding, experienced genre players for strategic depth, and people with relevant access needs for accessibility experience. Record who participated and how they were recruited. Friends, developers, enthusiasts, existing fans, and festival visitors can each produce useful but different evidence.

Treat small rounds as qualitative discovery. Report “three of five participants missed the marker in this build,” not a population estimate or proof of universal failure. Include conflicting observations and withdrawals. Repeated sessions with the same person show learning as well as design changes. For comparisons, vary order where practical and record prior exposure, device differences, and other changes.

Do not use a fixed tester count as a guarantee. Broaden recruitment when a decision depends on an unrepresented audience or observations conflict. Preserve the distinction between an individual preference and an obstacle shared across contexts.

## Measure the relevant behavior

Select a few measures that answer the decision: time to first meaningful action, unassisted completion, repeated failed attempts, choice diversity, interruptions, or whether participants choose to continue when genuinely free to stop. Define start and stop events, units, denominators, and exclusions before collecting numbers where feasible.

Pair measurements with observations. Fast completion may reflect understanding, guessing, or skipping content. Long play may reflect engagement or confusion. A short session does not establish long-term retention. A stated willingness to buy is a report, not a purchase. Disclose missing logs and distinguish observed counts from estimates.

## Turn findings into revisions

Group findings by player consequence: blocking progress, obscuring a decision, weakening feedback, or expressing a preference. Select the smallest change that addresses the most consequential supported problem. Preserve alternative explanations in the experiment card and state what a follow-up would distinguish.

Fix directly demonstrated defects without waiting for a broad playtest. Repeat human observation when the unresolved question concerns experience. Avoid changing unrelated systems together if that would make the next result uninterpretable. Summarize the observation, interpretation, change, uncertainty, and next decision. Apply release gates only when the project actually defines them.

## Continue without human testers

Inspect the build, reproduce defects, review input and progression paths, run relevant simulations, prepare the next experiment, and improve clear implementation problems. Produce a reviewable build or concise findings rather than stopping at “needs playtesting.” Mark experiential claims as unvalidated and list the specific human observation still needed.

Prepare recruitment messages or public test materials when useful. Send messages, recruit through another person's account, or publish a build only within the user's authorization; do not treat a prepared draft as permission to distribute it.
