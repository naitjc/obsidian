---
created: 2026-06-18
updated: 2026-06-18
tags: [query-answer, research-planning, hate-speech, ihc, llm, ideation, transfer-screening]
sources: []
promotion_reason: "Durable transfer-screening report for mining generative-LLM mechanisms across CS fields and mapping them to the current IHC target-relation hate-speech task."
---

# Transfer Idea Screening: Generative LLM Mechanisms for IHC Hate Speech Detection

## Screening Purpose

This page screens current generative-LLM research ideas from NLP, information extraction, retrieval, evaluation, agents, weak supervision, safety, software-style tool use, and bias testing for transfer value into the current IHC/SBIC-style hate speech task.

The local task assumption is:

- Core task: text-first implicit hate speech detection, with IHC as the immediate anchor and SBIC/cross-dataset transfer as later validation.
- Current bottleneck: target information is useful but can become a shortcut when row-level targets are fed directly; the safer formulation is candidate-target relation grounding.
- Useful LLM advantage: generation should produce structured semantic objects, candidate evidence, critique, verification actions, preference signals, or hard diagnostic cases, not merely longer explanations.
- Primary metric boundary: keep Macro-F1 as the main row-level metric, but require relation F1, target-present benign false-positive rate, toxic target-present false-negative rate, target shuffle/mask sensitivity, evidence deletion, JSON validity, and uncertainty/action rate where relevant.

## Research Profile

| Field | Value |
|---|---|
| Target tasks | IHC/SBIC implicit hate detection; candidate-target relation classification; evidence and definition-controlled moderation. |
| Prefer | Structured outputs, relation/evidence grounding, selective retrieval, uncertainty gates, compact verifiers, weak-label auditing, hard-slice evaluation, prompt/pipeline optimization tied to diagnostics. |
| Downweight | Generic "use CoT" ideas, all-sample retrieval prompting, bulk synthetic row generation as the main contribution, large unbounded knowledge graphs, free-form explanations without fidelity checks, papers that only show LLMs can classify hate speech. |
| Positive keywords | structured output, information extraction, target span, relation extraction, RAG, self-reflection, verifier, uncertainty, abstention, LLM annotation, weak supervision, DPO, red teaming, bias test generation, explanation reward model. |
| Negative keywords | survey-only, benchmark-only, leaderboard-only, generic bigger-model comparison, unrelated multimodal architecture with no transferable mechanism. |
| Scoring dimensions | transferability to target-relation grounding; use of generative LLM strengths; implementation feasibility with 4B-8B models; evaluation value; shortcut/leakage risk. |

## Candidate Pool

- Source of candidate metadata: local wiki pages plus web search over arXiv, ACL Anthology, OpenReview, NeurIPS proceedings, ACM/IEEE/Springer/PeerJ pages, and official paper pages on 2026-06-18.
- Inclusion boundary: papers whose core mechanism can be translated into an input-process-state-output path for the current hate-speech task.
- Exclusion boundary: papers that only recommend larger LLMs, only report zero-shot/few-shot hate classification, or require data/modalities outside the current text-first task before a relation baseline is validated.
- Deduplication rule: local anchors already in the vault, such as PIC, HateXScore, HARM, Target Span Detection, community-driven agents, DuPL, ReAct, and RA-HMD-related retrieval are marked as "local anchor"; external papers are kept as reading candidates unless already represented by a local source page.

## Screening Rules

- Each idea below includes a fit check before the proposed transfer.
- "Pass" means the mechanism can be evaluated under the current IHC constraints.
- "Conditional" means useful only as a diagnostic, auxiliary loss, or later-stage ablation.
- "Reject as main path" means do not make it the headline method even if it may be useful for analysis.

## P0 Shortlist

These are the strongest candidates after checking the local task path.

1. Candidate-target relation JSON generation with constrained outputs.
2. Evidence-cue faithfulness testing using deletion and relation consistency.
3. Selective ReAct/Self-RAG verifier triggered by uncertainty and target-present hard cases.
4. Retrieval as same-target opposite-relation memory, trained to ignore distractors.
5. Pragmatic/latent-component decomposition before final relation verdict.
6. Weak LLM relation labeling with manual audit, reliability weights, and active selection.
7. Prompt/pipeline optimization against diagnostic metrics, not generic accuracy.
8. Bias/red-team test generation for target identity, target presence, quotation, and counterspeech.
9. Preference optimization over structured outputs, using faithful relation/evidence preference pairs.
10. Distillation of compact teacher traces into small generative LLMs without long CoT at inference.

