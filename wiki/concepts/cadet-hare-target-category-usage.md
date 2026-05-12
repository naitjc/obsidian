---
created: 2026-05-12
updated: 2026-05-12
tags: [query-answer, hate-speech, implicit, target-aware, explainability, causal]
sources:
  - raw/sources/2510.07707v2.pdf
  - raw/sources/HARE_ Explainable Hate Speech Detection with Step-by-Step Reasoning.pdf
promotion_reason: Durable comparison of how CADET and HARE use target and category annotations.
---

# Query Answer: CADET and HARE Target/Category Usage

## Question

CADET 和 HARE 是怎么去使用数据集的 target 和 category 的？

## Promotion Rationale

This answer has durable wiki value because it clarifies a recurring methodological distinction in hate-speech work: whether target/category labels are used as supervised prediction heads, causal latent factors, prompt conditions, rationales, or merely evaluation slices.

## Short Answer

Here `category` means hate-speech type or implicit-hate taxonomy category, not explicit-vs-implicit style.

CADET does not appear to use the Implicit Hate fine-grained hate-type category as a central input or prediction target in the paper's main formulation. Its formal data tuple is text, binary hate label, explicit/implicit style, and optional target group. It uses target group as a discrete latent factor and style as a separate explicit/implicit factor. The paper reports target/style disentanglement and cross-style evaluation, but it does not describe a supervised head for categories such as grievance, incitement, inferiority, irony, stereotypical, or threatening.

HARE also does not use the fine-grained hate-type category as a model input in its described prompt format. Its Co-HARE prompt uses post `P`, target group `T`, and implied statement `I`; it asks the LLM to explain how the post targets the group and leads to the implied statement. The classification output is hate/offensive vs not hate/offensive. On Implicit Hate, explicit and implicit hate are merged into one hate class for detection rather than preserving the six fine-grained implicit-hate categories as labels.

The fine-grained category labels themselves come from the Implicit Hate dataset, not from HARE. In ElSherief et al.'s Latent Hatred benchmark, annotators first label explicit hate, implicit hate, or not hate, then expert annotators label implicit-hate examples with the six-class taxonomy. HARE mainly uses the target group and implied statement annotations from these datasets, while generating missing step-by-step rationales with GPT-3.5.

CADET's `optional` target means the formal corpus can include a target group field when the dataset supplies one, but target is not required for every dataset/example in the problem definition. The paper does not state that all missing target groups are generated or manually filled. It defines a target latent factor and target loss when target supervision is available, but the exact missing-target encoding and per-dataset target ontology are left to the released dataset/code rather than fully specified in the paper text.

HARE's `Target: T` is whatever free-text target group annotation exists in SBIC or Implicit Hate, not a single closed label set introduced by HARE. Examples in the paper and Latent Hatred include targets such as black folks, Jewish people or Holocaust victims, women/girls, non-white people, white people, Mexicans, minorities, Muslims, and non-whites. The `implied statement` is also a human annotation from those benchmark datasets: for Implicit Hate, two annotators provided each implicit-hate tweet's target demographic group and implied statement in free text; for SBIC, HARE uses the benchmark's existing target-group and implied-statement style rationales. HARE then asks GPT-3.5 to generate a step-by-step rationale conditioned on those fields in Co-HARE.

## Evidence

- [[008-2510-07707v2]] defines CADET's corpus as `(x, y, s, t)`, where `s` is explicit/implicit style and `t` is the optional targeted group. It uses target and style as latent factors and includes target/style losses, orthogonality constraints, and counterfactual style flipping.
- The CADET source does not describe a hate-type category head for the Implicit Hate six-class taxonomy in the main method.
- [[042-hare-explainable-hate-speech-detection-with-step-by-step-reasoning]] defines HARE's generation format around class `C`, target group `T`, and implied statement `I`; Co-HARE uses `T` and `I` in prompts, while Fr-HARE generates rationales without benchmark annotations.
- The HARE source states that Implicit Hate explicit and implicit classes are merged into one hate category for its detection task, and that GPT-3.5-turbo-0613 extracts multiple rationales per sample.
- [[031-elsherief-2021-latent-hatred-a-benchmark-for-understanding-implicit-hate-speech]] provides the relevant Implicit Hate background: its six fine-grained implicit-hate categories, target groups, and natural-language implication annotations.
- Latent Hatred states that each of the 6,346 implicit-hate tweets receives two free-text target demographic group and implied statement annotations.
- [[implicit-hate-speech-detection]] records the broader issue: implicit hate requires target and world-knowledge reasoning, and models often struggle across domains and targets.

## Synthesis Notes

- CADET is target-aware architecturally, but the `category` it emphasizes is explicit/implicit style, not the six-class Implicit Hate type taxonomy.
- HARE is target-conditioned explanatorily: target annotations are used to guide rationale generation, not to define a separate target prediction task.
- Neither paper's main method appears to train on the Implicit Hate fine-grained category taxonomy as a primary supervised objective; CADET uses target/style factors, while HARE uses target/implied-statement rationales.
- `optional target` in CADET should be treated as an available-if-present annotation, not as proof that the paper generated missing targets.

## Follow-up Questions

- Verify from CADET code or dataset card which target-group ontology is used for each dataset and how missing targets are encoded.
- Check whether HARE's released preprocessing keeps all SBIC and Implicit Hate target/implied-statement fields or filters examples with missing annotations.
