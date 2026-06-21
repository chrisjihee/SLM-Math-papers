# archive/ — legacy 자료 보존소 (2026-06-21 정리)

> 이 디렉터리는 `SLM-Math-papers`의 **historical context**를 보존한다.
> **active queue / current claim boundary 판단에 사용하지 않는다.** 삭제하지 않고 보존만 한다.
> 진실값(source of truth)은 항상 top-level canonical 문서가 보유한다.

## 현재 source of truth (archive 아님)

- registry: `../papers.yaml`
- active queue: `../READING-QUEUE-202606.md` + root `../../CURRENT-READING.md`
- positioning: `../RELATED-WORK-MATRIX.md`, `../POSITIONING-NOTES.md`
- frame: `../CURRENT-FRAME-202606.md`
- corpus status: `../REPO-CORPUS-STATUS-20260621.md`
- 이동 계획/근거: `../CLEANUP-PLAN-20260621.md`
- 노트 본문: `../md/`, canonical PDF: `../paper/`(canonical-slug)

## 구조

### `legacy-reading-pipeline-2026-01/`
2026-01 이전 PDF extraction / sentence-level reading / summary pipeline 산출물.
- `prompts/` — `paper-search-prompt-2025.08.txt`, `paper-search-prompt-2025.12.txt`, `paper-extracting-prompt-2026.01.txt`, `paper-reading-prompt-2026.01.txt`
- `contents/` (7) — 원문 추출 텍스트/마크다운
- `reading/` (7) — 문장단위 reading 요약(일부 `*R*` PDF 포함)
- `summary/` (1) — 요약본
- 상세: `legacy-reading-pipeline-2026-01/README.md`

### `legacy-paper-filenames/` (13 PDF)
canonical-slug PDF(`../paper/2xxx-*.pdf`)와 **동일 논문**인 old numbered/괄호명 PDF. 보존용 중복본.
- canonical PDF는 `../paper/`에 유지되며 `papers.yaml.source_pdf`가 그쪽을 가리킨다.
- 2026-06-21 검증: 13편 모두 canonical과 same-paper.
  - sha256 동일(11): `01.Self-Instruct`, `03.Phased-IFT`, `04.Scaling-TTC`, `06.PRM-That-Think`, `07.Let's-Verify`, `08.UniCoTT`, `09.MAGDi`, `10.Mentor-KD`, `11.SWITCH`, `(ACL25)Unveiling`, `(NAACL25)RASC`.
  - 버전 차이(같은 논문, 2): `02.Distilling Step-by-Step`(legacy 15p Findings-ACL ↔ canon 13p preprint), `05.Rewarding Progress`(legacy 31p ICLR2025 ↔ canon 31p preprint). published 버전을 보고 싶을 때 여기서 찾는다.
- **Filename 주의**: `11. (EMNLP25) SWITCH …` 의 `(EMNLP25)`는 오기다. canonical venue는 **NAACL 2025 Findings**(`../papers.yaml`, `../md/2025-switch.md` 기준).

### `legacy-plans/`
현재 active queue가 아닌 historical plan/list(이미 non-canonical notice 보유).
- `MUST-READ-PLAN.md` — 2026-06-14 framing 단계 must-read plan.
- `UNIFIED-PAPER-LIST.md` — secondary/legacy 통합 인덱스.
- `READING-GUIDE-P0.md` — 2026-01 P0 읽기 가이드(deprecated).

### `legacy-reports/`
현재 canonical 운영 문서가 아닌 기록.
- `research-report-0730.txt` — CG-기반 초기 연구 report.
- `related-source.txt` — venue/journal source list.
- `requirements.txt`, `setup.sh` — 옛 `LM-based-KG-papers` conda 환경 setup(현재 워크플로 미사용; 현재는 root `.venv` 사용).

_2026-06-21 physical cleanup. 이동은 `git mv`로만 수행했고 삭제한 파일은 없다(`.DS_Store` 제외)._
