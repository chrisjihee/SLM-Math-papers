# Mentor-KD: Making Small Language Models Better Multi-step Reasoners review

## 1. Metadata

- Title: Mentor-KD: Making Small Language Models Better Multi-step Reasoners
- Authors: Hojae Lee, Junho Kim, SangKeun Lee (Korea University)
- Year: 2024
- Venue / Status: EMNLP 2024 (arXiv 2410.11325)
- Links:
  - Paper: https://aclanthology.org/2024.emnlp-main.* (Proceedings of EMNLP 2024, pp. 17643–17658) / https://arxiv.org/abs/2410.11325
  - GitHub / Code (official): 미확인
- Source PDF (local, source-of-record): `paper/2024-mentor-kd.pdf`
- Source Grounding Log:
  - PDF: `paper/2024-mentor-kd.pdf` — 16 pages, sha256 `520a5271e97a97def9782a140dd002bb2ddfa1af2209ac229b02335acd996d7c`(legacy `paper/10. ….pdf`의 canonical 복사본, 동일 sha256; 중복 legacy 사본은 2026-06-21 cleanup에서 삭제), pypdf/pymupdf 본문 추출 정상(약 64k자). venue("Proceedings of the 2024 Conference on EMNLP")·title·authors·abstract·method 직접 확인.
  - TeX source/ar5iv: 미사용.
  - 주의: arXiv id(2410.11325) 미재확인, official code URL 미확인.
- Paper Type: `training` / `reasoning distillation (CoT KD via intermediate mentor)` — teacher-guided distillation boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

Mentor-KD는 LLM teacher의 CoT rationale set이 data quality가 낮고 soft label을 못 준다는 reasoning distillation의 두 한계를, **intermediate-sized task-specific fine-tuned "mentor" 모델**로 다양한 rationale을 augment하고 soft label을 제공해 보완함으로써 작은 student의 multi-step reasoning을 끌어올린 teacher-guided distillation 논문이다.

## 3. 핵심 문제 설정

- 문제: reasoning distillation(LLM teacher의 CoT rationale로 small LM fine-tune)은 (1) teacher rationale set의 **품질·다양성 부족**, (2) hard label만 쓰고 **soft label 미제공**이라는 한계가 있다.
- 해법: **mentor**(중간 크기 task-specific fine-tuned 모델)를 두어 (1) 정답 유도 CoT rationale을 **추가 생성(augment)** 하고 (2) student에 **soft label**(distribution)을 제공 → distillation set 보강.
- 내 연구와의 연결: Mentor-KD는 **small model multi-step reasoning distillation / teacher-guided reasoning improvement를 선점**했다. 우리 기여는 **training-time KD가 아니라 fixed backbone 위 test-time path-pool allocation**이다.

## 4. 핵심 방법

- mentor: student보다 크고 teacher보다 작은 intermediate task-specific fine-tuned 모델.
- rationale augmentation: mentor가 추가 CoT rationale을 생성해 distillation set을 늘림(정답 필터링 포함).
- soft label: mentor가 student에 soft target(distribution)을 제공(단순 hard label 한계 보완).
- 학습: training-heavy KD. test-time 제어/search/verifier 없음.
- selection unit: **rationale / soft label(학습 supervision)**. heterogeneous path-family 선택/budget allocation/STOP은 아님.
- 실험: teacher LLM(예: GPT-3.5), student small LM, 복잡 reasoning(GSM8K/StrategyQA/CommonsenseQA 등). 기존 reasoning distillation 대비 향상.

## 5. SLM-Math 관점의 재해석

- Mentor-KD는 직접 baseline 경쟁자라기보다 **teacher-guided reasoning distillation의 대표 reference이자 boundary**다.
- 공통점: 작은 모델의 multi-step reasoning을 개선, rationale 다양성·품질의 중요성.
- 차이점:
  - Mentor-KD는 **training-time KD(mentor augmentation + soft label)**. 우리는 **fixed backbone 위 test-time path-pool 구성·STOP**.
  - mentor의 rationale 다양화는 학습 데이터 다양화. 우리의 path 다양화는 inference-time path-family 다양화.
