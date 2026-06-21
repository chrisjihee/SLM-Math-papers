# Self-Instruct: Aligning Language Models with Self-Generated Instructions review

## 1. Metadata

- Title: Self-Instruct: Aligning Language Models with Self-Generated Instructions
- Authors: Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi, Hannaneh Hajishirzi (UW / Tehran Polytechnic / ASU / JHU / Allen Institute for AI)
- Year: 2023
- Venue / Status: ACL 2023 (pp. 13484–13508; arXiv 2212.10560)
- Links:
  - Paper: https://aclanthology.org/2023.acl-long.754/ / https://arxiv.org/abs/2212.10560
  - GitHub / Code (official): https://github.com/yizhongw/self-instruct
- Source PDF (local, source-of-record): `paper/2023-self-instruct.pdf`
- Source Grounding Log:
  - PDF: `paper/2023-self-instruct.pdf` — 25 pages, sha256 `87f1d8476fa041d0c6b09b9239253ed698c4efac973347aebe83c487eab91c78`(legacy `paper/01. ….pdf`의 canonical 복사본, 동일 sha256; 중복 legacy 사본은 2026-06-21 cleanup에서 삭제), pypdf/pymupdf 본문 추출 정상(약 90k자). venue("Proceedings of the 61st Annual Meeting of the ACL")·title·authors·abstract·method·code 직접 확인.
  - legacy 자료: 문장단위 reading 노트는 `archive/legacy-reading-pipeline-2026-01/reading/01.…`에 historical-only 보존(`contents/01`은 2026-06-21 cleanup에서 삭제). source-of-record는 canonical PDF 재추출.
  - TeX source/ar5iv: 미사용.
- Paper Type: `training` / `instruction tuning (self-generated instruction bootstrapping)` — instruction-tuning boundary reference
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

Self-Instruct는 human-written instruction 의존을 줄이기 위해, 모델이 **자체 생성한 instruction·input·output**을 부트스트랩해 필터링·fine-tune하는 self-generated instruction tuning framework로, vanilla GPT-3에 적용해 SUPERNI에서 33% 절대 향상을 보인 instruction-tuning 대표 논문이다.

## 3. 핵심 문제 설정

- 문제: instruction-tuned 모델은 강력하지만 human-written instruction data의 **양·다양성·창의성 한계**에 의존한다.
- 해법: **self-instruct** — 모델 자체 생성으로 instruction을 만들고, 각 instruction에 대한 input/output instance를 생성·필터링해 fine-tune, 이를 반복(self-bootstrapping of instruction data).
- 내 연구와의 연결: Self-Instruct는 **self-generated instruction data / synthetic instruction generation / instruction tuning을 선점**했다. 우리 연구에서 prompt family·route instruction 설계가 **단순 self-instruction으로 보이지 않도록**, test-time selection problem으로 분리해야 한다.

## 4. 핵심 방법

- instruction 생성: seed instruction에서 시작해 모델이 새 instruction을 생성.
- instance 생성: 각 instruction에 대해 input/output을 모델이 생성.
- 필터링: 중복·저품질 제거(diversity 확보).
- fine-tune: 생성·필터된 instruction data로 모델을 instruction-tune, 반복.
- 학습: training-heavy(instruction tuning). test-time 제어/search/verifier 없음.
- selection unit: **instruction/instance data(학습 supervision)**. heterogeneous path-family 선택/budget allocation/STOP은 아님.
- 결과: vanilla GPT-3 +33% absolute(SUPERNI), InstructGPT에 근접.

## 5. SLM-Math 관점의 재해석

- Self-Instruct는 직접 baseline 경쟁자라기보다 **instruction-tuning / self-generated data의 대표 reference이자 boundary**다.
- 공통점: 모델 자체 생성을 활용(우리 path 후보 생성과 표면적으로 닿음).
- 차이점:
  - Self-Instruct는 **training-time instruction data 부트스트랩**. 우리는 **fixed backbone 위 test-time path-pool 구성·STOP**.
  - Self-Instruct의 생성물은 학습 데이터. 우리의 path 후보는 inference-time 추론 경로.
