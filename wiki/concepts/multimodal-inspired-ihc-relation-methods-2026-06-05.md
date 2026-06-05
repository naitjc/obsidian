---
created: 2026-06-05
updated: 2026-06-05
tags: [query-answer, hate-speech, ihc, multimodal, target-relation, retrieval, uncertainty, contrastive-learning]
sources:
  - raw/sources/Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning.pdf
  - raw/sources/Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection.pdf
  - raw/sources/Yang 等 - 2024 - Uncertainty-Aware Cross-Modal Alignment for Hate Speech Detection.pdf
  - raw/sources/Zhang 等 - 2023 - TOT Topology-Aware Optimal Transport For Multimodal Hate Detection.pdf
  - raw/sources/Hee 等 - 2024 - Bridging Modalities Enhancing Cross-Modality Hate Speech Detection with Few-Shot In-Context Learnin.pdf
  - raw/sources/Garg 等 - 2026 - Just KIDDIN Knowledge Infusion and Distillation for Detection of INdecent Memes.pdf
promotion_reason: "Durable method-design answer that translates multimodal hate-detection ideas into IHC target/statement relation modeling after full completion."
---

# Query Answer: Multimodal-Inspired IHC Relation Methods

## Question

After the IHC dataset has completed `not_toxic.target` and full `not_toxic.statement` fills on `xu-l20`, what innovative methods can be derived from the wiki's multimodal hate-detection papers?

## Short Answer

The strongest direction is not another row-level generative SFT condition. The useful transfer from multimodal hate detection is to treat completed IHC fields as heterogeneous views that must be aligned, contrasted, retrieved, and uncertainty-gated.

User constraint after this design pass: do not manually add, delete, expand, or rewrite the dataset. The method must use the existing completed artifacts only. Allowed operations are reshaping rows into candidate-level training instances, building retrieval indexes over existing rows, changing losses or sample weights, masking statement artifacts during encoding, and adding evaluation slices. Disallowed operations are manual data augmentation, synthetic new examples, deleting hard rows, or human-created replacement labels for the main dataset.

Core model constraint: use small-parameter generative LLMs such as Qwen2.5, Qwen3, Mistral-7B, or comparable 4B-8B instruction models. The method should therefore be implemented as constrained generative SFT or lightweight QLoRA with structured JSON outputs, not as a large encoder-only architecture or a full-size multimodal model.

The recommended method is a multimodal-inspired, text-only relation model implemented with a small generative LLM:

```text
grounding view:  text + candidate_target
semantic view:   generated/native statement
memory view:     retrieved same-target and same-relation examples
output:          JSON relation_state -> row verdict
```

At inference time, the model should use only `text + candidate_target` and generate a compact JSON relation output. Statements and retrieved examples are training-time or adaptation-time support signals, not required inputs for the final classifier unless explicitly evaluated as a separate retrieval setting.

## Local Evidence

Remote inspection on `xu-l20` shows that `IHC_target_v1` is now complete:

```text
total rows                         18,664
toxic rows                          5,457
not_toxic rows                     13,207
not_toxic with non-empty target     9,587
not_toxic mentioned_not_attacked    9,411
```

The full statement fill covers all `not_toxic` train, validation, and test rows under `text_only`, `text_label`, and `text_label_target`.

Fine-tuning results show a mixed signal:

- Strict target completion improves toxic-target Jaccard for all four models, but Macro F1 improves only for Qwen3-8B.
- Full statement supervision with Qwen3-4B gives the best full condition at `text_label_target_1x` with Macro F1 `0.8235` and toxic-target Jaccard `0.3746`.
- All full-statement conditions reduce all-row target Jaccard relative to the target-completion reference.

Thus, completed targets and statements are useful supervision, but direct concatenation is not a clean grounding method.

## Transfer From Multimodal Hate Papers

### Retrieval-Guided Contrast

