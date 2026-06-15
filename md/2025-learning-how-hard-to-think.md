# Learning How Hard to Think: Input-Adaptive Allocation of LM Computation review

## 1. Metadata

- Title: Learning How Hard to Think: Input-Adaptive Allocation of LM Computation
- Authors: Mehul Damani, Idan Shenfeld, Andi Peng, Andreea Bobu, Jacob Andreas
- Year: 2025
- Venue / Status: ICLR 2025 conference paper
- Links:
  - OpenReview: https://openreview.net/forum?id=6qUUgw9bAZ
  - arXiv: https://arxiv.org/abs/2410.04707
  - ICLR Proceedings: https://proceedings.iclr.cc/paper_files/paper/2025/hash/ff414825df833edb8b1839e3d5d495e9-Abstract-Conference.html
- Code / Data:
  - Code: 공식 GitHub URL은 현재 미확인
  - Data / Benchmarks: Numina-COT, TACO, LMSYS-Chat, MATH, GSM8K, Anthropic HH
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

입력별로 추가 test-time compute의 marginal benefit을 예측하는 lightweight predictor를 학습하고, 이를 바탕으로 best-of-k sample 수나 weak/strong decoder routing을 adaptive하게 배분하는 input-adaptive TTC 논문이다.

## 3. 핵심 문제 설정

- 모든 입력에 동일한 decoding budget을 쓰는 것은 비효율적이라는 문제를 다룬다.
- 핵심 질문은 "어떤 query가 추가 compute로 실제 이득을 보는가"다.
- 이 논문은 query `x`와 budget `b`에 대해 expected reward 또는 marginal reward를 예측하고, 그 예측을 기반으로 budget을 배정한다.
- 다루는 setting은 크게 두 가지다.
  - `Adaptive Best-of-k`
  - `Adaptive Routing` between weak and strong decoders
- 따라서 selection unit은 reasoning trace 내부 state보다는 **query-level budget / sample count / decoder choice**에 가깝다.

## 4. 핵심 방법

- 학습 시 각 문제에 대해 여러 budget 또는 sample count에서 empirical reward curve를 만든다.
- 이후 LM hidden state 기반 MLP probe 또는 LoRA probe를 사용해 marginal reward를 예측한다.
- `Adaptive Best-of-k`
  - query별로 몇 개의 sample을 생성할지 정한다.
  - 생성된 후보 중 verifier 또는 reward model로 가장 좋은 답을 고른다.
- `Adaptive Routing`
  - weak decoder와 strong decoder 중 어느 쪽에 compute를 배정할지 정한다.
  - strong output이 weak output보다 나을 확률을 predictor가 예측한다.
- 중요 포인트:
  - allocation은 **query-only** 또는 query-level representation 기반이다.
  - 현재 reasoning pool의 answer histogram, disagreement, route usage 같은 **state-conditioned signal**은 핵심 입력이 아니다.

## 5. SLM-Math 관점의 재해석

- 이 논문은 내 연구와 매우 가깝지만, 정확히 같은 문제는 아니다.
- 공통점:
  - 제한된 TTC 안에서 어디에 compute를 쓸지 다룬다.
  - uniform budget보다 adaptive budget이 더 낫다는 framing을 공유한다.
- 차이점:
  - 이 논문은 주로 `query-level budget allocation`과 `weak/strong routing`을 다룬다.
  - 내 연구는 **현재까지 생성된 reasoning pool을 본 뒤, 다음에 어떤 reasoning path family 또는 macro strategy를 추가로 획득할지 결정**하는 문제를 본다.
- 따라서 이 논문은 "얼마나 더 생각할 것인가"에 가깝고, 내 연구는 "무엇을 더 생각할 것인가"에 가까워야 한다.

## 6. 우리 연구에 대한 novelty risk

- adaptive TTC 자체는 이미 새롭지 않다.
- input difficulty를 예측해 compute를 배분하는 것도 이미 새롭지 않다.
- MATH / GSM8K에서 adaptive compute allocation을 평가하는 것도 선행연구가 있다.
- weak/strong model routing도 이미 수행되었다.
- oracle allocation, uniform best-of-k, random routing 비교 구조도 이미 있다.
- 가장 위험한 claim:
  - `adaptive test-time compute allocation for mathematical reasoning`
