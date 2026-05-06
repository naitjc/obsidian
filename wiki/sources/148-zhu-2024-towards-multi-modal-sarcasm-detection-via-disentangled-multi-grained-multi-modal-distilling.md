---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, multimodal, sarcasm, prompting, retrieval, benchmark, graph, causal]
sources: [raw/sources/Zhu 等 - 2024 - Towards Multi-modal Sarcasm Detection via Disentangled Multi-grained Multi-modal Distilling.pdf]
---

# Zhu 等 - 2024 - Towards Multi-modal Sarcasm Detection via Disentangled Multi-grained Multi-modal Distilling

## Metadata
- Source file: `raw/sources/Zhu 等 - 2024 - Towards Multi-modal Sarcasm Detection via Disentangled Multi-grained Multi-modal Distilling.pdf`
- Year: 2024
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- Towards Multi-modal Sarcasm Detection via Disentangled
- Multi-modal sarcasm detection aims to identify whether a given sample with multi-modal information (i.e., text and
- dubbed DMMD (Disentangled Multi-grained Multi-modal Distilling) for multi-modal sarcasm detection, which conducts
- Keywords: Multi-modal Sarcasm Detection, Disentangled Representation Learning, Multi-modal Knowledge Distilling

## Method
- the heterogeneity and distribution gap between them. To address these issues, we propose a new framework
- Inspired by the successful pre-trained models
- cated modules (e.g., graph neural networks (Liang
- nal object detection model, and there is still infor- encourage distinct subspace representations
- framework termed DMMD (short for Disentangled

## Data and Evaluation Setup
- Extensive experiments demonstrate the effectiveness of our DMMD over state-of-the-art baselines. More
- • Extensive experiments demonstrate the effec-
- diversity for modality-specific representations, we dataset based on X and proposed a hierarchical fu-
- in each subspace to obtain two subspace represen- Table 1: Statistics of the experimental data.
- phete, which can measure the differences between 5.1. Experimental Setup

## Results and Claims
- Extensive experiments demonstrate the effectiveness of our DMMD over state-of-the-art baselines. More
- Despite significant progress existing methods
- achieved, most of them treat the representation of
- spaces, which has achieved success in several
- where homo → hete denotes the knowledge Following Cai et al. (2019), we perform Accuracy,

## Limitations and Follow-ups
- ifies the effectiveness of our proposed approach Future work can further explore interpretable
- 2024a. Halc: Object hallucination reduction via Proc. of CVPR.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: prompting, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph, causal
- Mentioned datasets: ATIS, TOP
- Mentioned metrics: accuracy, macro-f1, f1, precision, recall, f1-score

## Abstract (Extracted)
> Multi-modal sarcasm detection aims to identify whether a given sample with multi-modal information (i.e., text and image) is sarcastic, which has received increasing attention due to the rapid growth of multi-modal posts on social media. Existing mainstream methods (1) process th

## Benchmark Evidence Lines
- Extensive experiments demonstrate the effectiveness of our DMMD over state-of-the-art baselines. More
- diversity for modality-specific representations, we dataset based on X and proposed a hierarchical fu-
- in each subspace to obtain two subspace represen- Table 1: Statistics of the experimental data.
- temperature parameter controlling whether to trans- tion benchmark dataset (Cai et al., 2019). There-
- where homo → hete denotes the knowledge Following Cai et al. (2019), we perform Accuracy,
- transferring from the modality-agnostic to modality- Precision, Recall and F1-score metrics to evaluate
- ton et al. (2015), we sharpen the predicted dis- bution of the dataset is imbalanced, following Pan
- Precision(%) Recall(%) F1-score(%) Precision(%) Recall(%) F1-score(%)

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[sarcasm-detection]]
- [[role-playing-agents]]
- [[emotion-recognition]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
