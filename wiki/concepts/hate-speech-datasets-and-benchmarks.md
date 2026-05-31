---
created: 2026-04-23
updated: 2026-05-27
tags: [concept, hate-speech, datasets]
sources:
  - raw/sources/17745-13-21239-1-2-20210518.pdf
  - raw/sources/2021.naacl-demos.17.pdf
  - raw/sources/2022.tacl-1.82.pdf
  - raw/sources/2025.coling-main.446.pdf
  - raw/sources/2025.emnlp-main.703.pdf
  - raw/sources/2025.woah-1.21.pdf
  - raw/sources/2025.woah-1.45.pdf
  - raw/sources/1804.04257v1.pdf
  - raw/sources/N19-1144.pdf
  - raw/sources/W19-3504.pdf
  - raw/sources/2020.coling-main.552.pdf
  - raw/sources/2022.naacl-main.433.pdf
  - raw/sources/2023.acl-short.66.pdf
  - raw/sources/2023.eacl-main.244.pdf
  - raw/sources/2026.findings-eacl.230.pdf
---

# Hate Speech Datasets and Benchmarks

## Common Benchmarks
- Latent Hatred
- ToxiGen
- ETHOS
- Hateful Memes
- ToxiCN
- HateXplain
- HateBRXplain
- Toxic Spans Detection / MUDES
- PLEAD
- U-PLEAD / TARGET
- Hate Lingo directed/generalized hate
- OLID
- AbuseAnalyzer
- Context-aware hate/counter-speech Reddit dataset
- TBO
- IHC / SBIC target-span settings
- SBIC-Explain / HARM explanation evaluation
- HateCheck / Learning from the Worst / Measuring Hate Speech for definition-prompt evaluation

## Notes
- Dataset shift remains a central challenge: models tuned on one source often degrade on new domains.
- Implicit hate benchmarks are harder due to annotation ambiguity and context requirements.
- Recent text-only benchmarks increasingly annotate rationales, spans, slots, definitions, or functional tests rather than only sentence-level labels.
- The target-relation line should distinguish post-level target categories from token-level target-expression links; see [[target-relation-grounding-literature-map]].

## Current Supplement Boundary for the IHC/SBIC Target-Relation Line

The current data-completion scope is restricted to IHC and SBIC. The immediate goal is not to add a third dataset or enlarge a mixed binary-classification training pool, but to make the two existing corpora support a leakage-controlled target-relation study. Target completion and relation labeling should be audited under a uniform candidate-construction protocol within these two datasets.

| Scope | Resource | Role in the Current Project | Boundary |
|---|---|---|---|
| Current completion corpus | IHC | Complete target candidates and relation states for toxic and not-toxic rows, with special attention to implicit targets and target-present benign cases. | Preserve native annotations; completed fields remain weak or audited additions, not replacements. |
| Current completion corpus | SBIC | Build the same normalized candidate/relation representation so it is comparable with IHC and can test whether conclusions generalize across the two corpora. | Map SBIC-native fields explicitly; do not silently treat its supervision as identical to IHC. |
| Future evaluation reference only | TBO, HateXplain, HateCheck, PLEAD, context-aware Reddit, Toxic Spans / MUDES | Retain as literature-backed options for later external evaluation, functional diagnostics, schema comparison, context testing, or evidence-span analysis. | They are outside the current data-completion scope and should not drive the first IHC/SBIC completion pipeline. |

### Deferred or Diagnostic-Only Resources

- OLID, AbuseAnalyzer, Hate Lingo, TBO, HateXplain, HateCheck, PLEAD, context-aware Reddit, and Toxic Spans / MUDES are not current completion targets. They remain possible later evaluation or comparison resources only if the paper claim needs them.
- Bulk generated augmentation should be deferred until the untouched-data and shortcut baselines are in place. [[174-casula-tonelli-2023-generation-based-data-augmentation-for-offensive-language-detection-is-it-worth-it]] shows that generated offensive-language data can have unreliable utility and bias effects.
- SBIC-Explain and HARM belong to the later `statement` or explanation-evaluation stage, not the first candidate-target classifier. [[176-puppi-vecchi-2026-harm-learning-hate-aware-reward-model-for-evaluating-natural-language-explanations-of-offensive-content]] motivates task-specific fidelity checks for generated explanations.

### Minimal Current Completion Package

For the first leakage-controlled study, the only datasets to supplement are:

1. IHC, with completed candidate targets and relation states for both toxic and not-toxic rows.
2. SBIC, with the same normalized output schema and an explicit mapping from its native annotation fields.

Within both datasets, completion should prioritize comparable examples for `attacked_target`, `mentioned_not_attacked`, `no_relevant_target`, and `uncertain_target`, with completion provenance and audit status retained. External datasets can be reconsidered at the evaluation-design stage; they are not required for the current supplement task.
