---
created: 2026-06-06
updated: 2026-06-06
tags: [paper, deep-ingest-v2, multimodal, llm-reasoning, retrieval, benchmark, prompting]
sources: [raw/sources/2024.acl-long.289.pdf]
---

# Lin 等 - 2024 - PreFLMR Scaling Up Fine-Grained Late-Interaction Multi-modal Retrievers

## Metadata
- Source file: `raw/sources/2024.acl-long.289.pdf`
- Year: 2024
- Venue: ACL 2024 Long Papers
- Pages: 23
- Ingest level: deep-ingest-v2 (abstract, dataset construction, method, experiment setup, results, and conclusion checked from local PDF text)

## Problem Framing
- KB-VQA retrieval requires retrievers that can handle image-to-text, question-to-text, and image-plus-question-to-text retrieval rather than a single narrow task.
- The paper argues that scaling behavior for late-interaction multimodal retrieval had not been systematically studied.
- It positions task diversity, model size, visual/text encoder design, and pre-training data scale as central questions for general-purpose multimodal retrievers.

## Method
- Introduces M2KR, a multi-task multi-modal knowledge retrieval benchmark suite built from nine vision-language datasets.
- Builds PreFLMR, a pre-trained version of FLMR, using large-scale vision-language pre-training and task-specific fine-tuning.
- Keeps the fine-grained late-interaction retrieval mechanism while scaling the retriever through more diverse tasks, larger encoders, and more pre-training data.
- Uses instructions/prompts associated with component tasks to support a unified retrieval format.

## Data and Evaluation Setup
- M2KR covers image-to-text, question-to-text, and image-and-question-to-text retrieval tasks.
- Includes KB-VQA-oriented datasets such as OKVQA, Infoseek, and E-VQA, plus other vision-language retrieval sources.
- Evaluates with recall-style retrieval metrics, including Recall@K or pseudo-recall where gold target documents are unavailable.
- Compares PreFLMR against FLMR and other retrieval baselines before and after task-specific fine-tuning.

## Results and Claims
- Reports consistent retrieval gains across the M2KR tasks from multi-task pre-training and task-specific fine-tuning.
- Claims PreFLMR sets strong or state-of-the-art retrieval results across a range of KB-VQA and multimodal retrieval benchmarks.
- Presents scaling observations for vision/text encoder choices, training data size, and task diversity.
- Exact numerical improvements should be checked against original tables before publication-grade citation.

## Limitations and Follow-ups
- M2KR repurposes existing datasets, so benchmark coverage reflects available annotations and conversion choices.
- Pseudo-recall remains necessary for tasks without gold evidence-document labels.
- Local relevance: provides the scaled retriever context for [[188-lin-2023-fine-grained-late-interaction-multi-modal-retrieval-for-retrieval-augmented-visual-question-answering]] and the retrieval side of [[191-chen-2026-berag-bayesian-ensemble-retrieval-augmented-generation-for-knowledge-based-visual-question-answering]].

## Related Concepts
- [[multimodal-learning-source-hub]]
- [[llm-reasoning-source-hub]]
- [[retrieval-augmented-generation]]
- [[multimodal-learning]]