[[080-mei-2024-improving-hateful-meme-detection-through-retrieval-guided-contrastive-learning]] and [[081-mei-2025-robust-adaptation-of-large-multimodal-models-for-retrieval-augmented-hateful-meme-detection]] motivate retrieval-guided hard examples rather than bulk augmentation.

IHC transfer:

- retrieve same-target toxic and not-toxic rows;
- retrieve same relation with different targets;
- retrieve false positives and false negatives from current checkpoints;
- train contrastive pairs where target identity stays similar but relation state changes.

This directly uses the large target-present benign pool to break `target identity -> toxic` shortcuts.

These are retrieval and pairing operations over the existing dataset, not new sample generation. A retrieved neighbor can change the loss context, contrastive batch, or support prompt, but it should not create a new labeled dataset row.

### Cross-View Alignment

[[121-yang-2024-uncertainty-aware-cross-modal-alignment-for-hate-speech-detection]] and [[136-zhang-2023-tot-topology-aware-optimal-transport-for-multimodal-hate-detection]] motivate explicit alignment rather than opaque feature fusion.

IHC transfer:

- encode `text + candidate_target` as the grounding view;
- encode masked `statement` as the semantic view;
- align matched pairs and contrast shuffled statements;
- keep the classifier head on the grounding view only.

This matches [[dual-view-target-statement-relation-alignment]] while borrowing the multimodal alignment principle: different evidence channels should be aligned under constraints, not simply concatenated.

### Uncertainty-Gated Supervision

Yang's uncertainty-aware alignment suggests that not every view should receive equal training weight.

IHC transfer:

- downweight `uncertain`, `implicit_target`, fallback-template, and label-template-heavy statements;
- reduce alignment loss for `text_label_target` statements containing direct verdict artifacts such as "not toxic" or "no selected target";
- report uncertainty slices separately instead of merging them into a single relation label.

The goal is not to maximize statement usage. The goal is to use statements only where they add semantic evidence without leaking the answer.

### Cross-Modality Support Transfer

[[046-hee-2024-bridging-modalities-enhancing-cross-modality-hate-speech-detection-with-few-shot-in-context-learnin]] shows that text hate examples can support vision-language hate detection.

IHC transfer:

- use IHC completed candidate-relation instances as support examples for SBIC or multimodal hateful meme prompts;
- use SBIC cleaner target supervision as support for IHC implicit cases;
- evaluate support retrieval by target, relation, and statement type rather than random few-shot examples.

This can become a cross-dataset transfer experiment without needing new image data.

Under the no-dataset-change constraint, this is an evaluation and prompting/support-selection setup only. It should not merge datasets, import external examples into IHC training, or create new synthetic support cases.

### Knowledge Graph or Context Graph

[[034-garg-2026-just-kiddin-knowledge-infusion-and-distillation-for-detection-of-indecent-memes]] and [[019-cai-2025-unpacking-hateful-memes-presupposed-context-and-false-claims]] motivate external context and graph-like reasoning for implicit hateful meaning.

IHC transfer should stay minimal:

- first build a lexical target ontology or alias graph from `target_lexicon.json`;
- optionally connect targets, target types, statement types, and relation states;
- use graph or knowledge features only as an ablation after the relation baseline works.

Do not start with a full knowledge-graph method; it would add complexity before the candidate-relation task is validated.

The graph must be derived from existing fields such as `target`, `target_lexicon.json`, `target_status`, `statement_condition`, and `statement_type`. It should not introduce new external knowledge nodes for the first paper version.

## Recommended Method

Name-level framing:

```text
Retrieval- and Uncertainty-Guided Dual-View Relation Alignment for Implicit Hate Detection
```

Minimal implementation with a small generative LLM:

1. Convert completed IHC rows into candidate-level instances:

```text
text, candidate_target, relation_state, statement_condition, statement,
target_source, target_status, split
```

This conversion is a view over the existing artifact, not a dataset expansion claim. If one row has multiple existing targets, multiple candidate instances may be used for training, but evaluation must still report back to the original row-level split.

