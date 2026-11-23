# Project board

Project brief / current milestone / integrator: <links and owner>
Canonical coordination mechanism: <serialized integrator, atomic claim service, or established project mechanism>

This document records ownership. Editing it is not an atomic lock. Confirm exclusive ownership through the stated mechanism; use nonoverlapping work or an isolated proposal when exclusivity cannot be established.

| Task ID | Player/design outcome | Owner and run ID | Status | Owned paths | Dependencies | Claim epoch and expiry | Base commit | Completion evidence |
|---|---|---|---|---|---|---|---|---|
| <ID> | <outcome> | <owner/run> | <ready/claimed/working/review/blocked/done> | <paths> | <IDs> | <epoch/UTC> | <SHA> | <artifact/test/decision> |

For each accepted claim, keep a linked record with repository/branch, acceptance criteria, lease start and expiry, last checkpoint, implementation/integration commits when available, evidence paths, pending human evidence, and next action. Use actual observed values; a missing timestamp or commit remains unknown.

## Collaboration rules

- Preserve the existing team roles and accepted priorities.
- Accept a claim through the coordination mechanism, then re-read current state before editing.
- Treat expiry as a recovery signal. Check for owner activity and preserve their changes before reassignment.
- Keep each run bounded. Write a unique run note at the established location, such as `runs/<UTC>-<role>-<run-id>.md`.
- Append evidence and decisions through separate files where possible. Have the integrator update shared summaries.
- Reconcile intervening changes before publishing; resolve overlapping design intent explicitly.
- Keep tasks waiting for human evidence separate from work that can proceed.

## Message board entries

Use the project's existing board. When there is no board, prefer unique entries under `messages/` with task ID, author/run, timestamp, question or decision, relevant artifact, and requested owner. Posting here is project collaboration only when already authorized; it does not authorize messages to external people.
