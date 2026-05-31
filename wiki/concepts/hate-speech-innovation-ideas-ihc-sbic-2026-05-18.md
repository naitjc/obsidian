---
created: 2026-05-18
updated: 2026-05-18
tags: [query-answer, hate-speech, ihc, sbic, innovation, intent-slot, target-aware]
sources:
  - raw/sources/2022.tacl-1.82.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/Ji 等 - 2025 - LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-S.pdf
promotion_reason: "Durable research-planning answer combining wiki evidence with current IHC/SBIC fine-tuning scores and bad-case structure."
---

# Query Answer: Hate Speech Innovation Ideas for IHC/SBIC

## Question

The user is working on hate speech detection and asked for broader early-stage innovation ideas. They wanted the answer to inspect existing paper gaps in the built wiki, optionally search related papers, and use the remote IHC/SBIC fine-tuning results, bad cases, and processed datasets.

## Promotion Rationale

This answer has durable value because it connects the local IHC/SBIC experimental failure modes with the wiki's recent target-aware, intent-slot, span-level, and compositional-generalization evidence.

## Short Answer

The strongest direction is not simply to improve binary classification. The current fine-tuning setup already reaches or exceeds the reference macro-F1 on IHC/SBIC, but its structured outputs are still label-coupled: false positives generate non-empty targets for originally target-empty non-toxic cases, while false negatives generate empty targets for target-bearing toxic cases. This suggests that target prediction is mostly following the class decision rather than independently grounding the attacked group.

A better innovation line is to turn IHC/SBIC into a leakage-resistant structured hate-understanding benchmark: first identify group/social mentions, then classify whether each mention is attacked, neutrally mentioned, or irrelevant, then derive the final hate verdict from the relation and evidence. This uses target/span/intent ideas from recent papers while directly addressing the observed bad-case pattern in the user's fine-tuning runs.

## Evidence

- [[hate-speech-final-synthesis]] records that recent pure-text hate work is moving from binary labels toward target spans, intent/group tags, rationales, modular definitions, and compositional tests.
- [[hate-speech-intent-slot-refactor-plan]] recommends `text -> {mentions, intents, target_links, evidence_spans, verdict}` rather than feeding row-level target as a shortcut.
- [[ihc-sbic-target-completion-layer]] distinguishes attacked targets, neutral mentioned targets, no relevant target, and uncertain target states.
- [[llm-augmentation-fields-in-related-papers]] argues for adding task-aligned intermediate fields rather than fully relabeling natural examples.
- [[163-calabrese-ross-lapata-2022-explainable-abuse-detection-as-intent-classification-and-slot-filling]] motivates policy-aware intent-slot modeling.
- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] motivates target-expression-slot recombination tests.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] supports IHC/SBIC target-span identification.
- [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] reports that intent tags are more useful than group tags alone.
- Remote evidence from `xu-l20:/data/chenjt/hate/FineTune/experiments/eval_results.md`: best IHC macro-F1 is 0.8363 with Mistral class-target; best SBIC macro-F1 is 0.8797 with Qwen3-8B class-target. IHC target Jaccard remains low, around 0.33-0.38, while SBIC target Jaccard is around 0.65-0.69.
- Remote error aggregation shows a structural coupling: in representative class-target/full runs, IHC false positives have empty gold targets but generated non-empty targets, and false negatives have gold targets but generated empty targets. The same pattern appears in SBIC.
- Additional remote evidence from `xu-l20:/data/chenjt/hate/FineTune_filled_not_toxic`: after filling not-toxic IHC targets with LLM labels and feeding target as input, target-input class-only models reach approximately 0.985-0.988 macro-F1. However, target shuffling drops macro-F1 to roughly 0.40-0.48, and replacing every target with `other` yields macro-F1 0.4107 with toxic recall 0. This is direct evidence that the model learned a target-label shortcut.
- The filled IHC datasets under `DATA/llm_target_filled_new/IHC/processed` make 93-95% of not-toxic rows target-present, while toxic rows are nearly always target-present. The old filled version used `other` heavily for not-toxic rows; the new version reduces `other` but still leaves target identity highly predictive when used as a row-level input.

## Synthesis Notes

- Idea 1: Build a target-relation completion layer. Add a uniform `group_mentions` field for toxic and non-toxic rows, then label relation states as `attacked_target`, `neutral_mentioned_target`, `no_relevant_target`, or `uncertain_target`.
- Idea 2: Evaluate target independence. Add metrics that condition on target presence: non-toxic target-present false-positive rate, toxic target-present false-negative rate, target-link accuracy, and class-target mutual dependence.
- Idea 3: Use bad cases as a curriculum. Mine high-confidence false positives and false negatives to create hard positive/negative pairs. Contrast examples with the same group mention but different relation states.
- Idea 4: Make compositional splits over target and expression. Hold out target-expression combinations rather than random rows, following U-PLEAD/TARGET-style generalization.
- Idea 5: Add a minimal intent layer before full slot parsing. Start with a small ontology such as `neutral`, `derogation`, `threat`, `dehumanization`, `exclusion`, `support_harm`, and `other_hate`; compare it against target-only enrichment.
- Idea 6: Separate mention extraction from hate judgment at inference time. A two-stage or constrained joint model can prevent the model from outputting empty targets simply because it chose `non_toxic`.
- Idea 7: Treat LLM-filled not-toxic targets as diagnostic annotations, not direct classifier inputs. They should be used to build target-present non-toxic slices, target-shuffle tests, and relation labels; feeding them as row-level target context creates a shortcut unless the task explicitly asks whether a given target is attacked.

## Follow-up Questions

- Should the first prototype prioritize IHC, where target grounding is hardest, or a combined IHC/SBIC benchmark where SBIC provides cleaner target supervision?
- How large should the audited subset be for relation labels before weak LLM labels can be trusted?
- Should neutral target mentions include only protected/social groups, or broader political and ideological groups as well?
