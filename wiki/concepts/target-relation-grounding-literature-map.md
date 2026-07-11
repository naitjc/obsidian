---
created: 2026-05-21
updated: 2026-07-11
tags: [concept, hate-speech, target-relation, explainability]
sources:
  - raw/sources/1804.04257v1.pdf
  - raw/sources/N19-1144.pdf
  - raw/sources/W19-3504.pdf
  - raw/sources/2020.coling-main.552.pdf
  - raw/sources/2022.naacl-main.433.pdf
  - raw/sources/2023.acl-short.66.pdf
  - raw/sources/S18-2018.pdf
  - raw/sources/2021.acl-long.277.pdf
  - raw/sources/2601.09342v2.pdf
  - raw/sources/3774904.3792159.pdf
---

# Target-Relation Grounding Literature Map

This page routes papers that are useful for arguing that hate and offensive language detection should move from flat text classification toward target-conditioned relation grounding.

## Core Structural Claim

The useful gap is not simply missing target labels. The gap is that many systems know the post label, sometimes know a target category, and sometimes know a toxic span, but do not explicitly bind a harmful expression to the candidate target it acts upon.

## Evidence Clusters

### Target Is Structurally Central

- [[164-elsherief-2018-hate-lingo-a-target-based-linguistic-analysis-of-hate-speech-in-social-media]] distinguishes directed and generalized hate, showing that target configuration changes hate-speech language.
- [[165-zampieri-2019-predicting-the-type-and-target-of-offensive-posts-in-social-media]] introduces a hierarchical offensive-language setup where target category is part of the task, but remains post-level.
- [[167-chandra-2020-abuseanalyzer-abuse-detection-severity-and-target-prediction-for-gab-posts]] adds abuse presence, severity, and target prediction, supporting the claim that flat detection is structurally incomplete.

### Span and Target Must Be Linked

- [[169-zampieri-2023-target-based-offensive-language-identification]] is the closest anchor: it annotates harmfulness plus token-level targets and offensive argument expressions.
- [[014-bai-2025-state-toxicn-a-benchmark-for-span-level-target-aware-toxicity-extraction-in-chinese-hate-speech-det]] shows the hate-specific version of target-argument directionality in Chinese target-aware toxicity.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] supports candidate target span identification for IHC/SBIC-style implicit hate settings.

### Context Can Change the Relation

- [[168-yu-2022-hate-speech-and-counter-speech-detection-conversational-context-does-matter]] shows that parent context can change human hate, counter-hate, and neutral judgments.
- This supports treating quotation, counterspeech, reply stance, and conversational dependency as modifiers of the target-expression relation.

### Shortcut and Bias Risk

- [[166-davidson-2019-racial-bias-in-hate-speech-and-abusive-language-detection-datasets]] shows that hate and abuse classifiers can over-predict negative labels for African-American English, motivating shortcut-resistant evaluation.
- [[043-hartvigsen-2022-toxigen-a-large-scale-machine-generated-dataset-for-adversarial-and-implicit-hate-speech-detection]] and [[059-kim-2023-conprompt-pre-training-a-language-model-with-machine-generated-data-for-implicit-hate-speech-detect]] remain useful for identity-term and implicit-hate shortcut framing.
- [[192-gajewska-2026-improving-implicit-hate-speech-detection-via-a-community-driven-multi-agent-framework]] adds a community-context route for reducing under-detection of implicitly hateful content against marginalised groups, but its broad demographic agents are not a replacement for explicit candidate-target relation labels.

### Agentic Verifiers Need Structured Anchors

- [[193-sun-2026-rethinking-implicit-hate-speech-detection-focusing-on-latent-hate-components-via-dual-process-argumentation]] is the closest new anchor for a ReAct-style verifier. It does not simply ask multiple agents to debate the whole post; it first mines Latent Hate Components, filters noisy candidates, and then performs component-wise pro/con deliberation.
- The local transfer is to replace free-form chain-of-thought with auditable intermediate fields: `candidate_target`, `evidence_span`, `relation_state`, and `context_modifier`.
- The paper's false-positive and false-negative framing matches the local need to separate target-mentioned benign rows from implicit hateful rows rather than optimizing only aggregate classification.

### Partial Relation Supervision Is a Method Analogy

- [[170-ning-2018-exploiting-partially-annotated-data-for-temporal-relation-extraction]] shows that partially annotated relation edges can help only under constraints rather than naive negative interpretation.
- [[173-xie-2021-revisiting-the-negative-data-of-distantly-supervised-relation-extraction]] treats missing knowledge-base relations as positive-unlabeled structure rather than reliable negatives.
- These papers motivate the supervision boundary for candidate-target relations; they do not provide direct hate-speech accuracy evidence. See [[missing-annotation-completion-and-utility-literature-map]] for the broader completion protocol.

## Relation to Current Project

- [[p0-target-grounding-reading-synthesis-2026-06-01]] records the P0 follow-up alignment: candidate spans, target-identity diagnostics, structured evidence evaluation, optional pragmatic traces, and modular definition frames should be connected but evaluated separately.
- [[leakage-resistant-target-relation-modeling]] is the current thesis page: use uniform candidate construction, relation labels, and target-present non-hateful tests rather than feeding row-level targets as features.
- [[hate-speech-intent-slot-refactor-plan]] provides the structured task framing: mentions, harmful relation or intent, target links, evidence spans, context modifiers, and derived verdict.
- [[candidate-target-relation-grounding-experiment-plan-2026-05-18]] moves this literature map into a concrete experiment design, but the literature-level claim should stay focused on the missing relation unit.
- [[llm-guided-hate-factor-structure-induction-2026-06-30]] binds observable communicative motives to extracted targets through `motive_target_assignments`, separates expression style, and keeps final labels outside the factor path. Only repeated audited pool gaps—not mapper, binding, missing-context, or label errors—can propose a later pool change.

## Boundary

These papers do not by themselves prove that a new relation-grounding method will outperform flat classifiers. They justify the task-structure critique: target categories, offensive spans, context, and bias audits each expose part of the same problem, but none alone guarantees that models distinguish attacked targets from merely mentioned targets.
