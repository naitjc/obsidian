---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, stance-detection, zero-shot, few-shot, prompting, retrieval, cross-lingual, conversational, target-adaptive, bias]
sources: [raw/sources/Zhang 等 - 2025 - T-MAD Target-driven Multimodal Alignment for Stance Detection.pdf]
---

# Zhang 等 - 2025 - T-MAD Target-driven Multimodal Alignment for Stance Detection

## Metadata
- Source file: `raw/sources/Zhang 等 - 2025 - T-MAD Target-driven Multimodal Alignment for Stance Detection.pdf`
- Year: 2025
- Pages: 16
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- T-MAD: Target-driven Multimodal Alignment for Stance Detection
- Multimodal Stance Detection (MSD) aims to 2022; Wen and Hauptmann, 2023) as social media
- neutral - toward a target by analyzing multi-
- zero-shot settings. Experiments on the MMSD ments (Wang et al., 2024). These limitations reduce

## Method
- T-MAD: Target-driven Multimodal Alignment for Stance Detection
- Abstract 2023; Liang et al., 2024). First, models struggle
- dress these challenges, we propose the Target- gest opposition, while the text expresses support.
- driven Multi-modal Alignment and Dynamic Current approaches like MLLM-SD and TMPT
- utilize large language models and target-specific

## Data and Evaluation Setup
- zero-shot settings. Experiments on the MMSD ments (Wang et al., 2024). These limitations reduce
- and MultiClimate datasets show that T-MAD performance, especially in complex scenarios with
- Despite progress, existing MSD methods face stance detection accuracy in cases of modality
- * Corresponding author. • We conduct extensive experiments on the
- MMSD and MultiClimate datasets, showing MMVax specifically for COVID-19, comprising

## Results and Claims
- ing robust performance in both in-target and inference, limiting flexibility for dynamic adjust-
- and MultiClimate datasets show that T-MAD performance, especially in complex scenarios with
- outperforms state-of-the-art models, with op-
- Despite progress, existing MSD methods face stance detection accuracy in cases of modality
- that T-MAD outperforms state-of-the-art mod- 11,300 instances (Weinzierl and Harabagiu, 2023).

## Limitations and Follow-ups
- dress these challenges, we propose the Target- gest opposition, while the text expresses support.
- prompts but face challenges in fine-grained align-
- zero-shot settings. Experiments on the MMSD ments (Wang et al., 2024). These limitations reduce
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, retrieval, llm-reasoning, multimodal, cross-lingual, conversational, target-adaptive, bias
- Mentioned datasets: WT-WT, ARC, MTS, Twitter
- Mentioned metrics: accuracy, acc, macro f1, f1, f1-score

## Benchmark Evidence Lines
- content often covers unpredictable topics absent
- zero-shot settings. Experiments on the MMSD ments (Wang et al., 2024). These limitations reduce
- outperforms state-of-the-art models, with op-
- Despite progress, existing MSD methods face stance detection accuracy in cases of modality
- that T-MAD outperforms state-of-the-art mod- 11,300 instances (Weinzierl and Harabagiu, 2023).
- els in both in-target and zero-shot settings. Subsequently, Liang et al. expanded existing
- the best accuracy, and a depth of 5 optimally multimodal stance detection datasets, totaling
- balancing accuracy and efficiency. 17,544 annotated instances (Liang et al., 2024).

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
- [[sentiment-analysis]]
