---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, zero-shot, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S.pdf]
---

# Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S

## Metadata
- Source file: `raw/sources/Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S.pdf`
- Year: 2025
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Modeling for Zero-Shot and Few-Shot Stance Detection
- Stance detection aims to identify the attitude
- detection focus primarily on learning general-
- in stance detection can primarily be divided into

## Method
- Modeling for Zero-Shot and Few-Shot Stance Detection
- novel two-stage framework: First, a data aug- Imp. Target: democracy campaign legal system
- mentation framework named Hierarchical Col- Imp. Stance: Favor Against Against
- ploys Large Language Models (LLMs) to iden- Figure 1: Example from VAST illustrating the omission
- Thought (CoT) prompting and multi-LLM vot- clear textual cues are annotated, whereas implicit but

## Data and Evaluation Setup
- the benchmark dataset demonstrate that our ap-
- dataset annotation guidelines prioritize explicitly- dynamically adjust the relative influence of text and
- of the models and hinders their ability to generalize • Extensive experiments on benchmark datasets
- information in existing dataset. The framework seen targets. Allaway and McKeown (2020) con-
- operates through two collaborative stages: First, structed the VAried Stance Topics (VAST) dataset

## Results and Claims
- ing, significantly enriching training data with semantically important targets are overlooked.
- proach achieves state-of-the-art results, con- (Hasan and Ng, 2014; Mohammad et al., 2016;
- analyzing significant events, such as public policy the field toward more practical direction.
- While these approaches have achieved notable suc- structs a joint semantic representation to captures
- crucial targets (e.g., the target “democracy” in Fig- sensitivity to contextual variation but also improves

## Limitations and Follow-ups
- cess, two fundamental limitations remain. Issue1: holistic text-target relations; (2) The Local module
- variation. This limitation reduces the adaptability
- get augmentation and model design. methods to related challenges to validate their
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, sarcasm, emotion-recognition, benchmark, graph
- Mentioned datasets: SemEval, ATIS, TOP, Facebook
- Mentioned metrics: accuracy, macro f1, f1, f1-score

## Benchmark Evidence Lines
- the benchmark dataset demonstrate that our ap-
- proach achieves state-of-the-art results, con- (Hasan and Ng, 2014; Mohammad et al., 2016;
- While these approaches have achieved notable suc- structs a joint semantic representation to captures
- dataset annotation guidelines prioritize explicitly- dynamically adjust the relative influence of text and
- cial. However, existing state-of-the-art methods
- of the models and hinders their ability to generalize • Extensive experiments on benchmark datasets
- To address the aforementioned issues, we pro- state-of-the-art performance on both ZSSD
- information in existing dataset. The framework seen targets. Allaway and McKeown (2020) con-

## Related Concepts
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
