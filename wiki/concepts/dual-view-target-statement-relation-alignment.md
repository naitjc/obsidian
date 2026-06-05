---
created: 2026-06-01
updated: 2026-06-05
tags: [query-answer, hate-speech, target-relation, statement, contrastive-learning, representation-learning, weak-supervision]
sources:
  - raw/sources/2024.findings-naacl.32.pdf
  - raw/sources/Ahn 等 - 2024 - SharedCon Implicit Hate Speech Detection using Shared Semantics.pdf
  - raw/sources/Kim 等 - 2024 - Label-aware Hard Negative Sampling Strategies with Momentum Contrastive Learning for Implicit Hate S.pdf
promotion_reason: "Durable method-design answer for using completed not_toxic target and statement fields as leakage-resistant dual-view relation supervision."
---

# Query Answer: Dual-View Target-Statement Relation Alignment

## Question

After completing `not_toxic.target` and `not_toxic.statement`, how should those fields be used effectively? Can the idea resemble the syntax-semantics separation and matching pattern in [[175-zhang-2024-graph-induced-syntactic-semantic-spaces-in-transformer-based-variational-autoencoders]]?

## Short Answer

Use the completed fields as training supervision for relation grounding, not as ordinary row-level classifier inputs.

The useful transfer from the NAACL syntax-semantics paper is the architectural principle: separate two heterogeneous views, encode them independently, and align them under controlled objectives. For the current task, the two views are not literally syntax and semantics:

- structural grounding view: `(text, candidate_target, optional evidence_span)`;
- semantic explanation view: `statement`, preferably normalized with a reason type.

Train the final relation classifier from the structural grounding view. Use the statement view only as a weak semantic teacher and contrastive anchor during training. At inference time, the model should classify the relation from raw text and candidate targets without requiring a generated statement. This prevents completed statements from becoming a new label-leakage channel.

## Why Direct Concatenation Is Not Recommended

The completed `target` and `statement` fields are useful but weak:

- `target` completion creates necessary target-present `not_toxic` negatives, but row-level target input previously produced near-perfect normal evaluation and collapsed under target ablations, showing shortcut risk.
- The archived `full_statement` runs generate `class + hate_class + target + statement`, but adding `statement` does not consistently improve the best classification result.
- Statement Jaccard remains low in the archived exact-match-style evaluation, so free-form statements should not be treated as stable gold strings.
- A generated statement can reveal the label lexically through phrases such as "not hateful", "neutral mention", or "attacks the group".

Therefore, the first model should not learn:

```text
text + target + statement -> class
```

It should learn:

```text
text + candidate_target -> relation_state
statement -> training-only semantic anchor
```

## Data Reshaping

Convert every row into candidate-level instances:

```text
{
  text,
  candidate_target,
  relation_state,
  statement,
  statement_type,
  evidence_span,
  target_source,
  statement_source,
  confidence,
  flags
}
```

Use the same candidate-generation pipeline for toxic and not-toxic rows.

Minimal relation states:

```text
attacked
mentioned_not_attacked
not_a_candidate_target
```

Keep uncertainty outside the class label:

```text
implicit_target
quotation_or_counterspeech
factual_report
definition_sensitive
annotator_uncertain
```

Normalize free-form statements into a small `statement_type` vocabulary:

```text
attack_supported
benign_mention
factual_report
quotation_or_counterspeech
unrelated_target
no_relevant_target
insufficient_evidence
```

Preserve the original free-form statement for audit and semantic encoding. Do not discard provenance.

## Minimal Model

### Two Encoders

Encode the structural grounding view and semantic statement view separately:

```text
z_ground = Encoder_ground(text, candidate_target)
z_stmt   = Encoder_stmt(mask_label_words(statement))
```

The final classifier uses only `z_ground`:

```text
relation_logits = Classifier(z_ground)
```

The statement branch acts as a training-only teacher:

```text
z_ground <-> z_stmt
```

This is analogous to syntax-semantics separation only at the level of design principle: heterogeneous information receives separate representations and controlled alignment. A VAE, graph encoder, or latent generative model is not required for the first implementation.

### Training Objective

Use a small multi-task objective:

```text
L = L_relation
  + alpha * L_statement_type
  + beta  * L_alignment
  + gamma * L_same_target_contrast
```

- `L_relation`: cross-entropy for `attacked`, `mentioned_not_attacked`, and `not_a_candidate_target`, predicted from `z_ground`.
- `L_statement_type`: optional auxiliary classification of the normalized explanation type.
- `L_alignment`: InfoNCE or cosine alignment between matched `z_ground` and `z_stmt`.
- `L_same_target_contrast`: separate instances sharing the same target but having different relation states.

If evidence spans become available, add an independent span loss:

```text
+ delta * L_evidence_span
```

Do not force statement generation into the first model. Statement reconstruction is optional and should remain an ablation.

## Negative-Pair Construction

The completed not-toxic fields are valuable because they enable hard negative pairs that were previously missing.

