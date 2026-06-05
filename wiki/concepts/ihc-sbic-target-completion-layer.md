---
created: 2026-05-18
updated: 2026-06-01
tags: [query-answer, hate-speech, ihc, sbic, target-completion, intent-slot]
sources:
  - raw/sources/ElSherief 等 - 2021 - Latent Hatred A Benchmark for Understanding Implicit Hate Speech.pdf
  - raw/sources/2022.tacl-1.82.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/W19-3504.pdf
promotion_reason: "Durable method-design answer specifying the target completion layer for adapting IHC/SBIC to intent-slot hate speech parsing."
---

# Query Answer: IHC/SBIC Target Completion Layer

## Question

What should the first layer, target completion, do when refactoring IHC and SBIC hate speech detection into an intent-slot formulation?

## Promotion Rationale

This answer has durable value because target completion is the key data-layer step for avoiding target-presence leakage when not-toxic examples lack native target annotations.

## Short Answer

Target completion should convert asymmetric row-level annotations into comparable structured frames. Toxic examples often contain target-like information, while not-toxic examples may have no target field. The completion layer should not force every not-toxic sample to have a target; instead, it should distinguish three states: attacked target, neutral mentioned target, and no relevant social/protected target mention.

The purpose is to prevent the model from learning `target exists -> toxic` or `target empty -> not toxic`. The completed dataset should contain toxic-with-target, not-toxic-with-target, and not-toxic-without-target examples, with explicit frame labels for each case.

## Evidence

- [[163-calabrese-ross-lapata-2022-explainable-abuse-detection-as-intent-classification-and-slot-filling]] motivates separating policy-relevant slots from the final abuse verdict.
- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] shows why balancing target-expression-slot combinations matters for generalization.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] supports explicit target span identification as a fine-grained supervision task.
- [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] supports intent tags as stronger moderation evidence than group tags alone.
- [[plead-u-plead-target-follow-up-trace]] records why U-PLEAD/TARGET should be treated as a design template rather than a mature downstream-used resource.

## Synthesis Notes

- Input: IHC/SBIC raw text, original label, optional original target/implication fields, and dataset provenance.
- Processing flow: extract candidate social/protected mentions; decide whether each mention is attacked, neutrally mentioned, or irrelevant; assign evidence spans only when text supports the relation; output a normalized intent-slot frame.
- State changes: not-toxic examples are no longer uniformly empty-target examples. They become either neutral-target frames or empty frames depending on the text.
- Output states:
  - `attacked_target`: target mention is linked to harmful intent and evidence.
  - `neutral_mentioned_target`: target/social group is mentioned but no harmful intent is linked.
  - `no_relevant_target`: no protected/social target is present.
  - `uncertain_target`: candidate mention exists but weak labeling cannot reliably decide relation.
- Upstream impact: weak LLM labels require audit, especially for implicit targets and generic nouns that may or may not denote social groups.
- Downstream impact: training and evaluation should balance target presence across toxic and not-toxic labels and report separate performance on target-present not-toxic hard negatives.

## 2026-05-20 Completion Rule

A practical first-pass pipeline can combine deterministic matching and LLM completion, but each step should preserve uncertainty and relation state:

1. Build a normalized toxic-target lexicon from the training split and match it against `not_toxic` text as a candidate generator.
2. Send unmatched or ambiguous `not_toxic` rows to an LLM prompt that extracts candidate social/protected targets, relation state, and a short non-hate explanation.
3. Keep `no_relevant_target` when neither matching nor LLM extraction finds a policy-relevant target. Do not force a target into every `not_toxic` row.
4. Use `mentioned_not_attacked` for target-present benign rows and reserve `attacked_target` for rows where harmful intent is supported by text evidence.
5. Store LLM explanations as weak `statement` labels only after schema checks; allow `insufficient_evidence` and `uncertain_target` instead of over-completing hard cases.

The initial `hate_class` simplification should be interpreted narrowly. `threat` versus `non_threat` is useful for analyzing one harmful-intent dimension, but it is not a complete non-hate label. The safer slot schema is `intent = neutral/no_hate_intent` for not-toxic examples, and `harm_subtype = threat/non_threat_harm` only after an attacked relation has been established.

