---
created: 2026-04-23
updated: 2026-06-06
tags: [concept, llm-reasoning, evaluation]
sources:
  - raw/sources/2026.findings-eacl.230.pdf
  - raw/sources/关于自然语言理解课题的思考.pdf
  - raw/sources/2508.16406v2.pdf
  - raw/sources/2604.22678v1.pdf
---

# LLM Evaluation

This page routes evaluation work on model judgments, generated explanations, and reliability of automated evaluators.

## Current Additions
- [[176-puppi-vecchi-2026-harm-learning-hate-aware-reward-model-for-evaluating-natural-language-explanations-of-offensive-content]] provides direct evidence that general-purpose reward models may mis-rank context-rich offensive-content explanations, motivating domain-aware explanation evaluation.
- [[177-natural-language-understanding-topic-reflections]] proposes reliable LLM-as-a-judge workflows and agent-oriented customer-service benchmarking as research agenda items; these are proposals requiring subsequent benchmark and reliability validation.
- [[190-yang-2025-retrieval-augmented-defense-adaptive-and-controllable-jailbreak-prevention-for-large-language-models]] adds a safety-utility evaluation pattern based on attack score, false refusal rate, and operating curves.
- [[191-chen-2026-berag-bayesian-ensemble-retrieval-augmented-generation-for-knowledge-based-visual-question-answering]] adds document-posterior attribution and insufficient-grounding deflection as RAG evaluation/control signals.

## Related Concepts
- [[role-playing-agents]]
- [[llm-reasoning]]
- [[dialogue-systems]]
- [[explainable-hate-speech-detection]]
