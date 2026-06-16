---
created: 2026-04-23
updated: 2026-06-06
tags: [concept, llm-reasoning, retrieval]
sources:
  - raw/sources/NeurIPS-2023-fine-grained-late-interaction-multi-modal-retrieval-for-retrieval-augmented-visual-question-answering-Paper-Conference.pdf
  - raw/sources/2024.acl-long.289.pdf
  - raw/sources/2508.16406v2.pdf
  - raw/sources/2604.22678v1.pdf
---

# Retrieval-Augmented Generation

Retrieval-augmented generation covers systems that retrieve external examples, passages, or documents and use them to condition generation, detection, reranking, or safety decisions.

## Current Source Threads

- [[188-lin-2023-fine-grained-late-interaction-multi-modal-retrieval-for-retrieval-augmented-visual-question-answering]] and [[189-lin-2024-preflmr-scaling-up-fine-grained-late-interaction-multi-modal-retrievers]] show a multimodal retriever path for KB-VQA: move from DPR-style single-vector retrieval to fine-grained late interaction, then scale across M2KR tasks.
- [[191-chen-2026-berag-bayesian-ensemble-retrieval-augmented-generation-for-knowledge-based-visual-question-answering]] gives a non-concatenative RAG path: condition on individual documents and use Bayesian document posteriors for attribution, deflection, and pruning.
- [[190-yang-2025-retrieval-augmented-defense-adaptive-and-controllable-jailbreak-prevention-for-large-language-models]] applies retrieval to jailbreak defense rather than answer generation: retrieve attack examples, infer malicious intent/strategy, and tune the safety-utility threshold.

## Working Distinctions

- Retriever-side improvements: better evidence recall or relevance scoring before generation, as in FLMR and PreFLMR.
- Generator-side aggregation: how retrieved evidence is combined during generation, with BERAG contrasting against concatenative RAG.
- Retrieval as control memory: using retrieved examples to update behavior without retraining, as in RAD's defense database.

## Related Concepts
- [[llm-reasoning]]
- [[llm-evaluation]]
- [[multimodal-learning]]
