---
created: 2026-05-21
updated: 2026-05-21
tags: [paper, deep-ingest-v2, hate-speech, benchmark, explainability]
sources: [raw/sources/2020.coling-main.552.pdf]
---

# Chandra 等 - 2020 - AbuseAnalyzer Abuse Detection Severity and Target Prediction for Gab Posts

## Metadata
- Source file: `raw/sources/2020.coling-main.552.pdf`
- Year: 2020
- Venue: COLING 2020
- Pages: 7
- Ingest level: deep-ingest-v2 (target-relation literature pass)

## Problem Framing
- Most abuse detection work predicts whether a post is abusive, but moderation and harm assessment also need severity and target information.
- The paper frames online abuse as a multi-dimensional prediction problem: presence, severity, and target.
- It is useful for showing that flat detection is structurally incomplete even before relation grounding is introduced.

## Method
- Creates AbuseAnalyzer over Gab posts with labels for abuse presence, abuse severity, and abuse target.
- Uses severity levels inspired by the Anti-Defamation League pyramid of hate.
- Compares traditional feature-based classifiers and neural models across the three tasks.

## Data and Evaluation Setup
- Dataset: 7,601 Gab posts.
- Tasks: abuse presence prediction, abuse target prediction, and abuse severity prediction.
- Target labels distinguish whether abuse is aimed at individuals, groups, or related target categories.

## Results and Claims
- Reports roughly 80 percent accuracy for abuse presence, 82 percent for target prediction, and 65 percent for severity prediction.
- Shows that target and severity prediction are feasible but harder and more fine-grained than binary abuse detection.
- Exact values should be verified in the original paper tables before external citation.

## Limitations and Follow-ups
- Target prediction is still post-level and categorical, not candidate-level relation classification.
- Gab is a high-abuse, domain-specific source, so generalization to ordinary target-present non-hateful content needs external testing.
- Follow-up role: supports the multi-field task framing in [[target-relation-grounding-literature-map]].

## Structured Signals
- Detected method keywords: abuse detection, severity prediction, target prediction, Gab, multi-task analysis
- Mentioned datasets: AbuseAnalyzer, Gab posts
- Mentioned metrics: accuracy for abuse presence, target prediction, severity prediction

## Related Concepts
- [[target-relation-grounding-literature-map]]
- [[hate-speech-datasets-and-benchmarks]]
- [[explainable-hate-speech-detection]]
- [[leakage-resistant-target-relation-modeling]]
- [[hate-speech-source-hub]]
