---
created: 2026-05-12
updated: 2026-05-21
tags: [query-answer, hate-speech, intent-slot, target-aware, ner, hard-negative]
sources:
  - raw/sources/2020.acl-main.713.pdf
  - raw/sources/2020.findings-emnlp.163.pdf
  - raw/sources/0523.pdf
  - raw/sources/2022.tacl-1.82.pdf
  - raw/sources/2023.acl-short.66.pdf
  - raw/sources/2022.naacl-main.433.pdf
promotion_reason: "Durable method-design answer connecting target leakage in local IHC experiments with recent intent-slot, NER-enrichment, and span-level hate-speech papers."
---

# Query Answer: Intent-Slot Style Hate Speech Modeling

## Question

Can recent hate-speech and SLU papers inspire an intent-slot / NER-style formulation for target-aware hate speech detection, especially after target-input experiments showed target-label leakage?

## Promotion Rationale

The answer has durable value because it reframes local target leakage as a task-definition problem and connects it to recent source evidence on intent tags, group/target spans, compositional generalization, and dialogue intent-slot modeling.

## Short Answer

The most promising direction is to stop treating `target` as a sample-level feature and instead model hate speech as a structured semantic frame. A minimal frame can use `intent` for the harmful speech act, `target` for the affected group or entity, and optional `argument/evidence` spans for the phrase that realizes the attack. This follows the intent-slot intuition from SLU while matching hate-speech evidence that intent annotations and target spans help explain moderation decisions.

For local experiments, the immediate replacement for direct `Text + target -> class` is a two-stage or joint setup: first extract candidate entities/groups with NER/span tagging, then classify the relation between each candidate and an intent label such as derogation, threat, dehumanization, exclusion, support for harm, or neutral mention. This forces the model to decide whether a mentioned group is attacked, rather than learning target priors.

## Evidence

- [[163-calabrese-ross-lapata-2022-explainable-abuse-detection-as-intent-classification-and-slot-filling]] is the direct PLEAD source for policy-aware abuse detection as intent classification and slot filling.
- [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] reports that intent-tag enrichment is more useful than group tags alone for machine classification and human moderation.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] frames implicit target identification as BIO tagging, supporting span-level target supervision.
- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] uses intent-classification and slot-filling structure to test compositional generalization and target-expression balancing.
- [[014-bai-2025-state-toxicn-a-benchmark-for-span-level-target-aware-toxicity-extraction-in-chinese-hate-speech-det]] supports span-level target-aware toxicity extraction where hate directionality is tied to target and argument.
- [[161-qin-2020-agif-an-adaptive-graph-interactive-framework-for-joint-multiple-intent-detection-and-slot-filling]] and [[158-ding-2021-focus-on-interaction-a-novel-dynamic-graph-model-for-joint-multiple-intent-detection-and-slot-filling]] provide earlier SLU evidence for graph-based intent-slot interaction under multiple intents.
- [[160-lin-2020-a-joint-neural-model-for-information-extraction-with-global-features]] is a peripheral structured extraction source showing why local span/link decisions may need global consistency constraints.
- [[125-yin-2024-uni-mis-united-multiple-intent-spoken-language-understanding-via-multi-view-intent-slot-interaction]] and [[126-yin-2025-eclm-entity-level-language-model-for-spoken-language-understanding-with-chain-of-intent]] provide cross-direction analogies for intent-slot interaction and entity-level formulation.
- [[using-not-toxic-targets-for-hate-speech-detection]] records the prior hard-negative proposal for using benign target mentions.
- [[169-zampieri-2023-target-based-offensive-language-identification]] supports the target-plus-offensive-argument structure that the local hate relation task can adapt.
- [[168-yu-2022-hate-speech-and-counter-speech-detection-conversational-context-does-matter]] supports adding context modifiers rather than treating every offensive-looking expression as directly hateful.

## Synthesis Notes

- The local leakage pattern arises because toxic examples use native attacked-target labels while not-toxic examples use LLM-extracted mentioned entities; those are different annotation ontologies.
- Intent-slot modeling separates three questions that were previously collapsed: what entities are mentioned, what harmful intent is present, and which entity the intent targets.
- A practical output schema can be:
  - `entities`: normalized mentions or group spans;
  - `intent`: `neutral`, `derogation`, `threat`, `dehumanization`, `exclusion`, `support_harm`, `other_hate`;
  - `target`: one or more entities linked to non-neutral intent;
  - `evidence`: span(s) supporting the intent-target link.
- Training should include same-target positive and negative pairs so targets do not encode labels by themselves.

## Follow-up Questions

- Which intent ontology should be small enough for reliable annotation while covering IHC/SBIC hate phenomena?
- Should target candidates be extracted by an NER model, by LLM prompting, or by a hybrid NER plus group-normalization dictionary?
- Can synthetic slot recombination, as in compositional generalization work, balance target-intent co-occurrences without creating unnatural examples?
