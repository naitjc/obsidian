---
created: 2026-04-23
updated: 2026-05-06
tags: [paper, deep-ingest-v2, cross-lingual]
sources: [raw/sources/Wang 等 - 2017 - Neural Machine Translation Advised by Statistical Machine Translation.pdf]
---

# Wang 等 - 2017 - Neural Machine Translation Advised by Statistical Machine Translation

## Metadata
- Source file: `raw/sources/Wang 等 - 2017 - Neural Machine Translation Advised by Statistical Machine Translation.pdf`
- Year: 2017
- Pages: 7
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Imprecise translation problem (Arthur, Neubig, and
- better translations, and in this work we propose to incorpo-
- Experimental results on Chinese-English focus on the above NMT problems, in this work, we try to
- translation show that the proposed approach achieves signifi- address the problems together in a single approach.

## Method
- Neural Machine Translation (NMT) is a new approach to ma-
- ral, therefore, to leverage the advantages of both models for flect the original meaning of the source sentence.
- which are jointly trained within the NMT architecture in an Instead of employing different models which individually
- translation show that the proposed approach achieves signifi- address the problems together in a single approach.

## Data and Evaluation Setup
- Experimental results show that translation quality
- which are jointly trained within the NMT architecture in an Instead of employing different models which individually
- Experimental results on Chinese-English focus on the above NMT problems, in this work, we try to
- Compared with the conven- has been observed at least once in the training data.

## Results and Claims
- that have been translated or need to be translated, resulting
- Experimental results show that translation quality
- Then we employ an auxiliary classifier to score degrades rapidly with the number of UNK words increas-
- Experimental results on Chinese-English focus on the above NMT problems, in this work, we try to

## Limitations and Follow-ups
- However, recent studies show that NMT generally produces
- Background tuned by the minimum error rate training (MERT) algorithm
- ing cost as follows (Koehn, Och, and Marcu 2003):
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: synthetic-data, retrieval, benchmark, llm-reasoning
- Mentioned datasets: ATIS, TOP
- Mentioned metrics: acc, bleu, em

## Abstract (Extracted)
> 1. Coverage problem (Tu et al. 2016b; Cohn et al. 2016): NMT lacks of a mechanism to record the source words Neural Machine Translation (NMT) is a new approach to ma- that have been translated or need to be translated, resulting chine translation that has made great progress in recent years. in either “over-translation” or “under-translation” (Tu et However, recent studies show that NMT generally produces al. 2016b). fluent but inadequate translations (Tu et al. 2016b; 2016a; He et al. 2016; Tu et al. 2017). This is in contrast to con- 2. Imprecise translation problem (Arthur, Neubig, and ventional Statistical Machine Translation (SMT), which usu- Nakamura 2016): NMT is prone to generate words that ally yields adequate but non-fluent translations. It is natu- seem to be natural in the target sentence, but do not re- ral, therefore, to leverage the advantages of both models for flect the

## Related Concepts
- [[zero-shot-learning]]
- [[nlp-research-collection]]
