# Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes review

## 1. Metadata

- Title: Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes
- Authors: Cheng-Yu Hsieh, Chun-Liang Li, Chih-Kuan Yeh, Hootan Nakhost, Yasuhisa Fujii, Alexander Ratner, Ranjay Krishna, Chen-Yu Lee, Tomas Pfister (University of Washington / Google Cloud AI Research / Google Research)
- Year: 2023
- Venue / Status: ACL 2023 Findings (arXiv 2305.02301)
- Links:
  - Paper: https://arxiv.org/abs/2305.02301 (ACL Anthology 2023.findings-acl.507)
  - GitHub / Code (official): https://github.com/google-research/distilling-step-by-step
- Source PDF (local, source-of-record): `paper/2023-distilling-step-by-step.pdf`
- Source Grounding Log:
  - PDF: `paper/2023-distilling-step-by-step.pdf` — 13 pages, sha256 `100bd0de2606d205f9d9108395d05f82c4f6c848097f89933d42471f4db36ff9`, pypdf/pymupdf 본문 추출 정상(약 50k자). title/authors/abstract/method/benchmarks 직접 확인.
  - arXiv abstract: venue("Accepted to Findings of ACL 2023")·official code 확인.
  - legacy 자료: `reading/02`, `contents/02` 존재 — 보조 참고만, source-of-record는 PDF 재추출. legacy `paper/02. ….pdf`는 보존(canonical 신규 PDF 추가).
  - TeX source/ar5iv: 미사용.
