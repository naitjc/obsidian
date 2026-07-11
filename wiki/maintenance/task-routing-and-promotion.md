---
created: 2026-05-19
updated: 2026-06-17
tags: [maintenance, workflow]
sources: []
---

# Task Routing and Promotion

## Subagent Coordination

Use [[subagent-collaboration-workflow]] when a task needs bounded context gathering, remote run inspection, result diagnosis, wiki/literature deduplication, or cleanup/publish auditing before the main thread acts. The main thread may choose these subagents autonomously; the user does not need to request them explicitly. Subagents should report evidence and risks; the main thread remains responsible for final judgment, edits, experiment launches, commits, pushes, and durable wiki promotion.

## Ingest Workflow

1. Read the new source.
2. Create or update the relevant page under `wiki/sources/`.
3. Create or update relevant entity and concept pages.
4. Update the relevant direction source hub, map, metrics workspace, or status page if the source changes direction-level knowledge.
5. Update the [master index](../index.md).
6. Append `log.md`.

## Query Workflow

1. Check the [master index](../index.md) for relevant pages.
2. Read the relevant direction map, source hub, synthesis, and evidence-bearing source pages.
3. Synthesize the answer with citations and confidence boundaries.
4. If the answer has durable research value, file it using [[query-answer-template]] or the nearest existing wiki page.
5. Update the [master index](../index.md) and append `log.md` when a durable page is created or materially changed.

## Idea-Scouting Workflow

Use this route when the task is to find new research ideas or transferable mechanisms from papers that are not yet part of the wiki.

1. Read [[ai-assisted-research-ideation-workflow]] before screening.
2. Define the local research profile: target task, preferred mechanisms, downweighted paper types, keywords, and scoring dimensions.
3. Use rule-based filtering only to reduce candidate volume; do not equate keyword hits with research value.
4. Rank candidates by inferred core idea, transferable mechanism, local fit, feasibility, evaluation value, and risk.
5. Record useful screening outputs with [[transfer-idea-screening-template]] when the result should be reused.
6. Promote only read and checked papers into `wiki/sources/`; keep unverified LLM rankings as reading queues or planning notes.

## Experiment Workflow

1. Keep run artifacts under `experiments/`.
2. Keep external paper implementations under `baselines/`.
3. Record run-level observations in run folders and cross-run conclusions in `experiments/{dataset}/notes/`.
4. Promote only durable, checked, or cross-run conclusions into `wiki/`.
5. Link promoted experiment findings from the relevant concept, method, or direction page.

## Promotion Rule

Promote a query answer, experiment conclusion, or maintenance decision into `wiki/` when it:

- synthesizes multiple sources, directions, or runs;
- creates a reusable comparison, taxonomy, timeline, decision record, or research hypothesis;
- resolves a tension between pages or records a caveat that should not be rediscovered later;
- changes task routing, schema, lint expectations, or verification boundaries.

Do not promote transient command output, local status updates, git housekeeping, simple yes/no answers, or answers that merely repeat an existing page without adding synthesis.
