---
created: 2026-05-05
updated: 2026-05-05
tags: [synthesis, stance-detection, sota]
sources: []
---

# Stance Detection SOTA Landscape

## Coverage

- Reviewed stance-tagged source pages: **24**
- Deep-ingested source pages: **24**
- Parsing mode: automatic multi-section extraction with PDF table evidence left for manual verification
- Confidence note: high for direction-level qualitative structure; exact benchmark ranking requires table-level checks in [[stance-detection-metrics-matrix]]

## Method Families

| Method family | Representative sources | Direction-level role |
|---|---|---|
| Synthetic data and augmentation | [[143-zhao-2024-zerostance-leveraging-chatgpt-for-open-domain-stance-detection-via-dataset-generation]], [[026-ding-2024-edda-an-encoder-decoder-data-augmentation-framework-for-zero-shot-stance-detection]] | Expand target/domain coverage when labels are scarce |
| Prompting and explicit reasoning | [[100-taranukhin-2024-stance-reasoner-zero-shot-stance-detection-on-social-media-with-explicit-reasoning]], [[111-weinzierl-harabagiu-2024-tree-of-counterfactual-prompting-for-zero-shot-stance-detection]] | Improve zero-shot interpretability and target-sensitive inference |
| Knowledge and retrieval | [[071-lin-2024-kpatch-knowledge-patch-to-pre-trained-language-model-for-zero-shot-stance-detection-on-social-media]], [[137-zhang-2024-an-llm-enabled-knowledge-elicitation-and-retrieval-framework-for-zero-shot-cross-lingual-stance-iden]] | Add target/domain knowledge missing from surface text |
| Target-aware adaptation | [[035-garg-caragea-2024-stanceformer-target-aware-transformer-for-stance-detection]], [[110-wang-pan-2024-target-adaptive-consistency-enhanced-prompt-tuning-for-multi-domain-stance-detection]] | Reduce target mismatch across domains |
| Bias and target sensitivity | [[075-li-zhang-2024-pro-woman-anti-man-identifying-gender-bias-in-stance-detection]], [[030-dubreuil-2025-are-stereotypes-leading-llms-zero-shot-stance-detection]] | Expose target priors and demographic/stereotype effects |
| Multimodal and structural stance | [[016-barel-2025-acquired-taste-multimodal-stance-detection-with-textual-and-structural-embeddings]], [[142-zhang-2025-t-mad-target-driven-multimodal-alignment-for-stance-detection]] | Handle image-text or structural evidence beyond plain text |
| Verification and reliability | [[141-zhang-2025-mpvstance-mitigating-hallucinations-in-stance-detection-with-multi-perspective-verification]], [[140-zhang-2025-mprf-interpretable-stance-detection-through-multi-path-reasoning-framework]] | Mitigate hallucinated rationales and unreliable LLM stance judgments |

## Resolved Tensions

- **Data generation vs prompting:** generation helps create target coverage; prompting helps at inference time. They solve different parts of zero-shot transfer.
- **Target-aware modeling vs open-domain generality:** target-specific methods can be stronger in controlled benchmarks, while open-domain systems optimize broader coverage and robustness.
- **LLM reasoning vs classifier stability:** reasoning improves explanation and zero-shot flexibility but introduces hallucination risks, motivating verification frameworks.
- **Text-only vs multimodal stance:** text-only benchmarks dominate, but multimodal stance becomes necessary when stance evidence is distributed across text, image, structure, or conversation.

## Remaining Publication-Grade Work

- Verify exact metric values directly from each PDF table before external citation.
- Normalize dataset names and splits across SemEval, VAST, P-Stance, EZ-STANCE, ZeroStance/CHATStance, conversational stance, and multimodal stance settings.
- Avoid a single global SOTA ranking because tasks mix zero-shot, in-domain, cross-lingual, conversational, multimodal, and LLM-prompted evaluation settings.
