---
created: 2026-04-23
updated: 2026-05-05
tags: [paper, deep-ingest-v2, llm-reasoning, few-shot, prompting, retrieval, benchmark, graph]
sources: [raw/sources/Sap 等 - 2020 - Social Bias Frames Reasoning about Social and Power Implications of Language.pdf]
---

# Sap 等 - 2020 - Social Bias Frames Reasoning about Social and Power Implications of Language

## Metadata
- Source file: `raw/sources/Sap 等 - 2020 - Social Bias Frames Reasoning about Social and Power Implications of Language.pdf`
- Year: 2020
- Pages: 14
- Ingest level: deep-ingest-v2 (multi-direction extraction)

## Problem Framing
- the core of the challenge is that it is rarely
- evaluation with 150k structured annotations of Figure 1: Understanding and explaining why an ar-
- My problem with Korean artists: I dont yes no no yes Korean have weird names no
- Most previous approaches to understanding the mographic groups.

## Method
- Reasoning about Social and Power Implications of Language
- conceptual formalism that aims to model the yes
- tions about a thousand demographic groups. quires reasoning about conversational implicatures and
- of-the-art neural models are effective at high-
- (potentially subtle) offensive implications about various demographic groups.

## Data and Evaluation Setup
- evaluation with 150k structured annotations of Figure 1: Understanding and explaining why an ar-
- and failure to do so can result in the deployment of large-scale learning and evaluation with over 150k
- ing English Twitter datasets annotated for toxic
- lect datasets of tweets containing racist or sexist
- Table 3: Statistics of the SBIC dataset. Skews indi-

## Results and Claims
- Hovy, 2016; Founta et al., 2018; Davidson et al., tured text. We find that while state-of-the-art neu-
- Given a post, we establish baseline performance of
- Some models did not predict the positive class for “in-group language,” their performance is denoted by “–”. We
- variable probabilities.9 This can allow variables to rameters on the dev. set, and report performance
- We evaluate performance of our models in the and consider training for e ∈ {1, 2, 5} epochs.

## Limitations and Follow-ups
- types and project social biases onto others. At
- the core of the challenge is that it is rarely
- express social biases and power differentials in
- Verify exact metrics and dataset splits before citing quantitative conclusions.

## Structured Signals
- Detected method keywords: few-shot, prompting, retrieval, llm-reasoning, multimodal, dialogue, sarcasm, role-playing, emotion-recognition, benchmark, graph
- Mentioned datasets: ATIS, TOP, ECHO, Persona
- Mentioned metrics: precision, recall, bleu, rouge

## Benchmark Evidence Lines
- evaluation with 150k structured annotations of Figure 1: Understanding and explaining why an ar-
- Table 1: Examples of inference tuples in SBIC. The types of inferences captured by SOCIAL BIAS FRAMES cover
- and failure to do so can result in the deployment of large-scale learning and evaluation with over 150k
- Hovy, 2016; Founta et al., 2018; Davidson et al., tured text. We find that while state-of-the-art neu-
- groups. ased online content, shown in Table 2, to select
- Table 2: Breakdown of origins of posts in SBIC. Mi-
- ing English Twitter datasets annotated for toxic
- lect datasets of tweets containing racist or sexist

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
