# SLM-Math Papers

이 저장소는 `SLM-Math`의 관련 연구를 추적하고, 선택적으로 `NFM` 브리지 가능성을 정리하기 위한 문헌/포지셔닝 저장소다.

현재 기준점은 **2026-06 이후 연구 프레임**이다.

- 이 저장소의 메인 질문은 더 이상 "CG가 CoT보다 우월한가"가 아니다.
- 현재 메인라인은 **수학 추론에서 heterogeneous reasoning path pool을 어떻게 구성하고, 제한된 테스트타임 계산량 안에서 어떤 path를 선택·검증·중단할 것인가**다.
- `CG`는 삭제하지 않는다. 다만 **여러 structured reasoning path family 중 하나**로 보존한다.
- `NFM`은 본 thesis의 대체 주제가 아니라, **선별된 application/bridge domain**으로만 다룬다.

## Canonical source of truth (2026-06-21 기준)

현재 corpus의 single source of truth는 아래 5개다. deep-interview / 연구미팅 준비는 이 파일들만 보면 된다.

1. **[papers.yaml](papers.yaml)** — canonical paper registry. 모든 strategically-read 논문의 구조화 metadata(18 필드 + `source_pdf`)가 여기에 있다. (현재 39 entries)
2. **[READING-QUEUE-202606.md](READING-QUEUE-202606.md)** + root **`CURRENT-READING.md`** — active reading/status queue. unread/read 판단은 이 둘로만 한다.
3. **[RELATED-WORK-MATRIX.md](RELATED-WORK-MATRIX.md)** — 같은 기준으로 비교한 관련연구 표(novelty risk / 빌려올 요소 / 우리와의 차이).
4. **[POSITIONING-NOTES.md](POSITIONING-NOTES.md)** — 하면 안 되는 주장, 안전한 제목·contribution framing 메모.
5. **[CURRENT-FRAME-202606.md](CURRENT-FRAME-202606.md)** — 현재 연구 프레임의 canonical 문서. 어떤 주장까지 가능한지 정리.

논문 노트 본문은 **[md/](md/)** 디렉터리(11섹션 Strategic Reading Note)에 있고, 원본 PDF는 **[paper/](paper/)** 에 있다.

## 먼저 읽을 파일

1. [CURRENT-FRAME-202606.md](CURRENT-FRAME-202606.md)
   현재 연구 프레임의 canonical 문서다. Axis 1/2와 2026-06 미팅 이후 어떤 주장까지 가능한지 정리한다.

2. [READING-QUEUE-202606.md](READING-QUEUE-202606.md) + root `CURRENT-READING.md`
   P0/P1/P2 우선순위 읽기 큐 + 완료/배경 상태. 이 둘이 active queue다.

3. [RELATED-WORK-MATRIX.md](RELATED-WORK-MATRIX.md)
   핵심 논문들을 같은 기준으로 비교한 표다. novelty risk, 빌려올 수 있는 요소, 우리와의 차이를 빠르게 확인할 수 있다.

4. [POSITIONING-NOTES.md](POSITIONING-NOTES.md)
   논문화용 메모다. 어떤 주장을 하면 안 되는지, 어떤 제목과 contribution framing이 안전한지 blunt하게 적어 두었다.

## NFM 브리지 문서

- [NFM-BRIDGE-PLAN.md](NFM-BRIDGE-PLAN.md)
  `TeleMath`, `TeleTables`, `TeleLogs` 중심으로 최소 브리지 실험을 어떻게 설계할지 정리했다.

- [PHD-STRATEGY-2026-2027.md](PHD-STRATEGY-2026-2027.md)
  2026-2027 논문화/졸업 전략 문서다. 메인 수학 논문과 NFM 브리지 논문의 관계도 포함한다.

## 템플릿 / 가이드

- [PAPER-REVIEW-TEMPLATE.md](PAPER-REVIEW-TEMPLATE.md)
  새 논문을 읽을 때 바로 복사해 쓰는 **11섹션 Strategic Reading Note 템플릿**이다. canonical 원본은 root `prompts/paper-strategic-note-template.md`이며 이 파일은 그 미러다.

## 비-canonical / 보조·역사 문서 (active queue로 쓰지 말 것)

아래 자료는 **`archive/` 에 historical-only로 보존**한다. unread/read 판단이나 active queue로 사용하지 않는다. 개요는 [archive/README.md](archive/README.md) 참고. (2026-06-21 simplification에서 exact-duplicate PDF 11편 + 옛 env/prompt/contents/summary 산출물은 superseded로 삭제.)

- [archive/legacy-plans/](archive/legacy-plans/) — `MUST-READ-PLAN.md`, `UNIFIED-PAPER-LIST.md`, `READING-GUIDE-P0.md` (historical plan/list).
- [archive/legacy-reading-pipeline-2026-01/](archive/legacy-reading-pipeline-2026-01/) — 옛 문장단위 reading 노트(historical only) + 복원된 Gemini focused-reading prompt 2개(`prompts/`, optional utility, canonical 아님). contents/summary와 search prompt는 삭제됨.
- [archive/legacy-paper-filenames/](archive/legacy-paper-filenames/) — version-different legacy PDF **2편**(Distilling Step-by-Step, Rewarding Progress)만 보존. canonical PDF는 `paper/`.
- [archive/legacy-reports/](archive/legacy-reports/) — `research-report-0730.txt`, `related-source.txt`, `CONFERENCE-TARGETS-2024-KIISE.md`.
- [archive/legacy-cg-phase/LEGACY-CG-PAPERS.md](archive/legacy-cg-phase/LEGACY-CG-PAPERS.md) — CG-centric phase 역사 index.
- [archive/maintenance/CLEANUP-PLAN-20260621.md](archive/maintenance/CLEANUP-PLAN-20260621.md) — 1차 archive split 계획서(역사적).

## 현재 권장 사용 순서

1. `CURRENT-FRAME-202606.md`로 현재 연구 질문과 금지 주장부터 맞춘다.
2. `READING-QUEUE-202606.md` + root `CURRENT-READING.md`로 읽기 우선순위/상태를 본다.
3. 논문을 읽을 때는 `PAPER-REVIEW-TEMPLATE.md`(11섹션)를 사용하고, metadata는 `papers.yaml`에 기록한다.
4. 논문을 다 읽은 뒤에는 `RELATED-WORK-MATRIX.md`와 `POSITIONING-NOTES.md`를 갱신한다.
5. NFM 관련 아이디어는 메인 math line이 흔들리지 않는 범위에서만 `NFM-BRIDGE-PLAN.md`에 반영한다.

## Deep-interview 준비 상태

관련연구 corpus는 deep-interview / 2026-06-25 연구미팅에 바로 쓸 수 있을 만큼 정리되었다(39편 strategically-read, papers.yaml/queue/matrix/positioning 정합). 다음 단계는 **새 논문을 더 읽는 것이 아니라 실험 방향(path-pool / STOP / verifier-voting allocation) 수렴**이다. 상세 audit은 [REPO-CORPUS-STATUS-20260621.md](REPO-CORPUS-STATUS-20260621.md) 참고.

## 역사적 참고

이 저장소에는 `LM-based-KG` / `CG distillation` 중심 시기의 legacy 자료가 남아 있다. 이 자료들은 삭제하지 않지만, **현재 canonical frame은 2026-06 문서들**이다. 과거 자료를 읽을 때는 반드시 현재 프레임 문서와 함께 본다.
