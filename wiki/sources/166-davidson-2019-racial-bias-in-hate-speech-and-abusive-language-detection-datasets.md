---
created: 2026-05-21
updated: 2026-05-21
tags: [paper, deep-ingest-v2, hate-speech, bias, benchmark]
sources: [raw/sources/W19-3504.pdf]
---

# Davidson 等 - 2019 - Racial Bias in Hate Speech and Abusive Language Detection Datasets

## Metadata
- Source file: `raw/sources/W19-3504.pdf`
- Year: 2019
- Venue: ALW 2019
- Pages: 11
- Ingest level: deep-ingest-v2 (target-relation literature pass)

## Problem Framing
- Hate and abuse classifiers can reproduce dataset bias, creating false positives against the same populations moderation systems are meant to protect.
- The paper studies racial bias in Twitter hate speech and abusive language datasets by comparing classifier behavior on African-American English and Standard American English.
- This directly motivates separating identity or dialect cues from actual harmful relations.

## Method
- Trains classifiers on multiple existing hate speech and abusive language datasets.
- Uses a Twitter corpus with demographic language information to compare predictions on African-American English and Standard American English.
- Applies bootstrap sampling to estimate prediction disparities.

## Data and Evaluation Setup
- Audits datasets including Waseem and Hovy, Waseem, Davidson et al., Golbeck et al., and Founta et al. style Twitter abuse resources.
- Evaluates whether classifiers assign negative labels disproportionately across dialect-associated tweet subsets.
- Also conditions on potentially abusive keywords to test whether bias persists beyond simple keyword effects.

## Results and Claims
- Finds systematic racial bias across classifiers trained on the audited datasets.
- Classifiers tend to assign negative classes to African-American English tweets at substantially higher rates.
- The paper supports the warning that surface identity, dialect, or group-associated language can become a shortcut for abuse labels.

## Limitations and Follow-ups
- The audit is centered on Twitter and AAE/SAE contrast rather than target-relation annotation.
- It does not propose a structured hate-speech task, but it supplies strong motivation for shortcut-resistant evaluation.
- Follow-up role: supports target-present non-hateful diagnostics in [[leakage-resistant-target-relation-modeling]].

## Structured Signals
- Detected method keywords: racial bias audit, dataset bias, dialect bias, classifier audit, false positive bias
- Mentioned datasets: Waseem and Hovy, Waseem, Davidson, Golbeck, Founta, AAE/SAE Twitter corpus
- Mentioned metrics: prediction rate gaps, bootstrap estimates

## Related Concepts
- [[target-relation-grounding-literature-map]]
- [[leakage-resistant-target-relation-modeling]]
- [[hate-speech-datasets-and-benchmarks]]
- [[hate-speech-generalization-and-transfer]]
- [[hate-speech-source-hub]]
