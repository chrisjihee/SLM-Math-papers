# CLEANUP PLAN — 2026-06-21 (physical cleanup / archive split)

> deep-interview 직전, `SLM-Math-papers`에서 canonical corpus와 legacy 자료가 top-level에 섞여 있는 상태를 물리적으로 분리한다.
> **원칙: 삭제 < archive < canonical pointer 정리.** legacy는 삭제하지 않고 `archive/` 아래로 이동해 보존한다(`.DS_Store` 제외).
> 진실값(source of truth)은 항상 top-level canonical 문서가 보유한다. 이 문서는 이동 계획·근거 기록이다.

## 분류 요약

| 카테고리 | 대상 |
|---|---|
| 1. Keep top-level canonical | README, CLAUDE, CURRENT-FRAME-202606, PHD-STRATEGY-2026-2027, POSITIONING-NOTES, RELATED-WORK-MATRIX, READING-QUEUE-202606, papers.yaml, NFM-BRIDGE-PLAN, REPO-CORPUS-STATUS-20260621, PAPER-REVIEW-TEMPLATE, CLEANUP-PLAN-20260621, `.gitignore`, `md/`, `paper/`(canonical-slug PDF) |
| 2. Keep top-level but mark historical | LEGACY-CG-PAPERS.md(legacy index), CONFERENCE-TARGETS-2024-KIISE.md(venue 전략) |
| 3. Move to archive | legacy prompts(4), `contents/`·`reading/`·`summary/`, 13 legacy-named PDF, MUST-READ-PLAN, UNIFIED-PAPER-LIST, READING-GUIDE-P0, research-report-0730.txt, related-source.txt, requirements.txt, setup.sh |
| 4. Keep in place (links/usage depend) | canonical-slug PDF(`paper/2xxx-*.pdf`) — papers.yaml `source_pdf` 타깃; `md/` 노트 |
| 5. Remove untracked only | `.DS_Store` (paper repo: 없음 / root repo: `.venv/.../mistral_common/.DS_Store` 1건, gitignored) |
| 6. Do not touch | papers.yaml 내용, md 노트 내용, canonical PDF 파일명 |

## 상세 (action / reason / risk / update-needed)

### 1. Keep top-level canonical
- **README.md / CLAUDE.md / CURRENT-FRAME-202606.md / PHD-STRATEGY-2026-2027.md / POSITIONING-NOTES.md / RELATED-WORK-MATRIX.md / READING-QUEUE-202606.md / papers.yaml / NFM-BRIDGE-PLAN.md / REPO-CORPUS-STATUS-20260621.md / PAPER-REVIEW-TEMPLATE.md**
  - action: 유지. reason: 현재 source of truth + 11섹션 canonical template. risk: 없음. update: README/REPO-CORPUS-STATUS는 archive 이동 반영 링크 갱신.

### 2. Keep top-level, historical
- **LEGACY-CG-PAPERS.md** — action: 유지(legacy index 역할). risk: 내부 링크가 `paper/01-03`, `reading/01-03`, `contents/01-03`를 가리켜 이동 후 끊김. update: 링크를 archive 경로로 갱신.
- **CONFERENCE-TARGETS-2024-KIISE.md** — action: 유지. reason: 현재 venue 전략과 관련. risk: 없음. update: 없음.

### 3. Move to archive
- **legacy prompts(4)**: `paper-search-prompt-2025.08.txt`, `paper-search-prompt-2025.12.txt`, `paper-extracting-prompt-2026.01.txt`, `paper-reading-prompt-2026.01.txt`
  - → `archive/legacy-reading-pipeline-2026-01/prompts/`. reason: 2026-01 이전 search/extract/read pipeline. risk: README/REPO-CORPUS-STATUS 링크. update: 두 문서 갱신.
- **`contents/`(7), `reading/`(7), `summary/`(1)** → `archive/legacy-reading-pipeline-2026-01/{contents,reading,summary}/`. reason: 옛 PDF추출/문장단위 reading/summary 산출물. risk: LEGACY-CG-PAPERS가 `reading/01-03`,`contents/01-03` 링크; README/REPO-CORPUS-STATUS 언급. update: 세 문서 갱신.
- **13 legacy-named PDF** (`01.`~`11.` + `(ACL25) Unveiling…`, `(NAACL25) Reasoning Aware Self-Consistency…`) → `archive/legacy-paper-filenames/`. reason: canonical-slug PDF와 동일 논문(Phase 3에서 13/13 확인: 11편 sha256 동일, 2편[Distilling, Rewarding Progress]은 published↔preprint 버전 차이지만 동일 논문). risk: LEGACY-CG-PAPERS가 `paper/01-03` 링크. update: LEGACY-CG-PAPERS + archive manifest. **canonical-slug PDF는 `paper/`에 유지.**
- **MUST-READ-PLAN.md, UNIFIED-PAPER-LIST.md, READING-GUIDE-P0.md** → `archive/legacy-plans/`. reason: 이미 non-canonical notice 보유, active queue 아님. risk: README/REPO-CORPUS-STATUS 링크. update: 두 문서 갱신.
- **research-report-0730.txt, related-source.txt** → `archive/legacy-reports/`. reason: CG-시기 research report / venue-journal source list(현재 운영 문서 아님). risk: 낮음. update: archive manifest.
- **requirements.txt, setup.sh** → `archive/legacy-reports/`. reason: 옛 `LM-based-KG-papers` conda 환경 setup(현재 paper-reading workflow는 root `.venv` 사용, 미사용). risk: 낮음(현재 어떤 워크플로도 참조 안 함). update: archive manifest.

### 5. Remove untracked `.DS_Store` only
- paper repo: tracked/untracked 모두 0건. root repo: `.venv/lib/python3.12/site-packages/mistral_common/.DS_Store` 1건(gitignored) → 삭제(파일은 `.DS_Store`만).

## Phase 3 PDF 검증 결과 (13/13 same-paper)
- sha256 동일(11): Self-Instruct, Phased-IFT, Scaling-TTC, PRM-That-Think, Let's-Verify, UniCoTT, MAGDi, Mentor-KD, SWITCH, Unveiling-CoT, RASC.
- 버전 차이지만 동일 논문(2): **Distilling Step-by-Step**(legacy 15p Findings-ACL ↔ canon 13p preprint), **Rewarding Progress**(legacy 31p ICLR2025 ↔ canon 31p 2024-10-11 preprint). → archive manifest에 버전 차이 명시. canonical(source_pdf) 유지, legacy 보존.
- 보류(이동 금지) 항목: 없음.

## Filename mismatch (manifest에 명시)
- **SWITCH**: legacy 파일명 `(EMNLP25)` ↔ canonical venue **NAACL 2025 Findings**(legacy 파일명이 오기).

## 이동 후 링크 갱신 대상
- `README.md`, `LEGACY-CG-PAPERS.md`, `REPO-CORPUS-STATUS-20260621.md`, 그리고 신규 `archive/README.md` + `archive/legacy-reading-pipeline-2026-01/README.md`.

_작성: 2026-06-21. 이동은 이 계획에 따라 `git mv`로만 수행하고 삭제하지 않는다._