## Screened Ideas

### 1. Candidate-Target Relation JSON SFT

- Fit check: Pass. It directly matches the local need to stop using `target` as a row-level shortcut and instead model `(text, candidate_target) -> relation_state`.
- Source mechanism: Unified IE and instruction-tuned IE show how generative models can emit schema-bound structures rather than flat labels: [UIE](https://arxiv.org/abs/2203.12277), [USM](https://arxiv.org/abs/2301.03282), [InstructUIE](https://arxiv.org/abs/2304.08085), and [CodeIE](https://aclanthology.org/2023.acl-long.855/).
- Transfer: fine-tune Qwen/Mistral to emit compact JSON with `relation_state`, `candidate_target`, `evidence_cue`, and `flags`.
- Minimal validation: JSON validity, relation Macro-F1, row Macro-F1 derived from attacked candidates, target-present benign false-positive rate.
- Risk: relation labels can still collapse to row labels unless candidate construction and relation evaluation are separated.

### 2. Code-Style or Schema-First Output Formatting

- Fit check: Pass. The current task needs reliable structured fields more than fluent explanations.
- Source mechanism: [CodeIE](https://arxiv.org/abs/2305.05711) recasts extraction outputs as code-like structures; structured IE papers use schema prompts.
- Transfer: represent outputs as JSON or Python-literal-style records; use strict parsers and automatic repair only for syntax, not semantics.
- Minimal validation: parse failure rate, repair rate, field-level exact match, and whether repairs change labels.
- Risk: constrained formatting can create false confidence; semantic errors still require evidence checks.

### 3. Definition-Frame Relation Probing

- Fit check: Pass. Hate labels shift with policy and cultural definitions; the local relation classifier should expose this rather than hide it.
- Source mechanism: Constitutional AI uses explicit rule lists for critique/revision and AI feedback [Bai et al. 2022](https://arxiv.org/abs/2212.08073); local hate-definition papers already show prompt sensitivity.
- Transfer: add compact definition frames such as `protected_group_hate`, `broader_group_abuse`, or `platform_policy_harm`, then compare relation-state stability.
- Minimal validation: definition-swap rate, changed false positives on target-present benign rows, changed false negatives on implicit toxic rows.
- Risk: do not relabel the dataset by prompt; treat this as probing unless manually audited.

### 4. Evidence-Cue Faithfulness Tests

- Fit check: Pass. Explanations are valuable only if tied to target and harmful expression.
- Source mechanism: local anchors [HateXScore](https://arxiv.org/abs/2601.13547) and [HARM](https://aclanthology.org/2026.findings-eacl.230/) evaluate hate-explanation quality beyond accuracy.
- Transfer: require an evidence cue and test whether deleting it lowers `attacked` confidence; test target replacement and statement mismatch.
- Minimal validation: evidence deletion sensitivity, protected-group identification consistency, conclusion-evidence logical consistency.
- Risk: a short evidence cue is safer than long free-form rationale; do not claim explanation faithfulness unless deletion tests pass.

### 5. Pragmatic Inference Chain as Compact Fields

- Fit check: Pass, but only if converted to structured fields. The current task needs implicit meaning recovery, not open-ended CoT.
- Source mechanism: [PIC](https://aclanthology.org/2025.emnlp-main.296/) improves LLM reasoning for authentic implicit toxic language by using pragmatic inference steps.
- Transfer: map PIC-like reasoning into fields: literal content, implied stereotype, target candidate, harmful implication, relation state.
- Minimal validation: improvement on implicit-toxic false negatives and coded-language slices.
- Risk: long reasoning may leak label words or become unfaithful; keep inference fields short and auditable.

### 6. Latent Hate Component Mining Before Verdict

- Fit check: Pass. It matches the need to separate target, cue, implication, and verdict.
- Source mechanism: local DuPL anchor [Rethinking Implicit Hate Speech Detection](https://dl.acm.org/doi/10.1145/3774904.3792159) mines latent hate components and then deliberates over them.
- Transfer: stage 1 extracts components; stage 2 classifies target relation using extracted components plus original text.
- Minimal validation: component recall on false negatives, component noise rate, relation F1 with and without components.
- Risk: component generation can become another weak-label source; audit a subset.

### 7. Selective ReAct Relation Verifier

- Fit check: Pass if gated. Always-on agentic reasoning is too costly and locally risky because all-sample retrieval previously hurt recall.
- Source mechanism: [ReAct](https://openreview.net/forum?id=WE_vluYUL-X) interleaves reasoning, actions, and observations; local ReAct page already anchors this in the vault.
- Transfer: base classifier first; only hard cases trigger actions: retrieve same-target neighbors, extract evidence, check definition, or request community context.
- Minimal validation: trigger rate, baseline-correct-to-verifier-wrong conversions, false-negative corrections, action ablations.
- Risk: loops and noisy retrieval; cap actions and make every action auditable.

### 8. Toolformer-Style Action Selection

- Fit check: Conditional. Useful as a design pattern, not necessary as full self-supervised tool training.
- Source mechanism: [Toolformer](https://arxiv.org/abs/2302.04761) trains LMs to decide when and how to call APIs.
- Transfer: a small controller predicts whether to call target lexicon, retrieved examples, definition frame, translation, or evidence checker.
- Minimal validation: compare fixed-action, no-action, and learned-action policies on hard slices.
- Risk: overengineering before the relation baseline works.

### 9. Self-RAG / Adaptive-RAG Retrieval Gating

- Fit check: Pass. It directly addresses the local failure mode of indiscriminate retrieval.
- Source mechanism: [Self-RAG](https://arxiv.org/abs/2310.11511) retrieves and critiques on demand; [Adaptive-RAG](https://arxiv.org/abs/2403.14403) chooses retrieval strategy by query complexity.
- Transfer: retrieve only for uncertain, target-present benign, implicit, counterspeech, or definition-sensitive rows.
- Minimal validation: retrieval-trigger precision, toxic recall, target-present benign false-positive rate, and retrieval ablations.
- Risk: retrieval can suppress toxic recall if injected for easy cases.

### 10. RAFT-Style Distractor-Aware Retrieval Training

- Fit check: Pass. It trains the model not to overuse misleading retrieved examples.
- Source mechanism: [RAFT](https://arxiv.org/abs/2403.10131) fine-tunes models to answer with retrieved documents while ignoring distractors.
- Transfer: train relation verifier with same-target attacked, same-target benign, and irrelevant target distractors; reward use of correct support only.
- Minimal validation: distractor sensitivity and same-target opposite-relation accuracy.
- Risk: if retrieval labels are weak, the model may learn support-example shortcuts.

### 11. Corrective RAG for Retrieval Quality Checks

- Fit check: Pass as a retrieval guard, not as a headline method.
- Source mechanism: [CRAG](https://arxiv.org/abs/2401.15884) adds a retrieval evaluator and correction path.
- Transfer: before showing support examples to the LLM, score whether retrieved examples match target, relation, and definition.
- Minimal validation: rate of rejected retrievals, downstream F1 after filtering, retrieved-neighbor audit.
- Risk: another evaluator can inherit the same bias; keep simple criteria first.

### 12. HyDE / Query2doc for Target-Relation Retrieval

- Fit check: Conditional. Useful for retrieval candidate discovery, but risky if generated pseudo-documents hallucinate harmful context.
- Source mechanism: [HyDE](https://arxiv.org/abs/2212.10496) and [Query2doc](https://arxiv.org/abs/2303.07678) generate hypothetical documents or pseudo-documents for retrieval.
- Transfer: generate a short hypothetical attacked/benign relation description from `(text, candidate_target)` and retrieve real training cases near that semantic pattern.
- Minimal validation: retrieval precision by relation state; compare with plain embedding retrieval.
- Risk: pseudo-doc can inject stereotypes; use it only to retrieve real rows, not as evidence.

### 13. FLARE-Style Forward-Looking Retrieval

- Fit check: Conditional. It is more useful for multi-step explanation generation than simple classification.
- Source mechanism: [FLARE](https://arxiv.org/abs/2305.06983) anticipates next generation and retrieves when low-confidence.
- Transfer: if the model is generating a structured explanation, retrieve only when the next field is uncertain, e.g. target or evidence.
- Minimal validation: field-level uncertainty-triggered retrieval accuracy.
- Risk: not needed for the first compact JSON classifier.

### 14. RAPTOR / GraphRAG for Target-Context Memory

- Fit check: Conditional. Useful as a later index, not first model.
- Source mechanism: [RAPTOR](https://arxiv.org/abs/2401.18059) retrieves over recursive summaries; [GraphRAG](https://arxiv.org/abs/2404.16130) builds graph/community summaries for global sensemaking.
- Transfer: build a target-alias/context graph from existing target lexicon, statements, evidence cues, and relation outcomes.
- Minimal validation: retrieval improves only on cross-target or definition-sensitive cases.
- Risk: a full graph can distract from the relation-task contribution.

### 15. Self-Consistency Over Structured Relation Outputs

- Fit check: Pass if used for uncertainty rather than majority-vote laundering.
- Source mechanism: [Self-consistency](https://arxiv.org/abs/2203.11171) samples multiple reasoning paths and aggregates consistent answers.
- Transfer: sample multiple JSON outputs; use semantic disagreement over relation/evidence/target as an uncertainty score.
- Minimal validation: uncertainty AUC for error prediction, abstention curves, manual-audit precision.
- Risk: majority vote can amplify systematic bias.

### 16. Semantic Uncertainty and SelfCheck for Relation Reliability

- Fit check: Pass. The task has many ambiguous cases; uncertainty should be explicit.
- Source mechanism: [SelfCheckGPT](https://arxiv.org/abs/2303.08896) checks consistency across samples; [semantic uncertainty](https://www.nature.com/articles/s41586-024-07421-0) groups semantically equivalent answers before estimating uncertainty.
- Transfer: cluster sampled relation explanations; high semantic spread becomes `uncertain` or triggers verifier actions.
- Minimal validation: calibration curves, abstention-vs-F1 tradeoff, hard-slice error detection.
- Risk: uncertainty is not ground truth; use it to route audit, not to change labels silently.

### 17. Abstention as a First-Class Output

- Fit check: Pass. The local schema already needs uncertainty flags.
- Source mechanism: [Know Your Limits](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00754/131566/Know-Your-Limits-A-Survey-of-Abstention-in-Large) surveys LLM abstention.
- Transfer: allow `uncertain_relation` or `needs_context` alongside relation state; evaluate selective prediction.
- Minimal validation: coverage-risk curve and manual-audit usefulness.
- Risk: safety-aligned models may over-abstain on sensitive targets.

### 18. Self-Refine for Invalid or Contradictory Outputs

- Fit check: Conditional. Useful for structured-output repair and contradiction checks, not for changing labels repeatedly.
- Source mechanism: [Self-Refine](https://arxiv.org/abs/2303.17651) iteratively critiques and revises outputs.
- Transfer: generate JSON, critique for missing target/evidence/definition contradictions, revise once.
- Minimal validation: syntax repair rate, contradiction reduction, whether revisions improve or degrade label accuracy.
- Risk: self-refinement can make outputs more plausible while less faithful.

### 19. Reflexion Memory for Error Taxonomy

- Fit check: Conditional. Good for experiment workflow and verifier lessons, less direct as model method.
- Source mechanism: [Reflexion](https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) stores verbal feedback from previous trials.
- Transfer: maintain an error-memory bank of false-positive/false-negative patterns and use it to select hard cases or update prompts.
- Minimal validation: before/after prompt or verifier performance on held-out hard slices.
- Risk: memory contamination if test errors are reused for training.

### 20. Tree/Graph of Thoughts for Competing Interpretations

- Fit check: Conditional. Useful only on ambiguous cases where multiple interpretations exist.
- Source mechanism: [Tree of Thoughts](https://arxiv.org/abs/2305.10601) and [Graph of Thoughts](https://arxiv.org/abs/2308.09687) explore and combine candidate reasoning paths.
- Transfer: generate competing interpretations: attack, benign mention, quote/counterspeech, stereotype implication; score each against evidence.
- Minimal validation: ambiguous slice accuracy and cost per corrected case.
- Risk: too expensive and hard to audit for normal rows.

### 21. Multi-Agent Debate for Relation Ambiguity

- Fit check: Conditional. Stronger as a verifier than as a classifier.
- Source mechanism: [multi-agent debate](https://arxiv.org/abs/2305.14325) and [Debate-to-Detect](https://aclanthology.org/2025.emnlp-main.764/) use adversarial roles to improve reasoning and misinformation detection.
- Transfer: one agent argues `attacked`, one argues `mentioned_not_attacked`, judge must cite evidence and target relation.
- Minimal validation: correction rate on ambiguous hard cases, judge consistency, token cost.
- Risk: debate over the whole post may become generic; restrict debate to candidate relation.

### 22. Community-Agent Consultation

- Fit check: Conditional. Relevant for culturally situated implicit hate, but must not replace relation labels.
- Source mechanism: local anchor [community-driven multi-agent IHS detection](https://arxiv.org/abs/2601.09342).
- Transfer: trigger community-context lookup only for uncertain implicit cases involving identity-specific coded language.
- Minimal validation: performance by target group, balanced accuracy, and false-positive audit.
- Risk: persona/community agents can import stereotypes; keep them as consultation evidence, not final authority.

### 23. Persona-Infused Sensitivity Analysis

- Fit check: Conditional. Useful to study annotator/identity sensitivity, not to personalize final moderation labels.
- Source mechanism: [Persona-Infused LLMs for Human-Centric Hate Speech Detection](https://arxiv.org/html/2510.19331v1) studies persona effects on hate sensitivity.
- Transfer: run persona perturbation as an analysis layer: which examples flip under victim/community/moderator personas?
- Minimal validation: flip-rate by target and relation state.
- Risk: persona simulation is not demographic truth; report as sensitivity, not gold.

### 24. LLM Annotation With Active Selection

- Fit check: Pass if labels are weak and audited. This fits relation-label bootstrapping.
- Source mechanism: [LLMs as Annotators](https://arxiv.org/abs/2306.15766), [ChatGPT text annotation](https://arxiv.org/abs/2303.15056), and [LLM annotation survey](https://arxiv.org/abs/2402.13446).
- Transfer: use LLMs to weak-label relation/evidence only for selected uncertain or high-value rows; audit a stratified subset.
- Minimal validation: weak-label precision/recall against manual audit and downstream gain over no weak labels.
- Risk: LLM annotator bias is severe in hate speech; never treat weak labels as final source claims.

### 25. Programmatic Weak Supervision Plus LLM Labeling Functions

- Fit check: Pass. Relation labels can combine lexicon, target span, intent cue, counterspeech cue, and LLM votes.
- Source mechanism: [programmatic weak supervision survey](https://arxiv.org/abs/2202.05433) and LLM-assisted labeling-function generation papers such as [LLM-assisted LF generation](https://arxiv.org/abs/2408.16173).
- Transfer: create labeling functions for relation states; let LLM propose candidate rules, then human-review them.
- Minimal validation: labeling-function conflict/coverage, noise-aware training, audit precision.
- Risk: treating missing relation as negative is dangerous; use abstain/unknown.

### 26. Reliability-Weighted Weak Supervision

- Fit check: Pass. Local completed statements/targets have different provenance and artifact risk.
- Source mechanism: reliability-aware weak-to-strong work reweights weak signals by reliability [arXiv 2406.19032](https://arxiv.org/abs/2406.19032).
- Transfer: weight relation labels by source: native target, LLM target, lexical match, uncertain flag, statement artifact flag.
- Minimal validation: performance and calibration by provenance group.
- Risk: wrong reliability weights can hide data issues.

### 27. Preference Optimization for Faithful Relation Outputs

- Fit check: Pass as a later post-training layer.
- Source mechanism: [DPO](https://arxiv.org/abs/2305.18290), [RLAIF](https://arxiv.org/abs/2309.00267), and Constitutional AI convert preferences or principles into model behavior.
- Transfer: build preference pairs: faithful target/evidence/relation JSON preferred over shortcut target-presence verdicts.
- Minimal validation: pairwise preference accuracy, hard-slice F1, evidence faithfulness after DPO.
- Risk: preference data construction is the real contribution; noisy preferences can overfit style.

### 28. AI-Critique and Revision Pairs From a Moderation Constitution

- Fit check: Conditional. Useful for training output style and policy consistency, not as standalone evidence.
- Source mechanism: [Constitutional AI](https://arxiv.org/abs/2212.08073) uses principle-guided critique and revision.
- Transfer: define moderation principles: target must be policy-relevant, evidence must attack target, quotation/counterspeech requires context flag.
- Minimal validation: policy-violation reduction in generated JSON/explanations.
- Risk: principles encode the definition; keep definition frames explicit.

### 29. Distilling Step-by-Step Into Small Models

- Fit check: Pass. The user line favors small generative LLMs and compact outputs.
- Source mechanism: [Distilling step-by-step](https://arxiv.org/abs/2305.02301) trains smaller models with LLM rationales; [Orca](https://arxiv.org/abs/2306.02707) learns from rich explanation traces.
- Transfer: use stronger teacher outputs as structured supervision, then train Qwen3-4B/8B to emit short fields without long CoT at inference.
- Minimal validation: compare label-only SFT, relation JSON SFT, and relation-plus-teacher-field SFT.
- Risk: teacher traces can teach style instead of reasoning; evaluate with evidence deletion.

### 30. STaR-Style Self-Bootstrapping

- Fit check: Conditional. It can improve reasoning fields but risks reinforcing shortcuts.
- Source mechanism: [STaR](https://arxiv.org/abs/2203.14465) iteratively trains on rationales that lead to correct answers.
- Transfer: keep only generated relation explanations that pass label, evidence, and consistency checks, then iterate.
- Minimal validation: held-out hard-slice improvement without shortcut-gap increase.
- Risk: if "correct" means only row label, it will amplify target shortcuts.

### 31. Quality-First Data Curation Instead of Bulk Synthetic Expansion

- Fit check: Pass as a principle. It matches the local need to avoid another uncontrolled augmentation loop.
- Source mechanism: [LIMA](https://arxiv.org/abs/2305.11206), [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644), and [Quality Matters](https://aclanthology.org/2024.emnlp-main.285/) support small, high-quality instruction or synthetic data over unvalidated volume.
- Transfer: create a small audited set of relation-format exemplars and counterexamples for prompt/SFT calibration.
- Minimal validation: few-shot exemplar set ablation and cross-slice performance.
- Risk: if used as new training data, document it as weak/audited auxiliary data, not dataset expansion.

### 32. Bias Test Case Generation

- Fit check: Pass. Bias/counterfactual testing is directly relevant to hate speech.
- Source mechanism: [BTC-SAM](https://aclanthology.org/2025.emnlp-main.763/) uses LLMs to generate rich bias test cases for sentiment models.
- Transfer: generate naturalistic target-swapped, relation-preserving, and relation-flipping examples for diagnostics: same sentence frame, different identity group, attacked vs mentioned.
- Minimal validation: identity bias gap, target-present benign false-positive rate, template diversity.
- Risk: generated hate examples are sensitive; store only approved diagnostic summaries unless release is reviewed.

### 33. Automated Red-Teaming Taxonomies

- Fit check: Pass as evaluation and hard-case discovery.
- Source mechanism: red-teaming surveys and frameworks such as [A Survey on Red Teaming for Generative Models](https://arxiv.org/html/2404.00629v1) and [Holistic Automated Red Teaming](https://aclanthology.org/2024.emnlp-main.760.pdf).
- Transfer: create a taxonomy of failure probes: coded hate, quotation, counterspeech, reclaimed slur, demographic dialect, target ambiguity, definition ambiguity.
- Minimal validation: per-probe failure table and regression checks across model variants.
- Risk: generated adversarial content must be handled under vault/publication boundaries.

### 34. Counterfactual and Variation-Theory Test Design

- Fit check: Pass. It operationalizes "same target, different relation" and "same relation, different target".
- Source mechanism: counterfactual augmentation and variation-theory papers use controlled variable changes to test conceptual understanding.
- Transfer: generate paired tests that vary one factor: target identity, harmful predicate, negation, quote, speaker stance, context.
- Minimal validation: pair consistency and relation flip accuracy.
- Risk: do not train on the test cases unless they are separated from evaluation.

### 35. Prompt Optimization Against Hate-Specific Diagnostics

- Fit check: Pass. Prompt fragility is known locally and in the literature.
- Source mechanism: [APE](https://arxiv.org/abs/2211.01910), [OPRO](https://arxiv.org/abs/2309.03409), [ProTeGi](https://aclanthology.org/2023.emnlp-main.494/), and [DSPy](https://arxiv.org/abs/2310.03714).
- Transfer: optimize relation-verifier prompts against a weighted metric: Macro-F1, toxic recall, target-present benign FPR, JSON validity, evidence consistency.
- Minimal validation: held-out prompt dev set and untouched test set.
- Risk: prompt search can overfit the dev slice; freeze prompts before final evaluation.

### 36. Declarative LLM Pipeline Compilation

- Fit check: Conditional. Useful if the pipeline has multiple modules.
- Source mechanism: [DSPy](https://openreview.net/forum?id=sY5N0zY5Od) compiles LM pipelines against metrics.
- Transfer: define modules for candidate extraction, relation classification, evidence checking, and verifier routing; compile prompts/demos against diagnostic metrics.
- Minimal validation: module-wise ablation and global pipeline score.
- Risk: adds framework complexity; start with scripts unless module count grows.

### 37. Program-Aided Evaluation and Validators

- Fit check: Pass for evaluation infrastructure, not model reasoning.
- Source mechanism: [PAL](https://arxiv.org/abs/2211.10435) and [Program of Thoughts](https://arxiv.org/abs/2211.12588) separate language reasoning from executable computation.
- Transfer: let the LLM generate fields; use deterministic code to derive row verdict, compute shortcut gaps, check schema constraints, and run perturbations.
- Minimal validation: reproducible evaluation scripts and mismatch reports.
- Risk: do not let executable validators encode the desired result.

### 38. Retrieval-Augmented Classification With Label-Space Selection

- Fit check: Conditional. Good when label schema expands to relation/intents.
- Source mechanism: many-label ICL and retrieval work uses retrieval to reduce label/example space, e.g. [ICL with many labels](https://aclanthology.org/2023.genbench-1.14/).
- Transfer: retrieve only relevant definition frames, target types, or relation examples for a candidate row.
- Minimal validation: label-space retrieval accuracy and relation F1.
- Risk: label retrieval can leak priors for identity groups.

### 39. Dynamic Background Context Generation

- Fit check: Conditional. Useful for implicit/coded language, dangerous if simply concatenated.
- Source mechanism: LLM-as-dynamic-knowledge-base work in hate detection, e.g. [context-aware implicit textual and multimodal HSD](https://research.vu.nl/en/publications/leveraging-llms-for-context-aware-implicit-textual-and-multimodal/).
- Transfer: generate short background only for named entities/coded phrases, then keep it as a separate evidence view with provenance.
- Minimal validation: context-use ablation and hallucinated-context audit.
- Risk: background generation can hallucinate stereotypes; never use it as gold evidence.

### 40. Stance/Intent-Slot Reframing

- Fit check: Pass. It is strongly aligned with target-relation modeling.
- Source mechanism: stance detection and PLEAD-style intent-slot work treat target and intent as structured elements rather than flat labels; local pages already anchor this line.
- Transfer: output `speaker_stance_to_target`, `harm_type`, `target_link`, and `evidence_span`.
- Minimal validation: relation-state performance by stance/intent type.
- Risk: too many slots can make annotation unreliable; keep core relation state first.

### 41. Sarcasm/Humor Incongruity as Implicit-Hate Signal

- Fit check: Conditional. Useful for implicit and coded cases, not all hate speech.
- Source mechanism: sarcasm/humor detection work uses incongruity, implied meaning, and surface-vs-intent gaps.
- Transfer: add optional fields `literal_reading`, `implied_reading`, and `incongruity_flag` for suspected ironic/coded rows.
- Minimal validation: implicit/sarcastic slice improvement and false-positive control.
- Risk: incongruity is not hate; it must connect to target harm.

### 42. Cross-Lingual Definition and Translation Probes

- Fit check: Conditional. Useful after English IHC relation baseline is stable.
- Source mechanism: multilingual prompting and cross-lingual hate papers show prompt and culture sensitivity; local sources already include multilingual LLM hate detection.
- Transfer: translate or paraphrase candidate rows under protected definitions; compare relation consistency and target recovery.
- Minimal validation: translation consistency and target/relation preservation.
- Risk: translation can erase slurs, dialect, and cultural cues.

## Rejected as Main Directions

- Bigger model comparison as the contribution: not enough; it does not solve target leakage or relation grounding.
- Free-form CoT for every row: too expensive, hard to audit, and likely unfaithful.
- Direct `text + target + statement -> class`: already locally risky because row-level target/statement fields can become shortcut features.
- Bulk synthetic hate data generation: useful only as carefully separated diagnostic or weak auxiliary data, not the main paper under current constraints.
- Full external knowledge graph before relation baseline: too much infrastructure before the core relation formulation is validated.
- All-sample retrieval prompting: local retrieval evidence already suggests this can hurt toxic recall.

## Most Concrete Experiment Package

### E1: Relation JSON Baseline

- Input: `text`, uniformly generated or existing candidate target, optional target type.
- Process: Qwen3-4B/8B or Mistral QLoRA emits JSON relation fields.
- State change: row-level `target` becomes a candidate in a relation decision.
- Output: `relation_state`, `evidence_cue`, `flags`.
- Evaluation: row Macro-F1, relation Macro-F1, JSON validity, target-present benign FPR, toxic target-present FNR, target shuffle/mask/replacement.

### E2: Selective Verifier

- Input: E1 prediction plus uncertainty/error-slice trigger.
- Process: only triggered rows call retrieval, evidence check, definition frame, or community/context action.
- State change: expensive LLM capabilities become conditional actions.
- Output: revised JSON or abstention.
- Evaluation: trigger rate, corrected false negatives, induced false positives, cost, action ablation.

### E3: Retrieval and Preference Training

- Input: same-target attacked/benign neighbors and distractors.
- Process: train or prompt model to use correct support and ignore distractors; optionally DPO over faithful vs shortcut outputs.
- State change: retrieval becomes controlled support, not a context dump.
- Output: relation JSON with support attribution.
- Evaluation: same-target opposite-relation slice, distractor sensitivity, evidence deletion.

### E4: Bias and Red-Team Diagnostic Suite

- Input: LLM-generated controlled test pairs reviewed under sensitive-content boundaries.
- Process: vary target identity, relation, quote/counterspeech, negation, definition frame.
- State change: evaluation expands from aggregate F1 to shortcut and fairness slices.
- Output: diagnostic report, not training data by default.
- Evaluation: identity bias gap, pair consistency, relation flip accuracy.

## Promotion Candidates

- Candidate papers to ingest later if this line proceeds: APE, DSPy, Self-RAG, RAFT, HyDE, BTC-SAM, DPO, Distilling step-by-step, InstructUIE, CodeIE.
- Concept pages to update later: [[leakage-resistant-target-relation-modeling]], [[ihc-completed-small-llm-innovation-ideas-2026-06-05]], [[target-relation-grounding-literature-map]], [[llm-reasoning]], [[retrieval-augmented-generation]], [[explainable-hate-speech-detection]].
- Experiment plan to draft: a relation-JSON plus selective-verifier experiment plan under `experiments/hate/notes/` or `experiments/server-sync/staging/` only after the first implementation scope is chosen.

## Chain Check

- Input: local wiki routing, target-relation pages, completed-IHC small-LLM plan, RA-HMD retrieval lineage, hate-speech final synthesis, and external paper search results.
- Processing flow: screen by transferable mechanism rather than title similarity; require each idea to map onto input, process, state change, output, and measurable diagnostic.
- State changes: this page creates a screening report only; it does not ingest new PDFs, edit `raw/`, change experiment data, or promote external papers into source-grounded claims.
- Output: a transfer-oriented reading and experiment-idea queue with local fit checks.
- Upstream impact: future idea selection should prefer relation JSON, selective verifier, retrieval gating, weak-label auditing, and diagnostic generation over generic LLM classification.
- Downstream impact: any implemented method must separate row Macro-F1 from relation grounding, shortcut diagnostics, evidence faithfulness, uncertainty, and retrieval/action ablations.
- Assumptions or unverified premises: external papers were screened from abstracts/official pages and not deep-ingested unless already represented in the vault; exact numerical claims from external papers remain unverified for publication use.
