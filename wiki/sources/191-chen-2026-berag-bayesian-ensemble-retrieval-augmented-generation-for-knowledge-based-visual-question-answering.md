---
created: 2026-06-06
updated: 2026-06-06
tags: [paper, deep-ingest-v2, multimodal, llm-reasoning, retrieval, benchmark]
sources: [raw/sources/2604.22678v1.pdf]
---

# Chen 等 - 2026 - BERAG Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering

## Metadata
- Source file: `raw/sources/2604.22678v1.pdf`
- Year: 2026
- Venue: arXiv v1
- Pages: 14
- Ingest level: deep-ingest-v2 (abstract, method, experiment setup, results, conclusion, and limitations checked from local PDF text)

## Problem Framing
- Standard concatenative RAG can hide individual document contributions, suffer from lost-in-the-middle behavior, and scale poorly when many retrieved documents are concatenated.
- These issues become sharper for KB-VQA and document VQA, where retrieved evidence can include multimodal pages or long lists of candidate documents.
- The paper reopens ensemble-based RAG as an alternative to concatenating all retrieved context into one sequence.

## Method
- Proposes Bayesian Ensemble Retrieval-Augmented Generation (BERAG), where the model conditions on individual retrieved documents and ensembles token probabilities using document posterior weights.
- Introduces Bayesian Ensemble Fine-Tuning (BEFT) for end-to-end training of the ensemble RAG system.
- Updates document posteriors token by token using Bayes' rule during generation.
- Uses posterior distributions for probabilistic reranking, attribution, insufficient-grounding deflection, and pruning low-probability documents during decoding.

## Data and Evaluation Setup
- Evaluates primarily on KB-VQA and document VQA settings: E-VQA, Infoseek, SlideVQA, and multimodal needle-in-a-haystack tasks.
- Uses retrieval recall, VQA metrics, evidence selection / question answering metrics, and lost-in-the-middle diagnostics.
- Compares BERAG/BEFT against standard concatenative RAG, SFT/DPO baselines, and recent KB-VQA systems.

## Results and Claims
- Reports strong gains on E-VQA, Infoseek, SlideVQA, and multimodal needle-in-a-haystack settings.
- Claims BERAG avoids retrieval-list order sensitivity and mitigates lost-in-the-middle degradation.
- Shows document posterior signals can support deflection when retrieved evidence is insufficient and can speed decoding through pruning.
- Exact metric values should remain pending table-level verification before external citation.

## Limitations and Follow-ups
- The framework assumes per-document conditioning is practical for the chosen model and retrieval depth; deployment cost depends on parallel memory and decoding setup.
- Evidence attribution is clearer than in concatenative RAG, but still depends on the retrieved documents containing sufficient grounding.
- Local relevance: central for [[retrieval-augmented-generation]] because it gives an interpretable non-concatenative RAG design linked to multimodal QA.

## Related Concepts
- [[multimodal-learning-source-hub]]
- [[llm-reasoning-source-hub]]
- [[retrieval-augmented-generation]]
- [[llm-evaluation]]
