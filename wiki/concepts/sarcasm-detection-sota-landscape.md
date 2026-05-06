---
created: 2026-05-05
updated: 2026-05-05
tags: [synthesis, sarcasm, sota]
sources: []
---

# Sarcasm and Humor Detection SOTA Landscape

## Coverage

- Reviewed source pages: **16**
- Deep-ingested source pages: **16**
- Confidence note: qualitative structure is suitable for internal wiki use; exact benchmark rankings require table-level checks in [[sarcasm-detection-metrics-matrix]].

## Method and Topic Families

| Family | Direction-level role |
|---|---|
| multimodal incongruity detection | Core recurring subarea in this direction |
| commonsense and focused reasoning | Core recurring subarea in this direction |
| counterfactual/rhetorical augmentation | Core recurring subarea in this direction |
| humor explanation and benchmark construction | Core recurring subarea in this direction |

## Representative Sources

[[021-chen-2024-cofipara-a-coarse-to-fine-paradigm-for-multimodal-sarcasm-target-identification-with-large-multimod|Chen 等 - 2024 - CofiPara A Coarse-to-fine Paradigm for Multimodal Sarcasm Target Identification with Large Multimod]], [[040-guo-2025-multi-view-incongruity-learning-for-multimodal-sarcasm-detection|Guo 等 - 2025 - Multi-View Incongruity Learning for Multimodal Sarcasm Detection]], [[044-he-2025-chumor-2-0-towards-better-benchmarking-chinese-humor-understanding-from-ruo-zhi-ba|He 等 - 2025 - Chumor 2.0 Towards Better Benchmarking Chinese Humor Understanding from (Ruo Zhi Ba)]], [[048-hong-2025-rhetorical-device-aware-sarcasm-detection-with-counterfactual-data-augmentation|Hong 等 - 2025 - Rhetorical Device-Aware Sarcasm Detection with Counterfactual Data Augmentation]]

## Resolved Tensions

- Benchmark settings are not directly comparable across datasets, modalities, languages, or prompting regimes.
- LLM-based methods improve flexibility but need reliability checks for hallucination, data leakage, and prompt sensitivity.
- Synthetic or generated data is useful when target-aligned and curated, but noisy generation should not be treated as equivalent to human labels.

## Remaining Publication-Grade Work

- Verify exact metric values directly from PDF tables before external citation.
- Preserve dataset, split, metric, baseline, and model-size context.
