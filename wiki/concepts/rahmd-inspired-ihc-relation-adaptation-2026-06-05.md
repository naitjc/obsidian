---
created: 2026-06-05
updated: 2026-06-05
tags: [query-answer, hate-speech, ihc, target-relation, retrieval, small-llm, contrastive-learning]
sources:
  - raw/sources/Mei 等 - 2025 - Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection.pdf
  - raw/sources/Mei 等 - 2024 - Improving Hateful Meme Detection through Retrieval-Guided Contrastive Learning.pdf
promotion_reason: "Durable method-design answer mapping RA-HMD's two-stage retrieval-augmented adaptation into the completed-IHC small generative LLM relation setting."
---

# Query Answer: RA-HMD-Inspired IHC Relation Adaptation

## Question

How should the method from [[081-mei-2025-robust-adaptation-of-large-multimodal-models-for-retrieval-augmented-hateful-meme-detection]] be used in the current completed-IHC setting?

## Promotion Rationale

This answer has durable value because RA-HMD is the closest wiki paper for retrieval-augmented robust adaptation of a generative model. The current project should transfer its adaptation structure, not its multimodal image pipeline.

## Short Answer

Use RA-HMD as a blueprint for a two-stage retrieval-augmented relation adapter over candidate-level IHC instances:

```text
Stage 1:
  small generative LLM + relation projection head
  optimize JSON generation and relation classification together

Stage 2:
  freeze the LLM adapter
  optimize retrieval-aligned relation embeddings with contrastive hard neighbors

Inference:
  primary mode: generate compact relation JSON
  robust mode: retrieval-augmented relation KNN or JSON/KNN ensemble
```

The direct transfer is not image-text multimodal modeling. The transfer is: keep the generative model's structured-output ability, add a retrieval/classification representation path, separate task adaptation from retrieval alignment, and evaluate whether retrieval helps target-present benign and cross-split robustness more than in-context examples.

## Evidence

- [[081-mei-2025-robust-adaptation-of-large-multimodal-models-for-retrieval-augmented-hateful-meme-detection]] proposes RA-HMD with an added projection MLP, a classification head, two-stage fine-tuning, FAISS retrieval, contrastive training, and retrieval-augmented KNN classification.
- RA-HMD stage 1 jointly optimizes language modeling and logistic-regression classification losses, preserving generation while adapting representations.
- RA-HMD stage 2 freezes the LMM and trains the projection/classifier with contrastive loss plus classification loss, using retrieved same-label positives and opposite-label hard negatives.
- RA-HMD uses retrieval-augmented KNN classification for out-of-domain settings and reports that it uses examples more effectively than ordinary few-shot in-context learning.
- The wiki's publication-checked metrics matrix records that RA-HMD improves Qwen2-VL-7B supervised hateful-meme performance over SFT across the checked table rows, and that RA-HMD+RKC is the low-resource/out-of-domain inference mode.
- [[multimodal-inspired-ihc-relation-methods-2026-06-05]] and [[ihc-completed-small-llm-innovation-ideas-2026-06-05]] already constrain the local version: no dataset expansion, small generative LLMs, candidate-level views, statement-free inference, retrieval as support/loss/evaluation rather than synthetic data.

## IHC Mapping

### Inputs

Use only the existing completed artifact:

```text
xu-l20:/data/chenjt/hate/DATA/llm_restructed/IHC_target_v1
```

Reshape rows into candidate-level instances:

```text
{
  "row_id": "...",
  "split": "train" | "valid" | "test",
  "text": "...",
  "candidate_target": "...",
  "relation_state": "attacked" | "mentioned_not_attacked" | "not_a_candidate_target",
  "target_status": "...",
  "target_source": "...",
  "statement_condition": "none" | "text_only" | "text_label" | "text_label_target",
  "statement": "optional training-only weak view"
}
```

Do not create new labeled samples. Multiple candidate instances from one row are a view over the same row and must be aggregated back to the original row for final evaluation.

### Architecture

Replace RA-HMD's multimodal LMM with a small text generative LLM:

```text
backbone: Qwen3-4B / Qwen3-8B / Qwen2.5-7B / Mistral-7B
generation head: compact relation JSON
projection head: MLP(last_hidden_state) -> g_i
relation head: 3-way classifier over g_i
retrieval index: FAISS over g_i for train candidate instances
```

The relation head is an auxiliary adaptation path. The final paper should compare three inference modes, mirroring RA-HMD:

