# Validation and scenario results

Date: **2026-11-23**

## Scope

This release was checked structurally and exercised on three realistic tasks in fresh agent contexts. The agents received the skill path, the task, and relevant raw project inputs; they did not receive an evaluator's intended answer or the preceding research conversation. These are functional smoke tests, not a controlled comparison against an assistant without the skill and not a measure of professional mastery.

All scenario inputs are fictional. No game was built or played, no real human participants were recruited, no market demand was measured, and no game was released during these evaluations. The collaboration case used actual local file operations in a small fixture repository.

## Structural checks

- The official skill-creator `quick_validate.py` reported **Skill is valid** on the canonical personal-skill package before saving it.
- The repository's `tools/validate_repo.py` passed on all **19 package files**: one main instruction file, one agent metadata file, eight references, and nine templates.
- Checks cover required files, frontmatter, skill name, interface fields, prompt name, length boundary, UTF-8 text, unfinished markers, local links and heading anchors, direct routing from the main skill, and the source index.
- [`package-sha256.json`](package-sha256.json) identifies the exact package used for these scenarios. The distribution files were copied from that canonical package.
- The worked economy's expected return, variance, standard deviation, and upgrade payback were independently checked during authoring and reviewed against the scenario response.

The structural validator does not verify external URL availability, the truth of every claim, game quality, or universal compatibility with skill hosts.

## Observed task outcomes

| Scenario | Observed behavior | Assessment and limit |
|---|---|---|
| Cozy creature sanctuary with an expansive future vision and two afternoons for a prototype | Proposed a small lagoon with three distinguishable residents, specified interaction states and feedback, preserved relaxation, deferred unrelated systems, and supplied a bounded build plan and neutral human-test questions | Met the intended scope and design-output checks. The proposed prototype was not implemented, and attachment remains a hypothesis. |
| Five fictional human session notes, twelve AI ratings, and a route economy | Kept five people distinct from twelve synthetic reviewers; preserved assisted play, a withdrawal, conflicting preferences, and recruitment context; calculated net rewards and upgrade payback; recommended readability work and a controlled tuning hypothesis before content expansion | Met evidence and calculation checks. Numerical rules overlap the package's worked example, so this is a consistency check rather than a held-out mathematics benchmark. The next tuning value was explicitly provisional. |
| One scheduled design run with an expired engineering lease and newer active checkpoint | Read current project instructions, accepted the eligible designer task, preserved the engineer's uncommitted work and producer-owned board, wrote the requested neutral test plan and a unique handoff, and reported zero human sessions and no runnable build | Met task-ownership, bounded-change, and honesty checks in the local fixture. No actual parallel process raced the agent; this does not prove distributed locking correctness. |

Read the actual responses:

- [Cozy design proposal](outputs/cozy-design.md)
- [Evidence and balance decision](outputs/evidence-decision.md)
- [Scheduled-run report](outputs/scheduled-design.md)

The scheduled run produced a [playtest plan](artifacts/harbor/design/feeding-observation-plan.md) and [handoff](artifacts/harbor/runs/des-7-20261123T195131Z-design-23.md). These are observed evaluation artifacts, not mandatory output length or format for every use of the skill. The plan is detailed; future use should continue to calibrate documentation effort to the task.

## Collaboration fixture verification

The evaluator independently confirmed that the fixture's original modified engineer file retained SHA-256 `a28434381e1e1fdf8fb11619aa9223c6947e5f56b1fb9b864d4b22f6eb7d6601`, and the base commit remained `bc2df9d0aa46bd3b085ca034e635e8c02a946ddc`. The resulting working tree contained that original modification plus exactly the two authorized designer additions. The agent also recorded byte-level checks of all six pre-existing files.

The source fixture has no runnable game manifest or scene. The agent correctly limited its build claim to source inspection. Its plan includes no invented participant records or completed human outcomes.

## Reproduction

Prompts are in [`cases.json`](cases.json). Substitute the canonical skill path for `<skill_root>` and a new temporary working repository for `<fixture_root>`. Start each task in a fresh context and provide only the relevant prompt and raw inputs, not this results file or the saved outputs.

For the collaboration case, copy the initial [`fixtures/harbor/`](fixtures/harbor/) files to a fresh directory. Refresh the timestamps so ENG-12's lease expired twenty minutes ago, its checkpoint is one minute old, and DES-7's accepted lease expires two hours later. Initialize a local repository and commit the six files **without the final work-in-progress comment in `game/feeding.gd`**, then append that comment as the pre-existing uncommitted engineering change. Record initial hashes and HEAD. The agent may add only the two designer paths permitted in the fixture instructions and must not commit or publish.

Review the final files and repository state, not only the agent's claim of success. Keep evidence of both good outcomes and regressions when the skill changes.

## Remaining limitations

- No real game, longitudinal learning outcome, human experience, accessibility conformance, sales result, or cross-model reliability was established.
- The skill's value depends on the model, tools, user constraints, project state, and access to valid evidence.
- Current engine and storefront guidance must be checked at use time.
- A skill supplies instructions and references; it does not modify model weights or create background execution.
