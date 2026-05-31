---
created: 2026-05-17
updated: 2026-05-21
tags: [query-answer, hate-speech, intent-slot, target-aware, structured-prediction]
sources:
  - raw/sources/2022.tacl-1.82.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/2022.naacl-main.433.pdf
  - raw/sources/2023.acl-short.66.pdf
promotion_reason: "Durable method-design answer for refactoring hate speech detection into an intent-slot formulation grounded in PLEAD, target-span, NER-enrichment, and compositional-generalization evidence."
---

# Query Answer: Hate Speech Intent-Slot Refactor Plan

## Question

How should hate speech detection be refactored into an intent-slot style formulation, based on the current wiki evidence?

## Promotion Rationale

This answer has durable value because it turns the earlier target-leakage and intent-slot discussion into a concrete task schema and modeling plan.

## Short Answer

The refactor should not rename hate speech detection as ordinary intent detection. It should redefine the task as structured abuse understanding: detect mentioned entities or groups, identify harmful speech-act intent, link that intent to one or more targets, and preserve evidence spans. The final hate label becomes a derived decision from the frame, not the only supervised target.

A minimal complete formulation is `text -> {mentions, intents, target_links, evidence_spans, verdict}`. This keeps the target from becoming a sample-level shortcut and forces the model to distinguish benign mentions of protected groups from attacks against those groups.

## Evidence

- [[163-calabrese-ross-lapata-2022-explainable-abuse-detection-as-intent-classification-and-slot-filling]] provides the direct PLEAD formulation: policy-aware abuse detection as intent classification plus slot filling.
- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] extends PLEAD-style slots into compositional generalization tests over target-expression and slot-context combinations.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] supports target span identification as a BIO tagging task.
- [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] reports that intent tags are more useful than group tags alone for classifier generalization and human moderation.
- [[intent-slot-style-hate-speech-modeling]] records the earlier framing of target-aware hate detection as structured semantic-frame modeling.
- [[cross-direction-synthesis-2026-05-06]] notes that benchmark definitions and generalization pressure often explain method disagreements across directions.
- [[169-zampieri-2023-target-based-offensive-language-identification]] supports target-expression linking as a concrete offensive-language annotation design.
- [[168-yu-2022-hate-speech-and-counter-speech-detection-conversational-context-does-matter]] supports keeping context modifiers outside the bare target/intent slots.

## Synthesis Notes

- Input: raw text plus optional context. Do not pass a dataset-native `target` label as an ordinary feature during final hate classification unless it is part of a controlled ablation.
- Processing flow: extract candidate group/entity mentions; classify possible harmful intents; link each non-neutral intent to its target; attach supporting spans; derive the binary or multiclass moderation verdict from the structured frame.
- State changes: the annotation unit changes from a single row-level label to a set of relations. A text can contain multiple mentions, multiple intents, and neutral as well as attacked groups.
- Output: both machine-facing fields and human-auditable evidence. A compact schema is `mentions`, `intent`, `target`, `evidence`, `verdict`, and `confidence`.
- Upstream impact: datasets need either span/link annotations or LLM-assisted weak labels with quality checks. Same-target positive and negative examples become essential.
- Downstream impact: evaluation should include frame-level metrics, target-link accuracy, evidence-span F1, and stress tests where the same group appears in benign and hateful contexts.
- Minimal experiment: compare baseline row-label classification against a two-stage pipeline of target span tagging plus intent-target relation classification, then add controlled target-expression swaps from compositional generalization work.

## 2026-05-20 Slot Completion Assessment

The direction of reframing hate speech detection as an intent-slot problem remains sound, but the slot-completion procedure should be treated as candidate-frame construction rather than as simple field filling.

- `target`: keyword matching from toxic targets can be used as a high-precision bootstrap for `not_toxic` rows, but matched targets should become candidate targets with a relation label, not final attacked targets. Rows without a matched or LLM-supported social target should keep `no_relevant_target` instead of being force-filled.
- `hate_class`: mapping IHC-style hate classes into threat versus non-threat is usable only as a coarse intent attribute for attacked rows. For `not_toxic` rows, the cleaner state is `neutral` or `no_hate_intent`, not simply the negation of a toxic class, because "non-threat" can still include derogation, exclusion, dehumanization, or benign mention.
- `statement`: LLM completion should produce an evidence-grounded explanation of why the row is not hateful, such as benign mention, counterspeech, quotation, factual report, unrelated target, or no protected/social target. It should also allow `insufficient_evidence` when the text does not support a confident explanation.
- Quality control: LLM-filled fields need a small manually audited slice and target-presence diagnostics. The main model should be evaluated on target-present `not_toxic` examples, target-shuffle or target-mask tests, and relation-level labels, not only row-level macro-F1.

## Follow-up Questions

- What is the smallest reliable intent ontology for IHC/SBIC-style data: `neutral`, `derogation`, `threat`, `dehumanization`, `exclusion`, `support_harm`, and `other_hate`, or something narrower?
- Should weak span/link labels be generated by LLM prompting, rule-assisted NER, or a hybrid pipeline with manual audit?
- Should the first prototype optimize for interpretability and leakage control, or for benchmark score parity with existing binary classifiers?
