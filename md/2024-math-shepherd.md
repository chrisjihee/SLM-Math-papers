# Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations review

## 1. Metadata

- Title: Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations
- Authors: Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, Zhifang Sui
- Year: 2024
- Venue / Status: ACL 2024 Long Papers
- Link: https://aclanthology.org/2024.acl-long.510/
- Code / Data:
  - Human annotation 없이 자동 process supervision으로 구성된 PRM training data
  - `GSM8K`, `MATH`, `MATH500`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

Math-Shepherd는 자동 생성된 completion-based supervision으로 step-by-step reasoning의 Process Reward Model(PRM)을 학습해, best-of-N reranking과 step-level RL에서 Self-Consistency와 ORM보다 강한 verifier 성능을 보이는 논문이다.

## 3. 핵심 문제 설정

- LLM이 여러 수학 풀이 후보를 생성했을 때, 어떤 풀이가 최종 답으로 신뢰할 만한지 더 정밀하게 고르는 문제가 핵심이다.
- 기존 PRM은 사람의 step-level annotation에 의존하는 경우가 많아 비용이 크다.
- Math-Shepherd는 human label 없이 자동 process supervision을 구성해 PRM을 학습할 수 있는지를 묻는다.
- 즉, 이 논문은 **candidate generation**보다 **candidate verification / reranking**에 더 가깝다.
- 내 연구와의 연결점은 매우 직접적이지만, 차이점도 분명하다.
  - Math-Shepherd는 생성된 candidate solution을 어떻게 검증할지 다룬다.
  - 내 연구는 어떤 reasoning path family를 언제 더 샘플링할지, 그리고 언제 멈출지를 먼저 결정해야 한다.

## 4. 핵심 방법

- reasoning path는 step-by-step solution이다.
- PRM 학습을 위해 각 중간 step에서 여러 후속 completion을 생성하고, golden answer에 도달하는지 확인해 step label을 자동으로 만든다.
- verification 시에는 문제당 N개의 candidate solution을 생성한 뒤 PRM이 scoring하고, 최고 score candidate를 선택한다.
- 핵심 구조:
  - `ORM`: final answer correctness를 학습
  - `PRM`: 각 reasoning step의 correctness를 학습
  - `PRM final score`: step scores의 minimum
- Self-Consistency는 baseline이며, SC + PRM 결합도 실험한다.
- search는 MCTS가 아니라 completion-based Monte Carlo estimation과 best-of-N reranking에 가깝다.
- training-heavy 요소도 있다.
  - automatic process supervision으로 PRM 데이터 구축
  - step-level PPO까지 사용

## 5. SLM-Math 관점의 재해석

- 이 논문은 내 연구 pipeline에서 downstream verifier에 해당한다.
- 공통점:
  - multi-sample reasoning에서 어떤 풀이를 고를지 다룬다.
  - reasoning correctness를 final answer correctness와 분리해서 본다.
  - majority voting보다 verifier-based selection이 강할 수 있음을 보여준다.
- 차이점:
  - 이 논문은 이미 생성된 candidate pool을 평가한다.
  - 내 연구는 `direct`, `CoT`, `prompt-diverse CoT`, `PoT`, `CG`, `verifier-guided path` 같은 heterogeneous path family 중 무엇을 더 acquisition할지 결정해야 한다.
- 안전한 한 문장 차별화:
  - Math-Shepherd는 strong downstream PRM selector이고, 내 연구는 **PRM이 평가할 후보 풀을 어떻게 state-conditionally 구성할지**를 다뤄야 한다.

## 6. 우리 연구에 대한 novelty risk

- `verifier 기반 candidate selection`은 이미 선점되어 있다.
- `best-of-N reranking`도 새롭지 않다.
- `step-level process supervision`도 새롭지 않다.
- `SC보다 verifier가 강할 수 있다`는 주장도 이미 확인되었다.
- `자동 process annotation`도 이미 강한 선행축이다.
- 따라서 risk가 큰 claim:
  - `여러 reasoning candidates를 생성한 뒤 verifier/reranker로 고른다`
  - `best-of-N verification이 본 논문의 핵심 novelty다`
  - `candidate selection이 우리의 main contribution이다`
- 안전한 방향:
  - verification보다 앞단의 **candidate pool construction / path-family allocation / stopping**

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - top-1 generation은 불안정하다
  - step-level verification은 outcome-level보다 더 정밀하다
  - candidate generation과 selection은 분리해야 한다
- baseline:
  - Self-Consistency / majority voting
  - ORM
  - PRM
  - Self-Consistency + ORM
  - Self-Consistency + PRM
  - Best-of-N with verifier
