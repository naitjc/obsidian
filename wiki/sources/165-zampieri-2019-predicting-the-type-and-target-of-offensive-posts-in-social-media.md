---
created: 2026-05-21
updated: 2026-05-21
tags: [paper, deep-ingest-v2, hate-speech, benchmark, explainability]
sources: [raw/sources/N19-1144.pdf]
---

# Zampieri 等 - 2019 - Predicting the Type and Target of Offensive Posts in Social Media

## Metadata
- Source file: `raw/sources/N19-1144.pdf`
- Year: 2019
- Venue: NAACL-HLT 2019
- Pages: 6
- Ingest level: deep-ingest-v2 (target-relation literature pass)

## Problem Framing
- Previous work often treated hate speech, cyberbullying, aggression, profanity, and offensive language as separate flat classification tasks.
- The paper proposes a hierarchical view where offensive content is first detected, then classified by type, then classified by target.
- The target layer distinguishes individual, group, and other targets, making group-targeted insults close to ordinary hate-speech definitions.

## Method
- Introduces OLID, the Offensive Language Identification Dataset.
- Uses a three-level annotation scheme: offensive/not offensive, targeted/untargeted, and target category.
- Trains baseline classifiers for each hierarchy level.

## Data and Evaluation Setup
- Uses English Twitter data annotated with the three-layer OLID scheme.
- Level A predicts offensive language detection.
- Level B predicts targeted insult versus untargeted profanity.
- Level C predicts individual, group, or other target for targeted offensive posts.

## Results and Claims
- Establishes OLID as a reusable benchmark for hierarchical offensive language characterization.
- Shows that target information is useful but is represented as a class-level target category rather than a grounded relation between expression and candidate target.
- Exact model scores should be checked in the original result tables before external citation.

## Limitations and Follow-ups
- OLID's target layer is post-level and categorical; it does not annotate the offensive expression span or its explicit target link.
- The task is useful as background for target-aware classification but does not fully solve target-expression grounding.
- Follow-up role: provides a predecessor contrast for [[169-zampieri-2023-target-based-offensive-language-identification]] and [[target-relation-grounding-literature-map]].

## Structured Signals
- Detected method keywords: hierarchical annotation, offensive language detection, target identification, OLID
- Mentioned datasets: OLID
- Mentioned metrics: classification performance by hierarchy level

## Related Concepts
- [[target-relation-grounding-literature-map]]
- [[hate-speech-datasets-and-benchmarks]]
- [[explainable-hate-speech-detection]]
- [[leakage-resistant-target-relation-modeling]]
- [[hate-speech-source-hub]]
