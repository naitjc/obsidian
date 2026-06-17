---
created: 2026-05-31
updated: 2026-06-17
tags: [query-answer, hate-speech, target-relation, structured-prediction, information-extraction, evaluation]
sources: []
promotion_reason: "Durable deduplicated reading route for the active IHC/SBIC target-relation grounding work, expanded into adjacent NLP extraction and moderation robustness methods."
---

# Query Answer: Recent NLP Reading Route for Target Grounding

## Question

Which NLP papers from ACL-family venues or arXiv are worth reading next, given the recent IHC/SBIC target-completion, leakage-resistant relation-grounding, span-extraction, and moderation-evaluation work? The route may extend beyond a single task, but it should exclude papers already represented in this vault.

## Promotion Rationale

This route has durable value because the active project now spans three linked problems: extracting candidate target and evidence spans, deciding whether a candidate is actually attacked, and evaluating whether a moderation model relies on semantic evidence rather than identity or annotation-source shortcuts.

## Deduplication Boundary

The recommended titles below were checked against `wiki/`, `experiments/`, `log.md`, and `raw/sources/` on 2026-05-31. They are not currently represented by local source pages or raw PDFs.

Existing local anchors are intentionally not repeated as recommendations. These include STATE ToxiCN, Boudraa et al. (2025), PLEAD and U-PLEAD, Target-Based Offensive Language Identification, HateXplain, HateCheck, HARM, Jie et al. (2019), Mayhew et al. (2019), Ning et al. (2018), and Xie et al. (2021).

## Priority Reading Route

### Read First: Directly Useful for the Active Project

