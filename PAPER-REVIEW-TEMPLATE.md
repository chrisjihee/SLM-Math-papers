# Strategic Reading Note 템플릿 (11섹션)

> **Canonical 원본:** root `prompts/paper-strategic-note-template.md` 가 이 템플릿의 source of truth다.
> 이 파일은 paper repo에서 바로 복사해 쓰기 위한 **11섹션 미러**이며, 두 파일은 같은 구조를 유지한다.
> (2026-06-21 갱신) 이전의 16섹션 리뷰 템플릿은 폐기되었다. 모든 `md/*.md` 노트는 아래 11섹션 구조를 따른다.

## 작성 규칙 (필수)

- 섹션명과 순서를 바꾸지 않는다. 11개 섹션을 모두 채운다.
- 일반 요약이 아니라 SLM-Math의 **novelty risk / what-not-to-claim / baseline / ablation / Related Work 배치**를 중심으로 쓴다.
- 한국어로 작성하되 논문 제목·method·benchmark·model 이름은 영어 원문을 유지한다.
- `Source Grounding Log`에는 실제로 확인한 근거(local PDF + page/sha256, arXiv abstract, HF dataset card 등)만 기록한다. 확인하지 못한 source는 적지 않는다.
- priority는 `CURRENT-READING.md`, `READING-QUEUE-202606.md`, `papers.yaml` 의 현재 분류를 우선 따른다. 변경 제안은 본문에 `재분류 제안`으로만 적고 임의로 바꾸지 않는다.
- 피해야 할 주장: `CG > CoT`, adaptive TTC 자체 novelty, self-consistency efficiency 자체 novelty, verifier/reranker 도입 자체 novelty, SLM math reasoning 자체 novelty, long-CoT/self-verification 자체 novelty, tool-use reasoning 자체 novelty, heavy MCTS/self-evolution 자체가 우리 contribution.

---

# <Paper Title> review

## 1. Metadata

- Title:
- Authors:
- Year:
- Venue / Status:
- Links:
  - Paper:
  - GitHub / Model:
- Code / Data:
- Source PDF (local, source-of-record): `paper/<slug>.pdf`  (없으면 "없음 — arXiv/HF로 grounding")
- Source Grounding Log:
  - PDF: `paper/<slug>.pdf` — N pages, sha256 `...`, pypdf/pymupdf 본문 추출 정상. title/authors/abstract/method/metric 직접 확인.
  - arXiv abstract / HF dataset card: 교차확인 항목.
  - arXiv TeX/ar5iv: 사용/미사용. official code URL: 확인/미확인.
- Paper Type:
- Reading Status: `strategically-read`
- Current Priority: `<P0 / P1 / P2>`

## 2. One-line Summary

## 3. 핵심 문제 설정

## 4. 핵심 방법

## 5. SLM-Math 관점의 재해석

- (limited TTC / heterogeneous reasoning path pool / state-conditioned macro strategy allocation / STOP / verifier·voting-aware decision 중 무엇과 연결되는가)
- (selection unit: sample / answer / rationale / step / strategy / model / tool)
- (NFM이면 thesis core가 아니라 bridge/application 임을 명시)

## 6. 우리 연구에 대한 novelty risk

- 위협도:
- 경계(이렇게 쓰면 안 되는 wording):

## 7. 우리가 빌릴 수 있는 것

- framing / baseline / metric / ablation / terminology:

## 8. 우리가 하면 안 되는 주장

## 9. baseline / ablation 반영 아이디어

## 10. Related Work에 넣을 문장 초안

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `<P0 / P1 / P2>`
- 위협도: `높음 / 중간 / 낮음`
- 지금 당장 해야 할 일:
- 나중으로 미뤄도 되는 일:
- 한 문장 결론:
