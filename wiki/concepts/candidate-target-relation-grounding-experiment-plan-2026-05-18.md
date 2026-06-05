---
created: 2026-05-18
updated: 2026-06-01
tags: [query-answer, hate-speech, experiment-plan, semantic-grounding, target-relation, synthetic-data, explainability]
sources:
  - raw/sources/2022.tacl-1.82.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/2025.woah-1.45.pdf
promotion_reason: "Durable experiment plan for the definition-controllable candidate-target relation grounding paper direction."
---

# Query Answer: Candidate-Target Relation Grounding Experiment Plan

## Question

The user asked for an experiment plan after converging on a paper direction: definition-controllable candidate-target relation grounding, supported by curated synthetic hard cases and verifiable structured reasoning.

## Promotion Rationale

This answer has durable value because it turns the research framing into an executable experimental sequence with baselines, data construction, metrics, ablations, and accept/reject criteria.

## Short Answer

The minimal experiment should not start by training a larger classifier. It should first establish whether target/context information is currently used as a shortcut, then construct a uniform candidate-target relation task where every row, toxic or non-toxic, receives candidates from the same pipeline. The main model predicts relation states over `(content, candidate_target, definition_frame)` and derives the row-level hate verdict from attacked relations.

The paper-level evidence should come from three linked results: relation grounding improves target-present and definition-shift slices; curated failure-derived hard cases outperform bulk synthetic augmentation; and structured reasoning fields pass evidence/target perturbation tests better than free-form rationales.

## Core Method

The core method is a definition-conditioned candidate-target relation grounding model. It converts each post into candidate-level instances and predicts whether each candidate target is attacked under a given hate-speech definition or policy frame.

Formalized minimally:

`f(content, candidate_target, definition_frame) -> relation_state, evidence, uncertainty`

Then the row-level verdict is derived from the candidate relations:

`verdict = hateful if any candidate has relation_state = attacked under the active definition_frame`

The method has three components:

- Candidate construction: generate candidate targets for every row using the same raw-text pipeline, regardless of whether the original label is toxic or non-toxic.
- Relation grounding: classify each `(content, candidate_target, definition_frame)` tuple into `attacked`, `mentioned_not_attacked`, or `not_a_candidate_target`, with evidence and uncertainty.
- Controlled robustness training/evaluation: use curated failure-derived hard cases and perturbation tests to check whether the model uses evidence and definition semantics rather than target presence or target identity.

The main novelty is the task formulation and protocol, not a complicated architecture. The first implementation can be a standard encoder/LLM classifier with structured output; the contribution comes from conditioning on definitions, grounding candidate-target relations, and proving reduced shortcut dependence.

### Worked Examples

Example 1: explicit attack.

- Content: "Immigrants are parasites and should be kicked out."
- Candidate target: `immigrants`
- Definition frame: group-directed hate including dehumanization and exclusion.
- Output: `relation_state = attacked`; evidence = "parasites" and "kicked out"; uncertainty = low; verdict = hateful.

The important point is that the model does not predict hate only because the word "immigrants" appears. It predicts hate because the candidate target is linked to dehumanizing and exclusionary evidence.

Example 2: target-present but not attacked.

- Content: "Immigrants often face unfair stereotypes online."
- Candidate target: `immigrants`
- Definition frame: group-directed hate including dehumanization and exclusion.
- Output: `relation_state = mentioned_not_attacked`; evidence = "face unfair stereotypes"; uncertainty = low; verdict = not hateful.

A row-level target-input classifier may learn that some targets are highly correlated with hate labels. This relation task forces the model to distinguish attacked targets from benign or protective mentions.

Example 3: same text, different candidate.

- Content: "They say Muslims are dangerous, but that stereotype is harmful."
- Candidate target A: `Muslims`
- Output for A: `relation_state = mentioned_not_attacked`; evidence = "that stereotype is harmful"; flags = `quotation_or_counterspeech`.
- Candidate target B: `people who spread the stereotype`
- Output for B: likely `not_a_candidate_target` or `mentioned_not_attacked`, depending on target policy.
- Verdict: not hateful under a policy that excludes counterspeech.

The method makes quotation and counterspeech explicit instead of treating the target mention as enough evidence for hate.

