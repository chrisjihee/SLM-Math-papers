# Let's Verify Step by Step review

## 1. Metadata

- Title: Let's Verify Step by Step
- Authors: Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe
- Year: 2024
- Venue / Status: ICLR 2024 conference paper
- Link: https://openreview.net/forum?id=v8L0pN6EOi
- Code / Data:
  - Dataset: `PRM800K`
  - GitHub: https://github.com/openai/prm800k
- Benchmarks: `MATH`, OOD STEM subsets (`AP Calculus`, `AP Chemistry`, `AP Physics`, `AMC10/12`)
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

**Let's Verify Step by Step**은 mathematical reasoning에서 final answer만 보는 outcome supervision보다 각 reasoning step의 correctness를 학습한 **Process-Supervised Reward Model(PRM)**이 best-of-N candidate selection에서 더 강력한 verifier가 될 수 있음을 보인 canonical paper다.

## 3. 핵심 문제 설정

- multi-step mathematical reasoning에서는 final answer만 맞다고 해서 reasoning path 전체가 신뢰할 만한 것은 아니다.
- 기존 outcome-supervised verifier는 final answer correctness만 보기 때문에, 잘못된 reasoning이 중간에 포함된 solution도 positive로 학습될 수 있다.
- 이 논문은 핵심 질문을 다음처럼 둔다.
  - reward model을 final answer outcome으로 학습할 것인가
  - intermediate reasoning step correctness로 학습할 것인가
- 즉, 문제는 `어떤 path family를 생성할 것인가`보다 **이미 생성된 여러 solution candidate 중 어떤 path를 선택할 것인가**에 가깝다.
- 현재 SLM-Math와의 연결은 매우 직접적이다.
  - 이 논문은 downstream **verification / reranking / candidate selection** baseline이다.
  - 내 연구는 그보다 앞단의 **candidate pool construction / path-family allocation / stopping**으로 차별화해야 한다.

## 4. 핵심 방법

- generator는 `MATH` 문제마다 여러 개의 newline-delimited step-by-step solutions를 생성한다.
- 추론 시 구조는 간단하다.
  - N개의 solution 생성
  - reward model이 각 solution을 score
  - highest-score solution 선택
- 핵심 비교는 `ORM` vs `PRM`이다.
  - `ORM`: final answer correctness를 supervision으로 학습
  - `PRM`: 각 reasoning step의 correctness를 supervision으로 학습
- PRM은 step-level correctness probability를 solution-level score로 집계해 best-of-N selection에 사용한다.
- search는 `MCTS`나 reflection이 아니라 **fixed-budget sample generation + verifier reranking**에 가깝다.
- 데이터 측면에서는 `PRM800K`를 구축했고, 특히 current PRM이 높게 평가하지만 final answer는 틀린 `convincing wrong-answer solutions`를 우선 수집하는 active learning 전략을 사용했다.

## 5. SLM-Math 관점의 재해석

- 이 논문은 현재 연구의 전체 pipeline에서 **후단 selector**에 해당한다.
- 공통점:
  - 여러 reasoning candidates를 모은 뒤 무엇을 더 신뢰할지 다룬다.
  - majority voting보다 verifier-based selection이 강할 수 있음을 보여준다.
  - reasoning correctness와 final answer correctness를 분리해서 본다.
- 차이점:
  - 이 논문은 candidate pool이 이미 주어졌다고 본다.
  - 내 연구는 limited TTC 안에서 `direct`, `CoT`, `prompt-diverse CoT`, `PoT/PAL`, `structured rationale`, `CG`, `verifier-guided path` 등 **어떤 path family를 더 샘플링할지**를 먼저 결정해야 한다.
- 안전한 한 문장 차별화:
  - PRM은 fixed candidate pool 위의 strong selector이고, 내 연구는 **PRM이 평가할 candidate pool 자체를 어떻게 state-conditionally 구성할지**를 다뤄야 한다.

## 6. 우리 연구에 대한 novelty risk

- `여러 풀이 후보 중 verifier로 좋은 것을 고른다`는 claim은 새롭지 않다.
- `majority voting보다 reward-model selection이 강하다`는 점도 이미 보였다.
- `step-level process supervision`이 outcome supervision보다 강하다는 경험적 prior도 이미 강하다.
- 따라서 voting-only 결과만 제시하면 reviewer가 `왜 PRM/verifier baseline이 없는가`를 바로 물을 가능성이 높다.
- 특히 위험한 claim:
  - `verifier / reranker를 붙인 multi-sample reasoning`
  - `good candidate selection이 본 논문의 핵심 novelty`
  - `Best-of-N 성능 향상을 TTC allocation novelty로 해석`
- 안전한 방향:
  - `candidate selection`이 아니라
  - **candidate pool construction / path-family allocation / state-conditioned stopping**

## 7. 우리가 빌릴 수 있는 것

- 문제 framing:
  - final answer correctness는 reasoning correctness의 불완전한 proxy다
  - candidate generation과 candidate selection은 분리해서 봐야 한다
  - verifier는 path pool quality가 높을수록 더 중요해진다
