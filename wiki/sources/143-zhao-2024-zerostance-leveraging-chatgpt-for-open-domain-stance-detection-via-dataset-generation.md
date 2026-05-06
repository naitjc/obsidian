---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, target-adaptive, bias]
sources: [raw/sources/Zhao 等 - 2024 - ZeroStance Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation.pdf]
---

# Zhao 等 - 2024 - ZeroStance Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation

## Metadata
- Source file: `raw/sources/Zhao 等 - 2024 - ZeroStance Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation.pdf`
- Year: 2024
- Pages: 16
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- ZeroStance: Leveraging ChatGPT for Open-Domain Stance Detection via
- detect the stance (typically against, favor or
- target stance detection (Augenstein et al., 2016; Xu
- neutral) towards unseen targets has attracted

## Method
- previous studies only focus on targets from a Liang et al., 2021) where models are trained on
- domain), and thus zero-shot models cannot tination target that is unseen during training. How-
- which limits models’ ability to generalize to a wide
- at training a model that is able to generalize
- of interest. Particularly, we propose a novel emerging trend to explore zero-shot stance detec-

## Data and Evaluation Setup
- domain), and thus zero-shot models cannot tination target that is unseen during training. How-
- of interest. Particularly, we propose a novel emerging trend to explore zero-shot stance detec-
- dataset generation method ZeroStance, which tion (Allaway and McKeown, 2020; Liang et al.,
- open-domain dataset CHATStance that covers the stance towards unseen targets at the inference
- dataset after proper data filtering. Extensive

## Results and Claims
- comparing the performance of ZeroStance with pre-
- performance by improving the data diversity 2022). Li et al. (2023b) propose a teacher-student
- of existing datasets. augmented targets to improve the performance of
- annotated datasets. Moreover, the total cost the model performance. A common data augmenta-
- work to improve the model performance. How- 3.1 Problem Formulation

## Limitations and Follow-ups
- To address the limitations of prior works, we
- prediction errors, often due to mislabeling during
- Limitations Emily Allaway and Kathleen McKeown. 2020. Zero-
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, target-adaptive, bias
- Mentioned datasets: SemEval, VAST, P-Stance, COVID-19-Stance, ZeroStance, WT-WT, ARC, Twitter
- Mentioned metrics: f1

## Benchmark Evidence Lines
- domain), and thus zero-shot models cannot tination target that is unseen during training. How-
- of interest. Particularly, we propose a novel emerging trend to explore zero-shot stance detec-
- Our method requires only a task description domains, and thus zero-shot models perform poorly
- the generation by incorporating desired attributes Table 1: An example of CHATStance.
- Table 1 shows a generated sample from our CHAT-
- generalization abilities of zero-shot models. Con-
- detection that greatly improves the zero-shot mented data (Liang et al., 2022a,b; Li and Yuan,
- • Extensive results on six stance datasets show zero-shot models. However, most previous works

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