Example 4: definition-sensitive case.

- Content: "All landlords are greedy and should be banned."
- Candidate target: `landlords`
- Definition frame A: strict protected-class hate.
- Output under A: `mentioned_not_attacked` or `not_a_candidate_target`; verdict = not hateful.
- Definition frame B: broad group-directed abuse.
- Output under B: `attacked`; evidence = "greedy" and "should be banned"; verdict = abusive/hateful under the broader frame.

This is why `definition_frame` is part of the input. The model should not pretend there is one universal hate label when the label depends on the operative definition.

Example 5: evidence deletion test.

- Original content: "Women are too emotional to lead."
- Candidate target: `women`
- Output: `attacked`; evidence = "too emotional to lead"; verdict = hateful.
- Perturbed content: "Women lead many organizations."
- Expected output: `mentioned_not_attacked`; verdict = not hateful.

If the model keeps predicting `attacked` after the evidence is removed, it is relying on target identity rather than evidence.

## Evidence

- [[p0-target-grounding-reading-synthesis-2026-06-01]] records the post-browse P0 literature alignment: candidate spans must be evaluated upstream, identity sensitivity requires controlled functional slices, explanations should be structured and grounded, pragmatic traces should remain optional, and definition frames should be modular.
- [[leakage-resistant-target-relation-modeling]] defines the core research question and warns that candidate construction must be comparable across toxic and non-toxic rows.
- [[target-relation-grounding-literature-map]] consolidates the external target-category, target-expression, context, and bias papers that motivate the experiment structure.
- [[hate-speech-grounding-directions-review-2026-05-18]] recommends treating controlled grounding as the main contribution, hard cases as the data/evaluation engine, and verifiable reasoning as the reliability layer.
- [[target-relation-modeling-reject-review]] lists rejection risks that the experiment plan must directly test: self-inflicted leakage, artificial diagnostics, weak relation labels, candidate-generation leakage, and overclaiming understanding.
- [[ihc-sbic-target-completion-layer]] motivates attacked target, neutral mention, no relevant target, and uncertainty distinctions.
- [[hate-speech-intent-slot-refactor-plan]] supports deriving the final verdict from structured mentions, intent/relation labels, target links, and evidence rather than feeding target as a row-level shortcut.

## Synthesis Notes

### Phase 0: Reproduce Shortcut Diagnostics

Goal: establish the failure mode without making it the whole paper.

- Train or reuse text-only and row-level target-input classifiers on IHC and SBIC.
- Evaluate normal macro-F1, target shuffle, target mask, target replacement with `other`, and target-present non-toxic false-positive rate.
- Expected paper use: a motivating diagnostic showing why row-level target fields are unsafe.

Stop condition: if shortcut collapse only appears in one flawed local preprocessing variant and not under any comparable candidate setup, the paper should be reframed as a data-quality caution.

### Phase 1: Uniform Candidate Target Generation

Goal: remove annotation-source leakage before relation modeling.

- Input: raw text only.
- Generate candidates for every row using the same pipeline, such as LLM extraction, NER plus social-group lexicon, or hybrid extraction.
- Do not feed original gold toxic targets to the model. Keep them only for candidate recall and audit.
- Candidate fields: `candidate_target`, `target_type`, `explicit_or_implicit_candidate`, `candidate_source`, and `candidate_confidence`.
- Report candidate recall against gold toxic targets and a manually audited subset.
- Report explicit-target and implicit-target candidate recall separately.

Recommended first version: use a high-recall LLM candidate generator plus deterministic normalization. Recall matters more than precision because bad candidates can be assigned `not_a_candidate_target`.

### Phase 2: Relation and Evidence Labeling

Goal: build the actual task.

- Relation labels:
  - `attacked`: the content attacks, dehumanizes, excludes, threatens, or derogates the candidate.
  - `mentioned_not_attacked`: the candidate is present or recoverable but not attacked.
  - `not_a_candidate_target`: the candidate is invalid for this task or not actually a social/policy-relevant target.
