# REPO CORPUS STATUS — 2026-06-21

> deep-interview / 2026-06-25 연구미팅 직전, `SLM-Math-papers` corpus의 canonical 상태를 점검·고정한 audit 문서다.
> 목적은 새 논문을 더 읽는 것이 아니라, 이미 수집·정리한 관련연구 corpus를 바로 쓸 수 있게 canonicalize하는 것이다.
> 이번 작업에서 legacy 자료는 삭제·rename하지 않았다.

## 0. 현재 canonical research frame

- CG superiority가 아니라 **heterogeneous reasoning path pool construction**.
- **limited TTC under fixed backbone**.
- **state-conditioned macro strategy allocation**.
- **STOP under limited TTC**.
- **verifier / voting-aware final decision**.
- **NFM은 thesis core가 아니라 application/bridge domain**.

---

## 1. Current canonical files

| 파일 | 역할 |
|---|---|
| `papers.yaml` | canonical paper registry (구조화 metadata, 18 필드 + `source_pdf`). **39 entries, 모두 strategically-read.** |
| `READING-QUEUE-202606.md` | active reading/status queue (P0/P1/P2). |
| root `CURRENT-READING.md` | active 완료/배경 상태 + reflection 기록 (paper repo commit hash 연결). |
| `RELATED-WORK-MATRIX.md` | 관련연구 비교표(novelty risk / 빌릴 요소 / 차이). |
| `POSITIONING-NOTES.md` | 하면 안 되는 주장 + 안전한 contribution framing. |
| `CURRENT-FRAME-202606.md` | 현재 연구 프레임 canonical 문서. |
| `NFM-BRIDGE-PLAN.md` | NFM을 bridge/application으로만 붙이는 plan. |
| `md/` (39 notes) | 11섹션 Strategic Reading Note 본문. |
| `paper/` (canonical-slug PDF) | 원본 PDF source-of-record. |
| `PAPER-REVIEW-TEMPLATE.md` | 11섹션 템플릿 미러 (canonical 원본은 root `prompts/paper-strategic-note-template.md`). |
| `PHD-STRATEGY-2026-2027.md` | 졸업/논문화 전략 (math main + NFM bridge 관계). |

## 2. Legacy / historical files (보존, active 아님)

| 파일/디렉터리 | 비고 |
|---|---|
| `paper-search-prompt-2025.08.txt`, `paper-search-prompt-2025.12.txt` | legacy search pipeline prompt. |
| `paper-extracting-prompt-2026.01.txt`, `paper-reading-prompt-2026.01.txt` | legacy extract/read pipeline prompt. |
| `contents/` (7), `reading/` (7), `summary/` (1) | 2026-01 pipeline 산출물. |
| `paper/` 의 `01.`~`11.` 번호 PDF (11개) + `(ACL25) Unveiling…`, `(NAACL25) Reasoning Aware Self-Consistency…` (2개) | legacy-named PDF. canonical-slug 사본 존재. |
| `MUST-READ-PLAN.md`, `UNIFIED-PAPER-LIST.md` | non-canonical 보조 인덱스 (상단 status note 보유). |
| `READING-GUIDE-P0.md` | 2026-01 P0 읽기 가이드 (2026-06-21 deprecated notice 추가). |
| `LEGACY-CG-PAPERS.md`, `CONFERENCE-TARGETS-2024-KIISE.md`, `related-source.txt`, `research-report-0730.txt` | 역사적 참고. |

## 3. Current note corpus summary

