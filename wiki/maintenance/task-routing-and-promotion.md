---
created: 2026-05-19
updated: 2026-05-19
tags: [maintenance, workflow]
sources: []
---

# Task Routing and Promotion

## Ingest Workflow

1. Read the new source.
2. Create or update the relevant page under `wiki/sources/`.
3. Create or update relevant entity and concept pages.
4. Update the relevant direction source hub, map, metrics workspace, or status page if the source changes direction-level knowledge.
5. Update [[index]].
6. Append `log.md`.

## Query Workflow

1. Check [[index]] for relevant pages.
2. Read the relevant direction map, source hub, synthesis, and evidence-bearing source pages.
3. Synthesize the answer with citations and confidence boundaries.
4. If the answer has durable research value, file it using [[query-answer-template]] or the nearest existing wiki page.
5. Update [[index]] and append `log.md` when a durable page is created or materially changed.

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
