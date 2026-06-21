# archive/ — legacy 자료 보존소 (2026-06-21)

> 이 디렉터리는 `SLM-Math-papers`의 **historical context**를 보존한다.
> **active queue / current claim boundary 판단에 사용하지 않는다.**
> 진실값(source of truth)은 항상 top-level canonical 문서가 보유한다.

## 현재 source of truth (archive 아님)

- registry: `../papers.yaml`
- active queue: `../READING-QUEUE-202606.md` + root `../../CURRENT-READING.md`
- positioning: `../RELATED-WORK-MATRIX.md`, `../POSITIONING-NOTES.md`
- frame: `../CURRENT-FRAME-202606.md`
- corpus status: `../REPO-CORPUS-STATUS-20260621.md`
- 노트 본문: `../md/`, canonical PDF: `../paper/`(canonical-slug)

## 구조 (2026-06-21 simplification 후)

### `maintenance/`
- `CLEANUP-PLAN-20260621.md` — 1차 archive split 계획서(역사적 기록).

### `legacy-cg-phase/`
- `LEGACY-CG-PAPERS.md` — 2026-01 전후 CG-centric phase의 historical index. 내부 링크는 canonical `../../paper/`·`../../md/`로 정리됨.

### `legacy-plans/` (3)
현재 active queue가 아닌 historical plan/list(상단 non-canonical notice 보유).
- `MUST-READ-PLAN.md`, `UNIFIED-PAPER-LIST.md`, `READING-GUIDE-P0.md`.

### `legacy-reading-pipeline-2026-01/`
2026-01 이전 reading pipeline 잔존물. contents/·summary/와 search 프롬프트 2개는 2026-06-21에 삭제(canonical `../md/`로 대체). 남은 것:
- `reading/` (7) — 문장단위 reading 노트(`01`~`05R`, `04R`/`05R`는 보조 PDF 포함). **historical only, source of truth 아님.**
- `prompts/` (2, 복원) — **Gemini focused-reading utility**(`paper-extracting-prompt`/`paper-reading-prompt`). 특정 논문 PDF를 Gemini로 매우 깊게 추출·문장 단위 독해할 때만 선택적으로 쓴다. **canonical workflow 아님**(canonical은 `../PAPER-REVIEW-TEMPLATE.md` + `../md/*.md` 11섹션).

### `legacy-paper-filenames/` (2)
canonical-slug PDF와 sha256이 **다른**(published↔preprint) legacy PDF만 보존.
- `02. Distilling Step-by-Step …` (published Findings-ACL 2023; canonical preprint은 `../../paper/2023-distilling-step-by-step.pdf`)
- `05. Rewarding Progress …` (published ICLR 2025; canonical은 `../../paper/2025-rewarding-progress.pdf`)
- 나머지 11편(`01,03,04,06,07,08,09,10,11` + `(ACL25)Unveiling`, `(NAACL25)RASC`)은 sha256 완전 동일 → 2026-06-21 삭제(canonical로 대체).

### `legacy-reports/` (3)
현재 운영 문서가 아닌 기록.
- `research-report-0730.txt` — CG-기반 초기 연구 report.
- `related-source.txt` — venue/journal source list.
- `CONFERENCE-TARGETS-2024-KIISE.md` — 정보과학회 venue 목록(core 요약은 `../PHD-STRATEGY-2026-2027.md` §7에 보존).
- (`requirements.txt`, `setup.sh`는 옛 `LM-based-KG-papers` conda env 파일로 2026-06-21 삭제 — 현재는 root `.venv` 사용.)

## 삭제 정책 요약 (2026-06-21 simplification)

- **removed as exact duplicates:** canonical과 sha256 동일한 legacy PDF 11편.
- **removed as superseded intermediates:** 옛 search prompt 2 + raw contents 7 + summary 1 + env 2 = 12개.
- **restored as optional utility:** Gemini focused-reading prompt 2 (`paper-extracting-prompt`, `paper-reading-prompt`) — canonical workflow 아님.
- **preserved (historical only):** version-different PDF 2, reading 노트 7, plans 3, reports 3, cg-phase index 1, maintenance plan 1.

_이동/삭제는 모두 의도적이며, canonical 산출물(`../paper/`, `../md/`, `../papers.yaml`)은 영향받지 않았다._
