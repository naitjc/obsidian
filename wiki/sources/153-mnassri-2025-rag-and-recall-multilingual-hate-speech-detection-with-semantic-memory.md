---
created: 2026-05-12
updated: 2026-05-12
tags: [paper, deep-ingest-v2, hate-speech, cross-lingual, retrieval, prompting, benchmark]
sources: [raw/sources/2025.woah-1.20.pdf]
---

# Mnassri 等 - 2025 - RAG and Recall Multilingual Hate Speech Detection with Semantic Memory

## Metadata
- Source file: `raw/sources/2025.woah-1.20.pdf`
- Year: 2025
- Venue: WOAH 2025
- Pages: 9
- Ingest level: deep-ingest-v2 (multi-section extraction)

## Problem Framing
- Targets multilingual hate speech detection under cultural nuance and data scarcity.
- Frames fine-tuned models as brittle outside their training distribution and LLM-only approaches as costly, inefficient, and hallucination-prone.
- Proposes retrieval and semantic memory as a way to provide reusable context without updating model parameters.

## Method
- Introduces HS-RAG, a retrieval-augmented hate speech detection pipeline using multilingual context from the Hate Speech Superset and Wikipedia.
- Introduces HS-MemRAG, which adds a semantic cache before vector database retrieval to reuse responses for similar inputs.
- Uses LLaMA-3-8B as the base LLM, Chroma as the vector store, cosine-similarity retrieval, and prompt-based label mapping to hateful/non-hateful.

## Data and Evaluation Setup
- Languages: English, French, and Arabic.
- Structured source: Hate Speech Superset, downsampled for language balance.
- Unstructured source: Wikipedia snippets retrieved from hate/offensive/cyberbullying/hate-crime keywords in the relevant languages.
- Baselines include zero-shot HS-Base and fine-tuned HS-Base variants, with LoRA/4-bit quantization for efficient fine-tuning.

## Results and Claims
- HS-RAG improves over zero-shot HS-Base, especially in French and Arabic where retrieval can bridge knowledge gaps.
- HS-MemRAG reports the strongest overall F1 in English and improves efficiency by avoiding redundant retrieval.
- The paper also notes a class imbalance issue: one fine-tuned Arabic model can achieve high weighted metrics while failing on the hate class, so class-level metrics matter.

## Limitations and Follow-ups
- Results are based on a limited three-language setting and a single-run evaluation in the reported table.
- Retrieval quality depends on the keyword-built Wikipedia store and multilingual embedding behavior.
- Follow-up use: compare against [[037-ghorbanpour-2025-data-efficient-hate-speech-detection-via-cross-lingual-nearest-neighbor-retrieval-with-limited-label]] and [[157-ghorbanpour-2025-can-prompting-llms-unlock-hate-speech-detection-across-languages]] for multilingual low-resource strategy choices.

## Structured Signals
- Detected method keywords: RAG, semantic cache, multilingual retrieval, LoRA, prompt-based moderation
- Mentioned datasets: Hate Speech Superset, Wikipedia, English/French/Arabic hate speech subsets
- Mentioned metrics: accuracy, precision, recall, weighted F1, class-level confusion

## Related Concepts
- [[hate-speech-generalization-and-transfer]]
- [[retrieval-augmented-generation]]
- [[zero-shot-learning]]
- [[hate-speech-datasets-and-benchmarks]]
- [[hate-speech-research-map]]
