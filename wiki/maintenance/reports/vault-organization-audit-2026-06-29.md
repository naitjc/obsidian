---
created: 2026-06-29
updated: 2026-07-11
tags: [maintenance, audit, cleanup]
sources: []
---

# Vault Organization Audit 2026-06-29

## Scope And Assumption

This pass interpreted “organize the whole vault” as conservative structural maintenance: fix confirmed routing and repository-boundary defects, remove clearly reproducible local clutter, preserve active or provenance-bearing research artifacts, and document deferred storage decisions. It did not rewrite the research taxonomy, move experiment archives, inspect current remote processes, or alter immutable source files.

## Inputs Checked

- Root routing and policy: `README.md`, `AGENTS.md`, `EXPERIMENTS.md`, `baselines/README.md`, and `experiments/server-sync/README.md`.
- Wiki routing and maintenance rules: the [master index](../../index.md), [maintenance index](../index.md), [[wiki-maintenance-checklist]], and [[subagent-collaboration-workflow]].
- Git state, ignore rules, tracked/untracked boundaries, symlinks, large files, directory sizes, temporary files, and generated caches.
- Standard structural checks: `scripts/lint_wiki.py`, `scripts/wiki_inventory.py`, `scripts/check_source_tag_drift.py`, and `scripts/check_pdf_text_artifacts.py`.

## Inventory Before Durable Changes

| Area | Approximate size | Boundary decision |
|---|---:|---|
| `experiments/` | 1.8 GB | Preserve; about 1.6 GB is ignored server snapshot state under `server-sync/remotes/` |
| `raw/` | 394 MB | Preserve unchanged as immutable source material |
| `.git/` | 412 MB | Preserve; no manual object deletion or pruning |
| `.venv/` | 31 MB | Preserve; locally active and not reproducible from a root lockfile |
| `baselines/` | 7.3 MB | Repair ignore boundaries; no repository relocation |
| `wiki/` | 2.2 MB | Structurally healthy; fix only ambiguous index links and refresh the audit date |
| `tmp/` | 248 KB | Preserve three same-day IHC JSON files; remove only Finder metadata |

## Changes Applied

### Navigation And Wiki Integrity

- Replaced 10 ambiguous Wiki-page links to `index` with explicit relative Markdown links. The vault intentionally has both `wiki/index.md` and `wiki/maintenance/index.md`; explicit targets remove Obsidian resolution ambiguity. Historical `log.md` entries remain append-only.
- Extended `scripts/lint_wiki.py` to report ambiguous Wikilinks when a target slug maps to multiple files, preventing the same defect from silently returning.
- Refreshed the master index inventory and maintenance audit date after all four standard checks passed.
- Updated `欢迎.md` so the human landing page routes research, experiments, baselines, and maintenance through the current project entry points.

### Experiment And Baseline Boundaries

- Narrowed broad baseline `data` ignore patterns so LLAMA-FACTORY source-level data loaders and tests are not mistaken for runtime datasets.
- Kept unresolved CADET Git LFS sample pointers ignored, and explicitly allowlisted only the reviewed privacy-filter synthetic fixtures; downloaded datasets, checkpoints, caches, and generated outputs remain excluded.
- Corrected `baselines/README.md` to match the compact HARM notebook and fixture boundaries actually present in the mirror.
- Added `experiments/hate/rahmd-text-architecture/README.md` and routed the architecture exports from `experiments/hate/README.md`.
- Added `experiments/server-sync/manifests/2026-06-29-newrahmd-local-bundle-audit.md` with hashes for the current portable staging files. The remote run state remains unverified.

### Safe Local Cleanup

- Removed seven ignored `.DS_Store` files outside protected source and remote-mirror boundaries.
- Removed two ignored, reproducible Python `*.egg-info` directories.
- Removed the stale `newRAHMD.tar.gz` transfer archive because it predated the current staging bundle contents.

## Preserved By Design

- Existing user changes in `.obsidian/graph.json` and `.obsidian/workspace.json`.
- `raw/`, including the known byte-identical pair `2024.acl-long.291.pdf` and its descriptive-name copy; source provenance rules prohibit cleanup by deletion.
- `experiments/server-sync/remotes/` and its `merged/` symlink view; moving or deleting either side would break snapshot provenance and current links.
- `experiments/hate/xu-l20-snapshot-2026-05-19/`, `xu-l20-full-statement-2026-05-27/`, `ihc-private-gold/`, and agentic workflow data/history/runs.
- Three same-day JSON files under `tmp/`, because no byte-identical reconstruction path was confirmed.
- `.git/` loose and unreachable objects; repository recovery policy was not part of this pass.

