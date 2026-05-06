---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, cross-lingual, conversational, bias, verification]
sources: [raw/sources/Zhao和Caragea - 2025 - Bilingual Zero-Shot Stance Detection.pdf]
---

# Zhao和Caragea - 2025 - Bilingual Zero-Shot Stance Detection

## Metadata
- Source file: `raw/sources/Zhao和Caragea - 2025 - Bilingual Zero-Shot Stance Detection.pdf`
- Year: 2025
- Pages: 20
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Zero-shot stance detection (ZSSD) aims to de-
- termine whether the author of a text is in sup- target stance detection, models are trained with tar-
- port, against, or neutral toward a target that is gets that are closely related but different from test
- Mao, 2019). Zero-shot stance detection (ZSSD),

## Method
- termine whether the author of a text is in sup- target stance detection, models are trained with tar-
- vestigate ZSSD within a bilingual framework energy” for training and data related to “solar en-
- on the other hand, tests models on a large number
- guages, making it essential for models to accurately
- target stance detection focuses on training and test- stance detection models in real-world scenarios,

## Data and Evaluation Setup
- Zero-shot stance detection (ZSSD) aims to de-
- Mao, 2019). Zero-shot stance detection (ZSSD),
- dataset consisting of over 100,000 annotated cross-target approaches, ZSSD has emerged as a
- sourced from existing datasets. Additionally,
- we created an extended dataset that empha- English (Mohammad et al., 2016; Conforti et al.,

## Results and Claims
- tasks using state-of-the-art pre-trained lan-
- the performance differences. For each setting, • We carry out extensive experiments to estab-
- approach achieves a 96% agreement rate, indicat-
- sions in the test set that achieve a cosine similar-
- we employ the macro-averaged F1 score across all

## Limitations and Follow-ups
- To address the above limitations, in this paper,
- the unique challenges posed by bilingual contexts
- dataset to manually annotate for challenging claim
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, cross-lingual, conversational, bias, verification
- Mentioned datasets: SemEval, VAST, P-Stance, EZ-STANCE, ARC, Twitter, Weibo
- Mentioned metrics: f1

## Benchmark Evidence Lines
- Zero-shot stance detection (ZSSD) aims to de-
- Mao, 2019). Zero-shot stance detection (ZSSD),
- tasks using state-of-the-art pre-trained lan-
- tion, and zero-shot stance detection (ZSSD). In- This narrow focus hinders the applicability of
- Table 1: Comparison of our Bi-STANCE dataset with previous multilingual stance detection datasets: VaxxStance (Agerri et al.,
- diverse zero-shot stance predictions toward un- stance detection, and compare it with cross-
- zero-shot stance detection, conducting compre-
- • We investigate the task of bilingual zero-shot targets in the domain of Swiss independence. Other

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
- [[sentiment-analysis]]
