# Confidence Improves Self-Consistency in LLMs review

## 1. Metadata

- Title: Confidence Improves Self-Consistency in LLMs
- Authors: Amir Taubenfeld, Tom Sheffer, Eran Ofek, Amir Feder, Ariel Goldstein, Zorik Gekhman, Gal Yona
- Year: 2025
- Venue / Status: Findings of ACL 2025
- Links:
  - ACL Anthology: https://aclanthology.org/2025.findings-acl.1030/
  - Code: https://github.com/taubenfeld/CISC
  - Google Research mirror: https://github.com/google-research/google-research/tree/master/cisc
- Benchmarks: GSM8K, MATH, MMLU-Pro, Big-Bench-Hard
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

CISC는 Self-Consistency에서 단순 majority vote 대신 path별 confidence를 추정하고 confidence-weighted majority vote를 수행함으로써, 훨씬 적은 sample 수로 비슷하거나 더 높은 성능을 얻는 confidence-informed aggregation 방법이다.

## 3. 핵심 문제 설정

- 기존 Self-Consistency는 여러 reasoning path를 생성한 뒤 final answer frequency만으로 답을 고른다.
- 이 방식은 같은 weight로 모든 sample을 취급하기 때문에, 명백히 이상한 path와 신뢰할 만한 path를 구분하지 못한다.
- 논문은 이 비효율 때문에 SC가 높은 TTC cost를 가진다고 본다.
- 따라서 핵심 질문은 다음과 같다.
  - 이미 생성된 reasoning paths 중 어떤 것을 더 믿을 것인가
  - 같은 accuracy를 더 적은 sample 수로 달성할 수 있는가
- 중요한 점은 이 논문이 **어떤 path family를 더 만들지**가 아니라, **이미 생성된 homogeneous path pool을 어떻게 더 잘 aggregate할지**를 다룬다는 것이다.

## 4. 핵심 방법

- 핵심 방법은 `Confidence-Informed Self-Consistency (CISC)`다.
- 기본 흐름:
  - 여러 reasoning path를 샘플링
  - 각 path와 answer에 대해 confidence score 추출
  - confidence를 softmax + temperature scaling으로 정규화
  - answer별 confidence-weighted vote를 합산
  - weighted score가 가장 큰 answer를 선택
- confidence extraction 방법은 세 가지 축으로 비교된다.
  - `Response Probability`
  - `Verbal Confidence`
  - `P(True)`
- 중요한 구현 포인트:
  - confidence는 reasoning 생성 뒤에 붙이는 `two-step prompting`으로 추출
  - reasoning path를 다시 바꾸지 않고 같은 path pool 위에서 aggregation만 바꾸도록 설계
  - 별도 학습 verifier가 아니라 **model-derived self-assessment score**가 lightweight verifier 역할을 수행

## 5. SLM-Math 관점의 재해석

- CISC는 현재 연구의 aggregation / verification / stopping 쪽에 매우 직접적으로 연결된다.
- 공통점:
  - 제한된 TTC에서 같은 sample budget으로 더 나은 final answer selection을 추구한다.
  - majority vote보다 더 정보량이 큰 aggregation signal을 쓴다.
- 차이점:
  - CISC는 homogeneous reasoning path pool이 이미 주어졌다고 보고, 그 위에서 confidence-weighted aggregation을 한다.
  - 내 연구는 그보다 앞선 단계에서 **어떤 path family를 추가로 샘플링할지**, **어떤 macro strategy를 쓸지**, **언제 STOP할지**를 다뤄야 한다.
- 한 문장으로 정리하면:
  - CISC는 sampled paths를 어떻게 aggregate할지 연구한다.
  - 내 연구는 어떤 종류의 paths를 애초에 더 샘플링할지 연구해야 한다.

## 6. 우리 연구에 대한 novelty risk

- SC efficiency는 이미 강하게 연구되어 있다.
- confidence 기반 candidate selection은 이미 강한 baseline이다.
- 단순 majority vote 개선은 novelty가 아니다.
- within-question confidence discrimination 관점도 이미 있다.
- `모델의 self-confidence로 path quality를 평가할 수 있다`는 주장도 이미 강하다.
- 특히 위험한 claim:
  - "reasoning path를 여러 개 만들고, confidence/verifier로 좋은 답을 고른다"
- 안전한 방향:
  - confidence-informed aggregation을 강한 baseline으로 수용하고
  - 그보다 앞 단계의 `heterogeneous path-family acquisition / state-conditioned strategy allocation`으로 이동

## 7. 우리가 빌릴 수 있는 것

