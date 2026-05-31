---
created: 2026-05-27
updated: 2026-05-27
tags: [query-answer, hate-speech, ihc, sbic, target-completion, missing-data, weak-supervision, synthetic-data, evaluation]
sources:
  - raw/sources/S18-2018.pdf
  - raw/sources/N19-1079.pdf
  - raw/sources/K19-1060.pdf
  - raw/sources/2021.acl-long.277.pdf
  - raw/sources/2023.eacl-main.244.pdf
  - raw/sources/2026.findings-eacl.230.pdf
promotion_reason: "Durable literature map for completing structurally missing target or explanation fields while validating fidelity, shortcut risk, and downstream utility."
---

# Literature Map: Missing Annotation Completion and Utility Validation

## Question

Which papers are most relevant when filling missing dataset fields so that completed values are compatible with the original data and usable in downstream modeling, especially for the current IHC/SBIC target-completion work?

## Scope and Interpretation

This page interprets the question around the current project: filling missing structured annotations such as `target`, relation state, or later `statement` / explanation fields in implicit hate speech corpora. This is not primarily numerical missing-value imputation.

For IHC, the current wiki evidence records that native `target` is present for toxic rows and absent for not-toxic rows. The missingness is therefore annotation-policy and class conditioned, not missing completely at random. Whether it should be formally modeled as MAR or MNAR depends on which observed variables and annotation process are included; it should not be asserted as MNAR without a specified probabilistic model. Practically, this means a completed field can easily leak the label unless its construction and use are controlled.

The central success criterion is not only whether filled values resemble observed targets. It is whether the completed annotation:

- represents the same semantic variable across toxic and non-toxic rows;
- supports `attacked` versus `mentioned_not_attacked` distinctions rather than target-presence shortcuts;
- remains reliable under manual audit and perturbation tests;
- improves or preserves performance on untouched real evaluation sets and cross-dataset tests.

## Deduplication Boundary

This reading list is filtered against the existing vault as of 2026-05-27. Papers already present in source pages, concept pages, or experiment-linked wiki discussion are intentionally excluded from the recommended list. Excluded direct anchors include `Social Bias Frames` / SBIC, `Latent Hatred` / IHC, PLEAD, Boudraa et al. (2025), `Hate Explained`, `HateCheck`, `Learning from the Worst` / DynaHate, `ToxiGen`, and U-PLEAD.

Those existing pages remain the local problem definition. The papers below are additions for learning how to handle incomplete annotations, false negatives caused by missing structure, and the reliability or utility of generated completion fields.

## New Priority Reading Route

