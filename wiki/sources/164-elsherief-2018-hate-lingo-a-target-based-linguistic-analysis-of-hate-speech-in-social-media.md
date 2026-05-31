---
created: 2026-05-21
updated: 2026-05-21
tags: [paper, deep-ingest-v2, hate-speech, benchmark, bias, explainability]
sources: [raw/sources/1804.04257v1.pdf]
---

# ElSherief 等 - 2018 - Hate Lingo A Target-based Linguistic Analysis of Hate Speech in Social Media

## Metadata
- Source file: `raw/sources/1804.04257v1.pdf`
- Year: 2018
- Venue: ICWSM 2018 / arXiv version
- Pages: 10
- Ingest level: deep-ingest-v2 (target-relation literature pass)

## Problem Framing
- Argues that hate speech cannot be understood only as a binary hate/non-hate distinction because target structure changes the meaning and social implications of hate.
- Separates directed hate, aimed at a specific person or entity, from generalized hate, aimed at a protected group or community.
- Positions target type as a linguistic and policy-relevant distinction rather than a secondary metadata field.

## Method
- Builds target-centered directed and generalized hate subsets from social media posts.
- Compares lexical, semantic, and psycholinguistic markers across the two target configurations.
- Uses the target distinction to analyze how hate expression changes when aimed at an individual versus a group.

## Data and Evaluation Setup
- Reports a curated dataset of 28,318 directed hate speech tweets and 331 generalized hate speech tweets.
- Focuses on descriptive linguistic analysis rather than a new neural architecture.
- Uses target category as the main organizing variable for analysis.

## Results and Claims
- Directed hate is described as more personal, informal, angry, and explicitly attack-oriented.
- Generalized hate is described as more group-oriented, with stronger religious, quantity, and lethal-word markers.
- The paper supports the broader claim that target form changes the linguistic realization of hate speech.
- Exact dataset statistics and all quantitative linguistic comparisons should be checked in the original tables before external citation.

## Limitations and Follow-ups
- The directed and generalized subsets are highly imbalanced, especially for generalized hate.
- The paper distinguishes target forms but does not model candidate-target relation states such as attacked versus merely mentioned.
- Useful follow-up role: supports [[target-relation-grounding-literature-map]] as early evidence that target configuration is structurally central.

## Structured Signals
- Detected method keywords: target-based analysis, directed hate, generalized hate, linguistic analysis, psycholinguistic analysis
- Mentioned datasets: Twitter hate speech corpus, directed hate, generalized hate
- Mentioned metrics: descriptive lexical and psycholinguistic comparisons

## Related Concepts
- [[target-relation-grounding-literature-map]]
- [[leakage-resistant-target-relation-modeling]]
- [[hate-speech-datasets-and-benchmarks]]
- [[explainable-hate-speech-detection]]
- [[hate-speech-source-hub]]
