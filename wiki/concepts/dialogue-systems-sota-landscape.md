---
created: 2026-05-05
updated: 2026-05-05
tags: [synthesis, dialogue, sota]
sources: []
---

# Dialogue, Intent, and Slot Filling SOTA Landscape

## Coverage

- Reviewed source pages: **23**
- Deep-ingested source pages: **23**
- Confidence note: qualitative structure is suitable for internal wiki use; exact benchmark rankings require table-level checks in [[dialogue-systems-metrics-matrix]].

## Method and Topic Families

| Family | Direction-level role |
|---|---|
| task-oriented dialogue and dialogue state tracking | Core recurring subarea in this direction |
| intent detection and slot filling | Core recurring subarea in this direction |
| multi-intent and multi-domain spoken language understanding | Core recurring subarea in this direction |
| LLM-based multi-turn dialogue and response generation | Core recurring subarea in this direction |

## Representative Sources

[[004-2025-coling-main-170|2025.coling-main.170]], [[009-2654-rebuttal-2|2654-rebuttal-2]], [[015-balaraman-2021-recent-neural-methods-on-dialogue-state-tracking-for-task-oriented-dialogue-systems-a-survey|Balaraman 等 - 2021 - Recent Neural Methods on Dialogue State Tracking for Task-Oriented Dialogue Systems A Survey]], [[049-hosseini-asl-a-simple-language-model-for-task-oriented-dialogue|Hosseini-Asl 等 - A Simple Language Model for Task-Oriented Dialogue]]

## Resolved Tensions

- Benchmark settings are not directly comparable across datasets, modalities, languages, or prompting regimes.
- LLM-based methods improve flexibility but need reliability checks for hallucination, data leakage, and prompt sensitivity.
- Synthetic or generated data is useful when target-aligned and curated, but noisy generation should not be treated as equivalent to human labels.

## Remaining Publication-Grade Work

- Verify exact metric values directly from PDF tables before external citation.
- Preserve dataset, split, metric, baseline, and model-size context.
