# Hate Experiment Archives

This folder stores selected local experiment evidence for hate-speech modeling work. It is separate from `wiki/`: raw run artifacts stay here, while durable conclusions can be promoted into wiki concept pages when they are useful across tasks.

## Archives

- `xu-l20-snapshot-2026-05-19/`: selected evidence copied from `xu-l20:/data/chenjt/hate` for IHC/SBIC fine-tuning, filled-not-toxic target-input leakage diagnostics, and older Hidden CoT trials.
- `xu-l20-full-statement-2026-05-27/`: supplemental evidence for the completed `text -> class + hate_class + target + statement` runs, including evaluation outputs, processed data with `statement`, pipeline code, and execution logs.

## Public Repository Boundary

These folders are local evidence archives. The public repository keeps README
files, configs, pipeline code, aggregate metrics, and non-sample summaries.
Derived datasets, per-example JSONL predictions and errors, execution logs,
interpreter caches, and process state remain local unless their release is
reviewed explicitly.