- 문제 framing:
  - SC는 성능을 올리지만 긴 reasoning path를 많이 생성해야 하므로 비싸다
  - path quality를 반영한 aggregation이 sample efficiency를 높일 수 있다
- baseline:
  - vanilla SC
  - CISC with `P(True)`
  - CISC with `Response Probability`
  - CISC with `Verbal Confidence`
  - max-confidence
  - tie-breaker
- metric:
  - `% Cost Reduction`
  - `% Accuracy Improvement`
  - `Within-Question Discrimination (WQD)`
  - budget-accuracy curve
  - comparable SC responses
- ablation:
  - majority vote vs weighted vote
  - P(True) vs verbal confidence vs response probability
  - normalization vs no normalization
  - tuned temperature vs default temperature
  - max-confidence vs weighted aggregation
- figure idea:
  - budget-accuracy curve
  - SC가 같은 성능에 도달하기 위해 필요한 sample 수 비교
  - frequency vote와 confidence-weighted vote가 다른 결정을 내리는 case study

## 8. 우리가 하면 안 되는 주장

- Self-Consistency의 test-time cost를 줄이는 것이 주된 novelty라는 주장
- confidence 기반 weighted voting이 새로운 접근이라는 주장
- majority vote보다 confidence vote가 좋다는 점을 main contribution으로 삼는 주장
- self-confidence로 path 품질을 평가할 수 있다는 주장을 새로 한다는 서술
- calibration만 보면 충분하다는 주장
- highest-confidence sample 하나만 고르면 된다는 주장
- SC baseline만 이기면 충분하다는 주장

## 9. baseline / ablation 반영 아이디어

- `CISC with P(True)`를 현재 vote bank에 구현하기
- vanilla majority vote, CISC, max-confidence, tie-breaker를 함께 비교하기
- homogeneous SC와 heterogeneous pool 모두에서 CISC를 aggregation baseline으로 적용하기
- `WQD`를 route별 confidence scorer 평가 metric으로 도입하기
- confidence-weighted vote를 strategy-card reranker feature 후보로 올리기
- softmax temperature tuning protocol을 별도 spec으로 정리하기
- confidence overhead 포함/미포함 cost 계산을 분리하기
- main result table을 `SC 대비`가 아니라 `SC 및 CISC 대비` 구조로 재정리하기

## 10. Related Work에 넣을 문장 초안

Self-Consistency 계열 연구는 여러 reasoning path를 샘플링한 뒤 다수결로 최종 답을 선택함으로써 reasoning 성능을 개선하지만, 충분한 수의 긴 reasoning path를 생성해야 하므로 test-time compute 비용이 크다. `Confidence Improves Self-Consistency in LLMs`는 이 문제를 줄이기 위해 `Confidence-Informed Self-Consistency (CISC)`를 제안하였다. CISC는 각 reasoning path에 대해 모델이 산출한 confidence score를 부여하고, 이를 softmax temperature scaling으로 정규화한 뒤 confidence-weighted majority vote를 수행한다. 이 방법은 GSM8K, MATH, MMLU-Pro, BBH 및 여러 open-weight LLM에서 vanilla Self-Consistency보다 적은 sample 수로 유사하거나 더 높은 성능을 보였으며, 특히 `P(True)` 기반 confidence가 강한 결과를 보였다.

그러나 CISC는 주어진 path pool을 어떻게 더 잘 aggregate할 것인가에 초점을 둔다. 즉, 어떤 reasoning path family를 추가로 샘플링할지, 언제 heterogeneous path를 섞을지, 현재 answer distribution과 route history를 보고 STOP할지 여부는 직접 다루지 않는다. 본 연구는 CISC를 강한 aggregation baseline으로 포함하되, 그보다 앞선 단계인 제한된 TTC 안에서 heterogeneous reasoning path pool을 state-conditionally 구성하고, path-family 또는 macro strategy 수준에서 compute를 배분하는 문제를 다룬다.

## 11. 현재 우선순위와 다음 액션

- 최종 priority: `P0`
- 위협도: 높음
- 지금 바로 반영할 것:
  - `CISC with P(True)`를 baseline으로 구현
  - 현재 Axis 2 majority vote 결과를 CISC aggregation으로 재평가
  - homogeneous CoT-SC, multiple-CoT, CG-inclusive pool 각각에서 CISC gain을 확인
  - `WQD`를 confidence scorer 평가 metric으로 구현
  - 논문 draft에서 `SC 대비 개선`이 아니라 `SC 및 CISC 대비 개선`으로 result table 구조를 바꾸기
- 나중으로 미뤄도 되는 것:
  - hidden-state confidence 활용
  - trainable confidence model
  - full human evaluation 재현
  - Tree of Thoughts / Graph of Thoughts와의 결합