- 연결: prompt family/route card를 "self-instruction으로 만든 데이터"가 아니라 **inference-time에 선택·중단하는 의사결정 단위**로 명확히 구분.

## 6. 우리 연구에 대한 novelty risk

- **self-generated instruction data / synthetic instruction generation / instruction tuning**을 이미 선점 → 이 자체를 우리 novelty로 쓰면 충돌.
- "모델 자체 생성을 데이터로 쓰면 좋아진다"는 관찰도 선점.
- 위험 framing: `synthetic instruction generation이 우리 기여`, `self-instruction으로 route를 만든다`.
- 단, Self-Instruct는 training-time instruction tuning이라 우리 inference-time allocation과 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- framing: 모델 자체 생성의 활용, diversity 필터링, human data 의존 완화.
- baseline: instruction-tuned 모델을 우리 orchestration의 fixed backbone 후보로(경쟁 아님).
- metric: instruction-following 향상 — training-time gain과 inference-time gain 분해.
- ablation: 생성 데이터 diversity/필터링 효과(우리 path-pool 다양성 논의의 학습-측 대비).
- terminology: `self-instruct`, `self-generated instructions`, `instruction tuning`, `data bootstrapping`, `diversity filtering`.

## 8. 우리가 하면 안 되는 주장

- `self-generated instruction / synthetic instruction generation을 우리가 처음 제안한다`.
- `instruction tuning이 우리 기여다`.
- `모델 자체 생성을 활용하는 것이 우리 novelty다`.
- prompt family/route card를 단순 self-instruction 데이터 생성으로 정당화.

## 9. baseline / ablation 반영 아이디어

- prompt family/route card를 **inference-time 선택 단위**로 명시(학습 데이터 생성과 분리).
- instruction tuning은 backbone 확보 수단으로만, 비교 중심은 fixed backbone 위 test-time path-pool.
- 생성 diversity(학습)와 path-family diversity(추론)를 분리하는 ablation.

## 10. Related Work에 넣을 문장 초안

Self-Instruct(Wang et al., ACL 2023)는 instruction-tuned 모델이 human-written instruction data의 양·다양성 한계에 의존한다는 점에 착안해, 모델이 자체 생성한 instruction과 input/output instance를 필터링하여 fine-tune하는 self-generated instruction tuning을 제안했고, vanilla GPT-3에 적용해 SUPERNI에서 큰 향상을 얻었다. 이는 synthetic instruction generation과 instruction tuning의 대표적 연구다.

본 연구는 self-generated instruction이나 instruction tuning 자체를 새 기여로 두지 않는다. 우리의 prompt family와 route card는 training-time에 생성하는 instruction data가 아니라, fixed/given backbone 위에서 제한된 test-time compute 안의 heterogeneous reasoning path family를 문제별로 선택·중단하는 inference-time 의사결정 단위이며, 우리의 기여는 **state-conditioned test-time path-pool allocation**에 있다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 낮음~중간 (instruction tuning/self-generated data claim boundary; 직접 baseline 경쟁은 아님)
- 구현 결정: full reproduction 비대상. instruction tuning은 backbone 확보 수단으로만.
- 지금 할 일:
  - Self-Instruct를 Phased Instruction FT와 함께 instruction-tuning boundary로, distillation cluster 인접에 P1 reference로 고정.
  - `self-generated instruction / instruction tuning 자체를 novelty로 쓰지 않기` wording 가드.
  - prompt family/route card를 inference-time 선택 단위로 명시(self-instruction 데이터 생성과 분리).
- 나중으로 미뤄도 되는 일: Self-Instruct 재현, SUPERNI 평가.
- 한 줄 결론: Self-Instruct는 self-generated instruction tuning을 선점한 reference이며, 우리 prompt family/route card를 학습-측 instruction 생성이 아니라 test-time 선택 의사결정으로 분리하게 만드는 P1 reference다.
