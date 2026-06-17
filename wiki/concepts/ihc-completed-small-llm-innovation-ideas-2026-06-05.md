---
created: 2026-06-05
updated: 2026-06-17
tags: [query-answer, hate-speech, ihc, target-relation, small-llm, research-planning]
sources:
  - raw/sources/2022.tacl-1.82.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.42.pdf
  - raw/sources/2403.19836v2.pdf
  - raw/sources/2025.emnlp-main.296.pdf
  - raw/sources/2025.findings-naacl.175.pdf
  - raw/sources/2026.eacl-long.198.pdf
  - raw/sources/2026.findings-eacl.230.pdf
  - raw/sources/2025.tacl-1.67.pdf
  - raw/sources/2601.09342v2.pdf
  - raw/sources/3774904.3792159.pdf
  - raw/sources/07936-AAAI24.ZhangJ-SRRAI.pdf
promotion_reason: "Durable research-planning answer after full IHC target and statement completion, constrained to small generative LLMs and no further dataset augmentation."
---

# Query Answer: Completed-IHC Small-LLM Innovation Ideas

## Question

The user asked to search the wiki's paper knowledge, optionally check online, and propose innovative ideas under new constraints: IHC is already completed, the main model should be a small-parameter generative LLM, and the next work should not augment the dataset further. The user pointed to `xu-l20:/data/chenjt/hate/DATA/llm_restructed` and `xu-l20:/data/chenjt/hate/FineTune`.

## Promotion Rationale

This answer has durable value because the project state has changed from annotation completion to method design. The reusable decision is how to use completed IHC target and statement artifacts without turning them into row-level shortcuts or starting another data-augmentation loop.

## Short Answer

The strongest next direction is a leakage-controlled candidate-target relation protocol implemented with a small generative LLM. The model should generate compact structured JSON for `(text, candidate_target) -> relation_state`, while target-completed benign examples, generated statements, retrieval neighbors, and definition frames are used as training-time or evaluation-time controls.

The paper-level novelty should not be "we completed IHC" or "we add more generated explanations." It should be: completed IHC exposes a large natural pool of target-present non-toxic examples, enabling a controlled test of whether small generative LLMs distinguish attacked targets from benign mentions rather than exploiting target presence, target identity, or statement artifacts.

## Evidence

- [[hate-speech-final-synthesis]] records the field shift from flat labels toward target spans, intent/group tags, rationales, modular definitions, and compositional tests.
- [[ihc-sbic-target-completion-layer]] records the completed IHC target state and the key relation states: `attacked_target`, `mentioned_not_attacked`, `no_target`, `implicit_target`, and `uncertain`.
- [[dual-view-target-statement-relation-alignment]] records why completed targets and statements should be training supervision, not direct row-level classifier inputs.
- [[multimodal-inspired-ihc-relation-methods-2026-06-05]] maps retrieval, alignment, uncertainty, and graph ideas from multimodal hate detection into the completed IHC setting.
- [[154-boudraa-2025-implicit-hate-target-span-identification-in-zero-and-few-shot-settings-with-selective-sub-billion-parameter-models]] supports small and sub-billion model target-span identification on IHC/SBIC, but target spans alone do not decide relation.
- [[178-jafari-2024-target-span-detection-for-implicit-harmful-content]] supports upstream explicit and implicit target span extraction across SBIC, DynaHate, and IHC.
- [[155-carvallo-2025-hate-explained-evaluating-ner-enriched-text-in-human-and-machine-moderation-of-hate-speech]] supports intent tags as more useful than group tags alone for moderation and generalization.
- [[152-calabrese-2025-compositional-generalisation-for-explainable-hate-speech-detection]] creates novelty pressure because target-expression compositionality and slot-style evaluation already exist.
- [[180-chen-wang-2025-pragmatic-inference-chain-improving-llms-reasoning-of-authentic-implicit-toxic-language]] supports optional pragmatic cues for implicit toxicity, but long reasoning should remain an ablation.
- [[181-korre-2025-untangling-hate-speech-definitions-a-semantic-componential-analysis-across-cultures-and-domains]] and [[156-melis-2025-a-modular-taxonomy-for-hate-speech-definitions-and-its-impact-on-zero-shot-llm-classification-performance]] support explicit definition frames.
- [[182-hu-lee-2026-hatexscore-a-metric-suite-for-evaluating-reasoning-quality-in-hate-speech-explanations]] and [[176-puppi-vecchi-2026-harm-learning-hate-aware-reward-model-for-evaluating-natural-language-explanations-of-offensive-content]] support evaluating explanation faithfulness and hate-aware explanation quality rather than trusting free-form statement fluency.
- [[192-gajewska-2026-improving-implicit-hate-speech-detection-via-a-community-driven-multi-agent-framework]] supports gated community-context consultation for uncertain implicit-hate cases, but also warns that broad demographic agents should not replace explicit target-relation labels.
- [[193-sun-2026-rethinking-implicit-hate-speech-detection-focusing-on-latent-hate-components-via-dual-process-argumentation]] supports using structured latent components as reasoning anchors before agentic deliberation, which maps cleanly to compact relation/evidence fields in the local project.
- [[194-zhang-2024-efficient-toxic-content-detection-by-bootstrapping-and-distilling-large-language-models]] supports DToT-style confidence-gated context refinement and distilling expensive reasoning traces into smaller models.
- [[058-kim-2022-generalizable-implicit-hate-speech-detection-using-contrastive-learning]], [[060-kim-2024-label-aware-hard-negative-sampling-strategies-with-momentum-contrastive-learning-for-implicit-hate-s]], and [[056-jiang-2025-learn-from-failure-causality-guided-contrastive-learning-for-generalizable-implicit-hate-speech-det]] support hard-negative and failure-guided contrastive learning for implicit hate.
- [[080-mei-2024-improving-hateful-meme-detection-through-retrieval-guided-contrastive-learning]], [[081-mei-2025-robust-adaptation-of-large-multimodal-models-for-retrieval-augmented-hateful-meme-detection]], [[121-yang-2024-uncertainty-aware-cross-modal-alignment-for-hate-speech-detection]], and [[136-zhang-2023-tot-topology-aware-optimal-transport-for-multimodal-hate-detection]] motivate retrieval-guided contrast, cross-view alignment, and uncertainty gating.
- [[184-ao-2025-safe-pruning-lora-robust-distance-guided-pruning-for-safety-alignment-in-adaptation-of-llms]] is relevant to post-QLoRA adapter reliability checks for small generative LLM adaptation.

