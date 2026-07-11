---
created: 2026-06-05
updated: 2026-06-16
tags: [query-answer, research-planning, llm, ideation, workflow]
sources: []
promotion_reason: "Durable research-planning rule for using LLMs to generate non-generic research ideas from source-grounded conflicts, hard constraints, and profile-guided transfer screening."
---

# Query Answer: AI-Assisted Research Ideation Workflow

## Question

The user provided a reflection on why broad, context-free AI brainstorming produces generic ideas, and asked what inspiration should be written into the wiki.

## Promotion Rationale

This answer has durable value because it records a reusable workflow for future research-idea generation. It should guide later wiki-assisted ideation before a project commits to annotation, modeling, experiments, or manuscript claims.

## Short Answer

The useful lesson is that an LLM should not be treated as the origin of novelty. It should be treated as a high-bandwidth but context-poor research operator: first feed it dense source context, then make it locate conflicts, boundary conditions, hidden assumptions, measurable variables, transferable mechanisms, and reviewer-facing failure modes.

Good research ideas should be searched for at friction points between checked evidence, not in broad topic prompts. A useful prompt is therefore not "What are new directions for AI and psychology?" but "Given these papers, datasets, and experiment records, where do their methods, conclusions, task definitions, or evaluation boundaries become mutually incompatible?"

When the task is not to synthesize already-ingested sources but to scout outside fields, use a profile-guided transfer screen: define the local research problem and the mechanisms worth importing, prefilter a broad paper collection cheaply, then ask the LLM to judge whether each paper's core idea transfers to the current research constraints. The screen produces a reading queue, not a source claim.

## Agent Routing

Use this page when the user asks for:

- research idea generation grounded in this vault;
- cross-domain paper mining for transferable mechanisms;
- a reading queue that should distinguish topic similarity from method transfer;
- reviewer-risk checks before turning an idea into an experiment plan.

Start with the [master index](../index.md), the relevant direction/source/entity pages, and recent `experiments/` notes. For broad external paper collections, record the screening profile and shortlisted outputs with [[transfer-idea-screening-template]] rather than creating unlinked ad hoc notes.

Do not use this workflow to promote LLM-scored candidates into source claims. A candidate paper becomes source-grounded knowledge only after its original paper is read and ingested under `wiki/sources/`.

## Workflow Rule

### 1. Replace Broad Brainstorming With Source-Grounded Conflict Search

Before asking for ideas, collect the local evidence:

- Recent top-conference or journal papers.
- Full-text source notes under `wiki/sources/`.
- Dataset schemas, annotation rules, and benchmark pages under `wiki/entities/`.
- Local experiment artifacts and bad-case records under `experiments/`.
- Existing synthesis and rejection-risk pages under `wiki/concepts/`.

Then ask the LLM to find contradictions, not slogans. The target is a conflict such as:

- A method assumes a representation is stable, while another result shows it is boundary-sensitive.
- A benchmark rewards aggregate performance, while deployment-relevant slices expose shortcut behavior.
- A paper claims generalization, while its evaluation only changes surface domain, not task definition.
- A dataset annotation schema treats a variable as implicit background, while another line of work makes the same variable central.

The output should name the conflicting assumptions, the evidence boundary, and the minimal experiment that can decide whether the conflict is real.

### 2. Convert Ideas Into Iron Constraints Before Implementation

Each candidate idea should pass a constraint gate:

- Core variable: what variable, relation, representation, or boundary is being studied?
- Quantifiability: can it be represented as labels, spans, scores, perturbation axes, retrieval sets, or high-dimensional features?
- Observable state change: what should change in model behavior if the idea is true?
- Metric: what metric or diagnostic slice would prove progress beyond aggregate F1?
- Baseline pressure: what existing method would make the idea look trivial?
- Failure condition: what result would make the idea not worth continuing?

If the core variable cannot be operationalized, the idea should be rejected early rather than rescued with vague wording.

### 3. Use Adversarial Review Before Running the Full Study

After a minimal experiment design exists, run an explicit reviewer attack:

- From experimental control: what uncontrolled factor can explain the expected gain?
- From statistics: is the sample size, slice definition, or test reliable enough?
- From annotation: are the labels measuring the intended construct or leaking the answer?
- From novelty: is the contribution only a recombination of existing components?
- From evaluation: does the metric test the claim, or only the authors' own perturbation?

The point is to break weak ideas while they are still cheap. A design that survives this stage should have a clear main claim, bounded evidence requirements, and known rejection risks.

### 4. Profile-Guided Transfer Screening For Outside-Field Papers

When the search space is a large paper collection, separate three questions:

- Surface relevance: does the paper mention the same task, dataset, or keywords?
- Transferable mechanism: does the paper contain a reusable modeling idea, representation design, objective, diagnostic, or evaluation protocol?
- Local fit: can that mechanism be adapted under this vault's current data, model, compute, annotation, and publication constraints?

Use a compact research profile before screening:

| Field | Purpose |
|---|---|
| `target_tasks` | The local task, claim, or experiment family the candidate must help. |
| `prefer` | Mechanisms to reward, such as reusable objectives, representation designs, retrieval protocols, diagnostics, or evaluation slices. |
| `downweight` | Candidate types to demote, such as surveys, benchmark-only papers, dataset-only papers, or keyword-only matches. |
| `positive_keywords` | Cheap first-pass signals for the broad candidate pool. |
| `negative_keywords` | Cheap first-pass rejection or demotion signals. |
| `scoring_dimensions` | Weighted dimensions such as transferability, method novelty, representation value, implementation feasibility, and evaluation value. |

The useful migrated abstraction from IdeaScout is the profile and output schema, not its web portal or runner code. A minimal agent-readable output for each candidate should include:

| Field | Meaning |
|---|---|
| `idea_core` | One-sentence core idea inferred from title, abstract, and then the paper text if promoted. |
| `transferable_mechanism` | The reusable mechanism, not just the topic overlap. |
| `fit_reason` | Why the mechanism fits or fails the local profile. |
| `risk_or_limitation` | The main uncertainty, missing evidence, leakage risk, implementation risk, or reviewer objection. |
| `priority` | `keep`, `maybe`, or `drop` for reading triage. |
| `scores` | Numeric triage aids only; do not treat them as evidence. |

Use rule-based filtering only as a cost-control step. Keyword hits can select candidates for LLM or human review, but the final reading queue should be ranked by transferable mechanism and local fit, not by keyword overlap.

### 5. Promotion Boundary

Keep the layers separate:

- Screening output under this workflow is a hypothesis and reading queue.
- A candidate becomes durable source knowledge only after source-page ingestion.
- A candidate becomes a method proposal only after it passes the constraint gate and adversarial review above.
- Tool code, web portals, retry runners, and generated rankings stay outside `wiki/` unless they become maintained vault tooling under `scripts/` with a clear local use case.

## Operational Prompt Pattern

Use this pattern for future idea-generation turns:

```text
Given the attached/source-linked papers, dataset schemas, and local experiment results, do not brainstorm broad directions.
Find the strongest conflicts between their assumptions, methods, conclusions, and evaluation boundaries.
For each conflict, state:
1. the two incompatible assumptions or conclusions;
2. the exact evidence boundary where the conflict appears;
3. the measurable variable or representation involved;
4. the minimal experiment that could test it;
5. the metric and diagnostic slices;
6. the three most damaging reviewer objections.
Reject any idea whose core variable cannot be operationalized.
```

For profile-guided transfer screening, use this pattern:

```text
Given this research profile and candidate paper metadata, do not rank by keyword overlap.
First infer the candidate's core idea.
Then identify the transferable mechanism, local fit, implementation feasibility, evaluation value, and main risk.
Return one compact record with:
- priority: keep, maybe, or drop;
- idea_core;
- transferable_mechanism;
- fit_reason;
- risk_or_limitation;
- scores for the profile dimensions.
Treat the output as a reading queue, not as source-grounded evidence.
```

## Connections

- [[cross-direction-innovation-ideas-2026-05-18]] is the downstream use case: it turns cross-direction tensions into concrete candidate ideas.
- [[target-relation-modeling-reject-review]] shows the adversarial-review step: a plausible idea is useful only after its leakage, novelty, annotation, and evaluation risks are explicit.
- [[hate-speech-grounding-directions-review-2026-05-18]] records a reviewer-facing assessment pattern for turning broad directions into bounded contributions.
- [[p0-target-grounding-reading-synthesis-2026-06-01]] is an example of source-grounded narrowing before committing to experiment design.
- [[dual-view-target-statement-relation-alignment]] and [[ihc-completed-small-llm-innovation-ideas-2026-06-05]] show why constraints such as no dataset expansion, small generative LLMs, training-only fields, and diagnostic slices must be fixed before method design expands.
- [[transfer-idea-screening-template]] records the reusable profile and candidate-record structure for outside-field paper scouting.

## Chain Check

- Input: user-provided research-process reflection, existing wiki planning pages, current vault routing rules, and static inspection of an external IdeaScout-style profile-guided screening tool.
- Processing flow: reinterpret the reflection and external tool pattern as a reusable workflow, separate source-grounded claims from process heuristics, and connect it to existing idea-generation and reviewer-risk pages.
- State changes: no source claim or numeric benchmark result is upgraded; this page records a planning and screening rule.
- Output: a reusable AI-assisted ideation workflow centered on conflict search, operational constraints, metrics, adversarial review, and profile-guided transfer screening.
- Upstream impact: future research-question turns should read relevant source and synthesis pages before asking for ideas; outside-field scouting should first define a profile.
- Downstream impact: candidate ideas should be rejected early when they lack measurable variables, diagnostic metrics, a transferable mechanism, local implementation fit, or a reviewer-defensible experiment.

## Follow-up Questions

- Which current direction should be stress-tested with this workflow first: hate speech target-relation modeling, LLM reasoning evaluation, multimodal learning, or another registered direction?
- Should future idea pages include a fixed "conflict, variable, metric, reviewer attack" table by default?
- Should a later maintained script convert external conference/OpenReview/Semantic Scholar metadata into [[transfer-idea-screening-template]] records, or should this remain a prompt-and-note workflow?
