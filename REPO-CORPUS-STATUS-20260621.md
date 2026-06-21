# REPO CORPUS STATUS — 2026-06-21

> deep-interview / 2026-06-25 연구미팅 직전, `SLM-Math-papers` corpus의 canonical 상태를 점검·고정한 audit 문서다.
> 목적은 새 논문을 더 읽는 것이 아니라, 이미 수집·정리한 관련연구 corpus를 바로 쓸 수 있게 canonicalize하는 것이다.
>
> **갱신 이력:**
> - (1차 archive split) legacy 자료를 `archive/` 로 `git mv` 이동(삭제 0).
> - (2차 simplification, 같은 날) maintenance-cost 축소를 위해 **exact-duplicate legacy PDF 11편 + 옛 env/prompt/contents/summary 산출물 삭제**, 그리고 `CLEANUP-PLAN`/`LEGACY-CG-PAPERS`/`CONFERENCE-TARGETS`를 archive로 이동. version-different legacy PDF 2편(Distilling, Rewarding Progress)과 문장단위 reading 노트는 보존. 삭제/보존 목록은 아래 §11.

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

> **(2026-06-21 update)** 아래 legacy 자료는 `archive/` 로 물리 이동했다. 개요: `archive/README.md`. 상세 계획(1차)·simplification 기록: `archive/maintenance/CLEANUP-PLAN-20260621.md`.

| 파일/디렉터리 (현재 위치) | 비고 |
|---|---|
| `archive/legacy-reading-pipeline-2026-01/prompts/` (4 txt) | legacy search/extract/read pipeline prompt. |
| `archive/legacy-reading-pipeline-2026-01/{contents,reading,summary}/` (7/7/1) | 2026-01 pipeline 산출물. |
| `archive/legacy-paper-filenames/` (13 PDF) | 옛 번호(`01.`~`11.`) + 괄호명 2개. canonical-slug PDF와 동일 논문(검증 완료). canonical은 `paper/` 유지. |
| `archive/legacy-plans/MUST-READ-PLAN.md`, `archive/legacy-plans/UNIFIED-PAPER-LIST.md` | non-canonical 보조 인덱스 (상단 status note 보유). |
| `archive/legacy-plans/READING-GUIDE-P0.md` | 2026-01 P0 읽기 가이드 (deprecated notice 보유). |
| `archive/legacy-reports/{research-report-0730.txt, related-source.txt}` | 옛 report / source list. (`requirements.txt`, `setup.sh`는 2026-06-21 삭제) |
| `archive/legacy-reports/CONFERENCE-TARGETS-2024-KIISE.md` | venue 전략. core 요약은 top-level `PHD-STRATEGY-2026-2027.md` §7에 보존. |
| `archive/legacy-cg-phase/LEGACY-CG-PAPERS.md` | CG-centric phase 역사적 index. 링크는 canonical `paper/`·`md/`로 정리됨. |
| `archive/maintenance/CLEANUP-PLAN-20260621.md` | 1차 archive split 계획서(역사적). |

## 3. Current note corpus summary

