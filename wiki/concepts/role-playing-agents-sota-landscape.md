---
created: 2026-05-05
updated: 2026-05-05
tags: [synthesis, role-playing, sota]
sources: []
---

# Role-Playing Agents and Persona Modeling SOTA Landscape

## Coverage

- Reviewed source pages: **13**
- Deep-ingested source pages: **13**
- Confidence note: qualitative structure is suitable for internal wiki use; exact benchmark rankings require table-level checks in [[role-playing-agents-metrics-matrix]].

## Method and Topic Families

| Family | Direction-level role |
|---|---|
| role-play and character benchmarks | Core recurring subarea in this direction |
| persona and profile alignment | Core recurring subarea in this direction |
| social interaction and multi-agent gameplay | Core recurring subarea in this direction |
| hallucination and temporal consistency in characters | Core recurring subarea in this direction |

## Representative Sources

[[013-ahn-2024-timechara-evaluating-point-in-time-character-hallucination-of-role-playing-large-language-models|Ahn 等 - 2024 - TimeChara Evaluating Point-in-Time Character Hallucination of Role-Playing Large Language Models]], [[022-chen-2024-socialbench-sociality-evaluation-of-role-playing-conversational-agents|Chen 等 - 2024 - SocialBench Sociality Evaluation of Role-Playing Conversational Agents]], [[045-he-crab-a-novel-configurable-role-playing-llm-with-assessing-benchmark|He 等 - Crab A Novel Configurable Role-Playing LLM with Assessing Benchmark]], [[057-jiang-2025-know-me-respond-to-me-benchmarking-llms-for-dynamic-user-profiling-and-personalized-responses-at-s|Jiang 等 - 2025 - Know Me, Respond to Me Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at S]]

## Resolved Tensions

- Benchmark settings are not directly comparable across datasets, modalities, languages, or prompting regimes.
- LLM-based methods improve flexibility but need reliability checks for hallucination, data leakage, and prompt sensitivity.
- Synthetic or generated data is useful when target-aligned and curated, but noisy generation should not be treated as equivalent to human labels.

## Remaining Publication-Grade Work

- Verify exact metric values directly from PDF tables before external citation.
- Preserve dataset, split, metric, baseline, and model-size context.
