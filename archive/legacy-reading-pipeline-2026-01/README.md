# legacy-reading-pipeline-2026-01/

> 2026-01 이전의 **PDF extraction → sentence-level reading → summary** pipeline 산출물 보존소.
> 현재 canonical workflow(11섹션 Strategic Reading Note `../../md/` + `../../papers.yaml`)로 대체되었다.
> historical context로만 보존하며 active queue로 사용하지 않는다.

## 내용

- `prompts/` (4) — 옛 search/extract/read pipeline 프롬프트
  - `paper-search-prompt-2025.08.txt`, `paper-search-prompt-2025.12.txt`
  - `paper-extracting-prompt-2026.01.txt`, `paper-reading-prompt-2026.01.txt`
- `contents/` (7) — 원문 추출 텍스트(`01.`~`07.`, `.txt`/`.md`)
- `reading/` (7) — 문장단위 reading 노트(`01.`~`05R.`; `04R.`/`05R.`는 보조 `.pdf` 포함)
- `summary/` (1) — `04.` 요약본

## 현재 프레임에서의 위치

- 여기 정리된 논문 중 다수(Self-Instruct, Distilling Step-by-Step, Phased-IFT, Scaling-TTC, Rewarding Progress, PRM-That-Think, Let's-Verify 등)는 이미 `../../md/`에 11섹션 strategic note로 재작성되어 `papers.yaml`에 반영되어 있다.
- 따라서 이 폴더는 **재작성 이전의 원자료/요약 기록**이며, 최신 상태·우선순위는 `../../READING-QUEUE-202606.md`와 root `../../../CURRENT-READING.md`를 본다.

_2026-06-21 이동(`git mv`). 삭제 없음._
