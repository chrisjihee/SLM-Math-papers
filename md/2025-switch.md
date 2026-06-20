# SWITCH: Studying with Teacher for Knowledge Distillation of Large Language Models review

## 1. Metadata

- Title: SWITCH: Studying with Teacher for Knowledge Distillation of Large Language Models
- Authors: Jahyun Koo, Yerin Hwang, Yongil Kim, Taegwan Kang, Hyunkyung Bae, Kyomin Jung (Seoul National University / LG AI Research)
- Year: 2025
- Venue / Status: NAACL 2025 Findings (pp. 3733–3746) — ⚠️ legacy 파일명 "(EMNLP25)"는 오기
- Links:
  - Paper: https://aclanthology.org/2025.findings-naacl (Findings of NAACL 2025)
  - GitHub / Code (official): 미확인
- Source PDF (local, source-of-record): `paper/2025-switch.pdf`
- Source Grounding Log:
  - PDF: `paper/2025-switch.pdf` — 14 pages, sha256 `79315b3fe37865b45bcc2c7899d21b95340320d4d0f691737e91e6336a75092d`(legacy `paper/11. ….pdf`의 canonical 복사본, 동일 sha256, legacy 보존), pypdf/pymupdf 본문 추출 정상(약 53k자). venue("Findings of … NAACL 2025, pages 3733–3746")·title·authors·abstract·method 직접 확인.
  - TeX source/ar5iv: 미사용.
  - 주의: **venue를 NAACL 2025 Findings로 교정**(legacy 파일명 EMNLP25 오기). arXiv id·official code URL 미확인.
- Paper Type: `training` / `knowledge distillation (token-level, SGO + selective teacher intervention)` — teacher-student KD boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

SWITCH는 student-generated outputs(SGO)를 학습에 쓰면 train-inference mismatch는 줄지만 SGO가 noisy/biased(특히 long sequence)해 teacher misguidance가 생긴다는 문제를, teacher가 **token-level divergence가 큰 토큰에서 선택적으로 개입·교정**하는 "studying with teacher" 방식으로 완화한 LLM knowledge distillation 논문이다.

## 3. 핵심 문제 설정

- 문제: LLM KD에서 SGO를 학습데이터로 쓰면 train-inference 분포 mismatch는 줄지만, SGO는 noisy/biased(특히 긴 시퀀스)라 teacher가 잘못된 student 생성을 그대로 모방하도록 misguide할 수 있다.
- 해법: **SWITCH** — student 자체 생성을 사용하되, teacher와 student의 **token-level distribution divergence**가 큰 지점에서 teacher가 **선택적으로 개입/교정**(전 구간 강제 teacher forcing이 아니라 필요한 토큰만).
- 내 연구와의 연결: SWITCH는 **teacher-student KD / studying with teacher / distillation dynamics(token-level)를 선점**했다. 우리 연구에서는 **learned route family를 만드는 문제(training-time KD)** 와 **test-time route family를 선택하는 문제**를 분리해야 한다.

## 4. 핵심 방법

- SGO 사용: student가 생성한 출력을 학습데이터로(train-inference mismatch 완화).
- selective teacher intervention: token별 teacher-student divergence를 보고 큰 곳에서만 teacher distribution으로 교정(divergence 최소화).
- 학습: training-heavy KD. test-time 제어/search/verifier 없음.
- selection unit: **token(학습 supervision)**. heterogeneous path-family 선택/budget allocation/STOP은 아님.
- 실험: instruction-following 5개 데이터셋, GPT-4 feedback score. 기존 sequence-level/SGO KD 대비 향상.
- 주의: 주로 **instruction-following** KD(수학 reasoning 특화 아님).

## 5. SLM-Math 관점의 재해석

- SWITCH는 직접 baseline 경쟁자라기보다 **teacher-student KD dynamics의 대표 reference이자 boundary**다.
- 공통점: 작은 모델을 teacher 신호로 개선, train-inference mismatch 인식(우리 inference-time 관심과 일부 공명).
- 차이점:
  - SWITCH는 **training-time token-level KD(selective teacher intervention)**. 우리는 **fixed backbone 위 test-time path-pool 구성·STOP**.
  - SWITCH의 단위는 token. 우리는 path family / macro strategy.
