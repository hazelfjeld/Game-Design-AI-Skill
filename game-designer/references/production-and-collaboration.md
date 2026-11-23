# Production and collaboration

Turn design hypotheses into bounded, reviewable progress. Draw production principles from *A Playful Production Process* and iteration principles from *Designing Games*; see [sources](sources.md). Treat this agent coordination protocol as original synthesis, not a procedure claimed by those books.

## Contents

- [Choose the current production question](#choose-the-current-production-question)
- [Control scope through risk and cuts](#control-scope-through-risk-and-cuts)
- [Assign responsibilities and ownership](#assign-responsibilities-and-ownership)
- [Maintain a durable project board](#maintain-a-durable-project-board)
- [Resolve claims before shared edits](#resolve-claims-before-shared-edits)
- [Run one bounded scheduled cycle](#run-one-bounded-scheduled-cycle)
- [Integrate without losing work](#integrate-without-losing-work)
- [Leave a resumable handoff](#leave-a-resumable-handoff)

## Choose the current production question

Identify the project's phase from its actual artifacts and evidence. Use these distinctions to choose useful work:

| Artifact | Question it should answer | Completion evidence |
|---|---|---|
| Prototype | Does a specific interaction support the intended experience? | A playable experiment and observations relevant to the hypothesis |
| Representative slice | Can this team deliver a short, coherent sample at the intended quality? | An integrated sequence with representative controls, art, audio, onboarding, and measured production effort |
| Production build | Can the validated experience be extended and completed within scope? | Working content, integration evidence, progression coverage, and milestone acceptance |

Use temporary assets when they preserve the thing being tested. Include representative presentation early when attachment, visual readability, music, or atmosphere is the hypothesis. A prototype's unfinished appearance is acceptable only where it does not invalidate the question.

Do not treat one enjoyable interaction as proof of a complete game, a polished scene as proof of scalable production, or a completed milestone as evidence of commercial demand. Record each conclusion at the strength its evidence supports.

## Control scope through risk and cuts

List the largest uncertainties: core experience, controls, content cost, audience appeal, dependencies, platform constraints, and integration. Choose the smallest experiment that resolves a material uncertainty. Prefer learning before committing repeated production effort.

Estimate content using measured units such as accepted creatures per day or tested encounters per week. Include revision, integration, accessibility, audio, localization where required, and regression effort. Use ranges until the team has evidence. Separate an aspirational backlog from committed scope.

Define cuts before a deadline forces them. Protect the central promise and a complete beginning-to-end experience. Cut redundant content, secondary systems, and expensive edge cases before weakening every feature equally. Revisit the schedule when evidence changes; never disguise missing scope as completed work.

## Assign responsibilities and ownership

Respect the user's roles, decision rights, and priorities. When none are assigned, propose or adopt a lightweight responsibility map appropriate to the authorized task:

| Responsibility | Primary output | Boundary |
|---|---|---|
| Designer | Experience goals, rules, experiments, acceptance criteria | Keep tuning provisional until evidence supports it |
| Engineer | Working implementation, interfaces, technical checks | Surface design consequences of technical constraints |
| Art/audio | Readable presentation, animation, sound, style consistency | Coordinate asset interfaces and interactive feedback |
| Producer/integrator | Priorities, scope, task claims, dependencies, integration | Preserve user authority over direction |
| QA/playtest | Reproduction steps, checks, observations, evidence | Distinguish correctness from human experience |

Allow one person or agent to cover several responsibilities. Give each active task one accountable owner and explicit owned paths. Assign shared interfaces and aggregate files to an integrator. Have other contributors submit change proposals or isolated additions; avoid simultaneous edits to the same scene, registry, manifest, or board row.

## Maintain a durable project board

Follow existing repository conventions. Use [project-board.md](../assets/templates/project-board.md) and [run-handoff.md](../assets/templates/run-handoff.md) when a suitable format is absent. Include at least:

```text
task_id; objective; acceptance_criteria; state; dependencies
owner; run_id; claim_epoch; base_sha; owned_paths
lease_started_utc; lease_expires_utc; last_checkpoint_utc
evidence_paths; implementation_commit; integration_commit
pending_human_evidence; next_action
```

Use stable task IDs and unique run IDs. Record the actual repository and branch with the base SHA. Distinguish implementation complete, technically verified, awaiting human playtest, and accepted. Use an explicit blocked state with a cause and a next action.

Keep run observations append-only in uniquely named records, for example `run-notes/<run_id>/01-start.md` and `02-result.md`. Correct a mistake in a later record. Let the integrator update the board's current summary while preserving the underlying history. Do not create a competing board when one already exists.

## Resolve claims before shared edits

Treat Markdown claims as coordination records, not atomic locks. Two agents can read an unclaimed task simultaneously. Require either an existing atomic claim service or one designated coordinator that serializes claim acceptance. An unacknowledged proposed claim does not authorize overlapping edits.

Re-read the authoritative board and latest run records before accepting work. Confirm owner, epoch, paths, dependencies, and lease. If competing claims exist, have the coordinator select one according to established priority and assign the other contributor independent work. Record the resolution; never let both continue because their local snapshots looked valid.

Without a functioning claim mechanism, perform read-only analysis or work in an explicitly isolated branch/worktree for later review. Do not mutate disputed shared paths. Isolation preserves work but does not itself grant integration authority.

Treat an expired lease as a recovery signal. Inspect newer checkpoints, branches, commits, and any uncommitted work before reassignment. Have the coordinator issue a new claim epoch and record what survives. A returning owner must validate its epoch before writing; stale ownership cannot overwrite a successor's work. Stop shared edits when the lease cannot be renewed or ownership becomes ambiguous.

## Run one bounded scheduled cycle

Treat each invocation as a bounded continuation of the existing project. Follow the authorized schedule and communication channels; this skill does not create automations or independently authorize messages to other people.

1. **Recover context.** Read repository instructions, current branch and status, board, latest handoff, relevant decisions, and recent changes. Preserve unrelated dirty work. Confirm that task descriptions still match the implementation.
2. **Select one outcome.** Choose the highest-priority eligible task or an independent check. State a concrete artifact, acceptance criteria, owned paths, and an effort or time bound. Avoid restarting the project plan every hour.
3. **Obtain ownership.** Resolve the claim using the protocol above. Record the observed base SHA and dependencies. Re-read immediately before the first shared edit.
4. **Make the smallest coherent change.** Stay inside the task and agreed interfaces. Stop expanding when the outcome is achieved. If blocked, preserve findings and choose independent authorized work instead of fabricating completion.
5. **Check the relevant behavior.** Run proportionate technical checks and inspect the playable result when possible. Capture commands, results, build identity, and unresolved risks. Record unavailable human feedback explicitly.
6. **Reconcile and hand off.** Re-read ownership, current repository state, and intervening changes before committing or integrating. Link evidence to the actual delivered revision and record the next action.

If every useful task is claimed or blocked, leave a concise no-change checkpoint. Do not manufacture feature work to fill a scheduled run. Exit at the agreed bound with a resumable state.

## Integrate without losing work

Keep parallel contributors in separate worktrees or branches when tooling permits. Use normal review and integration rules. Stage only owned changes, inspect the diff, and exclude secrets, generated debris, and other contributors' work. Do not use force pushes, destructive resets, or blanket conflict resolutions to make integration appear successful.

On divergence, fetch or inspect the current base, reconcile deliberately, and rerun checks affected by the resolution. Preserve competing work. If a conflict expresses incompatible design decisions, record the alternatives and route the decision to the responsible owner. Proceed with independent tasks while that decision is pending.

Record the commit actually tested. If tests ran before integration, state their base and changes; verify relevant integration behavior afterward. Store the final commit SHA in a subsequent handoff or board update rather than inventing the hash of a commit that does not exist yet.

## Leave a resumable handoff

Record the task and run IDs, ownership epoch, base and delivered SHAs, branch/worktree, changed paths, outcome, checks with evidence, remaining assumptions, and exact next action. Include how to launch the relevant build and reproduce any open issue. Describe uncommitted changes and their locations if work must pause.

Separate pending human evidence from work that can continue. For example: “Attachment response awaits three target-player sessions; save/load verification and habitat readability checks remain independent.” Do not replace missing observation with an AI confidence score.

Release or renew the claim through the established mechanism. Make the next agent able to resume from durable artifacts without relying on this conversation or replaying completed work.
