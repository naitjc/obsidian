---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, zero-shot, few-shot, prompting, synthetic-data, retrieval, target-adaptive, verification]
sources: [raw/sources/Ding 等 - 2024 - EDDA An Encoder-Decoder Data Augmentation Framework for Zero-Shot Stance Detection.pdf]
---

# Ding 等 - 2024 - EDDA An Encoder-Decoder Data Augmentation Framework for Zero-Shot Stance Detection

## Metadata
- Source file: `raw/sources/Ding 等 - 2024 - EDDA An Encoder-Decoder Data Augmentation Framework for Zero-Shot Stance Detection.pdf`
- Year: 2024
- Pages: 11
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Stance detection aims to determine the attitude expressed in text towards a given target. Zero-shot stance detection
- Keywords: zero-shot stance detection, data augmentation, chain-of-thought
- Stance detection aims to automatically determine mentation of the textual content or targets. These
- the attitude (i.e., favor, against, or neutral) ex- data augmentation approaches can be categorized

## Method
- EDDA: An Encoder-Decoder Data Augmentation Framework for
- (ZSSD) has emerged to classify stances towards unseen targets during inference. Recent data augmentation
- techniques for ZSSD increase transferable knowledge between targets through text or target augmentation. However,
- these methods exhibit limitations. Target augmentation lacks logical connections between generated targets and
- source text, while text augmentation relies solely on training data, resulting in insufficient generalization. To address

## Data and Evaluation Setup
- Stance detection aims to determine the attitude expressed in text towards a given target. Zero-shot stance detection
- develop a rationale-enhanced network that fully utilizes the augmented data. Experiments on benchmark datasets
- Keywords: zero-shot stance detection, data augmentation, chain-of-thought
- feasible. Consequently, Zero-shot stance detec- tion methods lack inherent logical and semantic
- accuracy improvements compared to conventional

## Results and Claims
- demonstrate our approach substantially improves over state-of-the-art ZSSD techniques. The proposed EDDA
- accuracy improvements compared to conventional
- model comprehension and performance for ZSSD lates target-invariant and target-specific represen-
- forms current state-of-the-art methods. tation approaches for ZSSD. These methods ef-
- performance on text classification tasks. For stance effectively generates prediction rationales in if-then

## Limitations and Follow-ups
- these methods exhibit limitations. Target augmentation lacks logical connections between generated targets and
- exhaustively enumerating all potential in-target or tion approaches exhibit two key limitations when
- widely used benchmarks to verify the effective- Traditional Text Data Augmentation Zhang et al.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: zero-shot, few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, target-adaptive, verification
- Mentioned datasets: SemEval, VAST, ARC, Twitter
- Mentioned metrics: accuracy, macro f1, f1

## Abstract (Extracted)
> Stance detection aims to determine the attitude expressed in text towards a given target. Zero-shot stance detection (ZSSD) has emerged to classify stances towards unseen targets during inference. Recent data augmentation techniques for ZSSD increase transfera

## Benchmark Evidence Lines
- Stance detection aims to determine the attitude expressed in text towards a given target. Zero-shot stance detection
- demonstrate our approach substantially improves over state-of-the-art ZSSD techniques. The proposed EDDA
- framework increases semantic relevance and syntactic variety in augmented texts while enabling interpretable
- Keywords: zero-shot stance detection, data augmentation, chain-of-thought
- feasible. Consequently, Zero-shot stance detec- tion methods lack inherent logical and semantic
- approach focused on accurately classifying stance source text, which can yield uninterpretable and
- accuracy improvements compared to conventional
- (LLMs) understand and summarize the training scale dataset called VAST for ZSSD encompass-

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
