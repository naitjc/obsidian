---
created: 2026-05-18
updated: 2026-05-18
tags: [query-answer, hate-speech, llm-augmentation, target-aware, intent-slot]
sources:
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S.pdf
  - raw/sources/Bai 等 - 2025 - STATE ToxiCN A Benchmark for Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Det.pdf
promotion_reason: "Durable method-design answer summarizing which fields related papers add with LLMs or span-level annotation, to guide minimal IHC/SBIC augmentation."
---

# Query Answer: LLM Augmentation Fields in Related Papers

## Question

What information do related papers supplement with LLMs or span-level annotation, and how should this guide a minimal IHC/SBIC augmentation layer?

## Promotion Rationale

This answer has durable value because it compares field-level augmentation choices across related papers and constrains the proposed IHC/SBIC augmentation to avoid over-relabeling.

## Short Answer

Related papers usually do not ask LLMs to rewrite the whole dataset into a complete new ontology. They add task-aligned intermediate fields: intent/group tags, target spans, implicit targets, synthetic slot-balanced posts, or target-argument-hateful-group quadruples. The useful design pattern is to add only the field needed to expose the missing structure, while preserving original labels.

For IHC/SBIC, the conservative choice is to add a unified group/social mention field and optionally a coarse relation state for analysis, rather than generating a full target-intent-evidence frame for every sample.

## Evidence

- [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] uses GPT-4o to generate intent and group tags for training partitions, then trains RoBERTa-large NER models to insert intent/group tags into text.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] uses GPT-generated span-level labels where human target-span annotations are unavailable, converting sentence-level IHC/SBIC data into BIO-style target span supervision.
- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] uses LLMs to translate grammar-generated slot trees into synthetic posts, preserving controlled target-expression-slot combinations rather than relabeling natural examples.
- [[055-ji-2025-llm-driven-implicit-target-augmentation-and-fine-grained-contextual-modeling-for-zero-shot-and-few-s]] uses LLMs to identify annotation-omitted implicit targets and uses multi-LLM voting to assign stance pseudo-labels.
- [[014-bai-2025-state-toxicn-a-benchmark-for-span-level-target-aware-toxicity-extraction-in-chinese-hate-speech-det]] constructs human span-level target-aware annotations as Target-Argument-Hateful-Group quadruples and evaluates LLMs on extracting those fields.

## Synthesis Notes

- Hate Explained supplements semantic tags, not full examples: intent tags and group tags are inserted as enrichment.
- Boudraa et al. supplements missing token-level supervision: target span BIO labels.
- U-PLEAD supplements controlled examples, not natural-example labels: synthetic posts paired with known slot trees.
- HCTA supplements omitted targets in stance data: implicit target candidates plus voted stance pseudo-labels.
- STATE ToxiCN shows a richer endpoint for full span-level annotation, but its quadruple annotation is human-built and heavier than a light IHC/SBIC augmentation.
- For IHC/SBIC, a minimal layer should therefore be closer to Hate Explained and Boudraa than to full STATE ToxiCN: add group/social mention candidates and possibly BIO spans, while keeping original `class`, `hate_class`, `target`, and `statement` unchanged.

## Follow-up Questions

- Should IHC/SBIC augmentation expose only `group_mentions`, or also a binary `mention_in_text` / `target_label_aligned` diagnostic field for toxic examples?
- Should relation labels be reserved for a small audited subset rather than applied to the full train set?
- Can same-pipeline mention extraction across toxic and not-toxic samples avoid the annotation-source leakage caused by mixing gold toxic targets with LLM negative targets?
