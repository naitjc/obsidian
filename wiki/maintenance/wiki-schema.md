---
created: 2026-05-19
updated: 2026-05-19
tags: [maintenance, schema]
sources: []
---

# Wiki Schema

## Repository Namespaces

- `raw/`: immutable source documents, datasets, and captured assets. Do not edit files here.
- `wiki/`: durable research knowledge and maintenance rules.
- `experiments/`: local experiment process, configs, prompts, runs, metrics, and notes.
- `baselines/`: external paper code, upstream repositories, and baseline-specific reproduction work.
- `papers/`: manuscript-specific argument work when present.
- `scripts/` and `src/`: reusable tooling and code.

## Wiki Namespaces

- `wiki/index.md`: master router.
- `wiki/sources/`: source-grounded notes using the source-page format.
- `wiki/concepts/`: concepts, topics, methods, direction maps, synthesis pages, metrics matrices, and status pages.
- `wiki/entities/`: datasets, benchmarks, people, organizations, and other reusable named entities.
- `wiki/templates/`: reusable wiki page templates.
- `wiki/maintenance/`: schema, routing, lint, direction registry, and maintenance decisions.
- `wiki/maintenance/reports/`: dated lint reports, integrity reports, verification indexes, and historical maintenance status snapshots.

Future namespaces such as `wiki/questions/`, `wiki/comparisons/`, `wiki/claims/`, `wiki/datasets/`, or `wiki/methods/` may be added when they reduce ambiguity or duplication.

## Page Format

- Use Markdown with YAML frontmatter.
- Required frontmatter fields: `created`, `updated`, `tags`, `sources`.
- Use lowercase slug page names.
- Use double-bracket slug links for internal wiki cross-links.
- Use `[source](source-url)` for external citations.
- Separate extracted evidence from synthesis on source pages.

## Source Page Format

Required sections:

- `Metadata`
- `Problem Framing`
- `Method`
- `Data and Evaluation Setup`
- `Results and Claims`
- `Limitations and Follow-ups`
- `Structured Signals`
- `Related Concepts`

Tag a page `auto-ingest` only when it is metadata or first-pass extraction. Tag a page `deep-ingest-v2` only after the multi-section extraction is complete and linked into the relevant direction.

## Concept and Synthesis Pages

- Concept pages summarize stable knowledge across sources and link to evidence-bearing source pages.
- Synthesis pages may resolve tensions between papers, but must mark unverifiable quantitative claims as assumptions or pending verification.
- Direction status pages track completion criteria, remaining gaps, and whether a direction is complete for internal wiki use or publication-grade external citation.
- Maintenance and lint reports should stay under `wiki/maintenance/` or `wiki/maintenance/reports/`, not under `wiki/concepts/`.