- 연결: Mentor-KD로 얻은 student를 우리 orchestration의 **fixed backbone 후보**로(경쟁 아님). rationale 다양성↔우리 heterogeneous path family를 목적 분리(학습 vs 추론).

## 6. 우리 연구에 대한 novelty risk

- **small model multi-step reasoning distillation / teacher-guided rationale augmentation / soft label KD**를 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "작은 모델 multi-step reasoning을 distillation으로 향상"이라는 넓은 claim도 선점.
- 위험 framing: `SLM multi-step reasoning improvement가 우리 기여`, `rationale 다양화 distillation을 우리가 한다`.
- 단, Mentor-KD는 training-time KD라 우리 inference-time allocation과 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: teacher rationale 품질·다양성의 중요성, soft label의 효용, intermediate mentor 아이디어.
- baseline: Mentor-KD/일반 reasoning-distillation student를 우리 orchestration의 fixed backbone 후보로(경쟁 아님).
- metric: reasoning accuracy + rationale diversity/품질 분석 — training-time gain과 inference-time gain 분해.
- ablation: rationale augmentation on/off, soft vs hard label, mentor 크기.
- terminology: `reasoning distillation`, `rationale augmentation`, `soft label`, `mentor model`, `multi-step reasoner`.

## 8. 우리가 하면 안 되는 주장

- `small model multi-step reasoning distillation을 우리가 처음 제안한다`.
- `teacher-guided rationale augmentation / soft label KD가 우리 기여다`.
- `SLM reasoning improvement를 우리가 (distillation으로) 보였다`.
- 이 논문 대비 distillation 성능 SOTA 경쟁, training-time gain을 inference-time 기여로 혼동.

## 9. baseline / ablation 반영 아이디어

- distillation은 backbone 확보 수단으로만, 비교 중심은 fixed backbone 위 test-time path-pool.
- rationale 다양성(학습)과 path-family 다양성(추론)을 분리하는 ablation.
- mentor-augmented student를 backbone으로 둔 뒤 그 위에 우리 orchestration을 얹어 inference-time gain을 분해.

## 10. Related Work에 넣을 문장 초안

Mentor-KD(Lee et al., EMNLP 2024)는 LLM teacher의 chain-of-thought rationale로 작은 모델을 fine-tune하는 reasoning distillation이 teacher rationale의 품질·다양성 부족과 soft label 부재라는 한계를 가진다는 점에 착안해, 중간 크기의 task-specific fine-tuned mentor 모델로 다양한 rationale을 보강하고 soft label을 제공함으로써 작은 student의 multi-step reasoning을 향상시켰다. 이는 teacher-guided reasoning distillation의 대표적 연구다.

본 연구는 small model의 multi-step reasoning을 distillation으로 향상시키는 것 자체를 새 기여로 두지 않는다. 우리는 mentor/teacher 기반 training-time KD가 아니라, fixed/given backbone 위에서 제한된 test-time compute 안의 heterogeneous reasoning path family를 문제별로 구성·선택·검증·중단하는 **state-conditioned test-time path-pool allocation**에 위치하며, distillation은 backbone을 얻는 한 방법으로만 다룬다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (SLM reasoning distillation/teacher-guided improvement claim boundary; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. distillation은 backbone 확보 수단으로만, 비교 중심은 test-time orchestration.
- 지금 할 일:
  - Mentor-KD를 Distilling Step-by-Step·UniCoTT·MAGDi·STaR와 함께 distillation boundary cluster의 P1 reference로 고정.
  - `SLM multi-step reasoning distillation / teacher-guided improvement 자체를 novelty로 쓰지 않기` wording 가드.
  - training-time gain과 inference-time gain 분해 명시.
- 나중으로 미뤄도 되는 일: Mentor-KD 재현, mentor augmentation 평가.
- 한 줄 결론: Mentor-KD는 teacher-guided reasoning distillation을 선점한 reference이며, 우리 기여를 training-time KD가 아니라 fixed backbone 위 test-time path-pool allocation으로 분리하게 만드는 P1 reference다.