- Separate flags: `annotator_uncertain`, `implicit_target`, `quotation_or_counterspeech`, `irony_or_sarcasm`, `needs_context`, and `definition_sensitive`.
- Evidence field: minimal evidence span or cue supporting the relation.
- Definition frame: at least two compact definitions, such as strict protected-class hate and broader group-directed abuse.
- Evidence output: prefer minimal quoted spans or cues over unconstrained free-form statements.

Labeling strategy: generate weak labels with an LLM after the schema is fixed, then manually audit a stratified subset covering toxic, non-toxic target-present, implicit, quotation/counterspeech, and definition-sensitive cases.

### Phase 3: Models

Baselines:

- B0: text-only binary classifier.
- B1: row-level target-input classifier.
- B2: target-masked classifier.
- B3: candidate-target relation classifier without definition frame.
- B4: candidate-target relation classifier with definition frame but no evidence output.

Proposed model:

- M1: relation classifier over `(content, candidate_target, definition_frame)`.
- M2: M1 plus structured output fields: `relation_state`, `evidence`, `uncertainty`, and derived `verdict`.
- M3: M2 plus curated hard-case training.

Optional ablation:

- same-target contrastive objective where positive and negative examples share a candidate target but differ in relation.

### Phase 4: Curated Hard-Case Engine

Goal: make synthetic data a controlled stress test, not bulk augmentation.

- Mine false positives and false negatives from B0/B1/M1.
- Generate one-axis variants:
  - same target, attacked to neutral;
  - same target, neutral to attacked;
  - definition frame swap;
  - evidence deletion;
  - quotation/counterspeech insertion;
  - emotional disapproval without a target attack;
  - target replacement with same type or different type.
- Filter with schema checks, duplicate/contamination checks, model-disagreement checks, and a small human audit.
- Compare against bulk synthetic augmentation with similar size and class balance.

Main claim condition: curated hard cases should improve target-present, definition-shift, and cross-dataset slices more than bulk synthetic data.

### Phase 5: Evaluation

Core metrics:

- row-level macro-F1;
- relation macro-F1;
- candidate recall;
- evidence span/cue quality on audited subset;
- target-present non-toxic false-positive rate;
- toxic target-present false-negative rate;
- definition-swap consistency;
- evidence-deletion sensitivity;
- target-replacement sensitivity.
- explicit-target versus implicit-target candidate recall.

Generalization:

- IHC train/test and SBIC train/test.
- IHC-to-SBIC and SBIC-to-IHC transfer.
- Optional external functional set from HateCheck/DynaHate-style cases if mapping is feasible.

Faithfulness tests:

- Delete cited evidence: attacked relation should often become uncertain or change when evidence is necessary.
- Replace target: relation should change when the evidence no longer supports the new target.
- Swap definition: verdict should change only for definition-sensitive cases.
- Change prompt/model for weak labeling: relation labels should be stable on easy cases and flagged uncertain on unstable cases.

### Minimal Table Plan

- Table 1: candidate generation quality, including recall and audit precision.
- Table 2: in-domain row-level and relation performance.
- Table 3: cross-dataset transfer.
- Table 4: shortcut diagnostics, including target shuffle/mask/replacement and target-present non-toxic false-positive rate.
- Table 5: synthetic-data ablation, comparing no synthetic, bulk synthetic, and curated hard cases.
- Table 6: reasoning faithfulness tests, including evidence deletion, target replacement, and definition swap.

### Accept/Reject Criteria

Continue the paper if:

- uniform candidate generation has acceptable recall;
- relation modeling improves target-present benign and toxic slices;
- cross-dataset transfer improves or fails less severely than row-level target-input baselines;
- curated hard cases beat bulk synthetic augmentation on robustness slices;
- structured reasoning passes perturbation checks better than free-form rationales.

Reframe or stop if:

- relation labels are too noisy to audit;
- gains appear only on artificial perturbations;
- candidate generation misses too many implicit targets;
- the final verdict is not better than text-only classification outside local diagnostics;
- evidence fields behave like post-hoc decorations.

## Follow-up Questions

- What candidate generator should be used first: LLM-only, NER plus lexicon, or hybrid?
- How large is the feasible manual audit subset for relation labels and evidence cues?
- Should the first definition frames be platform-policy definitions, academic hate-speech definitions, or a modular element schema?