- baseline:
  - Majority Voting
  - ORM-style final-answer verifier
  - PRM-style step verifier
  - Best-of-N + verifier selection
- metric:
  - Best-of-N accuracy
  - accuracy vs N curve
  - budget-normalized accuracy
  - OOD Best-of-N
  - verifier false positive / false negative case analysis
- ablation:
  - Majority Voting vs ORM vs PRM
  - outcome supervision vs process supervision
  - step-score reduction 방식
  - active learning vs uniform sampling
  - low-budget vs high-budget regime
- figure/table idea:
  - x축 N, y축 solved % verifier comparison curve
  - path별 step score heatmap
  - verifier failure taxonomy
  - fixed pool + voting vs fixed pool + verifier selection 비교표

## 8. 우리가 하면 안 되는 주장

- `verifier/reranker를 도입한 것이 새롭다`고 쓰면 안 된다.
- `majority voting이 multi-sample reasoning의 최선의 selection rule`이라고 전제하면 안 된다.
- `final answer correctness만으로 reasoning path quality를 충분히 평가할 수 있다`고 쓰면 안 된다.
- `step-level verifier는 우리 범위 밖이므로 baseline 없이 넘어가도 된다`고 쓰면 안 된다.
- `우리 route reranker가 PRM과 같은 종류의 verifier다`라고 쓰면 안 된다.
- `CG나 structured rationale이 reasoning correctness를 자동 보장한다`고 쓰면 안 된다.
- `Best-of-N gain`을 곧바로 `adaptive TTC novelty`처럼 쓰면 안 된다.

## 9. baseline / ablation 반영 아이디어

- majority voting만이 아니라 verifier selection 결과도 함께 보고한다.
- fixed homogeneous CoT best-of-N + verifier selection을 strong baseline으로 둔다.
- `우리 방법 + majority voting`과 `우리 방법 + verifier selection`을 둘 다 평가한다.
- same candidate pool에서 voting과 verifier selection을 분리 비교한다.
- low-budget (`4, 8, 16, 32`) 구간에서 verifier gain이 얼마나 있는지 별도로 본다.
- verifier false positive taxonomy를 route/strategy reranker failure taxonomy와 연결한다.
- step-level PRM을 직접 학습하지 않더라도, 왜 first paper에서는 lightweight upstream controller를 우선하는지 문서에 명시한다.

## 10. Related Work에 넣을 문장 초안

**Let's Verify Step by Step**은 mathematical reasoning에서 final answer만을 supervision으로 사용하는 outcome-supervised reward model보다, 각 intermediate step의 correctness를 학습하는 process-supervised reward model이 더 신뢰할 수 있는 verifier가 될 수 있음을 보였다. 특히 `MATH`에서 다수의 sampled solutions를 생성한 뒤 PRM으로 best-of-N selection을 수행하면 majority voting과 outcome-supervised verifier보다 높은 성능을 달성할 수 있음을 보였으며, `PRM800K`라는 대규모 step-level human feedback dataset도 공개하였다.

그러나 이 연구는 주어진 generator가 생성한 candidate pool을 어떻게 평가하고 선택할 것인가에 초점을 둔다. 즉, 제한된 test-time budget 안에서 어떤 reasoning path family를 추가로 샘플링할지, 언제 exploration을 멈출지, heterogeneous path pool을 어떻게 구성할지는 직접 다루지 않는다. 따라서 PRM은 강력한 downstream selector이지만, candidate pool construction policy 자체는 별도의 문제로 남아 있다.

본 연구는 PRM-based verification을 대체하기보다, 그 앞단에서 작동하는 **state-conditioned reasoning path acquisition and stopping** 문제를 다룬다. 우리는 small language model이 제한된 TTC 안에서 `direct`, `CoT`, `prompt-diverse CoT`, `structured rationale`, `PoT`, `tool-augmented path` 등 heterogeneous reasoning paths를 어떻게 구성하고, 이후 majority voting 또는 verifier selection과 어떻게 결합할 수 있는지를 분석한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 높음
- 지금 당장 해야 할 일:
  - baseline 목록에 `Best-of-N + PRM / ORM / Majority Voting`을 명시
  - novelty 문장에서 `verifier로 candidate를 고른다`는 표현 제거
  - contribution을 `candidate pool construction`, `path-family allocation`, `state-conditioned acquisition`, `limited-budget stopping`으로 이동
  - voting-only 결과와 verifier-selection 결과를 모두 보여줄 계획 수립
- 나중으로 미뤄도 되는 일:
  - `PRM800K` full reproduction
  - full step-level human annotation pipeline
  - RL generator fine-tuning
- 한 문장 결론:
  - PRM은 경쟁자라기보다 **강한 downstream selector baseline**이고, 내 연구는 그 앞단의 **upstream path acquisition controller**로 포지셔닝하는 것이 가장 안전하다.