2. Fine-tune a small generative LLM to emit a constrained relation JSON:

```text
input:  text + candidate_target
output: {"relation_state": "attacked" | "mentioned_not_attacked" | "not_a_candidate_target"}
```

3. Add multimodal-inspired support losses:

```text
L = L_relation
  + beta * L_ground_statement_alignment
  + gamma * L_retrieval_guided_contrast
  + eta * L_statement_type
```

4. Apply uncertainty and provenance gates:

```text
weight = f(target_source, target_status, statement_condition, template_artifact_flags)
```

5. Derive row-level verdict from whether any candidate is predicted as `attacked`.

## First Experiments

E1 should be a candidate-relation generative baseline with Qwen2.5/Qwen3:

- build candidate-level JSONL from `IHC_target_v1` and one statement condition;
- use Qwen3-4B, Qwen3-8B, or Qwen2.5-7B QLoRA to generate a compact relation JSON;
- evaluate row-level Macro F1 and relation Macro F1 separately.

E2 should add retrieval-guided contrast:

- same target, toxic attack vs benign mention;
- same target, benign mention vs no relevant target;
- current false positive and false negative neighborhoods;
- target-shuffled negatives.

Do not materialize these as new augmented dataset rows. Use them as batch construction, loss pairs, or diagnostic perturbations.

E3 should add statement alignment:

- mask verdict words in statements;
- align matched `grounding view` and `statement view`;
- compare `text_only`, `text_label`, and `text_label_target` statements with provenance weighting.

E4 should test cross-dataset support:

- IHC relation model with SBIC support examples;
- SBIC-trained support retrieval on IHC implicit targets;
- optional text-support prompt evaluation for hateful meme datasets only after the text-only relation result is stable.

This is lower priority under the current constraint because it can be misread as dataset expansion. Keep the first implementation IHC-only unless the comparison is explicitly framed as zero-shot or support-selection evaluation.

## Evaluation Contract

Report more than aggregate F1:

- row-level Macro F1;
- candidate relation Macro F1;
- target-present not-toxic false-positive rate;
- toxic target-present false-negative rate;
- target shuffle, target mask, and target replacement sensitivity;
- statement shuffle sensitivity;
- retrieval support ablation;
- uncertainty-slice performance;
- IHC-to-SBIC and SBIC-to-IHC transfer when SBIC relation labels are prepared.

## Decision

The publishable innovation is a controlled relation-grounding protocol inspired by multimodal hate-detection mechanisms:

- retrieval from RGCL and RA-HMD becomes same-target hard-example memory;
- cross-modal alignment becomes ground-statement dual-view alignment;
- uncertainty-aware fusion becomes provenance- and artifact-gated weak supervision;
- graph/knowledge infusion becomes a later target-alias or context graph ablation.

This is stronger than directly feeding completed target and statement fields into another generative classifier, because it tests whether the model learns the relation between a target and the harmful expression rather than the presence of a target-like field.

## Chain Check

- Input: completed IHC target and statement artifacts, FineTune results, and multimodal hate-detection wiki pages.
- Processing flow: map multimodal retrieval, alignment, uncertainty, and knowledge mechanisms into text-only candidate-target relation modeling without changing dataset membership or manual labels.
- State changes: no source numeric claims are upgraded beyond locally inspected experiment summaries and wiki-recorded publication-checked values.
- Output: a minimal method and experiment sequence constrained to existing completed artifacts.
- Upstream impact: requires candidate-level data conversion and statement artifact masking before training.
- Downstream impact: evaluation must separate relation grounding, row verdict, target shortcut diagnostics, and statement/retrieval ablations.

## Related Pages

- [[multimodal-hate-detection]]
- [[dual-view-target-statement-relation-alignment]]
- [[rahmd-inspired-ihc-relation-adaptation-2026-06-05]]
- [[leakage-resistant-target-relation-modeling]]
- [[candidate-target-relation-grounding-experiment-plan-2026-05-18]]
- [[target-relation-grounding-literature-map]]