```text
LMH-style: JSON generation only
LRC-style: relation head over g_i
RKC-style: retrieval-augmented relation KNN over g_i
```

### Stage 1: JSON + Relation-Head QLoRA

Train the small LLM with QLoRA:

```text
L_stage1 = L_json + alpha * L_rel
```

Where:

- `L_json` trains the model to output constrained relation JSON.
- `L_rel` trains the projection and relation head from the final hidden state.
- The output should be compact:

```json
{"relation_state":"attacked","evidence_cue":"...","flags":[]}
```

This stage adapts the model to the IHC relation task while preserving structured generation. Do not include retrieved neighbors in the prompt for the first baseline.

### Stage 2: Retrieval-Aligned Relation Tuning

Freeze the LLM and QLoRA adapter. Train only the MLP projection and relation head:

```text
L_stage2 = L_rel + beta * L_contrast
```

Build retrieval positives and hard negatives from existing train instances:

| Anchor | Positive | Hard Negative |
|---|---|---|
| attacked candidate | same relation, semantically close | same target or similar text but `mentioned_not_attacked` |
| mentioned_not_attacked candidate | same relation, semantically close | same target but `attacked` |
| no-target / forced candidate | same invalid relation | similar text with valid target relation |
| implicit target | same relation or same implicit flag | explicit target shortcut neighbor |

This is the direct RA-HMD transfer: stage 2 makes the hidden representation useful for retrieval and robust classification without further changing the generative model.

### Inference Modes

Evaluate all three modes:

1. `JSON`: generate relation JSON from `text + candidate_target`.
2. `REL_HEAD`: classify relation from `g_i`.
3. `RKC`: retrieve top-K training instances and use similarity-weighted relation voting.

Optional ensemble:

```text
p_final = lambda * p_json + (1 - lambda) * p_rkc
```

But keep the first paper's interpretation simple: if RKC helps mainly on target-present benign slices or cross-dataset transfer, present it as a robustness mode, not as the default classifier.

## Evaluation

Report:

- row-level Macro F1;
- candidate relation Macro F1;
- target-present not-toxic false-positive rate;
- toxic target-present false-negative rate;
- JSON validity and schema repair rate;
- RKC top-K ablation, especially K = 1, 5, 10, 20;
- target shuffle, target mask, and target replacement sensitivity;
- performance on `implicit_target`, `uncertain`, and `lexicon_match` versus `llm_unmatched_extraction`;
- comparison of `JSON`, `REL_HEAD`, and `RKC`;
- optional IHC-to-SBIC and SBIC-to-IHC transfer when SBIC relation views are ready.

The RA-HMD paper found that more in-context examples do not necessarily help, while retrieval KNN can use examples more effectively. The local version should therefore compare:

```text
few-shot prompt support
vs
RKC over relation embeddings
```

This is a clean and publishable transfer of the RA-HMD insight.

## What Not To Transfer

- Do not use a large multimodal architecture or image pipeline.
- Do not add external meme examples or synthetic rows.
- Do not use retrieval as a way to insert extra labels into the dataset.
- Do not make rationale generation the main output.
- Do not merge stage 1 and stage 2 before validating the staged version; RA-HMD's own ablation argues that staged separation matters.

## Minimal Experiment Sequence

1. Build `ihc_relation_rahmd_view_v1` from `IHC_target_v1`.
2. Train `JSON` baseline with Qwen3-4B.
3. Add MLP relation head and run stage-1 joint `L_json + L_rel`.
4. Freeze the LLM and run stage-2 `L_rel + L_contrast` with FAISS hard-neighbor mining.
5. Evaluate `JSON`, `REL_HEAD`, and `RKC` on the normal test set and target-present diagnostic slices.
6. Repeat the best configuration with Qwen3-8B or Qwen2.5-7B.
7. Only after IHC works, test SBIC support or transfer.

## Chain Check

- Input: RA-HMD source page and PDF method sections, existing IHC completed artifacts, and current small-LLM/no-augmentation constraints.
- Processing flow: map RA-HMD's LMM backbone, MLP projection, classifier head, two-stage training, contrastive retrieval, and RKC inference into candidate-target relation modeling.
- State changes: no raw files, remote datasets, or model outputs are modified.
- Output: a concrete RA-HMD-inspired training and evaluation plan for IHC.
- Upstream impact: requires a candidate-level relation view builder, FAISS index builder, and training script changes for an MLP relation head.
- Downstream impact: final claims should be about robust relation grounding and retrieval effectiveness, not generic hateful meme adaptation.
