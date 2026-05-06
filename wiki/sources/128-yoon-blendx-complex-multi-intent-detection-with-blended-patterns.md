---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, few-shot, prompting, synthetic-data, retrieval, benchmark, graph]
sources: [raw/sources/Yoon 等 - BlendX Complex Multi-Intent Detection with Blended Patterns.pdf]
---

# Yoon 等 - BlendX Complex Multi-Intent Detection with Blended Patterns

## Metadata
- Source file: `raw/sources/Yoon 等 - BlendX Complex Multi-Intent Detection with Blended Patterns.pdf`
- Year: unknown
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- BlendX: Complex Multi-Intent Detection with Blended Patterns
- Task-oriented dialogue (TOD) systems are commonly designed with the presumption that each utterance represents
- express multiple intents within a single utterance. While there is an emerging interest in multi-intent detection (MID),
- existing in-domain datasets such as MixATIS and MixSNIPS have limitations in their formulation. To address these

## Method
- that state-of-the-art MID models struggle with the challenges posed by the new datasets, highlighting the need to
- datasets—ATIS (Mansour and Haider, 2021) and tection by cutting-edge models.3 Consequently, this
- as well as the framework used to create the datasets.
- ∗Corresponding author. 3For instance, a smart model may exploit the naïve
- to miami … Se b l a e s c e t d 2 ~ o 3 n s c i o m s i i l n a e r u si t m te i r la a r n it c y es Coreferences language model Review expert reviews

## Data and Evaluation Setup
- existing in-domain datasets such as MixATIS and MixSNIPS have limitations in their formulation. To address these
- issues, we present BlendX, a suite of refined datasets featuring more diverse patterns than their predecessors,
- elevating both its complexity and diversity. For dataset construction, we utilize both rule-based heuristics as well as a
- ensure the quality of the proposed datasets, we also introduce three novel metrics that assess the statistical properties
- of an utterance related to word count, conjunction use, and pronoun usage. Extensive experiments on BlendX reveal

## Results and Claims
- that state-of-the-art MID models struggle with the challenges posed by the new datasets, highlighting the need to
- testbed for MID, as shown in Figure 1. Remark- strates that BlendX significantly outperforms its pre-
- in the literature to address the issue. While re- Lastly, we revisit state-of-the-art MID models, i.e.,
- ated datasets. To achieve this, we introduce three
- not be simply achieved through rule-based heuris-

## Limitations and Follow-ups
- existing in-domain datasets such as MixATIS and MixSNIPS have limitations in their formulation. To address these
- that state-of-the-art MID models struggle with the challenges posed by the new datasets, highlighting the need to
- nuanced and comprehensive challenge for TOD which relies on simple concatenations, BlendX
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, synthetic-data, retrieval, llm-reasoning, multimodal, dialogue, role-playing, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, TOP
- Mentioned metrics: accuracy

## Abstract (Extracted)
> Task-oriented dialogue (TOD) systems are commonly designed with the presumption that each utterance represents a single intent. However, this assumption may not accurately reflect real-world situations, where users frequently express multiple intents within a single utterance. Wh

## Benchmark Evidence Lines
- existing in-domain datasets such as MixATIS and MixSNIPS have limitations in their formulation. To address these
- issues, we present BlendX, a suite of refined datasets featuring more diverse patterns than their predecessors,
- elevating both its complexity and diversity. For dataset construction, we utilize both rule-based heuristics as well as a
- ensure the quality of the proposed datasets, we also introduce three novel metrics that assess the statistical properties
- that state-of-the-art MID models struggle with the challenges posed by the new datasets, highlighting the need to
- reexamine the current state of the MID field. The dataset is available at https://github.com/HYU-NLP/BlendX.
- dialogue dataset contain multiple intents, under- faced criticism for the simplicity inherent in their
- surprisingly notable that resources supporting this to merge multiple utterances into a unified expres-

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[role-playing-agents]]
- [[multimodal-learning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
