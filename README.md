# SLM-Math Papers

이 저장소는 `SLM-Math`의 관련 연구를 추적하고, 선택적으로 `NFM` 브리지 가능성을 정리하기 위한 문헌/포지셔닝 저장소다.

현재 기준점은 **2026-06 이후 연구 프레임**이다.

- 이 저장소의 메인 질문은 더 이상 "CG가 CoT보다 우월한가"가 아니다.
- 현재 메인라인은 **수학 추론에서 heterogeneous reasoning path pool을 어떻게 구성하고, 제한된 테스트타임 계산량 안에서 어떤 path를 선택·검증·중단할 것인가**다.
- `CG`는 삭제하지 않는다. 다만 **여러 structured reasoning path family 중 하나**로 보존한다.
- `NFM`은 본 thesis의 대체 주제가 아니라, **선별된 application/bridge domain**으로만 다룬다.

## 먼저 읽을 파일

1. [CURRENT-FRAME-202606.md](CURRENT-FRAME-202606.md)
   현재 연구 프레임의 canonical 문서다. Axis 1/2와 2026-06 미팅 이후 어떤 주장까지 가능한지 정리한다.

2. [READING-QUEUE-202606.md](READING-QUEUE-202606.md)
   P0/P1/P2 우선순위로 다시 짠 읽기 큐다. 바로 읽어야 할 논문과 나중에 읽을 논문을 분리한다.

3. [RELATED-WORK-MATRIX.md](RELATED-WORK-MATRIX.md)
   핵심 논문들을 같은 기준으로 비교한 표다. novelty risk, 빌려올 수 있는 요소, 우리와의 차이를 빠르게 확인할 수 있다.

4. [POSITIONING-NOTES.md](POSITIONING-NOTES.md)
   논문화용 메모다. 어떤 주장을 하면 안 되는지, 어떤 제목과 contribution framing이 안전한지 blunt하게 적어 두었다.

## NFM 브리지 문서

- [NFM-BRIDGE-PLAN.md](NFM-BRIDGE-PLAN.md)
  `TeleMath`, `TeleTables`, `TeleLogs` 중심으로 최소 브리지 실험을 어떻게 설계할지 정리했다.

- [PHD-STRATEGY-2026-2027.md](PHD-STRATEGY-2026-2027.md)
  2026-2027 논문화/졸업 전략 문서다. 메인 수학 논문과 NFM 브리지 논문의 관계도 포함한다.

## 읽기/정리용 운영 파일

- [MUST-READ-PLAN.md](MUST-READ-PLAN.md)
  새 프레임에 맞춘 압축 must-read 목록이다. 빠르게 읽기 시작해야 할 테마별 핵심 논문만 남겼다.

- [UNIFIED-PAPER-LIST.md](UNIFIED-PAPER-LIST.md)
  현재 taxonomy 기준의 통합 목록이다. math frontier, TTC, verifier, strategy selection, NFM bridge까지 재분류했다.

- [PAPER-REVIEW-TEMPLATE.md](PAPER-REVIEW-TEMPLATE.md)
  새 논문을 읽을 때 바로 복사해 쓸 수 있는 템플릿이다.

## 메타데이터 파일

- `papars.yaml`
  과거 오탈자 파일명이지만, 기존 참조를 깨지 않기 위해 **당분간 이 이름을 유지**한다.
  2026-06 리프레시 이후에는 새 schema를 담는 canonical 메타데이터 파일로 계속 사용한다.

- 필요하면 나중에 `papers.yaml`을 추가할 수 있지만, 현재는 transition을 단순하게 유지한다.

## 현재 권장 사용 순서

1. `CURRENT-FRAME-202606.md`로 현재 연구 질문과 금지 주장부터 맞춘다.
2. `MUST-READ-PLAN.md`와 `READING-QUEUE-202606.md`로 읽기 우선순위를 정한다.
3. 논문을 읽을 때는 `PAPER-REVIEW-TEMPLATE.md`를 사용한다.
4. 논문을 다 읽은 뒤에는 `RELATED-WORK-MATRIX.md`와 `POSITIONING-NOTES.md`를 갱신한다.
5. NFM 관련 아이디어는 메인 math line이 흔들리지 않는 범위에서만 `NFM-BRIDGE-PLAN.md`에 반영한다.

## 역사적 참고

이 저장소에는 `LM-based-KG` / `CG distillation` 중심 시기의 legacy 자료가 남아 있다. 이 자료들은 삭제하지 않지만, **현재 canonical frame은 2026-06 문서들**이다. 과거 자료를 읽을 때는 반드시 현재 프레임 문서와 함께 본다.
