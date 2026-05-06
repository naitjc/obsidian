---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, cross-lingual]
sources: [raw/sources/Wang 等 - 2018 - Incorporating Statistical Machine Translation Word Knowledge Into Neural Machine Translation.pdf]
---

# Wang 等 - 2018 - Incorporating Statistical Machine Translation Word Knowledge Into Neural Machine Translation

## Metadata
- Source file: `raw/sources/Wang 等 - 2018 - Incorporating Statistical Machine Translation Word Knowledge Into Neural Machine Translation.pdf`
- Year: 2018
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- and more attention in recent years, mainly due to its simplicity tasks, e.g., image caption [13], text summarization [14], natural
- and English-to-German translation tasks show that the proposed
- lation process, both of which pose serious challenges for SMT.
- 1) Coverage problem [24]: NMT finishes target sentence

## Method
- Abstract—Neural machine translation (NMT) has gained more architecture, which is widely used in sequence transformation
- architecture consists of two neural networks: a neural network-
- framework for incorporating the SMT word knowledge into NMT
- the conventional SMT models [16]–[21], which exploit elabo-

## Data and Evaluation Setup
- to the SMT word recommendations in both training and testing model, which is essentially a conceptually single large neural
- knowledge from the training corpus with less effort of feature
- we train the SMT model on a parallel data by using the com-
- the corresponding target phrase “high - tech” appears three Experimental results on Chinese-to-English and English-

## Results and Claims
- forward to improve the translation performance by combining the decodes the vector representation to generate a variable-length
- consistently achieve significant improvements over NMT and SMT Lastly, the memory consumption of the NMT model is much
- cently achieved much progress in both academic and industrial
- words are properly tarnslated, resulting in either “over-

## Limitations and Follow-ups
- shown that NMT suffers from several limitations: source coverage
- properties that correspond well to these limitations.
- lation process, both of which pose serious challenges for SMT.
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: synthetic-data, retrieval, graph, benchmark, llm-reasoning, multimodal
- Mentioned datasets: ATIS, TOP
- Mentioned metrics: accuracy, acc, bleu, em

## Abstract (Extracted)
> No reliable abstract block was extracted automatically; use the section bullets as navigation evidence.

## Related Concepts
- [[zero-shot-learning]]
- [[nlp-research-collection]]