| Pair Type | Positive or Negative | Purpose |
|---|---|---|
| Same target, toxic attack vs benign mention | hard contrast | Break `target identity -> toxic` shortcuts |
| Same text, correct target vs shuffled target | negative | Test target-text compatibility |
| Same text-target pair, matched vs shuffled statement | negative | Prevent generic statements from aligning everywhere |
| Same target and relation, different evidence context | positive or near-positive | Learn reusable relation semantics |
| Target-present counterspeech vs direct attack | hard contrast | Separate quoted harm from authored harm |
| No relevant target vs forced candidate | negative | Prevent over-completion |

When shuffling statements, prefer within-target or within-type shuffles. Random shuffling is often too easy and may teach only topic mismatch.

## Weak-Label Controls

Because many not-toxic statements are generated, apply these controls:

1. Keep native and generated statements in separate provenance groups.
2. Weight generated statements lower than native statements in `L_alignment`.
3. Mask direct verdict phrases such as `not hateful`, `toxic`, or `neutral` before encoding statements.
4. Audit a stratified sample by relation state, statement type, target source, and explicit versus implicit target.
5. Exclude or downweight `insufficient_evidence` and `annotator_uncertain` rows from alignment loss.
6. Evaluate the relation classifier without supplying statements at inference time.

## Recommended Experiment Sequence

### E0: Hard-Negative Baseline

- Train text-only classification.
- Add completed target-present not-toxic rows through reweighting or sampling only.
- Measure target-present not-toxic false-positive rate.

### E1: Candidate-Relation Baseline

- Build `(text, candidate_target) -> relation_state`.
- Derive the row verdict from whether any candidate is `attacked`.
- Compare against row-level `target` concatenation and target-masked baselines.

### E2: Dual-View Alignment

- Add training-only statement encoding and `L_alignment`.
- Add normalized `statement_type`.
- Compare native-only, generated-only, and provenance-weighted statement alignment.

### E3: Span-Grounded Extension

- Add evidence-span supervision on an audited subset.
- Evaluate evidence-deletion sensitivity and HateXScore-inspired quotation faithfulness.

### E4: Optional Graph or Latent Extension

Only after E2 or E3 shows value, consider a heterogeneous graph:

```text
text node
  -> candidate_target nodes
  -> statement or statement_type nodes
  -> evidence_span nodes
```

Edges encode `mentions`, `supports`, `attacks`, or `does_not_attack`. This is the point where the graph-induced latent-space analogy becomes more concrete. Starting with this graph would add complexity before the relation task is validated.

## Evaluation Contract

Report:

- row-level macro-F1;
- relation macro-F1;
- target-present not-toxic false-positive rate;
- toxic target-present false-negative rate;
- explicit and implicit candidate recall;
- target shuffle, target mask, and target replacement sensitivity;
- statement shuffle sensitivity;
- performance with statements removed at inference;
- native-only versus generated-statement ablations;
- cross-dataset transfer between IHC and SBIC.

The key success condition is not merely higher in-domain F1. The aligned model should improve target-present benign slices and remain usable when statement input is absent.

## Decision

The recommended first implementation is a dual-view relation-alignment model:

```text
training:
  (text, candidate_target) -> relation representation
  statement                -> semantic teacher representation
  align matched views and contrast mismatched views

inference:
  (text, candidate_target) -> relation_state -> row verdict
```

This uses the completed `not_toxic.target` and `not_toxic.statement` fields without converting them into shortcut-bearing classifier inputs.

## 2026-06-02 Pilot Evidence

The first remote pilot under `xu-l20:/data/chenjt/hate/FineTune` tested a
smaller generative-SFT approximation before implementing the full dual-encoder
alignment model.

### Strict Target-Completion Ablation

The strict comparison changes only whether non-toxic targets are retained:

```text
class_target_toxic_only
vs
class_target_all_rows
```

| Model | Macro F1: toxic-only -> all rows | Toxic target Jaccard: toxic-only -> all rows |
|---|---:|---:|
| Mistral-7B-Instruct-v0.3 | 0.8363 -> 0.8217 | 0.3633 -> 0.3645 |
| Qwen2.5-7B | 0.8287 -> 0.8262 | 0.3661 -> 0.3733 |
| Qwen3-4B | 0.8233 -> 0.8188 | 0.3523 -> 0.3718 |
| Qwen3-8B | 0.8153 -> 0.8215 | 0.3425 -> 0.3836 |

Preserving non-toxic targets improves toxic-target extraction for all four
models, but row-level Macro F1 improves only for Qwen3-8B. This supports using
completed targets as structured supervision while keeping classification and
grounding metrics separate.

### Statement Pilot

The Qwen3-4B pilot adds 200 generated statements to train-split non-toxic rows
only. Evaluation removes statement generation from the inference contract by
using the `class_hate_class_target_all_rows` prompt.

Reference:

```text
class_hate_class_target_all_rows/Qwen3-4B
Macro F1: 0.8210
```

