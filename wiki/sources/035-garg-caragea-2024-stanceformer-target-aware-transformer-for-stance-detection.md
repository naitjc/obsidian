---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, target-adaptive, verification]
sources: [raw/sources/Garg和Caragea - 2024 - Stanceformer Target-Aware Transformer for Stance Detection.pdf]
---

# Garg和Caragea - 2024 - Stanceformer Target-Aware Transformer for Stance Detection

## Metadata
- Source file: `raw/sources/Garg和Caragea - 2024 - Stanceformer Target-Aware Transformer for Stance Detection.pdf`
- Year: 2024
- Pages: 16
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Stanceformer: Target-Aware Transformer for Stance Detection
- The task of Stance Detection involves discern- man ???! what montrosity is this
- cific subject or target. Prior works have relied Stance: Against
- sequently, these models yield similar perfor- Figure 1: Example of Stance Detection task

## Method
- sequently, these models yield similar perfor- Figure 1: Example of Stance Detection task
- former model that incorporates enhanced atten-
- 2021) have identified that the models tend to
- with various BERT-based models, including of a text takes a stance towards a specific target).
- state-of-the-art models and Large Language Therefore, it is crucial to ensure that models are

## Data and Evaluation Setup
- across three stance detection datasets, along-
- side a zero-shot dataset. Our approach Stance-
- only for the square block covering the target dataset that emphasizes the role of target entities in
- Experimental results demonstrate consistent the dataset with samples that have negated (or un-
- baseline models across various models and datasets, labels. Li and Caragea (2021b) proposed an aux-

## Results and Claims
- state-of-the-art models and Large Language Therefore, it is crucial to ensure that models are
- Models (LLMs), and evaluate its performance aware of the targets when making decisions to
- former not only provides superior performance
- 2019; Derczynski et al., 2017), rumor classification as well as two state-of-the-art methods for stance
- subwords (as illustrated in Figure 2). stance detection. They achieved this by augmenting

## Limitations and Follow-ups
- significance. To address this challenge, we task because they define the context and subject
- challenges the definition of the stance detection
- Stanceformer 67.00 71.97 58.46 65.88 There are several limitations to our work. First,
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, target-adaptive, verification
- Mentioned datasets: SemEval, VAST, P-Stance, RumourEval, ZeroStance, ARC, Twitter
- Mentioned metrics: accuracy, macro-f1, f1

## Benchmark Evidence Lines
- state-of-the-art models and Large Language Therefore, it is crucial to ensure that models are
- side a zero-shot dataset. Our approach Stance-
- 2019; Derczynski et al., 2017), rumor classification as well as two state-of-the-art methods for stance
- including both full-dataset and zero-shot dataset iliary sentence-based data augmentation technique
- parameters, in both zero-shot inference and training set by extracting diverse targets (unseen
- finetuned settings. Our approach outperforms both during training) and then predict the stance by
- models utilized in state-of-the-art methods
- full-dataset and zero-shot-dataset settings.

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