## 2026-05-25 Related-Paper Alignment For IHC Completion

The closest recent papers in this wiki do not build separate target lexicons for IHC train, validation, and test sets, and they do not provide a precedent for filling not-toxic targets from evaluation-split annotations.

- Boudraa et al. (2025) studies target-span identification on IHC/SBIC with weak span supervision and uses an `80/10/10` stratified train/validation/test split for each corpus.
- Carvallo et al. (2025) uses IHC/SBIC/DH with existing train/validation/test partitions, asks GPT-4o to generate intent and group tags for training partitions, and trains NER models to produce tags for later classification.
- Calabrese et al. (2025) does not augment IHC. U-PLEAD/TARGET balances target-expression-slot combinations in synthetic PLEAD-derived data, so it supports correlation control but not per-split lexicon construction.
- HARE uses IHC/SBIC target and implied-statement annotations to condition rationale generation for hateful examples; for not-hate samples without human rationales it falls back to free rationale generation rather than target completion.

Implementation implication for the current IHC prototype: retain the existing `80/10/10` ID split, build one lexicon from native `target` annotations in the train toxic subset only, keep validation/test target annotations out of lexicon creation, and treat completed not-toxic statements as weak generated labels requiring audit. For the initial matching run, the lexicon retains all normalized native train-toxic target values without pruning source anomalies; resulting matches involving placeholder or personal-name values must be treated as an explicit audit risk.

## 2026-05-25 First-Stage Execution Checkpoint

The initial unpruned target matching run matched 8,563 of 13,207 IHC `not_toxic` rows and queued 4,644 rows for target LLM completion. A `deepseek-v4-flash` target-only completion run successfully returned parseable target decisions for 4,145 queued rows; 499 rows remain deferred because of empty or non-JSON responses.

- Completed `not_toxic` target rows: 12,708; remaining target-LLM rows: 499.
- Deferred causes: 474 `empty_llm_response` and 25 `non_json_llm_response`.
- The unpruned lexicon created 666 matched rows containing the known source-anomaly target terms `Obama` or `Trump`; this is retained by design but must be separated in later audit.
- Among successful LLM completions, 32 rows returned `implicit_target` with `target=[]` because the model identified an implicit group relation without naming an extractable group. These rows require an explicit second-stage policy before generating group-perspective statements.

After a target-only rerun on 2026-05-26, 13 rows initially remained unresolved: 11 train, 1 validation, and 1 test row, all with `empty_llm_response`. Those 13 rows were subsequently manually completed and merged into the consolidated target output. The current authoritative output is `xu-l20:/data/chenjt/hate/DATA/llm_restructed/IHC_target_v1/`; its validation report records zero remaining target rows and treats the cumulative deferred JSONL as historical audit evidence rather than current pending work.

## 2026-05-26 Evidence-Backed Motivation Check

The reason to complete targets is demonstrable in the raw IHC annotation structure. A live check against the original split inputs found that every `toxic` row has a non-empty native target, while every `not_toxic` row has an empty native target:

| split | toxic rows with native target | not_toxic rows with native target | completed not_toxic rows with non-empty target |
|---|---:|---:|---:|
| train | 4,365 / 4,365 | 0 / 10,565 | 7,701 / 10,565 |
| valid | 545 / 545 | 0 / 1,320 | 908 / 1,320 |
| test | 547 / 547 | 0 / 1,322 | 978 / 1,322 |

This is annotation asymmetry, not yet a performance result: without completion, a structured target field reveals the label for all original rows (`target present` only occurs for `toxic`). Completing `not_toxic` targets creates target-present negative examples needed to test whether a system distinguishes mention from attack.

Concrete same-group contrasts in the consolidated output show why the relation state matters:

| Group | `toxic` / `attacked_target` example | `not_toxic` / `mentioned_not_attacked` example |
|---|---|---|
| Muslims | `thats why i always said he was a muslim president` (`943486585164783617`) | `also muslims were asked not to wear skull cap burqa during voting...` (`663632901720965121`) |
| Jewish people | `compensation for holocaust victims ... found other source to milk...` (`540982642380783616`) | `... came from bible & jewish texts.` (`648055302537936896`) |
| Gay / transgender people | `... will gender fluidity also apply to the animal kingdom?` (`600296498115534848`) | `we are black and white gay and straight ...` (`890785632028508161`) |