Remote verification on 2026-06-05:

```text
xu-l20:/data/chenjt/hate/DATA/llm_restructed/IHC_target_v1
total rows                         18,664
toxic rows                          5,457
not_toxic rows                     13,207
not_toxic with non-empty target     9,587
not_toxic mentioned_not_attacked    9,411
remaining target rows                   0
```

Statement fill is complete for train, validation, and test under `text_only`, `text_label`, and `text_label_target`; total successful cache coverage is `39,621 / 39,621`, with 29 conservative fallback records.

Remote full-statement Qwen3-4B results under `FineTune/experiments/statement_full_v1`:

| Condition | Macro F1 | Delta vs target-all reference | Toxic target Jaccard | All-row target Jaccard |
|---|---:|---:|---:|---:|
| `text_only_1x` | 0.8144 | -0.0066 | 0.3487 | 0.6492 |
| `text_label_1x` | 0.8222 | +0.0012 | 0.3638 | 0.6648 |
| `text_label_target_1x` | 0.8235 | +0.0025 | 0.3746 | 0.6325 |

This means statement supervision can help row-level classification and toxic-target extraction slightly, but it hurts all-row target grounding. Statements should therefore be weak semantic views, not direct inference inputs.

## Synthesis Notes

### Boundary Conditions

- Do not add new synthetic rows, manually expand the dataset, or rewrite completed labels.
- Do not feed completed `target` and generated `statement` as ordinary row-level input for the final classifier.
- Use small generative LLMs such as Qwen3-4B, Qwen3-8B, Qwen2.5-7B, or Mistral-7B with LoRA/QLoRA and constrained JSON generation.
- Treat existing completed fields as views, support signals, retrieval keys, sample weights, diagnostics, or weak supervision.
- Keep final claims narrow: reduced shortcut dependence and improved robustness under target and definition controls, not broad semantic understanding.

### Idea 1: Candidate-Target Relation JSON SFT

Core formulation:

```text
input:
  text
  candidate_target
  optional definition_frame

output:
  {
    "relation_state": "attacked" | "mentioned_not_attacked" | "not_a_candidate_target",
    "evidence_cue": "...",
    "flags": ["implicit_target" | "quotation_or_counterspeech" | "definition_sensitive" | "uncertain"]
  }
```

Why it is worth doing:

- It uses the completed `9,411` target-present benign rows as the main resource.
- It shifts the model from `target exists -> toxic` to `target-text relation -> verdict`.
- It fits a small generative LLM because the output is compact JSON, not long reasoning.
- It can be evaluated separately at relation level and row level.

Minimal experiments:

