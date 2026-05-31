---
created: 2026-05-17
updated: 2026-05-17
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, explainability, dialogue]
sources: [raw/sources/2022.tacl-1.82.pdf]
---

# Calabrese、Ross和Lapata - 2022 - Explainable Abuse Detection as Intent Classification and Slot Filling

## Metadata
- Source file: `raw/sources/2022.tacl-1.82.pdf`
- Year: 2022
- Venue: TACL 2022
- Pages: 15
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Standard abuse classifiers learn from labeled examples but are not explicitly given the moderation policy they are supposed to enforce.
- The paper argues that this causes models to conflate correlated cues, such as group identifiers, with actual policy violations.
- Reframes abuse detection as policy-aware classification: given a post and a policy, decide whether the post violates that policy.

## Method
- Decomposes abuse policy rules into intents and slots, borrowing the intent classification and slot filling formulation from spoken language understanding.
- Represents policy violation evidence with slots such as target, protected characteristic, dehumanizing comparison, threat, hate entity, support of hate crimes, and author stance.
- Introduces a sequence-to-sequence model that first generates a meaning sketch, fills slots, and then deterministically infers intent from filled slot combinations.
- Adds an intent-aware loss to improve tree structures that matter for intent classification.

## Data and Evaluation Setup
- Introduces PLEAD, the Policy-aware Explainable Abuse Detection dataset.
- Contains 3,535 English posts annotated with policy-related intent and slot structures.
- Uses train/dev/test splits while preserving intent distribution.
- Evaluates binary classification, fine-grained intent classification, production F1 for tree structures, exact match accuracy, and AAA-style bias/functionality checks.

## Results and Claims
- Shows that RoBERTa-style binary classifiers can achieve high F1 while behaving inconsistently on functionality/bias tests.
- Reports that the proposed structured model outperforms comparison models on production F1 for policy meaning trees.
- Binary classification F1 improves when fine-grained intent confusions are collapsed, indicating that some mistakes are between related hateful policy intents rather than hateful/non-hateful boundaries.
- Exact quantitative values are table-dependent and should be checked in Tables 4-5 before external citation.

## Limitations and Follow-ups
- PLEAD is small relative to broad platform moderation distributions and focuses on English policy examples.
- The formulation depends on careful policy-to-schema design; it should not be treated as automatic universal hate speech ontology induction.
- Follow-up: this is the key source for [[intent-slot-style-hate-speech-modeling]] and should be linked with U-PLEAD/TARGET compositional generalization.

## Structured Signals
- Detected method keywords: policy-aware abuse detection, intent classification, slot filling, meaning sketch, structured prediction, explainability
- Mentioned datasets: PLEAD, HateCheck
- Mentioned metrics: binary F1, intent F1, AAA, production F1, exact match accuracy

## Related Concepts
- [[intent-slot-style-hate-speech-modeling]]
- [[explainable-hate-speech-detection]]
- [[implicit-hate-speech-detection]]
- [[dialogue-systems]]
- [[hate-speech-source-hub]]
