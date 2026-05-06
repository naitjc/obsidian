---
created: 2026-04-23
updated: 2026-04-29
tags: [synthesis, hate-speech, sota]
sources: []
---

# Hate Speech Direction - SOTA Landscape v1

## Coverage
- Reviewed hate-speech source pages: **36**
- Parsing mode: automatic multi-section extraction (`pdfplumber`, up to 14 pages per paper)
- Confidence note: qualitative signals are strong; numeric SOTA margins should be cited only when table-located or manually verified in [[hate-speech-metrics-matrix]].

## Method Family Frequency
| Method family | Papers |
|---|---|
| explainability | 30 |
| multimodal | 29 |
| prompting | 28 |
| cross-lingual | 22 |
| retrieval | 21 |
| contrastive-learning | 18 |
| causal | 13 |
| graph | 5 |
| counterfactual | 4 |

## Dataset Mentions
| Dataset keyword | Papers |
|---|---|
| twitter | 34 |
| gab | 33 |
| reddit | 15 |
| founta | 11 |
| hateful memes | 10 |
| toxigen | 9 |
| stormfront | 7 |
| ethos | 6 |
| latent hatred | 3 |
| toxicn | 1 |

## Emerging Trends
- Generalization is central: many papers target domain/platform/language shift instead of in-domain gains only.
- Multimodal hate (memes/image-text) is a major subtrack with alignment and retrieval-heavy methods.
- Explainability and reasoning-based moderation signals appear increasingly often.
- Causal and counterfactual ideas are used to improve robustness and transferability.

## Closed Direction-Level Gaps
- Dataset aliases are centralized in [[hate-speech-dataset-alias-map]].
- The source hub is grouped into dataset foundations, implicit/text-centric detection, multimodal memes, and generalization/transfer.
- Contradictions are tracked at the scenario level and resolved as setting-dependent rather than absolute conflicts.


## Contradiction Tracker (Working)
- Resolved: Prompting vs fine-tuning depends on data regime and evaluation setup.
- Resolved: Causal transfer gains are promising but split-sensitive.
- Resolved: Synthetic augmentation quality controls outcome.
- **In-context prompting vs fine-tuning for multimodal hate**: evidence mixed across dataset sizes; resolve via standardized split comparison.
- **Cross-platform gains from causal/disentangled learning**: improvements reported, but transfer settings are not uniform.
- **Synthetic data augmentation**: quality and label noise tradeoff appears paper-dependent.

## Remaining Publication-Grade Work
- Table-check every numeric value before citing exact scores externally.
- Preserve setting context: dataset, split, metric, baseline, and model size.


## Final Direction Note
- [[hate-speech-final-synthesis]]