- Compare `class`, row-level `class_target_all_rows`, and relation JSON SFT.
- Derive row verdict from whether any candidate relation is `attacked`.
- Report row Macro F1, relation Macro F1, target-present not-toxic false-positive rate, toxic target-present false-negative rate, JSON validity, and target shuffle/mask/replacement sensitivity.

Reviewer risk:

- Relation labels may collapse into the final label. The paper must report candidate construction, relation classification, evidence cue quality, and final verdict separately.

### Idea 2: Retrieval-Guided Relation Memory Without Augmentation

Use retrieval as a training or inference support mechanism over existing rows:

```text
same target, attacked
same target, mentioned_not_attacked
same relation, different target
current checkpoint false positives
current checkpoint false negatives
```

Allowed uses:

- support examples in prompt-only or retrieval-ablation evaluation;
- contrastive batch construction;
- pairwise hidden-state alignment or ranking loss;
- diagnostic neighborhoods for error analysis.

Disallowed framing:

- do not call retrieved neighbors new training data;
- do not materialize them as synthetic rows;
- do not use retrieval to mask weak relation-label quality.

Expected contribution:

- Adapts RGCL/RA-HMD-style retrieval to text-only target relations.
- Tests whether same-target opposite-relation examples reduce identity shortcuts.
- Gives a clean ablation: no retrieval, same-target retrieval, same-relation retrieval, failure-neighbor retrieval.

For the concrete RA-HMD-style implementation, use [[rahmd-inspired-ihc-relation-adaptation-2026-06-05]]: stage 1 jointly trains constrained JSON generation and a relation head, stage 2 freezes the LLM and tunes retrieval-aligned relation embeddings, and inference compares JSON, relation-head, and retrieval-KNN modes.

### Idea 2b: ReAct-Style Relation Verifier With Gated Actions

The new agentic papers make the ReAct-style idea plausible only under a controlled verifier design:

```text
base pass:
  FineTune classifier -> label probability, uncertainty, error-slice flag

actions, only when triggered:
  retrieve same-target opposite-relation rows
  extract candidate target / evidence cue
  mine latent hate component
  check definition frame or community context
  compare attacked vs mentioned_not_attacked readings

output:
  compact JSON fields, not free-form chain-of-thought
```

Trigger rule:

- activate the verifier for borderline classifier probabilities, trigger-word false positives, implicit/contextual false negatives, target-present benign rows, and definition-sensitive cases;
- keep direct classifier output for easy high-confidence rows;
- report how often the verifier fires, because token/API cost is part of the method claim.

Why this is safer than always-on ReAct:

- It matches [[192-gajewska-2026-improving-implicit-hate-speech-detection-via-a-community-driven-multi-agent-framework]] and [[194-zhang-2024-efficient-toxic-content-detection-by-bootstrapping-and-distilling-large-language-models]]: extra reasoning is gated by uncertainty or low confidence.
- It matches [[193-sun-2026-rethinking-implicit-hate-speech-detection-focusing-on-latent-hate-components-via-dual-process-argumentation]]: deliberation should be anchored to explicit components, not applied as generic debate over the whole text.
- It respects the local retrieval evidence: previous all-sample retrieval prompting hurt toxic recall, so retrieval or ReAct actions should be selective and auditable.

Evaluation:

- primary: row Macro F1, toxic recall, target-present benign false-positive rate;
- verifier-specific: baseline-correct-to-verifier-wrong conversions, verifier-corrected false negatives, JSON validity, action ablations;
- robustness: target shuffle, evidence deletion, same-target opposite-relation support, and definition-frame perturbations.

Distillation option:

- If verifier inference is too expensive, use its accepted structured traces as weak supervision or auxiliary features for a smaller relation verifier. Do not claim explanation faithfulness unless checked with [[182-hu-lee-2026-hatexscore-a-metric-suite-for-evaluating-reasoning-quality-in-hate-speech-explanations]]-style diagnostics.

### Idea 3: Statement-as-Teacher With Artifact Gating

The full statement results make direct statement concatenation unattractive. A better design is:

```text
ground view:
  text + candidate_target

semantic view:
  masked statement

training:
  align matched views
  contrast shuffled statements
  predict coarse statement_type

inference:
  no statement input
```

Required controls:

- mask verdict words such as `not toxic`, `neutral`, and prompt-template remnants;
- downweight the 29 fallback records and rows with `uncertain` or malformed statement artifacts;
- compare `text_only`, `text_label`, and `text_label_target` statement sources;
- report statement shuffle sensitivity and all-row target Jaccard, not only Macro F1.

Likely paper angle:

