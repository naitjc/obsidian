---
created: 2026-04-23
updated: 2026-05-05
tags: [concept, stance-detection, nlp]
sources:
  - raw/sources/Zhao 等 - 2024 - ZeroStance Leveraging ChatGPT for Open-Domain Stance Detection via Dataset Generation.pdf
  - raw/sources/Taranukhin 等 - 2024 - Stance Reasoner Zero-Shot Stance Detection on Social Media with Explicit Reasoning.pdf
  - raw/sources/Wang 等 - 2024 - DEEM Dynamic Experienced Expert Modeling for Stance Detection.pdf
  - raw/sources/Zhang 等 - 2024 - An LLM-Enabled Knowledge Elicitation and Retrieval Framework for Zero-Shot Cross-Lingual Stance Iden.pdf
---

# Stance Detection

Stance detection identifies whether an author is in favor, against, or neutral towards a target (claim, topic, or entity).

## Direction Status

- Current direction hub: [[stance-detection-source-hub]]
- Research map: [[stance-detection-research-map]]
- Final synthesis: [[stance-detection-final-synthesis]]
- Completion report: [[stance-detection-completion-report-2026-05-05]]
- Scope: 24 stance-tagged source pages, all upgraded to `deep-ingest-v2` on 2026-05-05.

## Key Challenges

1. **Zero-shot generalization** - Detecting stances towards unseen targets
2. **Target arguments** - Stance often depends on target-specific arguments (Li & Scarton 2024)
3. **Gender bias** - Models exhibit gender bias in stance detection (Li & Zhang 2024)
4. **Cross-lingual transfer** - Limited labeled data for many languages
5. **Conversational and multimodal context** - Some stance signals appear across dialogue context, images, structure, or social context rather than the target text alone

## Approaches

### Zero-Shot Stance Detection
Using LLMs to generate training data (ZeroStance), explicit reasoning chains (Stance Reasoner).

### Knowledge-Enhanced Methods
DEEM uses experienced expert modeling; Zhang et al. use knowledge elicitation and retrieval.

### Multi-Domain Generalization
K-Patch (Lin et al. 2024) uses knowledge patches for zero-shot transfer across domains.

### Target-Adaptive Methods
Wang & Pan 2024 use consistency-enhanced prompt tuning for multi-domain stance detection.

### Reliability and Verification
Recent work such as MPVStance and MPRF treats stance detection as a reasoning and verification problem, especially when LLMs hallucinate stance rationales or overfit target priors.

### Bias and Target Sensitivity
Gender bias, stereotypes, target absence, and entity-to-entity stance all show that target formulation can change model behavior even when surface text is similar.

## Related Concepts

- [[zero-shot-learning]]
- [[sentiment-analysis]]
- [[synthetic-data-generation]]
- [[llm-reasoning]]
- [[multimodal-learning]]
