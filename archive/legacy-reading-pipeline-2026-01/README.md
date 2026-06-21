# legacy-reading-pipeline-2026-01/

> 2026-01 이전의 **PDF extraction → sentence-level reading → summary** pipeline 잔존물.
> 현재 canonical workflow(11섹션 Strategic Reading Note `../../md/` + `../../papers.yaml`)로 대체되었다.
> **historical only — active queue로 사용하지 않는다.**

## 남은 내용 (2026-06-21 simplification 후)

- `reading/` (7) — 문장단위 reading 노트(`01`~`05R`; `04R`/`05R`는 보조 `.pdf` 포함).
  - canonical 11섹션 노트(`../../md/`)의 보조 historical 기록일 뿐, source of truth가 아니다.

## 2026-06-21에 삭제된 것 (superseded)

- `prompts/` (4) — 옛 search/extract/read pipeline 프롬프트. 현재는 root `../../../prompts/` + `../../PAPER-REVIEW-TEMPLATE.md`가 canonical.
- `contents/` (7) — raw PDF 추출 텍스트. canonical `md/` 노트가 PDF를 직접 재추출하므로 불필요.
- `summary/` (1) — 중간 요약본. canonical 노트로 대체.

_삭제 사유: canonical 산출물로 완전히 대체되어 유지보수 가치가 없는 중간 산출물._