## Deferred Decisions

- `experiments/hate/xu-l20-full-statement-2026-05-27/` is the strongest archive candidate: almost all of its roughly 48 MB has exact copies elsewhere, but it is tracked and referenced, so archiving requires coordinated path updates.
- Server mirrors are the dominant storage consumer. They may be moved to external archival storage only after confirming restore expectations and updating the `merged/` links.
- Git object compaction or pruning requires an explicit recovery/retention decision; it is not ordinary file organization.
- The remaining `.DS_Store` files are inside `raw/` or a remote snapshot and were left untouched to respect those literal boundaries.

## Verification

The following checks passed after the organization changes:

```bash
python3 scripts/lint_wiki.py
python3 scripts/wiki_inventory.py
python3 scripts/check_source_tag_drift.py
python3 scripts/check_pdf_text_artifacts.py
git diff --check
```

No remote command, experiment launch, staging operation, commit, push, or destructive Git maintenance was performed.

## Refresh 2026-07-01

- Re-ran the full inventory after new June 30 and July 1 work while preserving all pre-existing dirty-worktree changes.
- Ingested the newly added, non-duplicate ReasonRAG PDF as [[196-zhang-2025-process-vs-outcome-reward-which-is-better-for-agentic-rag-reinforcement-learning]] and updated the source catalog, LLM reasoning hub, RAG and reasoning concepts, corpus overview, and master counts.
- Visually checked the source PDF's dataset and result tables before recording numeric claims.
- Removed only newly regenerated, ignored Finder metadata outside `raw/` and remote-mirror boundaries. Recent IHC diagnostics under `tmp/` remain preserved because their reconstruction path and retention status are not confirmed.
- The archive candidates and storage-heavy server-mirror decisions above remain deferred; this refresh did not move experiment archives, modify snapshots, prune Git objects, or alter `.venv` and Obsidian workspace state.

Current size snapshot after the refresh:

| Area | Approximate size | Current decision |
|---|---:|---|
| `experiments/` | 1.9 GB | Preserve; 1.6 GB is the local-only `server-sync/remotes/` snapshot tree |
| `.git/` | 419 MB | Preserve; no object pruning without an explicit recovery decision |
| `raw/` | 395 MB | Preserve unchanged; all 196 unique PDFs are now indexed |
| `.venv/` | 78 MB | Preserve as the current local tooling environment |
| `tmp/` | 31 MB | Preserve recent IHC diagnostics pending a confirmed reconstruction and retention decision |
| `baselines/` | 7.2 MB | Boundary repaired; compact code and approved fixtures retained |
| `wiki/` | 2.2 MB | 359 pages; structural checks pass |

## Publication Refresh 2026-07-11

- Re-ran all four structural checks, source-hub drift preview, `git diff --check`, and Python syntax validation for the modified runtime; all passed.
- Corrected the ReasonRAG source boundary after visually comparing the main tables and Appendix Table 5, which reveals an internal inconsistency in the paper's backbone-uniformity claim.
- Corrected the truncated newRAHMD configuration hash and marked the 2026-07-06 target-relation staging snapshot as superseded after the later huashan v9-like changes.
- Updated the active factor research note so the completed CATCH C/T run is historical Baseline 0 and the label-blind M/T/S factor pool is the current pre-implementation design.
- Removed newly regenerated Finder metadata outside protected `raw/` and remote-snapshot boundaries. No dataset, model, checkpoint, run evidence, server mirror, or Obsidian workspace state was deleted.

Current size snapshot:

| Area | Approximate size | Current decision |
|---|---:|---|
| `experiments/` | 1.9 GB | Preserve; 1.6 GB is ignored server snapshot state |
| `tmp/` | 4.7 GB | Preserve for now; dominated by the verified 2026-07-07 FineTune relay, which remains a separately documented cleanup candidate |
| `.git/` | 421 MB | Preserve; no object pruning without a recovery decision |
| `raw/` | 395 MB | Preserve immutable sources; 197 PDFs represent 196 unique ingested papers |
| `.venv/` | 78 MB | Preserve the active local tooling environment |
| `baselines/` | 7.2 MB | Track reviewed source/tests and explicit synthetic fixtures; keep unresolved LFS samples ignored |
| `wiki/` | 2.2 MB | 359 pages; structural checks pass |

The 4.7 GB relay is ignored and not a publication risk. It was not removed because this
refresh did not re-verify the remote restore path or receive a separate retention decision.