| Priority | Paper Not Previously in This Vault | Why It Adds Value |
|---|---|---|
| 1 | [[171-jie-2019-better-modeling-of-incomplete-annotations-for-named-entity-recognition]] | Direct analogy for missing target spans: unannotated spans cannot safely be treated as negatives; proposes learning with incomplete token annotations. |
| 2 | [[172-mayhew-2019-named-entity-recognition-with-partially-annotated-training-data]] | Treats unannotated entities as possible false negatives and learns weights for partial supervision; relevant to generated candidate targets. |
| 3 | [[170-ning-2018-exploiting-partially-annotated-data-for-temporal-relation-extraction]] | Closest conceptual bridge from missing mentions to missing relations: incomplete relational annotation can still help under constrained bootstrapping. |
| 4 | Min et al. (2013), [Distant Supervision for Relation Extraction with an Incomplete Knowledge Base](https://aclanthology.org/N13-1095/) | Establishes the false-negative problem when absent relation evidence is wrongly treated as negative; motivates positive-unlabeled thinking for target relations. |
| 5 | [[173-xie-2021-revisiting-the-negative-data-of-distantly-supervised-relation-extraction]] | Uses positive-unlabeled relation extraction to address relations missing because the supervision source is incomplete. |
| 6 | [[174-casula-tonelli-2023-generation-based-data-augmentation-for-offensive-language-detection-is-it-worth-it]] | New domain-adjacent control paper: generated offensive-language data can yield unreliable gains and shift lexical bias. |
| 7 | [[176-puppi-vecchi-2026-harm-learning-hate-aware-reward-model-for-evaluating-natural-language-explanations-of-offensive-content]] | New direct addition for the planned `statement` stage: evaluates generated offensive-content explanations with a hate-aware reward model and human-validated SBIC-Explain. |

## New NLP Transfer Papers

### Missing Target Spans as Partial Sequence Annotation

- Jie et al. (2019) studies NER training data in which entity annotations are incomplete. For your target-completion layer, the key transfer is that an empty or absent target span must not automatically supervise `no target`; it may be an unlabeled candidate requiring separate audit or weak completion.
- Mayhew et al. (2019) studies the case where only a fraction of entities are tagged and other tokens default to non-entity. Their false-negative framing is directly useful for auditing IHC/SBIC candidate target recall and for weighting weak generated spans rather than declaring them gold.

### Missing Target Relations as Positive-Unlabeled Structure

- Ning et al. (2018) shows that partially annotated relations can still support extraction under constrained bootstrapping, while naive use of missing relations harms performance. This is relevant after candidate generation, when `candidate_target` must be paired with an `attacked` or `mentioned_not_attacked` relation.
- Min et al. (2013) argues that incomplete supervision sources create false-negative relations and models relation extraction from positive and unlabeled examples. This maps to the risk of treating target-empty benign or incompletely annotated rows as definitive absence.
- Xie et al. (2021) revisits negative data in relation extraction and applies a positive-unlabeled formulation to mitigate missing-relation false negatives. It is a concrete method family to consider if your relation labels remain incomplete after weak annotation.

### Generated Completion Usability and Explanation Validation

- Casula and Tonelli (2023) is useful because it is not a success-only augmentation story: its offensive-language setting directly warns that generated examples may unpredictably affect bias and effectiveness. Use it to justify comparing completed-data training against an untouched-data baseline and inspecting target-identity lexical effects.
- Puppi Vecchi et al. (2026), HARM, is the most direct new paper found for the later statement/explanation stage. It supports evaluating generated explanations with task-specific, human-grounded criteria rather than treating fluent generated text as validated annotation.

## New Missing-Data Foundations

These papers were also absent from the existing vault. They are methodological background, not direct replacements for NLP target-relation modeling.

| Paper | Contribution | Correct Use in This Project |
|---|---|---|
| Rubin (1976), [Inference and Missing Data](https://doi.org/10.1093/biomet/63.3.581) | Defines the missingness-assumption foundation used to reason about ignorable and non-ignorable missing data. | State the annotation process and avoid asserting MAR/MNAR without an explicit model. |
| van Buuren and Groothuis-Oudshoorn (2011), [mice: Multivariate Imputation by Chained Equations in R](https://www.jstatsoft.org/article/view/v045i03) | Practical multiple imputation and uncertainty handling. | Motivate keeping uncertainty or multiple plausible completions rather than one generated field as gold. |
| Stekhoven and Buhlmann (2012), [MissForest](https://doi.org/10.1093/bioinformatics/btr597) | Nonparametric imputation for mixed variables with error estimation. | A possible structured-metadata baseline, not a semantic target extractor. |
| Yoon et al. (2018), [GAIN](https://proceedings.mlr.press/v80/yoon18a.html) | Adversarial imputation conditioned on observed variables. | Reference conditional-distribution fit, while not confusing distribution fit with relation validity. |
| Mattei and Frellsen (2019), [MIWAE](https://proceedings.mlr.press/v97/mattei19a.html) | Deep generative missing-data modeling under MAR assumptions. | Reference generative imputation uncertainty; do not import its assumptions directly. |
| Ipsen et al. (2021), [not-MIWAE](https://openreview.net/forum?id=tu29GQT0JFy) | Deep generative modeling for not-missing-at-random data. | Useful when formalizing annotation-selection mechanisms, not proof that IHC is MNAR. |
| Du et al. (2024), [ReMasker](https://proceedings.iclr.cc/paper_files/paper/2024/hash/258d234a229d1612a565f9d9a63e3e80-Abstract-Conference.html) | Masked-autoencoder imputation evaluated for fidelity and utility. | Borrow the fidelity-plus-utility reporting distinction for completed annotation fields. |

## New Distribution and Counterfactual Evaluation Background

| Paper | Relevant Lesson | Appropriate Use Here |
|---|---|---|
| Xu et al. (2019), [Modeling Tabular Data using Conditional GAN](https://papers.nips.cc/paper/8953-modeling-tabular-data-using-conditional-gan) | Synthetic data should be judged conditionally and by downstream ML utility. | Evaluate target types conditioned on original labels and relation states. |
| Kotelnikov et al. (2023), [TabDDPM](https://proceedings.mlr.press/v202/kotelnikov23a.html) | Modern synthetic-data work reports ML efficiency, not just resemblance. | Support downstream utility reporting, secondary to semantic audit. |
| Kaushik et al. (2020), [Learning the Difference that Makes a Difference with Counterfactually-Augmented Data](https://openreview.net/forum?id=Sklgs0NFvr) | Controlled counterfactual edits expose spurious correlations. | Motivate same-target attacked/neutral contrasts and evidence perturbation tests. |

For the current project, a marginal match such as similar target-frequency histograms is insufficient. A filled dataset may match frequencies while still encoding `target exists -> toxic` or hallucinating relations in benign text.

## Method Selection for the Current Project

| Desired Step | Closest Reading | Minimal Correct Interpretation |
|---|---|---|
| Understand why fields are missing | Rubin; Jie et al.; Mayhew et al. | Treat absence as an annotation-process outcome and potential false negative, not as random blank data. |
| Fill candidate targets | Jie et al.; Mayhew et al. | Add weak target/span fields with provenance and uncertainty; preserve native labels. |
| Add relation states | Ning et al.; Min et al.; Xie et al. | Treat unattested candidate relations cautiously; consider partial or positive-unlabeled supervision. |
| Control target/expression combinations | Kaushik et al. | Use curated contrasts or controlled counterfactual cases; do not call them natural-distribution repairs. |
| Add statements/explanations | HARM | Keep generated explanations separate from native statements and validate fidelity with task-specific checks. |
| Establish usefulness | Casula and Tonelli; ReMasker | Evaluate real held-out utility and bias/shortcut behavior, not only fit to generated-field statistics. |

## Proposed Validation Checklist

### Input and Construction Controls

- Keep original IHC/SBIC labels and native annotations immutable; store completed fields as new weak-label columns with source, model/prompt version, confidence or uncertainty, and audit status.
- Build any lexicon, completion prompt calibration, or selector only from the training partition. Do not use validation/test target annotations to construct completions used for model development.
- Apply comparable candidate-target generation to toxic and non-toxic examples when evaluating a relation model; otherwise annotation source itself can reveal the label.

### Completion Quality

- Manually audit a stratified sample across label, split, target-present/absent status, explicit/implicit target, and completion source.
- Report target candidate precision/recall where native or audited target evidence exists.
- Report relation agreement separately for `attacked`, `mentioned_not_attacked`, `no_relevant_target`, and uncertain cases.
- For generated statements, evaluate faithfulness to text and fixed target/relation state rather than fluent wording alone.

### Distribution and Shortcut Checks

- Compare conditional distributions by class and target type, not only the overall target frequency.
- Measure a target-presence-only baseline; it should not solve the task after completion.
- Evaluate target shuffle, target mask, target replacement, evidence deletion, and same-target attacked/neutral contrast sets.
- Report target-present non-toxic false-positive rate as a primary diagnostic.

### Downstream Utility

- Train on completed training data but evaluate first on untouched real held-out data.
- Run IHC-to-SBIC and SBIC-to-IHC transfer when field mappings are explicit.
- Evaluate on functional or adversarial slices such as HateCheck and, if mapped carefully, DynaHate or ToxiGen.
- Compare against text-only, native-annotation-only where available, naive filled-target input, and relation-grounded alternatives.

## Reading Order

1. Use the existing local IHC/SBIC and target-completion pages only to define your active schema; they are excluded from this new reading list.
2. Read Jie et al. and Mayhew et al. first for missing target-span supervision.
3. Read Ning et al., Min et al., and Xie et al. for missing relation labels and positive-unlabeled formulations.
4. Read Casula and Tonelli plus Kaushik et al. to design augmentation and shortcut controls.
5. Read Rubin, GAIN, MIWAE/not-MIWAE, and ReMasker only to sharpen missingness and fidelity/utility reporting.
6. Read HARM before executing statement/explanation generation or adopting automatic explanation scores.

## Relation to Existing Wiki Pages

- Current completed-target execution evidence and boundaries: [[ihc-sbic-target-completion-layer]]
- Proposed model and evaluation plan: [[candidate-target-relation-grounding-experiment-plan-2026-05-18]]
- Target/relation task framing: [[target-relation-grounding-literature-map]]
- Existing comparison of LLM-added annotation fields: [[llm-augmentation-fields-in-related-papers]]
- General synthetic-data topic entry: [[synthetic-data-generation]]

## Claim Boundary

The papers above justify an evaluation protocol and a carefully governed completion layer. They do not yet establish that the current completed IHC targets match the original latent target distribution, nor that adding them improves a leakage-controlled classifier. Those are experiment questions requiring audited labels and untouched downstream evaluation.
