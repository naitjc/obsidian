---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, target-adaptive]
sources: [raw/sources/Wen 等 - 2024 - Transitive Consistency Constrained Learning for Entity-to-Entity Stance Detection.pdf]
---

# Wen 等 - 2024 - Transitive Consistency Constrained Learning for Entity-to-Entity Stance Detection

## Metadata
- Source file: `raw/sources/Wen 等 - 2024 - Transitive Consistency Constrained Learning for Entity-to-Entity Stance Detection.pdf`
- Year: 2024
- Pages: 14
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Entity-to-entity stance detection identifies the
- forms entity-to-entity stance detection training
- consistency constrained learning, which first against the “attorney general”, and the “attorney general”
- and adds an additional objective to enforce Pilger” was also likely against the “new policy”.

## Method
- correlated. In this paper, we propose transitive and their consistency. If we know “Richard Pilger” was
- generation-based models and conduct exper- et al., 2021; Zhang et al., 2022), which identifies the
- to-entity stance detection model, while overly effective way without the extraction of complex de-
- language models struggle with predicting link
- 2010), and structured analysis (Kim and Hovy, 2021; Zhang et al., 2022) optimize model train-

## Data and Evaluation Setup
- We conduct our experiments on DSE (Park et al.,
- Table 2: Comparison of DSE and SEESAW datasets.
- As a result, for experiments on DSE, we can nat-
- extending the consistency constrained learning to parison of the two datasets are provided in Table 2.
- Table 3: Results on DSE dataset. The performances of our methods are averaged performance (%) over 5 runs.

## Results and Claims
- We further show that the performance is sensitive
- a performance degradation if we overstrictly en-
- obtain reliable performance on DSE. Our further
- performance on various tasks, especially for tasks words. The output text of a neutral label does not
- and achieves promising performance (Paolini et al., O

## Limitations and Follow-ups
- challenge. One is based on relation classification
- obtain reliable performances for this challenge, and chos, and Kalina Bontcheva. 2016. Stance detection
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, target-adaptive
- Mentioned datasets: SemEval, ARC, Twitter
- Mentioned metrics: macro f1, f1, precision

## Benchmark Evidence Lines
- Table 1: The transitive mapping of a pair of directed stances with a shared entity. “-” denotes no mapping between
- most existing resources only annotate one entity-to- illustrated in Table 1.
- Table 2: Comparison of DSE and SEESAW datasets.
- extending the consistency constrained learning to parison of the two datasets are provided in Table 2.
- Table 3: Results on DSE dataset. The performances of our methods are averaged performance (%) over 5 runs.
- Table 4: Results on SEESAW dataset. Different from
- Table 3 shows the experimental results on the
- Model Table 5: Comparison between vanilla data augmentation

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
