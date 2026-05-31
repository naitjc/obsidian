---
created: 2026-04-23
updated: 2026-05-27
tags: [concept, synthetic-data, data-augmentation]
sources:
  - raw/sources/2023.eacl-main.244.pdf
---

# Synthetic Data Generation

Synthetic data generation covers LLM- or model-assisted creation, filtering, augmentation, and evaluation of training or benchmark examples. In this wiki it mainly connects zero-shot stance detection, hate speech augmentation, role-playing agent data, and general data curation surveys.

## Where It Appears

- [[sources-index]] is the canonical paper catalog; use tags such as `prompting`, `counterfactual`, `retrieval`, and `benchmark` to locate related source pages.
- [[hate-speech-source-hub]] includes hate speech papers that use generated examples, counterfactuals, retrieval-assisted adaptation, or prompt-driven reasoning.
- [[zero-shot-learning]] and [[stance-detection]] are adjacent concepts where generated data often substitutes for in-domain labels.
- [[174-casula-tonelli-2023-generation-based-data-augmentation-for-offensive-language-detection-is-it-worth-it]] cautions that generative offensive-language augmentation has setup-dependent utility and can shift lexical bias; generated fields should be tested on untouched data and functional slices.

## Related Concepts
- [[zero-shot-learning]]
- [[llm-reasoning]]
- [[retrieval-augmented-generation]]
- [[stance-detection]]
- [[implicit-hate-speech-detection]]
