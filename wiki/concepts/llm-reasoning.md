---
created: 2026-05-05
updated: 2026-07-01
tags: [concept, llm-reasoning]
sources: []
---

# LLM Reasoning and Evaluation

Inference-time reasoning, LLM evaluation, RAG, uncertainty, latent representations, and reasoning-heavy NLP applications.

## Direction Status

- Current direction hub: [[llm-reasoning-source-hub]]
- Research map: [[llm-reasoning-research-map]]
- Final synthesis: [[llm-reasoning-final-synthesis]]
- Completion report: [[llm-reasoning-completion-report-2026-05-05]]
- Scope: 53 source pages, including the completed 2026-05-05 direction set plus later safety, RAG, explanation-evaluation, multimodal-retrieval, hate-moderation reasoning, ReAct tool-use reasoning, and process-supervised agentic RAG additions through 2026-07-01.

## Key Themes
- inference-time computation and reasoning expansion
- chain-of-thought and structured prompting as reusable reasoning scaffolds
- reasoning-action interleaving and bounded tool use
- retrieval and evidence-conditioned generation
- LLM evaluation, uncertainty, and hallucination control
- latent representations and text encoders
- retrieval-augmented defense and controllable safety-utility evaluation

## Recent Additions
- [[190-yang-2025-retrieval-augmented-defense-adaptive-and-controllable-jailbreak-prevention-for-large-language-models]] adds retrieval-augmented jailbreak detection with controllable safety-utility thresholds.
- [[195-yao-2023-react-synergizing-reasoning-and-acting-in-language-models]] adds the canonical ReAct pattern: interleaving thoughts, actions, and observations so LLMs can use external tools while keeping an inspectable reasoning trajectory.
- [[196-zhang-2025-process-vs-outcome-reward-which-is-better-for-agentic-rag-reinforcement-learning]] separates final-answer outcome supervision from process-level credit assignment, using MCTS-derived next-action preferences to train query generation, evidence extraction, and stopping decisions in agentic RAG.
- [[188-lin-2023-fine-grained-late-interaction-multi-modal-retrieval-for-retrieval-augmented-visual-question-answering]], [[189-lin-2024-preflmr-scaling-up-fine-grained-late-interaction-multi-modal-retrievers]], and [[191-chen-2026-berag-bayesian-ensemble-retrieval-augmented-generation-for-knowledge-based-visual-question-answering]] connect LLM reasoning to KB-VQA evidence retrieval and document-level RAG aggregation.
- [[192-gajewska-2026-improving-implicit-hate-speech-detection-via-a-community-driven-multi-agent-framework]], [[193-sun-2026-rethinking-implicit-hate-speech-detection-focusing-on-latent-hate-components-via-dual-process-argumentation]], and [[194-zhang-2024-efficient-toxic-content-detection-by-bootstrapping-and-distilling-large-language-models]] add a moderation-reasoning cluster: gated community consultation, latent-component argumentation, and confidence-gated DToT distillation.

## Related Concepts
- [[chain-of-thought-prompting]]
- [[multimodal-learning]]
- [[synthetic-data-generation]]
- [[zero-shot-learning]]
- [[llm-evaluation]]
- [[dialogue-systems]]
- [[sarcasm-detection]]
