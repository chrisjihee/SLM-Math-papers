# legacy-reading-pipeline-2026-01/

> 2026-01 이전의 **PDF extraction → sentence-level reading → summary** pipeline 잔존물.
> 현재 canonical workflow(11섹션 Strategic Reading Note `../../md/` + `../../papers.yaml`)로 대체되었다.
> **historical only — active queue로 사용하지 않는다.**

## 남은 내용 (2026-06-21 simplification 후)

- `reading/` (7) — 문장단위 reading 노트(`01`~`05R`; `04R`/`05R`는 보조 `.pdf` 포함).
  - canonical 11섹션 노트(`../../md/`)의 보조 historical 기록일 뿐, source of truth가 아니다.
- `prompts/` (2, 복원) — **Gemini focused-reading utility**:
  - `paper-extracting-prompt-2026.01.txt` — 논문 PDF 본문을 구조적으로 추출.
  - `paper-reading-prompt-2026.01.txt` — 문장 단위로 공부하듯 읽어 철저한 마크다운 독해 문서 작성.
  - **canonical workflow 아님.** routine paper registry update / deep-interview에는 쓰지 않는다. 특정 논문 PDF를 Gemini로 매우 깊게 읽고 본문 추출·문장 단위 독해가 필요할 때만 선택적으로 사용한다. current canonical strategic note는 여전히 `../../PAPER-REVIEW-TEMPLATE.md` + `../../md/*.md` 11섹션 구조다.

## 2026-06-21에 삭제된 것 (superseded)

- `prompts/` 중 search 계열 2개 (`paper-search-prompt-2025.08.txt`, `paper-search-prompt-2025.12.txt`) — 옛 search pipeline 프롬프트. 복원하지 않음.
- `contents/` (7) — raw PDF 추출 텍스트. canonical `md/` 노트가 PDF를 직접 재추출하므로 불필요.
- `summary/` (1) — 중간 요약본. canonical 노트로 대체.

_삭제 사유: canonical 산출물로 완전히 대체되어 유지보수 가치가 없는 중간 산출물. extract/reading 프롬프트 2개만 optional focused-reading utility로 복원._