- 안전한 방향:
  - `state-conditioned allocation over heterogeneous reasoning path families`
  - `macro strategy routing conditioned on the current reasoning pool`

## 7. 우리가 빌릴 수 있는 것

- 문제 framing:
  - not all inputs benefit equally from additional computation
  - marginal benefit of additional computation
  - hard-but-solvable queries
- baseline:
  - Uniform Best-of-k
  - Random routing
  - Oracle allocation
  - Query-only difficulty predictor
- metric:
  - Expected Success Rate
  - Compute reduction at matched accuracy
  - Accuracy improvement at fixed budget
  - Oracle gap
  - predictor calibration
- figure idea:
  - budget curve
  - difficulty / utility histogram
  - predicted vs actual utility calibration plot
  - budget별 allocation distribution
- protocol:
  - large sample bank 기반 empirical utility 추정
  - 같은 총 budget에서 uniform vs adaptive 비교

## 8. 우리가 하면 안 되는 주장

- 우리가 처음 adaptive TTC를 한다는 주장
- 우리가 처음 difficulty prediction으로 sample 수를 조절한다는 주장
- 우리가 처음 math reasoning에서 adaptive best-of-k를 다룬다는 주장
- uniform self-consistency보다 adaptive sampling이 좋다는 점 자체를 novelty로 삼는 주장
- hidden representation으로 reasoning difficulty를 예측하는 것이 새롭다는 주장
- title / abstract에서 `Adaptive Test-Time Compute Allocation`만 전면에 두는 것

## 9. baseline / ablation 반영 아이디어

- `Uniform Best-of-k / Self-Consistency` budget curve를 반드시 baseline으로 넣기
- `Query-only difficulty predictor` baseline을 별도 구현해 `state-conditioned reranker`와 직접 비교하기
- `Oracle allocation upper bound`를 micro-action과 macro-strategy 수준 모두에서 계산하기
- predictor calibration plot 추가하기
- low / medium / high difficulty bin별 allocation distribution 시각화하기
- `query-only vs state-conditioned` ablation을 main experiment question 중 하나로 올리기
- MATH / GSM8K English benchmark를 우선적인 비교축으로 검토하기
- false negative를 줄이는 2-stage answer verification 관점도 protocol에 반영하기

## 10. Related Work에 넣을 문장 초안

`Learning How Hard to Think`는 입력별로 추가 inference-time computation의 marginal benefit을 예측하고, 이를 바탕으로 best-of-k sample 수 또는 weak/strong decoder routing을 adaptive하게 결정하는 input-adaptive LM computation allocation 방법을 제안하였다. 이 연구는 Math, Code, Chat setting에서 learned predictor가 uniform compute allocation보다 더 효율적인 budget 사용을 가능하게 함을 보였고, 특히 MATH와 GSM8K에서도 adaptive allocation의 효과를 보고하였다.

그러나 이 연구의 selection unit은 주로 query-level budget 또는 weak/strong decoding procedure이며, 생성된 reasoning traces의 현재 상태를 바탕으로 heterogeneous reasoning path family를 순차적으로 구성하는 문제는 직접 다루지 않는다. 본 연구는 같은 prompt의 sample 수를 조절하는 adaptive best-of-k를 넘어서, CoT, prompt-diverse CoT, structured rationale, PoT, verifier-guided path 등 서로 다른 reasoning path family로 구성된 후보 풀을 state-conditioned 방식으로 확장하고, 제한된 TTC 안에서 어떤 path 또는 macro sampling strategy를 추가로 획득하고 언제 멈출지를 학습하는 문제에 초점을 둔다.

## 11. 현재 우선순위와 다음 액션

- 최종 priority: `P0`
- 위협도: 높음
- 지금 바로 반영할 것:
  - adaptive TTC 대표 related work로 고정
  - `adaptive compute allocation` 단독 claim을 피하도록 abstract/title 방향 수정
  - `query-only difficulty predictor` baseline 추가
  - `uniform SC / best-of-k / oracle allocation` curve를 protocol에 포함
  - `state-conditioned heterogeneous path-pool construction`을 핵심 차별점으로 고정
- 나중으로 미뤄도 되는 것:
  - 논문의 exact online/offline allocation algorithm 완전 재현
  - Chat/LMSYS setting 재현
  - Value-Augmented Sampling routing 재현