- `md/*.md` 노트 **39편**, 전부 `## 11.` 마커를 가진 **11섹션 구조**.
- 정합 상태: 39 노트 ↔ 39 `papers.yaml` entries (모두 `strategically-read`).
- **Source Grounding Log 보유: 19/39.** 나머지 20편(주로 초기 batch의 math mainline / verifier cluster: CoT, ToRA, Self-Consistency, DeepSeek-R1, DeepSeekMath, s1, RASC, Confidence, Learning-How-Hard, Scaling-TTC, Let's-Verify, Math-Shepherd, PRM-That-Think, Self-Discover, Automatic-Model-Selection, PAL, PoT, ToT, rStar-Math)는 11섹션이되 명시적 Source Grounding Log subsection이 없음 → **normalization backlog**(§9). 이번 작업에서 추측 stub을 넣지 않음.

## 4. Paper PDF corpus summary

- `paper/` PDF **48개** = canonical-slug **35** + legacy 번호(`01.`~`11.`) **11** + legacy 괄호명 **2**.
- canonical-slug 35개는 `papers.yaml`의 `source_pdf` 35개와 **1:1 매핑**.
- `papers.yaml` 35/39 entries가 `source_pdf` 보유. 나머지 4편(DeepSeek-R1, Chain-of-Thought, Self-Consistency, ToRA)은 **local canonical PDF가 없어** arXiv/원문 grounding으로 둠(추측 추가하지 않음).
- 2026-06-21 이번 작업에서 **14편**에 `source_pdf`를 신규 연결(아래 §9-A). 모두 PDF 첫 페이지 title을 직접 추출해 entry title과 일치 확인 후 추가(grounded, insertion-only).

## 5. Known duplicate PDF policy

- legacy-named PDF(`01.`~`11.` + 괄호명 2개, 총 13개)는 canonical-slug 사본이 존재한다.
- **source-of-record = canonical-slug PDF**(예: `paper/2025-switch.pdf`). `papers.yaml`의 `source_pdf`는 canonical-slug만 가리킨다.
- legacy-named PDF는 **삭제·rename하지 않고 보존**(원본 다운로드 이력/대조용). 중복이지만 의도된 보존이다.

## 6. Known legacy filename mismatch

| 항목 | legacy 표기 | canonical(검증) |
|---|---|---|
| SWITCH | `paper/11. (EMNLP25) SWITCH…pdf` | **NAACL 2025 Findings** (yaml `venue: "NAACL 2025 Findings"`, note에 "legacy filename EMNLP25 is wrong" 기록) |
| Mentor-KD | `paper/10. (EMNLP24) Mentor-KD…pdf` | EMNLP 2024 (일치) |
| ThinkPRM(Process Reward Models That Think) | `paper/06. (Arxiv25) …pdf` | arXiv 2025 (일치) |
| 그 외 `01.`~`09.` | 괄호 venue 표기 | canonical metadata는 `papers.yaml` 기준이 우선 |

- 원칙: **venue 진실값은 `papers.yaml` / `md/` 노트**가 가지며, legacy 파일명은 참고용일 뿐. 파일명은 rename 금지.

## 7. Current source of truth

1. `papers.yaml` — 구조화 metadata registry.
2. `READING-QUEUE-202606.md` — 누적 paper-repo 읽기/상태 기록.
3. root `CURRENT-READING.md` — active queue + 완료/배경 상태(권위).
4. `RELATED-WORK-MATRIX.md` — 관련연구 비교/claim boundary.
5. `POSITIONING-NOTES.md` — 금지 주장 / framing.

## 8. Files NOT to use as active queue

- `MUST-READ-PLAN.md` (historical must-read plan)
- `UNIFIED-PAPER-LIST.md` (secondary/legacy 통합 인덱스)
- `READING-GUIDE-P0.md` (2026-01 early pipeline, deprecated)
- legacy prompts (`paper-search-prompt-*.txt`, `paper-extracting-prompt-*.txt`, `paper-reading-prompt-*.txt`)

→ 위 문서로 unread/read를 판단하지 말 것. 상태 판단은 §7로만.

## 9. Remaining optional cleanup items (normalization backlog)

이번 작업 범위 밖(노트 내용 대규모 rewrite 금지)이라 backlog로만 기록한다.

- **(A) source_pdf 신규 연결 완료(2026-06-21):** rStar-Math, DeepSeekMath, s1, RASC, Confidence-Improves-SC, Learning-How-Hard-to-Think, Scaling-LLM-TTC, Let's-Verify, Math-Shepherd, Process-Reward-Models-That-Think, Self-Discover, Automatic-Model-Selection, PAL, Program-of-Thoughts — 14편. (PDF title 직접 확인 후 grounded insertion.)
- **(B) Source Grounding Log 미보유 20편:** 11섹션이되 명시 grounding log subsection 없음. 향후 노트별로 PDF page/sha256 + arXiv/HF 교차근거를 stub으로 보강(확인 가능한 source만). 지금은 추측 금지로 미수행.
- **(C) source_pdf 없는 4편**(DeepSeek-R1, CoT, Self-Consistency, ToRA): local canonical PDF 미보유. 필요 시 추후 PDF 확보하면 연결.
- **(D) `code_url` 빈 값 일부**(예: TeleTables/TeleLogs): 공식 코드 미확인. 확인 시 보강. drift 아님(추측 금지로 빈 값 유지).
- **(E) TeleMath venue 표기**: `arXiv`(번호 없음)로, 다른 Tele* 항목(`arXiv 2601.04202` 등)과 입도가 다름. arXiv id 확인 시 통일 고려.
- **(F) TeleResilienceBench**: `papers.yaml`/queue/note에는 NFM extension(P2)으로 반영됐으나 `NFM-BRIDGE-PLAN.md` 본문 stage table에는 미등재. 필요 시 extension 행 1줄 추가(필수 아님).

## 10. Deep-interview readiness summary

- **Related work corpus is READY.** 39편 strategically-read, `papers.yaml`/queue/matrix/positioning 정합, claim boundary(무엇을 우리 novelty로 쓰면 안 되는지)와 NFM bridge 경계가 문서화됨.
- **다음 단계는 새 논문 reading이 아니라 experiment direction convergence다.** 구체적으로: heterogeneous path-pool 구성, state-conditioned macro strategy allocation, STOP policy, generation-verification budget split / voting-aware decision의 실험 설계로 수렴.
- deep-interview에서 먼저 볼 파일: `CURRENT-FRAME-202606.md` → `POSITIONING-NOTES.md` → `RELATED-WORK-MATRIX.md` → `READING-QUEUE-202606.md`(+root `CURRENT-READING.md`) → `NFM-BRIDGE-PLAN.md`.

---

_마지막 갱신: 2026-06-21. 이 문서는 corpus 상태 snapshot이며, 진실값 자체는 §7 문서들이 보유한다._
