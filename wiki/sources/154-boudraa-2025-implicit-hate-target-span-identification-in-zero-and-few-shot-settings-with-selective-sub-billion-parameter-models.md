---
created: 2026-05-12
updated: 2026-05-12
tags: [paper, deep-ingest-v2, hate-speech, implicit, benchmark, zero-shot, few-shot, prompting, explainability]
sources: [raw/sources/2025.woah-1.21.pdf]
---

# Boudraa 等 - 2025 - Implicit Hate Target Span Identification in Zero- and Few-Shot Settings with Selective Sub-Billion Parameter Models

## Metadata
- Source file: `raw/sources/2025.woah-1.21.pdf`
- Year: 2025
- Venue: WOAH 2025
- Pages: 13
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Targets implicit hate where harmful meaning is localized in group references, charged phrases, or euphemistic constructions rather than explicit slurs.
- Argues that sentence-level hate classification is too coarse for moderation, auditing, and intervention because it cannot identify the linguistic anchor of the hateful implication.
- Frames implicit target span identification as a BIO tagging task that supports interpretability and fine-grained supervision.

## Method
- Benchmarks masked language models and sub-billion-parameter autoregressive/instruction-tuned models for implicit target span identification.
- Compares zero-shot, few-shot, fully supervised, and LoRA-adapted settings.
- Uses GPT-generated span labels where human span annotations are unavailable, then evaluates token-level BIO outputs.
- Uses LDA topic modeling over false negatives to identify systematic failure themes.

## Data and Evaluation Setup
- Main datasets: SBIC and IHC.
- Auxiliary testbed: OffensiveLang.
- Models include RoBERTa-Large, ModernBERT, LLaMA 3.2-1B variants, and SmolLM2 variants.
- Metrics include token-level precision, recall, accuracy, and F1 for span identification.

## Results and Claims
- RoBERTa-Large reports the strongest zero-shot F1 on IHC and SBIC, with ModernBERT-125M close behind despite much smaller size.
- Instruction-tuned variants generally outperform non-instructed variants.
- LoRA-adapted SmolLM2-135M Instruct comes close to full-data fine-tuning in few-shot settings, suggesting practical value for lightweight deployment.
- Error analysis finds recurring confusion between political/advocacy discourse and hate, and persistent failures on veiled socio-cultural hostility.

## Limitations and Follow-ups
- Span annotations partly rely on GPT-generated labels, so downstream claims inherit annotation-quality risk.
- Exact model comparisons should be checked in the paper tables before publication-grade citation.
- High-value follow-up: integrate with [[using-not-toxic-targets-for-hate-speech-detection]] to distinguish benign target mentions from implicit target anchors.

## Structured Signals
- Detected method keywords: implicit target span identification, BIO tagging, sub-billion models, instruction tuning, LoRA, LDA error analysis
- Mentioned datasets: SBIC, IHC, OffensiveLang
- Mentioned metrics: token-level F1, precision, recall, accuracy

## Related Concepts
- [[implicit-hate-speech-detection]]
- [[explainable-hate-speech-detection]]
- [[zero-shot-learning]]
- [[hate-speech-datasets-and-benchmarks]]
- [[hate-speech-research-map]]
