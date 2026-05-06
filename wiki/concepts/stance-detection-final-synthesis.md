---
created: 2026-05-05
updated: 2026-05-05
tags: [synthesis, stance-detection, final]
sources: []
---

# Stance Detection Final Synthesis

## Scope and Confidence

- Scope: 24 stance detection papers in this wiki direction.
- Confidence: high for qualitative direction structure; medium for method-family comparisons; exact numeric claims require table-level verification.

## Strongest Patterns by Scenario

- **Zero-shot and open-domain stance:** combine target-aware prompting/reasoning with synthetic data or knowledge augmentation. Representative sources include [[143-zhao-2024-zerostance-leveraging-chatgpt-for-open-domain-stance-detection-via-dataset-generation]], [[100-taranukhin-2024-stance-reasoner-zero-shot-stance-detection-on-social-media-with-explicit-reasoning]], and [[137-zhang-2024-an-llm-enabled-knowledge-elicitation-and-retrieval-framework-for-zero-shot-cross-lingual-stance-iden]].
- **Target and domain adaptation:** use target-aware architectures, consistency constraints, and target/domain knowledge. Representative sources include [[035-garg-caragea-2024-stanceformer-target-aware-transformer-for-stance-detection]], [[110-wang-pan-2024-target-adaptive-consistency-enhanced-prompt-tuning-for-multi-domain-stance-detection]], and [[071-lin-2024-kpatch-knowledge-patch-to-pre-trained-language-model-for-zero-shot-stance-detection-on-social-media]].
- **Bias and robustness:** inspect stereotype and gender target effects rather than treating target labels as neutral metadata. Representative sources include [[075-li-zhang-2024-pro-woman-anti-man-identifying-gender-bias-in-stance-detection]] and [[030-dubreuil-2025-are-stereotypes-leading-llms-zero-shot-stance-detection]].
- **Conversational and multimodal stance:** require context beyond a single text span, including dialogue history, visual cues, or structural embeddings. Representative sources include [[085-niu-2024-a-challenge-dataset-and-effective-models-for-conversational-stance-detection]], [[067-liang-2024-multi-modal-stance-detection-new-datasets-and-model]], [[016-barel-2025-acquired-taste-multimodal-stance-detection-with-textual-and-structural-embeddings]], and [[142-zhang-2025-t-mad-target-driven-multimodal-alignment-for-stance-detection]].
- **LLM reliability:** reasoning-based stance systems need verification because plausible rationales can still be wrong. Representative sources include [[141-zhang-2025-mpvstance-mitigating-hallucinations-in-stance-detection-with-multi-perspective-verification]] and [[140-zhang-2025-mprf-interpretable-stance-detection-through-multi-path-reasoning-framework]].

## Direction-Level Conclusion

Stance detection is shifting from closed-set classification toward target-general, data-efficient, and explanation-aware inference. The most important design choice is not just model architecture, but how the system represents the target, obtains target knowledge, and controls hallucinated or biased reasoning.

## Boundary

This direction is complete as an internal LLM wiki artifact: sources, concepts, synthesis, lint, metrics workspace, and completion report are connected. It is not a publication-ready numeric leaderboard until every metric row is manually checked against original result tables.