- `md/*.md` 노트 **39편**, 전부 `## 11.` 마커를 가진 **11섹션 구조**.
- 정합 상태: 39 노트 ↔ 39 `papers.yaml` entries (모두 `strategically-read`).
- **Source Grounding Log 보유: 19/39.** 나머지 20편(주로 초기 batch의 math mainline / verifier cluster: CoT, ToRA, Self-Consistency, DeepSeek-R1, DeepSeekMath, s1, RASC, Confidence, Learning-How-Hard, Scaling-TTC, Let's-Verify, Math-Shepherd, PRM-That-Think, Self-Discover, Automatic-Model-Selection, PAL, PoT, ToT, rStar-Math)는 11섹션이되 명시적 Source Grounding Log subsection이 없음 → **normalization backlog**(§9). 이번 작업에서 추측 stub을 넣지 않음.

## 4. Paper PDF corpus summary

- **(2026-06-21 simplification 후)** `paper/` = canonical-slug **35개만**. `archive/legacy-paper-filenames/`에는 version-different legacy PDF **2개**만 보존(Distilling Step-by-Step, Rewarding Progress). exact-duplicate legacy PDF 11편은 삭제.
- canonical-slug 35개는 `papers.yaml`의 `source_pdf` 35개와 **1:1 매핑** (전수 resolve 확인).
- `papers.yaml` 35/39 entries가 `source_pdf` 보유. 나머지 4편(DeepSeek-R1, Chain-of-Thought, Self-Consistency, ToRA)은 **local canonical PDF가 없어** arXiv/원문 grounding으로 둠(추측 추가하지 않음).
- 그 외 archive PDF 2개: `archive/legacy-reading-pipeline-2026-01/reading/{04R,05R}…pdf`(reading 노트 보조본). → archive PDF 합계 **4개**.

## 5. Known duplicate PDF policy

- 옛 legacy-named PDF 13편은 canonical-slug 사본과 **동일 논문**이었다(검증: 11편 sha256 동일, 2편 published↔preprint 버전 차이).
- **source-of-record = canonical-slug PDF**(예: `paper/2025-switch.pdf`). `papers.yaml`의 `source_pdf`는 canonical-slug만 가리킨다.
- 정책(2026-06-21 simplification): **sha256 완전 동일한 11편은 삭제**(canonical로 완전 대체). **버전이 다른 2편(Distilling Step-by-Step published Findings-ACL, Rewarding Progress published ICLR2025)만 `archive/legacy-paper-filenames/`에 보존** — published 버전 보존 가치.

## 6. Known legacy filename mismatch

> 옛 legacy 파일명 13편 중 11편은 삭제됨. 아래는 historical 기록(파일명 진실값은 `papers.yaml`/`md/` 기준).

| 항목 | 옛 legacy 파일명 | canonical(검증) |
|---|---|---|
| SWITCH | `11. (EMNLP25) SWITCH…pdf` (삭제됨) | **NAACL 2025 Findings** (yaml `venue: "NAACL 2025 Findings"`, `md/2025-switch.md`에 "legacy filename EMNLP25 is wrong" 기록) |
| Mentor-KD | `10. (EMNLP24) Mentor-KD…pdf` (삭제됨) | EMNLP 2024 (일치) |
| ThinkPRM(Process Reward Models That Think) | `06. (Arxiv25) …pdf` (삭제됨) | arXiv 2025 (일치) |
| Distilling / Rewarding Progress | `02.`/`05.` (archive 보존) | Findings-ACL 2023 / ICLR 2025 (published 버전) |

- 원칙: **venue 진실값은 `papers.yaml` / `md/` 노트**가 가지며, 옛 파일명은 참고용일 뿐.

## 7. Current source of truth

1. `papers.yaml` — 구조화 metadata registry.
2. `READING-QUEUE-202606.md` — 누적 paper-repo 읽기/상태 기록.
3. root `CURRENT-READING.md` — active queue + 완료/배경 상태(권위).
4. `RELATED-WORK-MATRIX.md` — 관련연구 비교/claim boundary.
5. `POSITIONING-NOTES.md` — 금지 주장 / framing.

## 8. Files NOT to use as active queue (모두 `archive/` 로 이동)

- `archive/legacy-plans/MUST-READ-PLAN.md` (historical must-read plan)
- `archive/legacy-plans/UNIFIED-PAPER-LIST.md` (secondary/legacy 통합 인덱스)
- `archive/legacy-plans/READING-GUIDE-P0.md` (2026-01 early pipeline, deprecated)
- `archive/legacy-reading-pipeline-2026-01/prompts/*` (legacy search/extract/read prompts)

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

## 11. 2026-06-21 simplification — deleted / preserved

**삭제 (총 25개, exact-duplicate / superseded intermediates):**
- exact-duplicate legacy PDF **11편** (`archive/legacy-paper-filenames/` 의 `01,03,04,06,07,08,09,10,11` + `(ACL25)Unveiling`, `(NAACL25)RASC`) — canonical-slug PDF와 sha256 완전 동일.
- 옛 환경 setup **2개** (`requirements.txt`, `setup.sh` — `LM-based-KG-papers` conda env, 현재 미사용).
- 옛 pipeline 산출물 **12개**: prompts 4 (`paper-search/extracting/reading-prompt`), contents 7 (raw 추출 텍스트), summary 1. canonical `md/`로 대체됨.

**보존 (active source of truth 아님, historical):**
- version-different legacy PDF **2편**: `archive/legacy-paper-filenames/{02 Distilling(Findings-ACL), 05 Rewarding Progress(ICLR2025)}` — published 버전.
- 문장단위 reading 노트 **7개**: `archive/legacy-reading-pipeline-2026-01/reading/` (04R/05R 보조 PDF 포함). canonical 11섹션 노트의 보조 historical only.
- archive로 이동: `legacy-plans/`(3), `legacy-reports/`(research-report, related-source, CONFERENCE-TARGETS), `legacy-cg-phase/LEGACY-CG-PAPERS.md`, `maintenance/CLEANUP-PLAN-20260621.md`.

---

_마지막 갱신: 2026-06-21(simplification pass). 이 문서는 corpus 상태 snapshot이며, 진실값 자체는 §7 문서들이 보유한다._
