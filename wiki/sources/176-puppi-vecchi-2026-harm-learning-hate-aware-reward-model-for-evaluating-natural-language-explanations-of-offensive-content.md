---
created: 2026-05-27
updated: 2026-05-27
tags: [paper, deep-ingest-v2, hate-speech, explainability, llm-reasoning, benchmark, synthetic-data]
sources: [raw/sources/2026.findings-eacl.230.pdf]
---

# Puppi Vecchi 等 - 2026 - HARM Learning Hate-Aware Reward Model for Evaluating Natural Language Explanations of Offensive Content

## Metadata
- Source file: `raw/sources/2026.findings-eacl.230.pdf`
- Year: 2026
- Venue: Findings of EACL 2026
- Pages: 39
- Ingest level: deep-ingest-v2 (explanation-evaluation pass; first page visually checked)

## Problem Framing
- Natural-language explanations can make offensive-content moderation more transparent, but evaluation by generic reward models may prefer sanitized explanations over contextually faithful ones.
- Explanations of stereotypes or offensiveness may require sensitive references that generic safety-oriented scoring penalizes.
- The paper asks for evaluation signals aligned with hate-explanation fidelity rather than generic response preferences.

## Method
- Introduces SBIC-Explain, a human-validated resource of 370,788 LLM-generated natural-language explanations grounded in SBIC.
- Organizes generated explanations into three levels of contextual access: text only, classification-aware, and semantics-informed.
- Proposes HARM, a hate-aware reward model that incorporates interpretable signals for pairwise preference over explanations.

## Data and Evaluation Setup
- Primary resource: SBIC-Explain derived from human-annotated SBIC context.
- Evaluates whether reward scores follow the expected directional preference for richer, more faithful explanation context.
- Compares HARM against general-purpose reward model baselines and LLM-as-a-judge evaluations.

## Results and Claims
- Reports that general-purpose reward models systematically assign lower scores to more context-rich, often more offensive, explanations.
- HARM improves natural-language explanation pairwise preference over general-purpose baselines.
- The relevant local use is evaluation of generated `statement` or explanation fields: fluency and generic reward alone do not establish faithful structured supervision.

## Limitations and Follow-ups
- SBIC-Explain uses LLM-generated explanations and a specific offensive-content context; transfer to IHC full-statement outputs must be checked empirically.
- Exact pairwise results and model comparisons require table verification before external citation.
- Follow-up use: evaluation anchor for [[ihc-sbic-target-completion-layer]] and statement-output experiments.

## Structured Signals
- Detected method keywords: hate-aware reward model, natural language explanations, preference evaluation, LLM as a judge, explanation fidelity
- Mentioned datasets: SBIC, SBIC-Explain
- Mentioned metrics: pairwise preference, reward alignment

## Related Concepts
- [[explainable-hate-speech-detection]]
- [[missing-annotation-completion-and-utility-literature-map]]
- [[llm-evaluation]]
- [[hate-speech-source-hub]]
