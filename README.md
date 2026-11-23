# Game Design AI Skill

A reusable **Game Designer** skill for developing, diagnosing, and improving indie games through concrete design decisions and observed evidence.

The package gives an AI assistant a structured way to reason about player experience, mechanics, interacting systems, balance, game feel, playtesting, production scope, and audience positioning. It also supports bounded runs by agents collaborating through a repository.

**Start with [`game-designer/SKILL.md`](game-designer/SKILL.md).** The skill loads focused references when needed instead of requiring the entire collection for every question.

## What it does

| Task | Expected result |
|---|---|
| Develop a new concept | A clear player experience, a few credible alternatives, and a scoped first experiment |
| Improve a weak prototype | A diagnosis tied to observed behavior, competing explanations, and a concrete revision |
| Design mechanics or progression | Explicit rules, state changes, feedback, edge cases, and acceptance checks |
| Analyze balance or an economy | Assumptions, units, auditable calculations, sensitivity, and limits of the model |
| Improve game feel | Experiments with input, response, feedback, readability, and comfort |
| Interpret playtests | Observations separated from interpretation, synthetic critique, and technical QA |
| Plan production | A representative slice, scope decisions, measured production assumptions, and milestones |
| Investigate an audience | Comparables, a truthful player promise, and separate tests of presentation and gameplay |
| Continue a shared project | One eligible task, explicit ownership, relevant verification, and a resumable handoff |
| Coach a beginner | A short design exercise and an observable learning milestone |

The skill adapts to cozy, competitive, narrative, systemic, expressive, experimental, and noncommercial games. It preserves the user's purpose rather than forcing every project toward combat, numerical optimization, or endless engagement.

## Use it in an AI instance

### With skill support

Install the complete `game-designer/` directory through the environment's supported skill workflow. Keep `SKILL.md`, `agents/`, `references/`, and `assets/` together. Where supported, invoke it by the skill name, `game-designer`, or select **Game Designer** in the skill interface.

Example prompt:

```text
Use $game-designer to review my current game concept and available project files.
Identify the most important design uncertainty, recommend a focused direction,
and produce the smallest useful prototype specification and playtest plan.
State assumptions and distinguish predictions from observed evidence.
```

### With repository or file access

Give the instance access to this repository or attach the package files, then use:

```text
Read game-designer/SKILL.md in hazelfjeld/Game-Design-AI-Skill.
Load the referenced modules needed for my request and follow their workflow.
Apply it to the project materials I provide. Do the authorized work, record
what was actually verified, and leave the next useful action.
```

A repository URL alone does not install a skill or guarantee that an assistant has read its files. The instance needs actual access and must read the relevant instructions. A text-only conversation can still produce design work, but it must not claim to have played a build it could not access.

## Run it with a team

Read [`production-and-collaboration.md`](game-designer/references/production-and-collaboration.md). Preserve the team's existing roles. If no roles exist, the reference offers a lightweight split across design, engineering, art/audio, production/integration, and QA/playtesting.

The recurring-run workflow is:

1. Read current project instructions, board, handoff, decisions, and repository state.
2. Select one eligible outcome and confirm ownership through the project's coordination mechanism.
3. Make a bounded change without overwriting another contributor's work.
4. Check relevant behavior and label any evidence still missing.
5. Preserve the artifact, decision, evidence, and next action in a durable handoff.

Use the [project-board template](game-designer/assets/templates/project-board.md) and [run-handoff template](game-designer/assets/templates/run-handoff.md) only when the project lacks a suitable format. Markdown claim records are not atomic locks; the workflow uses a serialized integrator or an existing atomic coordination service for exclusive claims.

For a run that has already been scheduled and authorized:

```text
Use game-designer for one bounded design run in <project repository>.
Read the current instructions, board, decisions, and latest handoff.
Complete one eligible task within your ownership. Preserve unrelated work,
verify what you can, and save a precise handoff with pending evidence.
Follow the project's existing publication and communication authorization.
```

This skill does not create schedules, provide background execution, grant account access, or authorize outreach, spending, or releases. Those capabilities and permissions belong to the host environment and the user's task.

## Contents

- **One main skill:** routing and the experience → rule → prototype → evidence → revision workflow.
- **Eight references:** foundations; systems and balance; playtesting; feel and accessibility; production and collaboration; audience and positioning; learning path; sources.
- **Nine templates:** design brief, mechanic specification, experiment, playtest plan, observation, decision record, slice plan, project board, and run handoff.
- **Agent interface metadata:** human-facing name and a starter prompt.
- **Repository validation and evaluations:** checks and behavior evidence for maintaining the package.

See [`evaluations/RESULTS.md`](evaluations/RESULTS.md) for the actual validation scope, task outcomes, and limitations. Run `python3 tools/validate_repo.py` to check structure, local links, frontmatter, metadata, and source coverage without network access. During skill development, `--skill-root /absolute/path/to/game-designer` checks the canonical package before it is mirrored into this repository. The official skill-creator validator is also run on the canonical skill during creation.

## Foundations and limits

The researched foundations are Tracy Fullerton's *Game Design Workshop*, Jesse Schell's *The Art of Game Design*, Tynan Sylvester's *Designing Games*, Richard Lemarchand's *A Playful Production Process*, Steve Swink's *Game Feel*, Raph Koster's *A Theory of Fun*, and Derek Yu's *Spelunky*. Practitioner and primary platform sources add audience research, developer case studies, and current-documentation habits.

See [`references/sources.md`](game-designer/references/sources.md) for editions, links, verification date, and access limits. This package is original operational synthesis from the research and general design reasoning. It does not contain the books, a copied lens deck, or claims that complete book texts were read during creation.

An installed skill supplies instructions and reusable references; it does not train new model weights or guarantee mastery, player enjoyment, or sales. Its quality depends on the host model, available tools, actual project context, and the evidence collected. In particular, AI persona feedback and automated checks remain distinct from human playtests.
