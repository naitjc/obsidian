---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, cross-lingual, conversational, target-adaptive, verification]
sources: [raw/sources/Yang 等 - 2024 - Reinforcement Tuning for Detecting Stances and Debunking Rumors Jointly with Large Language Models.pdf]
---

# Yang 等 - 2024 - Reinforcement Tuning for Detecting Stances and Debunking Rumors Jointly with Large Language Models

## Metadata
- Source file: `raw/sources/Yang 等 - 2024 - Reinforcement Tuning for Detecting Stances and Debunking Rumors Jointly with Large Language Models.pdf`
- Year: 2024
- Pages: 17
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- joint stance detection (SD) and rumor verifica- p11: Please be true👏👏👏👏 [Deny]
- racity labels for training stance detection and rumor
- detection task and suffer from poor generalizabil- tuning framework to detect stance and verify
- framework for joint stance detection and rumor

## Method
- Learning multi-task models for jointly detect-
- this issue, we leverage large language models p9: I don’t see an article here. Please post the article otherwise you look to be possibly [Deny]
- duce a novel reinforcement tuning framework and over and get louder every time. Sooner or later it will be a known fact.
- its lack of systematic moderation (Vosoughi et al., for improving rumor detection and verification ef-
- verification models, respectively, which are very

## Data and Evaluation Setup
- • Extensive experiments on multiple benchmark
- (2023) proposed zero-shot prompt learning for ru-
- zero-shot and few-shot prompt engineering. C ′ ∈ C
- We define a rumor dataset as C = { (c i , X i ) } | i C = | 1 , to perform data annotation, selection, and model
- beling, we pre-train the SD LLM with P-stance

## Results and Claims
- tasks, not only outperforming state-of-the-art that the rumor stance helps in understanding the
- PACA (Taori et al., 2023) have shown performance et al., 2017) extracted from claim and related
- the stance y for each post x X un- performance of both tasks.
- t We use micro-averaged, macro-averaged F1 score,
- where R and r are calculated by Equation 4, and how the percentage affects its performance (see

## Limitations and Follow-ups
- ing stance and verifying rumors poses chal- p2: Gossip 🤣 [Deny]
- detection task and suffer from poor generalizabil- tuning framework to detect stance and verify
- corpora for training. To address this limitation,
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, cross-lingual, conversational, target-adaptive, verification
- Mentioned datasets: SemEval, P-Stance, RumourEval, RumorEval, ARC, Twitter, Weibo
- Mentioned metrics: accuracy, f1

## Benchmark Evidence Lines
- tasks, not only outperforming state-of-the-art that the rumor stance helps in understanding the
- (2023) proposed zero-shot prompt learning for ru-
- zero-shot and few-shot prompt engineering. C ′ ∈ C
- beling, we pre-train the SD LLM with P-stance
- 2While we opt to host local, open-sourced LLMs, our 3P-stance is a general stance dataset with 3-category
- S5 (Yang et al., 2022) and SemEval-8 (Derczynski
- Policy Network We employ the widely used of- vided in Table 4 and Table 5 in Appendix B.
- t We use micro-averaged, macro-averaged F1 score,

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
- [[sentiment-analysis]]
