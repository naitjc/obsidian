---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, synthetic-data, llm-reasoning]
sources: [raw/sources/Liu 等 - 2024 - Best Practices and Lessons Learned on Synthetic Data.pdf]
---

# Liu 等 - 2024 - Best Practices and Lessons Learned on Synthetic Data

## Metadata
- Source file: `raw/sources/Liu 等 - 2024 - Best Practices and Lessons Learned on Synthetic Data.pdf`
- Year: 2024
- Pages: 25
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- cussing its applications, challenges, and future directions.
- Acquiring such datasets can be a significant challenge due to data scarcity
- Synthetic data has emerged as a promising solution to address these challenges (Nikolenko,
- Despite its promise, synthetic data also presents challenges that need to be addressed.

## Method
- The success of AI models relies on the availability of large, diverse, and
- powerful, inclusive, and trustworthy language models.
- heavily relies on the availability of large, diverse, and high-quality datasets for training
- patterns of real-world data, but is created through algorithms (Saxton et al., 2019), genera-

## Data and Evaluation Setup
- high-quality datasets, which can be challenging to obtain due to data
- heavily relies on the availability of large, diverse, and high-quality datasets for training
- Acquiring such datasets can be a significant challenge due to data scarcity
- abundant supply of training and testing data for AI models.

## Results and Claims
- data characteristics can improve model performance and generalization.
- have led to the development of various approaches to improve performance on math-
- found that the format of the augmented answers is crucial to final performance, with an-
- showing better performance than those in vanilla format.

## Limitations and Follow-ups
- cussing its applications, challenges, and future directions.
- Acquiring such datasets can be a significant challenge due to data scarcity
- (Babbar & Scho¨ lkopf, 2019), privacy concerns (Abay et al., 2019), and the sheer cost of data
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, synthetic-data, retrieval, prompting, graph, benchmark, llm-reasoning, multimodal
- Mentioned datasets: MASSIVE, ATIS, TOP
- Mentioned metrics: accuracy, acc, em

## Abstract (Extracted)
> The success of AI models relies on the availability of large, diverse, and high-quality datasets, which can be challenging to obtain due to data scarcity, privacy concerns, and high costs. Synthetic data has emerged as a promising solution by generating artificial data that mimics real-world patterns. This paper provides an overview of synthetic data research, dis- cussing its applications, challenges, and future directions. We present em- pirical evidence from prior art to demonstrate its effectiveness and high- light the importance of ensuring its factuality, fidelity, and unbiasedness. We emphasize the need for responsible use of synthetic data to build more powerful, inclusive, and trustworthy language models.

## Related Concepts
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[nlp-research-collection]]
