---
created: 2026-06-06
updated: 2026-06-06
tags: [paper, deep-ingest-v2, multimodal, llm-reasoning, retrieval, benchmark]
sources: [raw/sources/NeurIPS-2023-fine-grained-late-interaction-multi-modal-retrieval-for-retrieval-augmented-visual-question-answering-Paper-Conference.pdf]
---

# Lin 等 - 2023 - Fine-grained Late-interaction Multi-modal Retrieval for Retrieval Augmented Visual Question Answering

## Metadata
- Source file: `raw/sources/NeurIPS-2023-fine-grained-late-interaction-multi-modal-retrieval-for-retrieval-augmented-visual-question-answering-Paper-Conference.pdf`
- Year: 2023
- Venue: NeurIPS 2023
- Pages: 21
- Ingest level: deep-ingest-v2 (abstract, method, experiment setup, results, conclusion, and limitations checked from local PDF text)

## Problem Framing
- Knowledge-based VQA needs external document retrieval because many visual questions require world knowledge beyond image content.
- Earlier RA-VQA pipelines rely heavily on image-to-text transforms and DPR-style single-vector retrieval, which can miss visual details and fine-grained query-document relevance.
- The paper frames retrieval quality, especially pseudo-recall over relevant evidence passages, as a bottleneck for downstream answer generation.

## Method
- Proposes Fine-grained Late-interaction Multi-modal Retrieval (FLMR) for retrieval-augmented visual question answering.
- Encodes question, image-derived text, and aligned visual tokens as multi-dimensional token embeddings.
- Uses late interaction between query and document token embeddings so relevance can be captured at a finer granularity than dense single-vector retrieval.
- Aligns large vision-model outputs with an existing text retriever through a lightweight alignment network, allowing visual representations to complement caption/object-detection text.

## Data and Evaluation Setup
- Focuses on OK-VQA and retrieval-augmented VQA settings with Google Search and Wikipedia corpora.
- Also evaluates transfer-style retrieval on FVQA and Infoseek.
- Uses pseudo-relevance recall / recall-style retrieval metrics and VQA answer scores.
- Compares against RA-VQA retrievers, DPR-style retrieval, and retrieval-augmented generation variants with stronger answer models.

## Results and Claims
- Reports large improvements in OK-VQA knowledge retrieval, including about an 8 point gain in PRRecall@5 over prior RA-VQA retrievers.
- Claims FLMR improves downstream VQA score when paired with strong language or multimodal answer generators.
- Shows that aligned vision features help when they complement image-to-text transforms, while naive region feature addition can add noise.
- Exact table values should remain `pending-manual-verification` before use in external quantitative claims.

## Limitations and Follow-ups
- The paper relies on pseudo-relevance labels for OK-VQA because gold supporting-document annotations are unavailable.
- Benefits depend on retriever/corpus construction and may not transfer unchanged to non-VQA RAG settings.
- Local relevance: FLMR is a direct precursor for [[189-lin-2024-preflmr-scaling-up-fine-grained-late-interaction-multi-modal-retrievers]] and a useful source for multimodal retrieval design in [[retrieval-augmented-generation]].

## Related Concepts
- [[multimodal-learning-source-hub]]
- [[llm-reasoning-source-hub]]
- [[retrieval-augmented-generation]]
- [[multimodal-learning]]
