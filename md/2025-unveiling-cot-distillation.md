# Unveiling the Key Factors for Distilling Chain-of-Thought Reasoning review

## 1. Metadata

- Title: Unveiling the Key Factors for Distilling Chain-of-Thought Reasoning
- Authors: Xinghao Chen, Zhijing Sun, Wenjin Guo, Miaoran Zhang, Yanjun Chen, Yirong Sun, Hui Su, Yijie Pan, Dietrich Klakow, Wenjie Li, Xiaoyu Shen (HK PolyU / Ningbo / Saarland University 등)
- Year: 2025
- Venue / Status: ACL 2025 Findings (pp. 15094–15119)
- Links:
  - Paper: https://aclanthology.org/2025.findings-acl.* (Findings of ACL 2025)
  - GitHub / Code (official): 미확인
- Source PDF (local, source-of-record): `paper/2025-unveiling-cot-distillation.pdf`
- Source Grounding Log:
  - PDF: `paper/2025-unveiling-cot-distillation.pdf` — 26 pages, sha256 `84ef527dd30709e2699a0ed7681ab927dfb4170b2fff1808b651ca1daddfd488`(legacy `(ACL25) Unveiling….pdf`의 canonical 복사본, 동일 sha256, legacy 보존), pypdf/pymupdf 본문 추출 정상(약 88k자). venue("Findings of ACL 2025")·title·authors·abstract·factors 직접 확인.
  - TeX source/ar5iv: 미사용.
  - 주의: arXiv id·official code URL 미확인.
- Paper Type: `analysis` / `CoT distillation factor study` — distillation-confound boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

이 논문은 CoT distillation 성능을 좌우하는 핵심 요인(granularity·format·teacher model)을 4 teacher × 7 student × 7 dataset 규모로 체계 분석해, SLM은 LLM과 다른 경향을 보이며 student capacity·rationale 형식·teacher 선택이 강한 confound임을 밝힌 distillation factor-analysis 논문이다.

## 3. 핵심 문제 설정

- 문제: CoT prompting은 강력하지만 연산 비용이 커서 SLM으로 CoT를 distill하려는 관심이 크다. 그러나 **무엇이 CoT distillation 성능을 좌우하는지** 체계적 이해가 부족했다.
- 해법: distillation에 영향을 주는 요인 — **rationale granularity, format, teacher model** — 을 대규모(4 teacher × 7 student × 7 dataset)로 분석.
- 내 연구와의 연결: 이 논문은 **CoT distillation 성공 요인 / teacher-student rationale transfer의 confound를 선점**했다. 우리가 CG/CoT route를 비교할 때 **"distillation 품질 / teacher rationale 품질 / student capacity" confound**를 반드시 통제·명시해야 함을 알려준다.

## 4. 핵심 방법

- factor 1 — granularity: rationale의 세분화 정도가 student 성능에 미치는 영향.
- factor 2 — format: rationale 표현 형식(구조/스타일)의 영향.
- factor 3 — teacher model: teacher 선택(크기·종류)이 student 성능에 미치는 영향.
- 실험 설계: **4 teacher × 7 student × 7 dataset**(math + commonsense) cross.
- 핵심 발견: SLM은 LLM과 다른(비단조적) 경향, **student capacity가 클수록 거동이 달라짐**, granularity·format·teacher가 결과를 좌우.
- selection unit(우리 관점): 분석 대상은 **rationale(학습 supervision)**의 속성. method 제안이 아니라 factor 분석.

## 5. SLM-Math 관점의 재해석

- 이 논문은 직접 baseline 경쟁자라기보다 **distillation confound를 통제하게 해주는 analysis reference**다.
- 공통점: SLM에서 rationale 형식·teacher·capacity가 reasoning에 미치는 영향에 관심.
- 차이점:
  - 이 논문은 **training-time distillation factor 분석**. 우리는 **fixed backbone 위 test-time path-pool 구성·STOP**.
  - 이 논문은 무엇을 학습시킬지(granularity/format/teacher). 우리는 무엇을 추론 시점에 더 샘플링할지(path family).
- 연결: 우리가 CoT_Lv1/Lv2/Lv3·CG route를 비교할 때 **결과 차이가 path family 자체 때문인지, 아니면 rationale 형식/teacher/capacity 때문인지** 분리해야 한다는 점을 정당화. → 우리 ablation에 distillation-confound 통제를 넣는 근거.

