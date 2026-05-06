---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, dialogue, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Yin 等 - 2025 - ECLM Entity Level Language Model for Spoken Language Understanding with Chain of Intent.pdf]
---

# Yin 等 - 2025 - ECLM Entity Level Language Model for Spoken Language Understanding with Chain of Intent

## Metadata
- Source file: `raw/sources/Yin 等 - 2025 - ECLM Entity Level Language Model for Spoken Language Understanding with Chain of Intent.pdf`
- Year: 2025
- Pages: 12
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- generation and general task performance. Slot O O B-WT O O O O B-LOC
- ing—particularly for token-level tasks, where
- level tasks through direct fine-tuning alone. To
- tasks: intent detection, which identifies the user’s

## Method
- ECLM: Entity Level Language Model for Spoken Language
- Large Language Models (LLMs) have demon- Utterance Get the weather and drive to the airport
- address these challenges, we propose the Entity-
- Chain of Intent, to enable step-by-step multi- the-art SLU systems often employ joint models to
- The rapid advancement of large language models

## Data and Evaluation Setup
- intent recognition. Experimental results show effectively capture the correlations between them
- baselines such as Uni-MIS, achieving gains of
- of LLMs, ECLM further achieves improve- Amazon internal dataset showed that 52% of
- ments of 8.5% and 21.2% on these datasets, examples are multi-intent (Gangadharaiah and
- tensive datasets, these models demonstrate excep-

## Results and Claims
- generation and general task performance. Slot O O B-WT O O O O B-LOC
- of LLMs, ECLM further achieves improve- Amazon internal dataset showed that 52% of
- tional performance across a wide range of NLP
- LLMs may generate undesirable outputs that do model, ECLM, outperforms strong baselines on
- ECLM achieves substantial improvements over into the domain of multi-intent SLU. By showing

## Limitations and Follow-ups
- address these challenges, we propose the Entity-
- LLMs for this specific task, several challenges per- task into an entity detection problem, thereby mit-
- as error propagation and misalignment, particularly handle multi-intent recognition in a step-by-step
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, retrieval, llm-reasoning, dialogue, benchmark, graph
- Mentioned datasets: ATIS, SNIPS, TOP
- Mentioned metrics: accuracy, acc, f1

## Benchmark Evidence Lines
- that ECLM significantly outperforms strong
- of LLMs, ECLM further achieves improve- Amazon internal dataset showed that 52% of
- ments of 8.5% and 21.2% on these datasets, examples are multi-intent (Gangadharaiah and
- tensive datasets, these models demonstrate excep-
- LLMs may generate undesirable outputs that do model, ECLM, outperforms strong baselines on
- not align one-to-one with the original tokens from two widely used datasets, MixATIS and MixSNIPS,
- state-of-the-art pre-trained models, such as Uni- an example of the ECLM training process, the key
- MIS. Specifically, ECLM achieves overall accuracy components of the framework are highlighted: the

## Related Concepts
- [[dialogue-systems]]
- [[llm-reasoning]]
- [[llm-evaluation]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