These pairs do not prove a particular model will improve. They establish the required negative supervision: the same social-group dimension can occur in attacked and non-attacked text, so `target` should be used as a relation candidate or diagnostic slice rather than as an unconditional label cue.

The literature supports this motivation at three levels:

- [Rottger et al. (2021), *HateCheck*](https://aclanthology.org/2021.acl-long.4/) explicitly constructs non-hateful contrasts that retain protected-group identifiers, such as positive statements about immigrants contrasted with hatred of immigrants. It reports that evaluated models misclassify non-hateful contrasts and show target-group performance biases.
- [[031-elsherief-2021-latent-hatred-a-benchmark-for-understanding-implicit-hate-speech|ElSherief et al. (2021), Latent Hatred]] establishes IHC as a benchmark for indirect hate where surface keyword rules are insufficient and target/implied-message grounding is necessary for finer analysis.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models|Boudraa et al. (2025)]] applies target-span identification to IHC/SBIC and reports that error analysis reveals confusion of political or advocacy discourse with hate, directly aligning with the need for `mentioned_not_attacked` examples.
- [[166-davidson-2019-racial-bias-in-hate-speech-and-abusive-language-detection-datasets|Davidson et al. (2019)]] independently shows that hate/abuse classifiers can assign negative labels disproportionately to identity- or dialect-associated content; this does not test IHC completion directly, but supports auditing identity-cue shortcuts rather than trusting aggregate F1 alone.

Current local experimental boundary: a surviving target-input Qwen3-4B run on a prior filled-not-toxic variant reports `macro_f1=0.982773` on its normal test set. Older wiki notes record sharp declines under target shuffle and replacement ablations, but the referenced ablation metric JSON files are not present in the currently inspected remote tree. Those decline values should be treated as historical, not re-verified evidence, until the perturbation evaluations are rerun or recovered.

## 2026-05-26 Statement-Completion Implementation Boundary

The current remote builder contains a statement generation prompt, but it is implemented inside the full `restructure` path rather than as a stage that consumes the completed `IHC_target_v1/` output.

- `toxic` rows retain native IHC `statement` annotations and never require generated statements.
- For a `not_toxic` row whose target decision succeeds, the implemented prompt freezes the selected `target` and `target_status`, then asks for exactly two short English explanations: one from an inside-target-group reader perspective and one from an outside-target-group perspective.
- The implementation limits each generated explanation to 20 words and fills missing list entries with deterministic fallback sentences.
- If statement generation fails while `--defer-refused-llm` is enabled, the entire row is omitted from that full-mode output and its fixed target/status plus failure reason are appended to `deferred_llm_rows.jsonl`.
- The current target-only output intentionally leaves every `not_toxic.statement=[]`; no statement generation has yet been executed for `IHC_target_v1/`.

This implementation should not be used directly as the next production step without adjustment. The verified target output now includes manually completed cache entries and explicit `target_source` provenance. A correct next-stage pipeline should read `IHC_target_v1/{split}.json`, preserve all target fields byte-for-byte, generate statements only for `not_toxic` rows, retain rows with deferred statement status rather than dropping them, and write a new `IHC_target_statement_v1/` result with a separate statement cache and validation report.

## Follow-up Questions

- Should target completion use only protected/social groups, or include broader social targets such as political groups, occupations, and nationalities?
- Should uncertain target cases be excluded from training or retained with an `ambiguous` verdict?
- What manual audit size is enough to validate weak target completion before full model training?

## 2026-06-01 Downstream Use Decision

Completed `not_toxic.target` and `not_toxic.statement` fields should not be concatenated directly into the final classifier input. Use [[dual-view-target-statement-relation-alignment]] as the downstream design:

- reshape rows into `(text, candidate_target) -> relation_state` instances;
- treat target-present not-toxic rows as hard negatives for `mentioned_not_attacked`;
- encode statements as training-only weak semantic anchors;
- align matched target-relation and statement representations while contrasting shuffled or opposite-relation pairs;
- remove statements at inference time and derive the final verdict from attacked candidate relations.

This keeps the completed fields useful without turning generated explanations into a new label-leakage path.