## 6. 우리 연구에 대한 novelty risk

- **CoT distillation factor analysis / granularity·format·teacher 영향 / SLM distillation 거동**을 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "어떤 rationale 형식이 SLM distillation에 좋은가"라는 분석도 선점.
- 위험 framing: `CoT distillation 요인 분석이 우리 기여`, `rationale 형식/teacher 선택 효과를 우리가 처음 본다`.
- 단, 이 논문은 training-time 분석이라 우리 inference-time allocation과 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: distillation 성능의 confound(granularity/format/teacher/student capacity), SLM≠LLM 거동.
- baseline/통제: 우리 path-family 비교에서 **distillation-confound 통제 변수**(teacher rationale 품질·형식·student size 고정)를 명시.
- metric: dataset별 accuracy + factor별 민감도.
- ablation: rationale granularity/format 통제, teacher 고정, student size sweep — 우리 "prompt-diversity vs structural effect" 분리 ablation과 연동.
- terminology: `rationale granularity`, `rationale format`, `teacher model selection`, `student capacity`, `distillation confound`.

## 8. 우리가 하면 안 되는 주장

- `CoT distillation factor 분석을 우리가 처음 한다`.
- `rationale granularity/format/teacher 선택 효과를 우리가 처음 밝혔다`.
- `우리 CG/CoT_Lv route 차이가 순수 path-family 효과다`(distillation/teacher/capacity confound 미통제 시).
- 이 논문 대비 SLM distillation 성능 SOTA 경쟁.

## 9. baseline / ablation 반영 아이디어

- 우리 route family 비교 실험에 **distillation-confound 통제**(같은 teacher rationale 품질·형식, 같은 student size)를 명문화.
- "path family 효과"와 "rationale 형식/teacher/capacity 효과"를 분리하는 ablation(CoT/Least-to-Most/UniCoTT 노트와 연동).
- training-time distillation 품질 차이가 inference-time path-pool 비교를 오염시키지 않도록 baseline 고정.

## 10. Related Work에 넣을 문장 초안

Chen et al.(Findings of ACL 2025)의 Unveiling the Key Factors for Distilling Chain-of-Thought Reasoning은 CoT 능력을 작은 모델에 증류할 때 rationale granularity, format, teacher model 선택이 성능에 미치는 영향을 4개 teacher와 7개 student, 7개 수학·상식 추론 데이터셋에 걸쳐 체계적으로 분석하여, 작은 모델이 큰 모델과 다른 거동을 보이며 student capacity와 rationale 형식·teacher 선택이 강한 요인임을 밝혔다.

본 연구는 CoT distillation의 요인 분석 자체를 새 기여로 두지 않는다. 다만 이 연구가 드러낸 distillation confound(rationale 품질·형식·teacher·student capacity)는, 우리가 fixed backbone 위에서 서로 다른 reasoning path family(CoT, prompt-diverse CoT, CG, PAL/PoT 등)를 비교할 때 결과 차이가 path family 자체에서 오는지 학습 측 요인에서 오는지를 분리하기 위해 통제해야 할 변수로 활용된다. 우리의 기여는 training-time distillation 설계가 아니라 제한된 test-time compute 안의 **state-conditioned path-pool allocation**에 있다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 낮음~중간 (analysis reference; distillation-confound 통제 측면에서 유용, 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. distillation-confound 통제 변수의 근거로 활용.
- 지금 할 일:
  - 이 논문을 distillation boundary cluster의 P1 reference로 고정(특히 ablation 통제 근거).
  - 우리 route-family 비교에 **distillation/teacher/capacity confound 통제**를 명문화.
  - `CoT distillation factor 분석 자체를 novelty로 쓰지 않기` wording 가드.
- 나중으로 미뤄도 되는 일: 4×7×7 cross 재현, factor별 정밀 분석.
- 한 줄 결론: 이 논문은 CoT distillation confound를 드러낸 analysis reference이며, 우리 path-family 비교에서 학습 측 confound를 통제하게 만들고 현재 기여를 test-time path-pool allocation으로 분리하게 하는 P1 reference다.
