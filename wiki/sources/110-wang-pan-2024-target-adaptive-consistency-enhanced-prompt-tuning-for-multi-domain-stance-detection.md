---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, stance-detection, few-shot, prompting, retrieval, cross-lingual, target-adaptive, bias]
sources: [raw/sources/Wang和Pan - 2024 - Target-Adaptive Consistency Enhanced Prompt-Tuning for Multi-Domain Stance Detection.pdf]
---

# Wang和Pan - 2024 - Target-Adaptive Consistency Enhanced Prompt-Tuning for Multi-Domain Stance Detection

## Metadata
- Source file: `raw/sources/Wang和Pan - 2024 - Target-Adaptive Consistency Enhanced Prompt-Tuning for Multi-Domain Stance Detection.pdf`
- Year: 2024
- Pages: 10
- Ingest level: deep-ingest-v2 (stance direction extraction)

## Problem Framing
- Stance detection is a fundamental task in Natural Language Processing (NLP). It is challenging due to diverse
- facing intricate information in multi-domain stance detection, these methods cannot be adaptive to multi-domain
- for stance detection with multiple domains. TCP incorporates target knowledge and prior knowledge to construct
- ablation studies demonstrate that TCP outperforms the state-of-the-art methods on nine stance detection datasets

## Method
- Target-Adaptive Consistency Enhanced Prompt-Tuning for
- expressions and topics related to the targets from multiple domains. Recently, prompt-tuning has been introduced to
- convert the original task into a cloze-style prediction task, achieving impressive results. Many prompt-tuning-based
- semantics. In this paper, we propose a novel target-adaptive consistency enhanced prompt-tuning method (TCP)
- target-adaptive verbalizers for diverse domains and employs pilot experiments distillation to enhance the consistency

## Data and Evaluation Setup
- target-adaptive verbalizers for diverse domains and employs pilot experiments distillation to enhance the consistency
- on the training process. Target-aware pilot experiments are conducted to enhance the consistency between the
- verbalizer and training by distilling the target-adaptive knowledge into prompt-tuning. Extensive experiments and
- ablation studies demonstrate that TCP outperforms the state-of-the-art methods on nine stance detection datasets
- not stable for the various datasets. The original way

## Results and Claims
- ablation studies demonstrate that TCP outperforms the state-of-the-art methods on nine stance detection datasets
- sistency distillation to ensure adaptive performance
- PLMs achieve impressive results on NLP tasks,
- achieves impressive results on diverse tasks. How-
- prompts and calculating the average performance performance is the average score of all datasets

## Limitations and Follow-ups
- ture the fine-grained domain knowledge. Train- bias terms of i-th sub-dataset in ℓ-th layer with m 1 -
- a self-attention head (m, ℓ) contains query, key to considerable bias error. This is because ev-
- ments on nine multi-domain datasets to verify the Zhiyuan Liu, Jingang Wang, Juanzi Li, Wei
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, retrieval, llm-reasoning, multimodal, cross-lingual, target-adaptive, bias
- Mentioned datasets: SemEval, VAST, P-Stance, IBMCS, ARC, FNC, ArgMin, Twitter
- Mentioned metrics: macro f1, f1, f1-score

## Benchmark Evidence Lines
- ablation studies demonstrate that TCP outperforms the state-of-the-art methods on nine stance detection datasets
- cannot make the model suitable for multi-domain
- not stable for the various datasets. The original way
- more feasible and stable. Hu et al. (2022) proposed
- However, due to the vast amount of information
- The rest of this paper is organized as follows. mapping function verbalizer is unsuitable for the
- targets. Subsequently, we employed an F1-score- y∈Y
- the output of the last layer (the first layer xℓ−1 is W ∈ W is weighted by α, according to the F1-

## Related Concepts
- [[stance-detection]]
- [[stance-detection-research-map]]
- [[zero-shot-learning]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
