---
created: 2026-05-17
updated: 2026-05-17
tags: [paper, deep-ingest-v2, information-extraction, graph, benchmark, cross-lingual]
sources: [raw/sources/2020.acl-main.713.pdf]
---

# Lin 等 - 2020 - A Joint Neural Model for Information Extraction with Global Features

## Metadata
- Source file: `raw/sources/2020.acl-main.713.pdf`
- Year: 2020
- Venue: ACL 2020
- Pages: 11
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Most neural information extraction systems use local classifiers for individual entities, relations, triggers, and event arguments.
- Local predictions can violate global consistency, such as assigning implausible duplicated event roles.
- The paper reframes sentence-level information extraction as searching for a globally optimal graph of knowledge elements.

## Method
- Introduces OneIE, an end-to-end joint neural IE framework.
- Pipeline: contextual sentence encoding, entity/trigger node identification, local scoring of node and pairwise link labels, then beam decoding for the best information graph.
- Adds learned global feature templates over cross-subtask and cross-instance interactions, including event schemas and entity-relation-event consistency.
- Does not rely on language-specific features, enabling multilingual adaptation.

## Data and Evaluation Setup
- English ACE2005 variants: ACE05-R, ACE05-E, and ACE05-E+.
- Additional ERE-EN benchmark from DEFT ERE corpora.
- Cross-lingual/multilingual evaluations include ACE05-CN and ERE-ES.
- Metrics are F-scores for entity, relation, trigger, argument, and event extraction subtasks.

## Results and Claims
- Reports that global features improve over a local-classifier baseline and achieve strong or state-of-the-art performance on ACE/ERE information extraction subtasks.
- Shows applicability to Chinese and Spanish data.
- The durable takeaway for this wiki is methodological: structured prediction with global constraints can reduce locally plausible but globally inconsistent extractions.
- Exact F-scores are table-dependent and should be checked in Tables 3-7 before external citation.

## Limitations and Follow-ups
- This is a general IE paper, not a direct hate speech or dialogue source; treat it as a peripheral method node unless a structured extraction task needs global consistency evidence.
- Global feature templates still encode task assumptions, so transfer requires checking whether the target schema has comparable constraints.
- Follow-up: use as background for relation-aware target/span modeling in policy-aware moderation and intent-slot formulations.

## Structured Signals
- Detected method keywords: information extraction, global features, beam decoding, structured prediction, graph decoding
- Mentioned datasets: ACE2005, ACE05-R, ACE05-E, ACE05-E+, ERE-EN, ACE05-CN, ERE-ES
- Mentioned metrics: F-score

## Related Concepts
- [[intent-slot-style-hate-speech-modeling]]
- [[explainable-hate-speech-detection]]
- [[multimodal-learning]]