- metric:
  - Best-of-N accuracy
  - accuracy vs N curve
  - OOD transfer score
  - greedy accuracy after RL
  - verifier cost까지 포함한 cost-normalized accuracy
- ablation:
  - N = 1, 4, 16, 64, 256
  - ORM vs PRM
  - PRM vs SC + PRM
  - HE vs SE labels
  - generator size vs verifier size mismatch
  - active learning vs uniform sampling
- figure/table idea:
  - accuracy vs candidate count curve
  - generator size × verifier size comparison
  - SC / ORM / PRM / SC+PRM table
  - verifier catches intermediate error case study

## 8. 우리가 하면 안 되는 주장

- `verifier/reranker를 도입한 것이 새롭다`고 쓰면 안 된다.
- `step-level reward를 human annotation 없이 만든 것이 새롭다`고만 쓰면 안 된다.
- `majority voting이 최선`이라고 쓰면 안 된다.
- `final answer correctness만으로 reasoning quality를 충분히 평가할 수 있다`고 쓰면 안 된다.
- `우리 route-card reranker가 PRM과 같은 verifier다`라고 쓰면 안 된다.
- `Best-of-N gain`을 그대로 `adaptive TTC novelty`로 번역하면 안 된다.
- `PRM 자체가 우리 연구의 novelty다`라고 쓰면 안 된다.

## 9. baseline / ablation 반영 아이디어

- SC, ORM, PRM, SC + PRM을 baseline taxonomy에 명시한다.
- verifier-based reranking baseline을 main table에 넣는다.
- `우리 방법 + majority voting`과 `우리 방법 + verifier selection`을 둘 다 평가한다.
- `N`을 여러 구간으로 바꿔 verifier benefit curve를 본다.
- `PRM final score = min step score` aggregation과 다른 aggregation을 비교한다.
- route-card / strategy-card는 candidate verification이 아니라 acquisition policy로 역할을 분리한다.
- completion-based oracle label과 우리 vote-bank oracle의 차이를 문서화한다.

## 10. Related Work에 넣을 문장 초안

Math-Shepherd는 human step-level annotation 없이도 automatic process supervision으로 Process Reward Model(PRM)을 학습할 수 있음을 보여 주었고, 이를 best-of-N verification과 step-level RL에 활용했다. 이 방법은 `GSM8K`와 `MATH`에서 Self-Consistency 및 Outcome Reward Model(ORM)보다 더 강한 verification 성능을 보였으며, step-level reward가 reasoning 오류를 더 정밀하게 포착할 수 있음을 시사한다.

그러나 Math-Shepherd의 초점은 이미 생성된 candidate solution을 step-level reward로 평가하고 rerank하는 데 있다. 즉, test-time budget 안에서 어떤 reasoning path family를 더 샘플링할지, 언제 exploration을 멈출지, heterogeneous path pool을 어떻게 구성할지는 직접 다루지 않는다. 따라서 PRM은 강력한 downstream selector이지만, candidate pool construction policy 자체는 별도의 문제로 남아 있다.

본 연구는 Math-Shepherd와 같은 verifier 기반 reasoning 연구를 기반으로 하되, verifier 자체를 새 contribution으로 제안하기보다 **state-conditioned reasoning path acquisition and stopping** 문제를 다룬다. 우리의 초점은 `CoT`, `prompt-diverse CoT`, `structured rationale`, `PoT`, `direct solving` 등 heterogeneous reasoning path pool을 제한된 TTC 안에서 어떻게 구성하고, 이후 majority voting 또는 verifier selection과 결합할지에 있다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 높음
- 지금 당장 해야 할 일:
  - Related Work에서 verifier / PRM 축의 핵심 논문으로 배치
  - SC-only, majority-voting-only 결과를 main claim으로 삼지 않도록 실험 설계 수정
  - PRM / ORM reranking을 baseline 또는 upper baseline으로 포함
  - route-card / strategy-card reranker를 solution verifier가 아니라 path acquisition policy로 문서화
  - MATH / MATH500에서 budget-accuracy curve와 verifier-aware selection을 포함
- 나중으로 미뤄도 되는 일:
  - full PRM을 직접 재학습하는 것
  - step-level PPO를 재현하는 것
  - 자동 process annotation dataset을 대규모로 새로 구축하는 것
- 한 문장 결론:
  - Math-Shepherd는 competition target이라기보다, **내 연구가 넘어서야 할 downstream verifier baseline**이며, 내 novelty는 그 앞단의 **candidate pool construction / path-family allocation**에 있어야 한다.