| Paper | Venue | Why Read It Now |
|---|---|---|
| Jafari et al., [Target Span Detection for Implicit Harmful Content](https://arxiv.org/abs/2403.19836) | arXiv 2024; later ICTIR 2024 | The closest new paper to the immediate candidate-target extraction problem. It studies target spans for implicit harmful content across SBIC, DynaHate, and IHC, which makes it directly comparable to the current IHC/SBIC completion layer. |
| Jin et al., [GPT-HateCheck: Can LLMs Write Better Functional Tests for Hate Speech Detection?](https://aclanthology.org/2024.lrec-main.694/) | LREC-COLING 2024 | A practical reference for turning the current target-shuffle, target-replacement, counterspeech, and evidence-deletion ideas into a controlled functional-test workflow rather than a small collection of hand-written diagnostics. |
| Jin et al., [What the #?*!: Disentangling Hate Across Target Identities](https://aclanthology.org/2025.naacl-long.10/) | NAACL 2025 | Directly extends the target-leakage question into an identity-conditioned moderation audit: does mentioning an identity change the predicted hatefulness score? This is useful for designing same-template target replacement slices. |

### Read Next: Reusable Span and Relation Extraction Methods

| Paper | Venue | Why Read It Now |
|---|---|---|
| Zaratiana et al., [GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer](https://aclanthology.org/2024.naacl-long.300/) | NAACL 2024 Long | A lightweight open-label span extractor that is a natural baseline for `target_mention` and `attack_evidence`. It is relevant to the Privacy-Filter-inspired encoder path without requiring a fixed conventional NER ontology. |
| Zaratiana et al., [GLiREL: Generalist Model for Zero-Shot Relation Extraction](https://aclanthology.org/2025.naacl-demo.5/) | NAACL 2025 Demo | A direct method reference for the second stage: classify relations between extracted spans under unseen relation labels. It is worth testing conceptually against `attacked`, `mentioned_not_attacked`, and `not_a_candidate_target`. |
| Zaratiana et al., [CNER: Concept and Named Entity Recognition](https://aclanthology.org/2025.acl-long.1539/) | ACL 2025 | Useful when the extraction target is a social concept or group mention rather than a standard named entity. This is closer to implicit-hate target discovery than ordinary person, organization, and location NER. |
| Sainz et al., [GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction](https://arxiv.org/abs/2310.03668) | arXiv 2023 | A useful transfer paper for the planned `definition_frame`: encode compact annotation guidelines and ask whether extraction behavior changes in controlled ways. Read it as a schema-conditioning design reference, not as a hate-speech baseline. |

### Expand the Evaluation Lens

| Paper | Venue | Why Read It Now |
|---|---|---|
| Pamungkas et al., [Disentangling Subjectivity and Uncertainty for Hate Speech Annotation and Modeling using Gaze](https://aclanthology.org/2024.emnlp-main.214/) | EMNLP 2024 | Useful for the manual-audit design. The current relation layer already needs uncertainty flags; this paper gives a stronger conceptual separation between disagreement, subjectivity, and model uncertainty. |
| Shandilya et al., [Who Speaks Matters: Analysing the Influence of Dialects and Accents on LLM-Based Hate Speech Classification](https://aclanthology.org/2025.findings-emnlp.1357/) | Findings of EMNLP 2025 | Broadens shortcut analysis beyond target identity. A relation-grounded model should still be checked for speaker-variety sensitivity rather than assuming that evidence grounding automatically removes dialect bias. |
| Fasching and Lelkes, [Model-Dependent Moderation: Inconsistencies in Hate Speech Detection Across LLM-based Systems](https://aclanthology.org/2025.findings-acl.1144/) | Findings of ACL 2025 | Useful for positioning the project as moderation robustness rather than only classifier accuracy. It motivates evaluating whether the same grounded cases receive stable decisions across systems. |
| Mane et al., [SLM-Mod: Small Language Models Surpass LLMs at Content Moderation](https://aclanthology.org/2025.naacl-long.526/) | NAACL 2025 | Relevant to the compact bidirectional encoder direction. It provides a broader moderation-system argument for keeping efficient specialist baselines alongside generative 4B-8B models. |

## Optional Multilingual Extension

| Paper | Venue | Why Read It Later |
|---|---|---|
| Kara et al., [HATECAT-TR: A Hate Speech Span Detection and Categorization Dataset for Turkish](https://aclanthology.org/2025.findings-emnlp.1393/) | Findings of EMNLP 2025 | A useful multilingual span-level endpoint once the English IHC/SBIC schema is stable. It is not a reason to expand the immediate data-completion scope beyond IHC and SBIC. |

## 2025-2026 Addendum

The following papers were checked against the same local deduplication boundary on 2026-06-01. They are newer additions rather than replacements for the first reading route.

### Highest Priority 2026 Papers

| Paper | Venue | Why Read It Now |
|---|---|---|
| Hu and Lee, [HateXScore: A Metric Suite for Evaluating Reasoning Quality in Hate Speech Explanations](https://aclanthology.org/2026.eacl-long.198/) | EACL 2026 Long | The closest new evaluation paper to the planned structured output. It evaluates conclusion explicitness, causal grounding of quoted spans, configurable protected-group identification, and logical consistency. These dimensions map directly to `verdict`, `evidence`, `candidate_target`, and relation consistency. |
| Mothilal et al., [Argument-Based Consistency in Toxicity Explanations of LLMs](https://aclanthology.org/2026.findings-eacl.310/) | Findings of EACL 2026 | Useful for testing whether a plausible free-form explanation is internally consistent. Its argument-based consistency view complements span deletion and target replacement diagnostics. |
| Ni et al., [Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?](https://aclanthology.org/2026.eacl-long.3/) | EACL 2026 Long | A cross-task paper rather than a hate-only paper. It is relevant because weak relation labels and manual audits should preserve disagreement instead of collapsing every ambiguous target relation into one hard label. |

### High-Value 2025 Papers

| Paper | Venue | Why Read It Now |
|---|---|---|
| Wang et al., [Pragmatic Inference Chain (PIC): Improving LLMs' Reasoning of Authentic Implicit Toxic Language](https://aclanthology.org/2025.emnlp-main.296/) | EMNLP 2025 Main | Directly relevant to implicit harmful language. It is worth reading before deciding whether the current structured pipeline needs an explicit pragmatic-inference component or only grounded relation labels. |
| Díaz Redondo et al., [Untangling Hate Speech Definitions: A Semantic Componential Analysis Across Cultures and Domains](https://aclanthology.org/2025.findings-naacl.175/) | Findings of NAACL 2025 | Strengthens the planned `definition_frame` component with an empirical map of how hate-speech definitions vary across cultures and domains. |
| Trager et al., [MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation](https://aclanthology.org/2025.findings-emnlp.851/) | Findings of EMNLP 2025 | Extends explanation evaluation beyond English and flat rationales: binary labels, moral categories, and span-level rationales across four languages. Read it as a later-stage explanation and multilingual benchmark reference. |

### Workshop-Level Conceptual Extension

| Paper | Venue | Why Read It Later |
|---|---|---|
| Pavlopoulos et al., [A Position Paper on Toxic Reasoning: Grounding Categories of Toxic Language in Implications and Attitudes](https://aclanthology.org/2026.wassa-1.12/) | WASSA 2026 | Not a four-main-conference paper, but conceptually close to the project. It argues for grounding toxic-language categories in implications and attitudes rather than treating fine-grained classes as sufficient explanations. |

## arXiv-First Addendum

The following entries were checked against `wiki/`, `experiments/`, `log.md`, and `raw/sources/` on 2026-06-01. This section prioritizes arXiv versions and distinguishes papers without a local source page from conference papers that also have an arXiv version worth tracking.

### New arXiv-First Papers Not Yet in the Vault

| Paper | Date | Why Read It Now |
|---|---|---|
| [[192-gajewska-2026-improving-implicit-hate-speech-detection-via-a-community-driven-multi-agent-framework|Gajewska et al., Improving Implicit Hate Speech Detection via a Community-Driven Multi-Agent Framework]] | arXiv 2026-01 / ICAART 2026 | Promoted to a source page on 2026-06-17. Extends implicit-hate detection with dynamically constructed demographic-group agents and socio-cultural context. It is a useful contrast to the current compact relation-grounding path: compare explicit candidate relations against community-context consultation. |
| Herrmann et al., [Beyond Hate: Differentiating Uncivil and Intolerant Speech in Multimodal Content Moderation](https://arxiv.org/abs/2603.22985) | arXiv 2026-03 | Separates rude tone from group- or identity-directed intolerance. This is relevant to the planned relation schema because it tests whether a fine-grained semantic decomposition improves moderation error balance. |
| Proskurina et al., [HatePrototypes: Interpretable and Transferable Representations for Implicit and Explicit Hate Speech Detection](https://arxiv.org/abs/2511.06391) | arXiv 2025-11 | Uses class-level prototypes for transfer between explicit and implicit hate. It is a useful efficiency and representation-learning comparison if the project evaluates compact baselines or cross-dataset transfer. |
| Park et al., [LLM-C3MOD: A Human-LLM Collaborative System for Cross-Cultural Hate Speech Moderation](https://arxiv.org/abs/2503.07237) | arXiv 2025-03 | A broader human-in-the-loop moderation reference. It adds RAG-supported cultural context, LLM consensus checks, and targeted human escalation for cross-cultural cases. |
| Mothilal et al., [Human-Aligned Faithfulness in Toxicity Explanations of LLMs](https://arxiv.org/abs/2506.19113) | arXiv 2025-06 | Evaluates whether free-form toxicity explanations align with coherent human reasoning. Read it alongside HateXScore before deciding whether generated `statement` fields are useful evidence or merely plausible text. |

### Track These arXiv Versions of Conference Papers

| Paper | arXiv | Why Track the arXiv Version |
|---|---|---|
| Chen and Wang, [Pragmatic Inference Chain (PIC)](https://arxiv.org/abs/2503.01539) | arXiv 2025-03 | The EMNLP 2025 paper is already in the route, but the arXiv page is useful for version tracking and direct access. |
| Hu and Lee, [HateXScore](https://arxiv.org/abs/2601.13547) | arXiv 2026-01 | The EACL 2026 version is already prioritized above. Track arXiv for metric implementation updates and revisions. |
| Ni et al., [Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?](https://arxiv.org/abs/2506.19467) | arXiv 2025-06 | The EACL 2026 version is already in the route. The arXiv version is useful for checking updates to the disagreement-modeling experiments. |
| Trager et al., [MFTCXplain](https://arxiv.org/abs/2506.19073) | arXiv 2025-06 | The Findings of EMNLP 2025 version is already in the route. Track arXiv for dataset and benchmark revisions. |
| Korre et al., [Untangling Hate Speech Definitions](https://arxiv.org/abs/2411.07417) | arXiv 2024-11 | The Findings of NAACL 2025 version is already in the route. Although the preprint is from 2024, it remains directly relevant to the `definition_frame`. |

## Integrated Priority Matrix

The route contains 24 unique papers. The five arXiv links in the version-tracking table above are not counted again. Priority is assigned by expected impact on the current IHC/SBIC leakage-resistant target-relation project, not by publication date alone.

### P0: Read Before Freezing the Next Experiment

| Paper | Core Contribution | Immediate Use |
|---|---|---|
| [Target Span Detection for Implicit Harmful Content](https://arxiv.org/abs/2403.19836) | Detects implicit harmful-content target spans on datasets including IHC and SBIC. | Define candidate-span extraction and compare the new completion layer with the closest task-specific work. |
| [What the #?*!](https://aclanthology.org/2025.naacl-long.10/) | Audits identity-conditioned changes in hate-speech model outputs. | Turn target replacement into a controlled same-template robustness slice. |
| [GPT-HateCheck](https://aclanthology.org/2024.lrec-main.694/) | Uses LLMs to create functional hate-speech tests. | Build systematic tests for target presence, replacement, counterspeech, quotation, and evidence deletion. |
| [HateXScore](https://aclanthology.org/2026.eacl-long.198/) | Evaluates conclusion explicitness, quoted-span grounding, protected-group identification, and logical consistency in hate explanations. | Specify metrics for `verdict`, `evidence`, `candidate_target`, and relation consistency. |
| [PIC](https://aclanthology.org/2025.emnlp-main.296/) | Models pragmatic inference chains for authentic implicit toxic language. | Decide whether implicit cases require an explicit inference layer beyond span and relation prediction. |
| [Untangling Hate Speech Definitions](https://aclanthology.org/2025.findings-naacl.175/) | Decomposes hate-speech definitions across cultures and domains. | Freeze a defensible `definition_frame` schema instead of using one underspecified hate label. |

### P1: Read While Building the First Baselines

| Paper | Core Contribution | Immediate Use |
|---|---|---|
| [GLiNER](https://aclanthology.org/2024.naacl-long.300/) | Open-label bidirectional span extraction. | Compact baseline for `target_mention` and `attack_evidence`. |
| [GLiREL](https://aclanthology.org/2025.naacl-demo.5/) | Zero-shot relation extraction under open relation labels. | Baseline reference for `attacked`, `mentioned_not_attacked`, and `not_a_candidate_target`. |
| [CNER](https://aclanthology.org/2025.acl-long.1539/) | Extends entity recognition toward concept recognition. | Better match for social groups and implicit targets that are not conventional named entities. |
| [GoLLIE](https://arxiv.org/abs/2310.03668) | Conditions zero-shot information extraction on annotation guidelines. | Design guideline-conditioned extraction and test controlled policy changes. |
| [SLM-Mod](https://aclanthology.org/2025.naacl-long.526/) | Shows the value of specialist small language models for moderation. | Justify compact encoder baselines alongside generative 4B-8B models. |
| [HatePrototypes](https://arxiv.org/abs/2511.06391) | Uses interpretable prototypes for explicit-to-implicit hate transfer. | Add an efficient cross-dataset representation baseline if transfer remains a core claim. |

### P2: Read Before Writing the Evaluation Section

| Paper | Core Contribution | Immediate Use |
|---|---|---|
| [Argument-Based Consistency](https://aclanthology.org/2026.findings-eacl.310/) | Evaluates whether toxicity explanations are internally coherent. | Complement evidence deletion and target replacement with explanation-consistency tests. |
| [Human-Aligned Faithfulness](https://arxiv.org/abs/2506.19113) | Tests whether LLM toxicity explanations align with human reasoning. | Determine whether generated `statement` fields are auditable evidence or only fluent rationales. |
| [Can Reasoning Help LLMs Capture Human Annotator Disagreement?](https://aclanthology.org/2026.eacl-long.3/) | Studies reasoning and human disagreement modeling. | Preserve uncertain relation cases rather than forcing hard weak labels. |
| [Disentangling Subjectivity and Uncertainty](https://aclanthology.org/2024.emnlp-main.214/) | Separates subjectivity and uncertainty using gaze-informed hate annotation analysis. | Improve manual-audit sampling and uncertainty flags. |
| [Who Speaks Matters](https://aclanthology.org/2025.findings-emnlp.1357/) | Audits dialect and accent sensitivity in LLM-based hate classification. | Check whether relation grounding reduces target shortcuts while leaving speaker-variety bias unresolved. |
| [Model-Dependent Moderation](https://aclanthology.org/2025.findings-acl.1144/) | Measures inconsistencies across LLM-based moderation systems. | Add model-choice sensitivity to the robustness analysis. |

### P3: Read as Deliberate Extensions

| Paper | Core Contribution | Best Use |
|---|---|---|
| [Community-Driven Multi-Agent Framework](https://arxiv.org/abs/2601.09342) | Adds demographic-group agents and socio-cultural context to implicit-hate detection. | Compare explicit relation grounding with agent-mediated cultural context. |
| [Beyond Hate](https://arxiv.org/abs/2603.22985) | Separates incivility from identity-directed intolerance in multimodal moderation. | Extend the relation ontology after the text-only schema is stable. |
| [LLM-C3MOD](https://arxiv.org/abs/2503.07237) | Combines cultural retrieval, LLM consensus, and human escalation. | Frame a later human-in-the-loop moderation system. |
| [MFTCXplain](https://aclanthology.org/2025.findings-emnlp.851/) | Provides multilingual multi-hop hate explanations and span rationales. | Evaluate explanation transfer after the first English pipeline works. |
| [HATECAT-TR](https://aclanthology.org/2025.findings-emnlp.1393/) | Adds Turkish span-level hate detection and categorization data. | Test multilingual span transfer later. |
| [A Position Paper on Toxic Reasoning](https://aclanthology.org/2026.wassa-1.12/) | Argues for grounding toxic categories in implications and attitudes. | Use for conceptual framing, not as a primary experimental anchor. |

## Suggested Reading Order

1. First week: Target Span Detection for Implicit Harmful Content, What the #?*!, GPT-HateCheck, HateXScore, PIC, and Untangling Hate Speech Definitions.
2. Baseline implementation: GLiNER, GLiREL, CNER, GoLLIE, SLM-Mod, and optionally HatePrototypes.
3. Evaluation design: Argument-Based Consistency, Human-Aligned Faithfulness, annotator-disagreement modeling, subjectivity and uncertainty, dialect sensitivity, and model-dependent moderation.
4. Later extensions: community-driven agents, fine-grained multimodal moderation, human-in-the-loop cross-cultural moderation, multilingual explanation data, Turkish span data, and toxic-reasoning framing.

## Synthesis Notes

- The active project should not be narrowed to one architecture. The stronger reading path connects hate-speech target spans, open-label extraction, zero-shot relation extraction, guideline-conditioned IE, and moderation robustness.
- GLiNER plus GLiREL suggests a clean baseline decomposition: `raw text -> open-label spans -> candidate relations -> derived verdict`.
- CNER is useful because IHC/SBIC targets are often social concepts or implicit groups, not only conventional named entities.
- GPT-HateCheck and What the #?*! strengthen the evaluation argument: target replacement should be a systematic controlled test family, not an isolated ablation.
- The moderation robustness papers prevent an overclaim: grounding target-evidence relations may reduce one shortcut without solving dialect, system, or annotation uncertainty.

## Related Pages

- [[p0-target-grounding-reading-synthesis-2026-06-01]]
- [[privacy-filter-inspired-span-grounded-hate-detection]]
- [[leakage-resistant-target-relation-modeling]]
- [[candidate-target-relation-grounding-experiment-plan-2026-05-18]]
- [[missing-annotation-completion-and-utility-literature-map]]
- [[intent-slot-style-hate-speech-modeling]]

## Follow-up Questions

- Should the first compact prototype compare Privacy Filter, GLiNER, and a standard encoder token classifier under the same span ontology?
- Can GLiREL-style relation labels be adapted cleanly to the three-state candidate-target schema without hiding uncertainty in the relation label?
- Should identity replacement, dialect variation, and model-dependent moderation be one unified robustness section or separate analysis modules?
