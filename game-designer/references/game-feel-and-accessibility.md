# Game Feel and Accessibility

## Contents

- [Define the intended interaction](#define-the-intended-interaction)
- [Separate the causes of feel](#separate-the-causes-of-feel)
- [Tune a complete action](#tune-a-complete-action)
- [Match the workflow to the game](#match-the-workflow-to-the-game)
- [Provide useful control and comfort options](#provide-useful-control-and-comfort-options)
- [Verify and report](#verify-and-report)

Use B5 in [sources.md](sources.md) for the provenance of the game-feel reference. Treat its focus on input, response, context, and feedback as a useful lens, not a prescription for every genre. This document supplies original working procedures and examples; it does not claim complete access to the book or functioning historical companion software.

## Define the intended interaction

Name the action, its purpose, and its desired sensation before adding effects. Examples: a heavy strike should feel committed and legible; petting a shy creature should feel gentle and responsive; moving a building should feel precise and reversible. Identify the input device, expected pace, camera, and likely physical demands.

Choose one representative interaction and include its full cycle: available state, input, response, consequence, recovery, and readiness for the next action. Reuse the experience goals in [design-brief.md](../assets/templates/design-brief.md). Avoid optimizing responsiveness in isolation when deliberate delay is part of the intended decision.

## Separate the causes of feel

| Component | Diagnostic question | Possible adjustment |
|---|---|---|
| Input | Can the player express the intended action reliably? | Binding, dead zone, hold or toggle behavior |
| Response | What state change follows, and when? | Acceleration, buffering, aim behavior, activation timing |
| Context | Does the surrounding space make the action useful? | Target spacing, camera framing, collision margins |
| Consequence | Do the rules make its result understandable? | Resource cost, commitment, interruption, recovery |
| Feedback | Can the player perceive what occurred? | Pose, sound, marker, vibration, text, animation |

Diagnose before decorating. An unreadable impact may require clearer timing; an unsatisfying impact may come from weak consequences; an unreliable interaction may have a small target. More particles will not establish which problem exists. Check whether visual appearance agrees with collision and interaction boundaries.

Distinguish functional feedback from spectacle. Communicate availability, acceptance, success or failure, cost, and recovery. Choose a coherent priority when several events happen together so the most actionable information remains readable.

## Tune a complete action

1. Capture the current behavior in a repeatable scene, build, or short recording. Use tool measurements only for properties the tool actually measures.
2. Write a hypothesis in [experiment-card.md](../assets/templates/experiment-card.md): the suspected cause, proposed parameter change, expected benefit, and possible cost.
3. Expose a small set of relevant parameters rather than scattering magic values through code. Keep a known baseline and label variants clearly.
4. Change one cause, or one tightly related group, at a time when comparison matters. Preserve input and scene conditions where practical.
5. Check the entire action cycle, including failure, interruption, repeated input, and transition into the next action.
6. Compare with human observation when available; record synthetic reviews and technical checks separately. Keep the variant that best supports the intended experience and evidence.

For a dash, examine activation, distance, acceleration, collision, recovery, and camera behavior before adding trails. A longer dash may improve expression while invalidating obstacle spacing. For feeding a creature, examine selection, range, acceptance, inventory change, the creature's response, and cancellation. Faster feedback may help while a longer celebration becomes irritating when repeated.

Use contrasting variants to discover direction, then refine. Do not present invented “industry standard” timing values as evidence. Derive initial values from the game's scale and intended pace, measure them, and keep tuning reversible.

## Match the workflow to the game

For action games, prioritize consistent input handling, readable motion, camera behavior, interrupt rules, and the relationship between animation and active states. Check behavior under the performance conditions the target build is expected to support. Do not confuse a smooth recording with a responsive playable build.

For management, strategy, and collection games, prioritize selection, information hierarchy, command confirmation, navigation, preview, undo where appropriate, and recovery from mistakes. Inspect repeated actions: a delightful first animation can become a bottleneck after twenty uses. Allow speed or skipping options where they preserve comprehension.

For narrative or contemplative games, preserve pacing and intentional ambiguity while making interaction expectations understandable. Avoid adding constant motion, reward sounds, or urgency simply because an action game uses them. Judge the result against the requested experience.

## Provide useful control and comfort options

Review access needs as part of the interaction, including motor demands, vision, hearing, cognition, and comfort. Choose options relevant to the actual game rather than adding an unused settings checklist. Consider:

- Remappable inputs, updated prompts, alternatives to repeated presses, and hold or toggle choices.
- Adjustable text and interface scale, readable contrast, clear focus indicators, and information that does not rely on color alone.
- Captions or other equivalents for essential audio information, and distinguishable visual or audio cues where useful.
- Motion, camera shake, vibration, flashing, and intense effects controls; preserve essential information when reducing effects.
- Pause, timing, difficulty, or assistance options where compatible with the game, explained by what they change.

Preserve settings across relevant transitions and provide a clear reset. Check menu navigation and error states with the supported devices. Avoid assuming that one accessibility option serves every player with the same diagnosis. Do not claim accessibility conformance from a checklist or simulation; consult current authoritative guidance for platform-specific requirements and include people with relevant experience when possible.

## Verify and report

Report the intended sensation, observed defect or uncertainty, changed parameters, checked conditions, tradeoff, and remaining human evaluation. Verify that reduced-effect settings retain critical cues and that remapped actions display correct prompts. Use [playtesting-and-evidence.md](playtesting-and-evidence.md) to keep technical correctness separate from player experience.

If direct interaction is unavailable, inspect code, event ordering, assets, and recordings, then prepare targeted checks. State the access limit precisely and continue with useful reversible improvements supported by available evidence.