- Paper Type: `training` / `distillation (rationale distillation, multi-task)` — distillation boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1` (rationale-distillation claim boundary)

## 2. One-line Summary

Distilling Step-by-Step는 teacher LLM에서 CoT rationale을 추출해 작은 student를 multi-task(label 예측 + rationale 예측)로 학습함으로써, 더 적은 데이터와 더 작은 모델로 LLM을 능가(예: 770M T5 > few-shot 540B PaLM)한 rationale distillation 논문이다.

## 3. 핵심 문제 설정

- 문제: LLM 배포는 메모리·연산 비용이 크고, 작은 task-specific model을 만들려면 보통 많은 학습 데이터가 필요하다.
- 해법: teacher LLM의 **rationale을 추가 supervision으로 추출**해, student를 label과 rationale을 동시에 예측하는 **multi-task**로 학습 → 데이터 효율↑, 모델 크기↓.
- 내 연구와의 연결: 이 논문은 **rationale distillation / smaller model / less training data를 선점**했다. 우리의 과거 CG distillation 축과 직접 닿지만, **현재 기여는 distillation이 아니라 제한된 TTC 안의 test-time path-pool allocation**으로 이동했음을 분명히 해야 한다.

## 4. 핵심 방법

- rationale 추출: teacher(**PaLM 540B**)에서 few-shot CoT로 각 예제의 rationale 생성.
- multi-task training: student(**T5 220M/770M/11B**)가 (1) `[label]` 예측, (2) `[rationale]` 예측을 별도 prefix task로 학습(추론 시 rationale 생성 없이 label만 써도 됨).
- 학습: training-heavy(distillation). test-time 제어/search/verifier 없음.
- selection unit: **rationale(학습 supervision)**. heterogeneous path-family 선택/budget allocation/STOP은 아님.
- 결과: standard finetuning·label-only distillation 대비 **적은 데이터로 더 높은 정확도**, 작은 모델이 큰 LLM 능가.
- benchmarks: e-SNLI, ANLI, CQA, **SVAMP(math)**.

## 5. SLM-Math 관점의 재해석

- 이 논문은 직접 baseline 경쟁자라기보다 **rationale distillation의 대표 reference이자 우리 (과거) CG distillation 축의 boundary**다.
- 공통점: 작은 모델에 rationale을 학습시켜 reasoning을 개선.
- 차이점:
  - 이 논문은 **training-time rationale distillation**. 우리 현재 mainline은 **fixed backbone 위 test-time path-pool 구성·선택·STOP**.
  - student는 단일 rationale을 학습. 우리는 inference-time에 heterogeneous path family를 획득·배분.
- 연결: CG를 structured rationale distillation의 한 갈래로 보존하되, **현재 기여는 distillation 자체가 아님**을 명문화. distillation은 backbone을 얻는 한 방법일 뿐, 그 위의 TTC orchestration이 핵심.

## 6. 우리 연구에 대한 novelty risk

- **rationale distillation / SLM에 rationale 증류 / less training data·smaller model**을 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "rationale을 student에 학습시키면 작은 모델이 좋아진다"는 관찰도 선점.
- 특히 우리 **CG distillation**을 novelty로 전면화하면 이 논문(및 UniCoTT/MAGDi)과 정면충돌.
- 위험 framing: `rationale distillation이 우리 기여`, `작은 모델 reasoning 향상을 distillation으로 보인다`.

## 7. 우리가 빌릴 수 있는 것

- framing: rationale을 supervision으로 쓰는 multi-task / data efficiency / 작은 student가 큰 teacher 능가.
- baseline: distillation으로 얻은 student backbone을 우리 orchestration의 **fixed backbone 후보**로(경쟁 대상이 아니라 substrate).
- metric: accuracy + **training-data efficiency, student size** — 우리 "fixed backbone, test-time cost" framing과 대비.
- ablation: rationale 유무, multi-task vs single-task, student size sweep.
- terminology: `rationale extraction`, `multi-task rationale prediction`, `data-efficient distillation`, `teacher rationale`.

## 8. 우리가 하면 안 되는 주장

- `rationale distillation / step-by-step distillation을 우리가 처음 제안한다`.
- `작은 모델에 rationale을 증류하면 reasoning이 좋아진다는 것을 우리가 보였다`.
- `CG distillation 자체가 우리 main novelty다`.
- `distillation with rationales가 우리 기여다`.
- 이 논문 대비 raw accuracy SOTA 경쟁.

## 9. baseline / ablation 반영 아이디어

- distillation은 backbone 확보 수단으로만 두고(경쟁 아님), 우리 비교의 중심은 **fixed backbone 위 test-time path-pool vs SC vs single-path**.
- 만약 CG/structured rationale를 student에 학습한다면, 그 효과를 **test-time allocation 효과와 분리**하는 ablation 설계.
- training-time gain(distillation)과 inference-time gain(orchestration)을 명확히 분해.

## 10. Related Work에 넣을 문장 초안

Distilling Step-by-Step(Hsieh et al., ACL 2023 Findings)은 teacher LLM에서 추출한 chain-of-thought rationale을 추가 supervision으로 삼아 작은 student를 multi-task(label·rationale 예측)로 학습함으로써, 더 적은 학습 데이터와 더 작은 모델 크기로 큰 LLM을 능가할 수 있음을 보였다(예: 770M T5가 few-shot 540B PaLM을 상회). 이는 rationale distillation과 data-efficient small-model reasoning의 대표적 연구다.

본 연구는 rationale distillation이나 작은 모델의 reasoning 향상 자체를 새 기여로 두지 않는다. 우리의 과거 Concept Graph distillation 축은 이러한 structured rationale distillation 계열에 속하지만, 현재 기여는 distillation이 아니라 fixed/given backbone 위에서 제한된 test-time compute 안의 heterogeneous reasoning path family를 구성·선택·검증·중단하는 **state-conditioned test-time path-pool allocation**으로 이동했다. 즉 distillation은 backbone을 얻는 한 방법일 뿐, 우리의 novelty는 그 위의 lightweight orchestration에 있다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1` (rationale-distillation claim boundary)
- 위협도: 중간 (특히 CG distillation novelty를 직접 제약; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. distillation은 backbone 확보 수단으로만, 비교 중심은 test-time orchestration.
- 지금 할 일:
  - Distilling Step-by-Step를 UniCoTT·MAGDi·STaR와 함께 distillation/rationale boundary cluster의 P1 reference로 고정.
  - `rationale distillation / CG distillation 자체를 novelty로 쓰지 않기` wording 가드(현재 기여는 test-time allocation).
  - training-time gain과 inference-time gain 분해를 평가 설계에 명시.
- 나중으로 미뤄도 되는 일: 재학습/재현, e-SNLI/ANLI/CQA/SVAMP 평가.
- 한 줄 결론: Distilling Step-by-Step는 우리 과거 CG distillation 축의 boundary이며, 현재 기여를 distillation이 아니라 fixed backbone 위 test-time path-pool allocation으로 분리하게 만드는 P1 reference다.
