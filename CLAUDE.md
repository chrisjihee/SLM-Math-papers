# CLAUDE.md for SLM-Math-papers

This repository is for strategic reading notes and related-work positioning for the SLM-Math project.

Main workdir:

`~/code/SLM-Math/SLM-Math-papers`

Do not run training, inference, evaluation, SFT, distillation, or checkpoint-producing jobs.

For each paper update, usually modify:

- `md/<paper>.md`
- `RELATED-WORK-MATRIX.md`
- `POSITIONING-NOTES.md`
- `READING-QUEUE-202606.md`
- `papers.yaml`

Before editing, read:

- `../CLAUDE.md`
- `../CURRENT-READING.md`
- `../prompts/paper-reading-context.md`
- `../prompts/paper-strategic-note-template.md`
- `../prompts/paper-repo-update.md`
- `RELATED-WORK-MATRIX.md`
- `POSITIONING-NOTES.md`
- `READING-QUEUE-202606.md`
- `papers.yaml`

Rules:

- Keep paper URL and code URL separate.
- Do not erase existing useful metadata.
- Do not mark `verifier`, `search`, `adaptive_budget`, `stopping`, or `reranking` as true unless the paper really supports that taxonomy.
- Do not commit/push unless the user explicitly asks; when the user gives explicit authorization, committing and pushing are allowed.
- After edits, show `git status --short` and `git diff --stat`.
- When selecting the next paper to read, prefer `../CURRENT-READING.md` as the active queue and use `READING-QUEUE-202606.md` as the accumulated paper-repo record.

Canonical vs archive:

- `archive/` is historical context only. Do NOT use it as an active source of truth, active queue, or current claim boundary.
- For deep-interview / experiment planning, read only the canonical files: `CURRENT-FRAME-202606.md`, `POSITIONING-NOTES.md`, `RELATED-WORK-MATRIX.md`, `READING-QUEUE-202606.md` (+ root `CURRENT-READING.md`), `papers.yaml`, `NFM-BRIDGE-PLAN.md`, plus `md/` and `paper/`.
- Current corpus snapshot / deletion record: `REPO-CORPUS-STATUS-20260621.md`.
