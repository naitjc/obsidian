---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, cross-lingual, target-adaptive, bias, verification]
sources: [raw/sources/Zhao和Caragea - 2024 - EZ-STANCE A Large Dataset for English Zero-Shot Stance Detection.pdf]
---

# Zhao和Caragea - 2024 - EZ-STANCE A Large Dataset for English Zero-Shot Stance Detection

## Metadata
- Source file: `raw/sources/Zhao和Caragea - 2024 - EZ-STANCE A Large Dataset for English Zero-Shot Stance Detection.pdf`
- Year: 2024
- Pages: 18
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- EZ-STANCE: A Large Dataset for English Zero-Shot Stance Detection
- Zero-shot stance detection (ZSSD) aims to de-
- termine whether the author of a text is in favor,
- against, or neutral toward a target that is un-

## Method
- ing state-of-the-art deep learning models. Fur- still exhibits several limitations. First, the VAST
- in which models are trained and evaluated using VAST generates data for the neutral class by ran-
- Garrido et al., 2020), and cross-target stance detec- class in Table 1). Deep learning models can easily
- tion, where the models are trained on source targets detect these patterns, consequently diminishing the
- models and pre-trained language models; 5) We

## Data and Evaluation Setup
- EZ-STANCE: A Large Dataset for English Zero-Shot Stance Detection
- Zero-shot stance detection (ZSSD) aims to de-
- EZ-STANCE, a large English ZSSD dataset it is unrealistic to incorporate every potential or
- with 47,316 annotated text-target pairs. In con- related target in the training set. As such, zero-shot
- trast to VAST (Allaway and McKeown, 2020), stance detection (ZSSD) has emerged as a promis-

## Results and Claims
- ing state-of-the-art deep learning models. Fur- still exhibits several limitations. First, the VAST
- model on our comprehensive dataset, we achieve pressed in a text towards a target. Usually, the tar-
- comparable or superior performance than training get is an entity / short noun-phrase, e.g., a political
- sider fine-tuning the base version of state-of-the-art targets; 2) the test subset with noun-phrase targets
- Table 7: Subtask A: Comparison of F1 of models on EZ-STANCE. : our approach improves the best ZSSD

## Limitations and Follow-ups
- ing state-of-the-art deep learning models. Fur- still exhibits several limitations. First, the VAST
- attempt to take subjects which challenge themselves? scription and analysis of our dataset; 2) We con-
- seen targets from completely new domains (out-of- 2021). However, the challenge often arises in gath-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, cross-lingual, target-adaptive, bias, verification
- Mentioned datasets: SemEval, VAST, P-Stance, RumourEval, EZ-STANCE, ARC, Twitter, Reddit
- Mentioned metrics: f1

## Benchmark Evidence Lines
- EZ-STANCE: A Large Dataset for English Zero-Shot Stance Detection
- Zero-shot stance detection (ZSSD) aims to de-
- with 47,316 annotated text-target pairs. In con- related target in the training set. As such, zero-shot
- trast to VAST (Allaway and McKeown, 2020), stance detection (ZSSD) has emerged as a promis-
- ing state-of-the-art deep learning models. Fur- still exhibits several limitations. First, the VAST
- hammad et al., 2016b; Küçük and Can, 2020; AL- overlooked. Second, VAST is designed solely to
- of stance detection tasks: in-target stance detection, for the development of zero-shot stance detection,
- in which models are trained and evaluated using VAST generates data for the neutral class by ran-

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