| Condition | Macro F1 | Delta vs reference | Toxic target Jaccard | All-row target Jaccard |
|---|---:|---:|---:|---:|
| `s1_native_toxic` | 0.8185 | -0.0025 | 0.3705 | 0.6894 |
| `s2_text_only_1x` | 0.8287 | +0.0077 | 0.3579 | 0.6906 |
| `s2_text_label_1x` | 0.8138 | -0.0072 | 0.3701 | 0.6857 |
| `s2_text_label_target_1x` | 0.8231 | +0.0021 | 0.3607 | 0.6817 |
| `s2_text_label_4x` | 0.8204 | -0.0006 | 0.3626 | 0.6789 |

`text_only_1x` is the strongest classification pilot condition. Label- or
target-conditioned statement generation does not produce a consistent target
metric gain. The 200 rows are the first train-split non-toxic rows rather than
a stratified audit sample, so this is pilot evidence rather than a final
method comparison.

The original decision remains unchanged: the next meaningful method step is
training-only semantic alignment with controlled provenance and hard-negative
pairs, not direct row-level statement concatenation.

## 2026-06-05 Full IHC Completion Reassessment

The completed remote artifact
`xu-l20:/data/chenjt/hate/DATA/llm_restructed` changes the feasible experiment
scale. `IHC_target_v1` now covers all train, valid, and test rows, and the three
statement conditions cover all `13,207` `not_toxic` rows.

Target-completion statistics over all splits:

```text
total rows                         18,664
toxic rows                          5,457
not_toxic rows                     13,207
not_toxic with non-empty target     9,587
not_toxic with empty target         3,620
not_toxic mentioned_not_attacked    9,411
not_toxic implicit_target             148
not_toxic uncertain                   131
```

This makes target-present benign examples the central asset. They are large
enough to support same-target contrastive learning and target-present
false-positive diagnostics, not just a small qualitative audit.

Full-scale Qwen3-4B statement-supervision results under
`xu-l20:/data/chenjt/hate/FineTune/experiments/statement_full_v1`:

| Condition | Macro F1 | Delta vs target-all reference | Toxic target Jaccard | All-row target Jaccard |
|---|---:|---:|---:|---:|
| `text_only_1x` | 0.8144 | -0.0066 | 0.3487 | 0.6492 |
| `text_label_1x` | 0.8222 | +0.0012 | 0.3638 | 0.6648 |
| `text_label_target_1x` | 0.8235 | +0.0025 | 0.3746 | 0.6325 |

The full-scale pattern differs from the 200-row pilot. `text_label_target_1x`
is the strongest full condition for Macro F1 and toxic-target Jaccard, but all
three full conditions reduce all-row target Jaccard. This supports using
generated statements cautiously as training-time semantic supervision, not as a
clean all-row grounding improvement.

Statement-quality diagnostics also show direct prompt and label artifacts:

```text
condition            rows   explicit/template traces
text_only           13207   low verdict-word leakage, 889 malformed n-prefix rows
text_label          13207   more neutral/factual/no-group phrasing, 1413 malformed n-prefix rows
text_label_target   13207   983 "not toxic" traces, 2939 "no selected target" traces
```

Recommended next method is therefore a constrained relation-alignment prototype:

1. Build candidate-level instances from the completed artifact:
   `(text, candidate_target, relation_state, statement_condition, statement,
   target_source)`.
2. Train the inference model only on `(text, candidate_target) ->
   relation_state`, where relation states are `attacked`,
   `mentioned_not_attacked`, and `not_a_candidate_target`.
3. Use statements only through masked training losses: statement-type
   prediction, ground-statement alignment, and within-target contrastive pairs.
4. Downweight or mask label/template words in generated statements, especially
   for `text_label_target`.
5. Evaluate target-present benign false-positive rate, toxic target-present
   false-negative rate, target shuffle/mask/replacement sensitivity, relation
   macro-F1, and row-level Macro F1.

The most publishable innovation is not another row-level SFT condition. It is a
full-split, leakage-controlled target-relation protocol where completed
`not_toxic` targets create natural hard negatives, and generated statements act
as weak semantic views whose usefulness is tested without being required at
inference time.

## Related Pages

- [[ihc-sbic-target-completion-layer]]
- [[using-not-toxic-targets-for-hate-speech-detection]]
- [[candidate-target-relation-grounding-experiment-plan-2026-05-18]]
- [[privacy-filter-inspired-span-grounded-hate-detection]]
- [[p0-target-grounding-reading-synthesis-2026-06-01]]
- [[175-zhang-2024-graph-induced-syntactic-semantic-spaces-in-transformer-based-variational-autoencoders]]
- [[012-ahn-2024-sharedcon-implicit-hate-speech-detection-using-shared-semantics]]
- [[060-kim-2024-label-aware-hard-negative-sampling-strategies-with-momentum-contrastive-learning-for-implicit-hate-s]]
