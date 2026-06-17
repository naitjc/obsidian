---
created: 2026-06-17
updated: 2026-06-17
tags: [maintenance, workflow, agents]
sources: []
---

# Subagent Collaboration Workflow

Use this workflow when a task crosses several context layers, such as the research wiki, local experiment notes, remote server runs, previous Codex threads, or project cleanup records. The main Codex thread keeps responsibility for final judgment and edits. Subagents collect bounded evidence and return structured summaries.

The main thread may decide to dispatch these subagents autonomously. The user does not need to request them explicitly. Dispatch is appropriate when it reduces context search, remote-status checking, result diagnosis, deduplication, or cleanup risk without changing the task objective.

Autonomous dispatch remains bounded: subagents should default to read-only inspection, diagnosis, and summary. The main thread must merge their outputs before state-changing actions such as file edits, remote uploads, experiment launches, process stops, staging, commits, pushes, or durable wiki promotion.

## Default Pattern

1. Define the concrete task and the likely workspace boundary.
2. Decide whether subagents are useful; dispatch only the roles needed for the task.
3. Require each subagent to report confirmed facts, assumptions, open risks, and exact file or server paths.
4. Merge subagent outputs in the main thread before making edits, launching runs, or drawing research conclusions.
5. Promote only durable workflow changes, checked experiment conclusions, or reusable research decisions into the vault.

Do not use subagents to broaden the task objective. They should reduce context search, verification, and diagnosis cost while preserving the user's stated goal.

## Subagent Roles

| Role | Use When | Inputs | Required Output |
|---|---|---|---|
| Context router | The task references recent work, "what I am doing", a broad research direction, or an ambiguous project path. | `wiki/index.md`, `EXPERIMENTS.md`, relevant `experiments/*/notes/`, recent thread summaries, and memory notes when relevant. | Current task line, confirmed prior results, likely start files, unresolved assumptions, and recommended next action. |
| Remote experiment monitor | A server run may be active or recently completed on `nlp06`, `xu-l20`, or another remote host. | Run root, expected log path, expected metrics path, server alias, and relevant environment hints. | Process status, current stage, log tail summary, metrics presence, failure signal if any, and exact commands or paths for follow-up. |
| Result diagnostician | Metrics or predictions exist and the question is whether a run is valid, useful, or better than a baseline. | `metrics.json`, prediction files, run config, baseline metric, and any known selection rule. | Primary metric comparison, confusion/error pattern, likely bottleneck, validity judgment, and the smallest next experiment or no-run recommendation. |
| Wiki and literature deduper | The task involves source ingestion, paper scouting, or deciding whether an idea is new to the local corpus. | `wiki/sources/`, `raw/sources/`, `wiki/concepts/`, `experiments/`, `log.md`, and optional browse results. | Duplicate status, nearest existing pages, source-vs-inference boundary, proposed routing updates, and whether source ingestion is justified. |
| Publish and cleanup auditor | The task involves cleanup, staging, committing, publishing, or moving files across local projects. | `git status`, directory inventories, `.gitignore`, project README files, and relevant maintenance rules. | Safe-to-touch list, archive-only list, do-not-touch list, stage/commit boundary, and rollback or restore notes. |

## Dispatch Templates

### Context Router

```text
Act as a context-router subagent. Read only the relevant local routing files, notes, and recent thread summaries. Return:
- current task line
- confirmed prior results
- files or paths the main thread should start from
- assumptions and unverified premises
- one recommended next action
Do not edit files or launch experiments.
```

### Remote Experiment Monitor

```text
Act as a remote-experiment monitor. On the specified server and run root, check process status, log tail, metrics existence, and obvious environment or permission failures. Return exact paths and a short status judgment. Do not modify code or stop processes.
```

### Result Diagnostician

```text
Act as a result-diagnosis subagent. Inspect the provided metrics, predictions, configs, and baseline rule. Decide whether the run is a valid result, a smoke test, or a failed run. Return the primary metric comparison, error pattern, suspected bottleneck, and smallest next step.
```

### Wiki And Literature Deduper

```text
Act as a wiki/literature dedupe subagent. Check the local corpus before recommending external papers or source ingestion. Separate direct source claims from synthesis or inference. Return duplicate status, nearest existing wiki pages, and proposed routing updates.
```

### Publish And Cleanup Auditor

```text
Act as a publish/cleanup auditor. Inventory first, then classify files as safe-to-touch, archive-only, or do-not-touch. Include git staging boundaries and restore notes. Do not delete, move, stage, commit, or push.
```

## Main Thread Merge Rule

The main thread should not simply concatenate subagent outputs. It should check the full path before acting:

- Inputs: which files, server paths, metrics, source pages, or thread summaries were used.
- Processing flow: what each subagent checked and what it intentionally did not check.
- State changes: whether edits, uploads, runs, cleanup, staging, commits, or pushes are about to happen.
- Outputs: what artifact, answer, experiment status, or wiki update the user receives.
- Upstream/downstream impact: which wiki routes, experiment notes, server bundles, baselines, or public repository boundaries are affected.

Any unverified premise must remain marked as an assumption until the main thread checks it directly or the task accepts it as a planning assumption.
