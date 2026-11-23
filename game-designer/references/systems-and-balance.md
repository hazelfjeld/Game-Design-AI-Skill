# Systems and balance

Evaluate mechanics, progression, economies, and interactions. Adapt ideas from *Designing Games* and *The Art of Game Design*; see [sources](sources.md). Treat these procedures, examples, and numerical assumptions as original synthesis.

## Contents

- [Define the experience and decision](#define-the-experience-and-decision)
- [Map interactions before adding content](#map-interactions-before-adding-content)
- [Check strategies and accessibility](#check-strategies-and-accessibility)
- [Model the economy with explicit units](#model-the-economy-with-explicit-units)
- [Worked example](#worked-example)
- [Align rewards and emergent stories](#align-rewards-and-emergent-stories)
- [Match the method to the genre](#match-the-method-to-the-genre)
- [Report a bounded recommendation](#report-a-bounded-recommendation)

## Define the experience and decision

Start with an intended experience and a concrete moment of play. Record what the player knows, can do, values, and risks losing. Distinguish expression from optimization: choosing a favorite color can be valuable without a tactical tradeoff.

For a decision intended to provide strategy, identify:

1. Alternatives that a player can recognize.
2. Consequences that differ along relevant goals, timing, or risk.
3. Information sufficient to form an expectation, with deliberate uncertainty identified.
4. Feedback that connects the outcome to the choice.
5. Conditions that could make a different alternative attractive later.

Investigate repeated automatic choices before adding options. Determine whether repetition supports mastery, comfort, expression, or an unwanted chore. Form a falsifiable hypothesis such as: “Players ignore shelter because its effect arrives after the expedition and is never attributed to shelter.” Test that explanation before changing several systems together.

## Map interactions before adding content

List mechanics, resources, creature traits, environments, and player verbs. Build an interaction matrix of plausible causal relationships; an empty cell can mean intentionally independent systems.

| Pair | Proposed interaction | Player-visible consequence | Evidence to seek |
|---|---|---|---|
| Ray temperament × habitat | A curious ray investigates changing decorations | New discoveries appear near rearranged objects | Players attribute a discovery to their arrangement |
| Current × movement | A sheltered route changes swimming control | Safer travel competes with an exposed shortcut | Players choose routes for different reasons |
| Food × expedition | Preparation changes one expedition capability | A preparation choice changes a later action | Players predict and use the capability |
| Weather × habitat | Shelter changes which visitors arrive | Environment supports a different collection goal | Players intentionally create distinct habitats |

Treat the matrix as hypotheses. Prototype one interaction with readable feedback. Check for decisions, expression, discovery, or memorable consequences. Remove redundancy and explainability costs.

Measure content leverage by useful variation per authoring, implementation, and testing effort. Recombining three legible rules can be valuable; generating thousands of combinations does not establish thousands of worthwhile experiences. Track unreachable combinations, equivalent outcomes, dominant combinations, and interactions that confuse players.

## Check strategies and accessibility

Specify the objective before declaring something overpowered. Examine ordinary play, expert play, and deliberate exploitation separately. Search for resource loops, compulsory actions, runaway advantages, and choices whose apparent diversity collapses into one answer.

Reserve “dominant” for an option or strategy that is at least as good across the relevant alternatives or opponent responses and better in some. Distinguish dominance from a higher average return, popularity, ease of execution, or preference among sampled players. A powerful strategy may intentionally express the fantasy; adjust it only when it damages the intended experience, variety, fairness, or challenge.

Test candidate fixes against the actual cause. Change costs, information, timing, context, counterplay, or feedback when appropriate. Avoid making every option numerically identical. Preserve different strengths when those differences produce understandable reasons to choose.

Separate strategic depth from the burden of learning rules or operating controls. Introduce a usable action first, reveal consequences, then add combinations. Offer readable previews, forgiving recovery, adjustable timing, or optional complexity where they support the audience. Observe both first-session comprehension and later adaptation; neither establishes the other.

## Model the economy with explicit units

Create a ledger for every resource: unit, source, sink, storage limit, transfer rule, conversion rate, and purpose. Identify whether measurements are per action, minute, expedition, player, or session. Never compare rates with different denominators without conversion.

Use a balance equation such as `inventory_next = inventory_now + earned - spent`. List assumptions about skill, session duration, failure, trading, and repeatability. Account for one-time rewards separately from renewable income. Check whether a sink is optional expression, necessary progression, maintenance, or punishment.

For discrete outcomes, calculate `E[X] = sum(p_i * x_i)` and `Var(X) = sum(p_i * (x_i - E[X])^2)`. State whether costs are fixed or outcome-dependent. Preserve distributions when rare failure, streaks, low starting wealth, or long waits matter. An average cannot show whether a player can afford the next action.

Evaluate novice, typical, expert, and exploit conditions without pretending those groups have measured probabilities. Label assumed rates. Use sensitivity ranges where evidence is missing. Check finite horizons, compounding upgrades, conversion cycles, caps, and whether the intended progression remains viable without repetitive grinding.

## Worked example

Assume a fictional collector has three-minute expeditions, a fixed four-shell departure cost, no travel variance, independent outcomes, and no rewards other than shells. Assume the player can afford either route. These numbers illustrate reasoning; they are not recommended tuning values.

| Route | Gross reward | Net outcomes | Expected net | Net standard deviation |
|---|---|---|---|---|
| Calm | 10 shells with certainty | 6 shells | 6 shells/trip | 0 shells |
| Storm | 18 shells with probability 0.5, otherwise 0 | 14 or -4 shells | 5 shells/trip | 9 shells |

Calculate storm expectation as `0.5 * 14 + 0.5 * (-4) = 5`. Calculate its variance as `0.5 * (14 - 5)^2 + 0.5 * (-4 - 5)^2 = 81 shells²`. Divide by three minutes to obtain expected net rates of 2 and approximately 1.67 shells/minute.

Under these assumptions, a risk-neutral player maximizing expected shells prefers calm. Do not call calm strictly dominant: storm can produce a larger realized reward. A player with only four shells also faces a possible loss of access to expeditions; determine whether that outcome serves the intended game.

Suppose an upgrade costs 20 shells and adds a guaranteed two net shells to every expedition without changing its duration. Its undiscounted payback is `20 / 2 = 10 trips`, or 30 minutes. Check that players expect to make ten more trips and that buying it does not prevent departure. Recalculate if the bonus is conditional or changes success probability.

Add a rare cosmetic discovery to storm only if collection is an intended goal. Then report a multi-objective decision; do not silently convert attachment or novelty into shell values. Test whether players understand and value that opportunity.

## Align rewards and emergent stories

Compare what the game promises with what its rewards encourage. Investigate whether players optimize away exploration, social cooperation, creativity, or interesting combat to maximize a counter. Prefer rewards that reinforce the desired activity; retain optional goals for differing tastes.

For emergent narrative, connect understandable states, player actions, and persistent consequences. Give players enough feedback to attribute an event and retell it. Evaluate whether they remember an interaction between systems, not merely a random event announcement. Preserve recoverability when attachment and care are central.

## Match the method to the genre

For real-time action, measure input timing, readability, recovery opportunities, and control feel alongside numerical balance. For strategy, examine information and adaptation. For cozy or expressive games, examine agency, attachment, pacing, and freedom from unwanted pressure; do not impose compulsory failure, optimal builds, or retention targets as universal requirements.

Use simulations to find arithmetic errors and candidate exploits. Label perfect-play agents, simplified rules, and missing emotions. A simulation establishes behavior under its model, not human enjoyment, discoverability, or willingness to continue.

## Report a bounded recommendation

Return the diagnosed experience, supporting evidence, explicit assumptions, one recommended change, a plausible alternative, and the next observation that would distinguish them. Mark human evidence pending where appropriate. Keep untested values provisional and preserve a baseline for comparison.