- 연결: "route family를 학습으로 만드는 것"과 "test-time에 route family를 선택하는 것"을 분리. SWITCH는 전자(training)의 reference이며, 우리 기여는 후자(test-time selection).

## 6. 우리 연구에 대한 novelty risk

- **teacher-student KD / studying with teacher / token-level distillation dynamics / SGO 활용**을 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "teacher 신호로 student를 개선" 류 넓은 claim도 선점.
- 위험 framing: `teacher-guided learning이 우리 기여`, `KD dynamics 개선을 우리가 한다`.
- 단, SWITCH는 training-time KD라 우리 inference-time allocation과 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: train-inference mismatch, SGO의 noise/bias, selective(전체가 아닌) 개입 아이디어.
- baseline: SWITCH로 distill한 student를 우리 orchestration의 fixed backbone 후보로(경쟁 아님).
- metric: instruction-following 품질/GPT-4 score — training-time gain과 inference-time gain 분해.
- ablation: selective vs full teacher intervention, SGO on/off.
- terminology: `knowledge distillation`, `student-generated outputs(SGO)`, `token-level divergence`, `selective teacher intervention`, `studying with teacher`.

## 8. 우리가 하면 안 되는 주장

- `teacher-student KD / studying with teacher / KD dynamics를 우리가 처음 제안한다`.
- `teacher-guided learning이 우리 기여다`.
- `SGO/token-level distillation 개선을 우리가 한다`.
- 이 논문 대비 KD 성능 SOTA 경쟁, training-time gain을 inference-time 기여로 혼동.

## 9. baseline / ablation 반영 아이디어

- "route family 생성(training-time KD)"과 "test-time route family 선택"을 명시적으로 분리하는 ablation.
- distillation은 backbone 확보 수단으로만, 비교 중심은 fixed backbone 위 test-time path-pool.
- selective intervention 아이디어는 우리 STOP/verifier가 "필요한 곳에서만 개입"하는 설계의 개념적 참고(단, training이 아니라 inference-time).

## 10. Related Work에 넣을 문장 초안

SWITCH(Koo et al., Findings of NAACL 2025)는 large language model의 knowledge distillation에서 student-generated outputs를 학습에 사용해 train-inference mismatch를 줄이되, 그 출력이 noisy·biased하여 teacher가 잘못된 시퀀스를 모방하도록 misguide될 수 있다는 문제에 착안해, teacher가 token-level divergence가 큰 지점에서만 선택적으로 개입하는 studying-with-teacher 방식을 제안했다. 이는 teacher-student knowledge distillation의 dynamics를 다룬 대표적 연구다.

본 연구는 teacher-student KD나 studying-with-teacher 자체를 새 기여로 두지 않는다. 우리는 learned route family를 만드는 training-time distillation 문제와 test-time에 어떤 reasoning path family를 선택·중단할지의 문제를 분리하며, 우리의 기여는 후자, 즉 fixed/given backbone 위에서 제한된 test-time compute 안의 **state-conditioned path-pool allocation**에 있다. SWITCH가 다룬 train-inference mismatch와 selective intervention은 우리 inference-time STOP/verifier 설계의 개념적 참고로만 활용한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 낮음~중간 (teacher-student KD claim boundary; instruction-following 중심이라 math mainline과 과제 차이; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. distillation은 backbone 확보 수단으로만.
- 지금 할 일:
  - SWITCH를 Mentor-KD·Distilling·UniCoTT·MAGDi와 함께 distillation boundary cluster의 P1 reference로 고정.
  - `teacher-student KD / studying with teacher 자체를 novelty로 쓰지 않기` wording 가드.
  - "route family 생성(training)"과 "test-time route family 선택"을 분리 명문화.
  - **venue를 NAACL 2025 Findings로 교정**(legacy EMNLP25 오기) — 인용 시 주의.
- 나중으로 미뤄도 되는 일: SWITCH 재현, instruction-following 평가.
- 한 줄 결론: SWITCH는 teacher-student KD dynamics를 선점한 reference이며, 우리 기여를 training-time KD가 아니라 fixed backbone 위 test-time route-family selection으로 분리하게 만드는 P1 reference다(venue: NAACL 2025 Findings).