- Generated statements are not treated as gold explanations. They are weak semantic teachers whose usefulness is tested by whether the statement-free relation model improves.

### Idea 4: Definition-Frame Relation Probing

Definition-sensitive hate work suggests that "hate" should not be a single implicit constant. The low-cost version does not relabel the dataset; it evaluates the same trained relation model under compact definition prompts:

```text
strict_protected_group_hate
broader_group_directed_abuse
```

Metrics:

- definition-swap consistency for clearly stable cases;
- definition-sensitive rate for ambiguous or borderline rows;
- false-positive shifts on target-present benign examples;
- false-negative shifts on implicit toxic examples.

Why this is useful:

- It makes the paper less tied to one IHC operational definition.
- It gives a principled alternative to prompt tinkering.
- It supports reviewer-facing claims about construct control without creating another dataset.

### Idea 5: Evidence-Cue Faithfulness Tests

Ask the small generative LLM for a short evidence cue, not a full chain-of-thought:

```json
{"evidence_cue": "short quoted or paraphrased cue"}
```

Then test:

- evidence deletion: mask the cited cue and check whether `attacked` confidence drops;
- target replacement: replace only the target and check relation compatibility;
- statement mismatch: pair the correct ground view with a shuffled statement;
- quotation/counterspeech slice: verify that quoted harm is not treated as authored attack.

This imports the useful part of HateXScore and HARM into the current structured-output pipeline. It avoids overclaiming explanation quality from free-form `statement` Jaccard.

### Idea 6: Relation-Adapter Reliability and Pruning

Because the main model is a small QLoRA-adapted generative LLM, adapter behavior is part of the method. A compact reliability idea:

- train the relation JSON adapter normally;
- measure layer-wise LoRA distance or contribution;
- prune or gate adapter components that improve aggregate F1 but worsen target-present benign false positives, JSON validity, or safety-oriented probes;
- compare full adapter, pruned adapter, and base model.

This should be a secondary method or ablation, not the headline contribution. It is useful because current results show small Macro F1 differences can hide grounding tradeoffs.

### Idea 7: SBIC as Support and Transfer Test, Not Extra Training Data

SBIC should be used after the IHC relation baseline works:

- IHC-to-SBIC and SBIC-to-IHC transfer;
- retrieval support examples from SBIC at inference time only;
- same relation and same target-type support selection;
- no mixing SBIC rows into the IHC train split unless the experiment is explicitly a cross-dataset training condition.

This tests whether the relation protocol generalizes beyond the completed IHC artifact rather than merely fitting its completion process.

## Prioritized Execution Order

1. Build the candidate-level relation JSONL view from existing `IHC_target_v1` and one statement condition, keeping original row IDs and split membership.
2. Train Qwen3-4B and Qwen3-8B relation JSON SFT baselines with statement-free inference.
3. Add target-present benign diagnostics, target shuffle/mask/replacement tests, and JSON validity checks.
4. Add retrieval-guided same-target hard-neighbor support or contrastive batches.
5. Add statement-as-teacher alignment with artifact masking and provenance weights.
6. Add definition-frame probing and evidence-cue deletion tests.
7. Only then consider SBIC transfer/support and adapter pruning.

## Non-Recommended Directions

- More data augmentation or synthetic hard-case training as a headline contribution.
- Direct `text + target + statement -> class` SFT as the main model.
- A large graph or knowledge-base method before the relation JSON baseline is validated.
- Long chain-of-thought generation for every row.
- A paper framed only around beating IHC/SBIC aggregate Macro F1.

## Chain Check

- Input: wiki hate-speech source hub, target-relation pages, completed IHC artifact on `xu-l20`, and FineTune result summaries.
- Processing flow: identify recurring literature gaps, remove directions that violate the new constraints, map remaining ideas to small generative-LLM experiments.
- State changes: no `raw/` files are edited and no remote data or model files are changed.
- Output: a ranked method plan centered on relation JSON SFT, retrieval memory, statement-as-teacher alignment, definition probing, evidence faithfulness, adapter reliability, and cross-dataset support tests.
- Upstream impact: requires a candidate-level view builder and evaluation scripts, not new annotation.
- Downstream impact: final claims must report relation grounding and shortcut diagnostics separately from row-level Macro F1.

## Follow-up Questions

- Which statement condition should seed the first relation JSONL view: `text_label`, which has best all-row target Jaccard among full statements, or `text_label_target`, which has best Macro F1 and toxic-target Jaccard?
- Should the first paper be pitched as a benchmark/protocol paper or as a method paper with protocol as the main evaluation contribution?
- What manual audit budget is available for relation labels and evidence cues?
