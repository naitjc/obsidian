---
created: 2026-04-23
updated: 2026-07-11
tags: [concept, hate-speech, research-direction]
sources: []
---

# Hate Speech Research Map

## Scope
This direction covers explicit/implicit hate speech, multilingual and cross-platform settings, and multimodal hateful memes.

## Subareas
- [[implicit-hate-speech-detection]]
- [[multimodal-hate-detection]]
- [[hate-speech-datasets-and-benchmarks]]
- [[hate-speech-generalization-and-transfer]]
- [[explainable-hate-speech-detection]]
- [[target-relation-grounding-literature-map]]

## Key Source Index
- Use [[hate-speech-source-hub]] as the canonical direction-level source index.
- Use [[sources-index]] for the global catalog.

## Synthesis Notes
- A large portion of recent work shifts from pure classification toward generalization, retrieval, causal signals, and explanation.
- Multimodal hate detection increasingly focuses on memes with weak text-only cues and high context dependence.
- The latest pure-text additions emphasize target spans, intent tags, rationale spans, compositional slot generalization, construct definitions, multilingual prompting, and retrieval memory.
- The target-relation line now separates post-level target categories, target-expression span links, context modifiers, and bias/shortcut audits.
- [[174-casula-tonelli-2023-generation-based-data-augmentation-for-offensive-language-detection-is-it-worth-it]] and [[176-puppi-vecchi-2026-harm-learning-hate-aware-reward-model-for-evaluating-natural-language-explanations-of-offensive-content]] add explicit controls for generated-data utility and generated-explanation evaluation.
- The new agentic-reasoning additions suggest a bounded design principle: trigger reasoning or consultation on uncertain examples, and require structured anchors such as community context, latent hate components, or evidence/relation fields rather than unbounded free-form chain-of-thought.
- [[llm-guided-hate-factor-structure-induction-2026-06-30]] now defines the active CADET-seeded M/T/S factor-pool boundary: bind observable motives to targets, keep style separate, hide the final label from Mapper/Auditor, and treat the older CATCH C/T run only as Baseline 0. Pool revision remains a held-out, post-pilot operation.


## Navigation
- [[hate-speech-source-hub]]
- [[hate-speech-sota-landscape]]
- [[hate-speech-lint-report-2026-04-23]]
- [[hate-speech-completion-report-2026-04-29]]

- [[hate-speech-metrics-matrix]]
- [[hate-speech-priority-papers]]

- [[hate-speech-direction-status]]
- [[hate-speech-final-synthesis]]
- [[target-relation-grounding-literature-map]]
- [[llm-guided-hate-factor-structure-induction-2026-06-30]]
