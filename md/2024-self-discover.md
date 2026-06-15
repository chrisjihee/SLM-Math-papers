# Self-Discover: Large Language Models Self-Compose Reasoning Structures review

## 1. Metadata

- Title: Self-Discover: Large Language Models Self-Compose Reasoning Structures
- Authors: Pei Zhou, Jay Pujara, Xiang Ren, Xinyun Chen, Heng-Tze Cheng, Quoc V. Le, Ed H. Chi, Denny Zhou, Swaroop Mishra, Huaixiu Steven Zheng
- Year: 2024
- Venue / Status: NeurIPS 2024
- Links:
  - arXiv: https://arxiv.org/abs/2402.03620
  - OpenReview: https://openreview.net/forum?id=BROvXhmzYK
- Code / Data:
  - 법적 제약 때문에 full code/data는 공개하지 못한다고 밝힘
  - 대신 재현을 위한 prompt와 inference procedure를 제공
- Benchmarks: BBH, T4D, MATH subset, MMLU subset
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

Self-Discover는 LLM이 atomic reasoning modules를 `SELECT-ADAPT-IMPLEMENT`하여 task-specific reasoning structure를 만들고, 이후 각 instance를 그 구조에 따라 풀게 함으로써 CoT, Plan-and-Solve, CoT-Self-Consistency보다 적은 inference call로 더 높은 성능을 얻는 structured prompting 방법이다.

## 3. 핵심 문제 설정

- 기존 CoT류 prompting은 하나의 reasoning method를 고정된 prior처럼 사용한다.
- 논문은 각 task마다 더 잘 맞는 intrinsic reasoning structure가 있을 수 있다고 본다.
- 따라서 핵심 질문은 다음이다.
  - reasoning method를 고정하지 말고 task에 맞게 스스로 구성할 수 있는가
  - 반복 sampling 없이도 structured prompting으로 compute-efficient한 성능 향상을 만들 수 있는가
- 내 연구와의 연결은 매우 직접적이지만, 선택 시점과 선택 단위가 다르다.
  - Self-Discover: task-level 또는 instance-level one-shot structure composition
  - 내 연구: 현재 reasoning state를 보고 다음 path family / macro strategy / STOP을 결정

## 4. 핵심 방법

- 핵심은 LLM이 atomic reasoning modules를 직접 조합해 task-specific reasoning structure를 만드는 것이다.
- 세 단계:
  - `SELECT`: 전체 reasoning module set에서 유용한 modules 선택
  - `ADAPT`: 선택된 modules를 task-specific하게 재표현
  - `IMPLEMENT`: adapted modules를 JSON-like key-value reasoning structure로 구현
- 이후 solving 단계에서는 이 structure를 prompt로 붙여 각 instance를 푼다.
- 방법 관점에서 보면:
  - reasoning path: 단일 CoT가 아니라 composition된 structured reasoning path
  - sampling: 반복 샘플링보다 structure composition으로 효율 확보
  - self-consistency: baseline으로 두지만 직접 사용하지는 않음
  - verifier / PRM: 없음
  - routing: task-level reasoning structure / strategy selection
  - search: MCTS류가 아니라 meta-prompt 기반 structure construction

## 5. SLM-Math 관점의 재해석

- Self-Discover는 `strategy selection / reasoning structure selection` 축의 강한 선행연구다.
- 공통점:
  - reasoning strategy는 task/problem에 따라 달라져야 한다는 점을 강하게 보여 준다.
  - structured prompting이 fixed CoT보다 나을 수 있음을 보인다.
- 차이점:
  - Self-Discover는 하나의 task-specific structure를 먼저 만들고, 그 구조를 따라 푼다.
  - 내 연구는 여러 reasoning structures/path families가 이미 가능할 때, **현재 answer distribution, disagreement, budget remaining, verifier signal**을 보고 다음 액션을 정하는 문제를 본다.
- 따라서 Self-Discover는 `one-shot strategy composition`, 내 연구는 `state-conditioned sequential path acquisition and stopping`으로 정리해야 한다.

## 6. 우리 연구에 대한 novelty risk

- `CoT 하나보다 task-specific reasoning structure가 낫다`는 주장은 이미 강하게 제시되었다.
- `여러 reasoning modules를 조합한다`는 claim도 이미 선점되었다.
- `Self-Consistency보다 compute-efficient한 structured prompting`이라는 주장도 이미 있다.
- `strategy selection 자체`만으로는 novelty가 되기 어렵다.
- `structured reasoning plan을 자동 생성한다`는 점도 이미 선행연구가 있다.
- 특히 위험한 claim:
  - `structured rationale이 CoT보다 낫다`
  - `우리가 처음으로 여러 reasoning strategy를 조합한다`
  - `strategy selection 자체가 novelty다`
- 안전한 방향:
  - `state-conditioned path acquisition`
  - `heterogeneous reasoning path pool`
  - `macro strategy routing`
  - `budget-aware stopping`

## 7. 우리가 빌릴 수 있는 것

- 문제 framing:
  - 각 task/problem에는 적합한 reasoning structure가 다르다
  - CoT는 하나의 atomic reasoning module일 뿐이다
  - reasoning method를 고정하지 말고 구성/선택해야 한다
- baseline:
  - Direct
  - CoT
  - Plan-and-Solve
  - CoT-Self-Consistency
  - Majority voting over reasoning modules
  - Best-of-each-module oracle
  - Self-Discover-style structure prompt
- metric:
  - Accuracy
  - Inference calls per instance
  - Token-adjusted compute
  - Budget-normalized accuracy
  - structure error vs execution/computation error
- ablation:
  - `SELECT` only vs `SELECT+ADAPT` vs `SELECT+ADAPT+IMPLEMENT`
  - task-level structure vs instance-level structure
  - model-generated structure vs prompt-optimized structure
  - teacher-generated structure transfer
- figure idea:
  - accuracy vs inference calls plot
  - action-stage ablation
  - structure error vs computation error 분석 표

## 8. 우리가 하면 안 되는 주장

- 우리가 처음 여러 reasoning strategy를 조합한다는 주장
- structured rationale이 CoT보다 낫다는 점 자체를 핵심 contribution으로 두는 주장
- SC보다 inference-efficient한 structured prompting이 새롭다는 주장
- `CG`가 graph/structure이므로 CoT보다 본질적으로 우월하다는 주장
- strategy selection 자체가 novelty라는 주장
- JSON structured output을 쓰면 reasoning quality가 좋아진다는 단순 주장

## 9. baseline / ablation 반영 아이디어

- Self-Discover-style `SELECT-ADAPT-IMPLEMENT` baseline 또는 최소 prompt-only baseline 설계
- `CoT`, `Plan-and-Solve`, `Self-Discover`, `CoT-SC`, `Prompt-diverse CoT`, `Macro Strategy Router`를 같은 budget table에 배치
- x축 compute, y축 accuracy의 budget-efficiency plot 작성
- strategy-card schema에 `selected modules`, `adapted rationale`, `expected failure mode`, `when useful` 필드 추가 검토
- `structure/planning error` vs `execution/computation error` 분석 도입
- task-level strategy vs instance-level strategy vs state-conditioned sequential strategy 비교

## 10. Related Work에 넣을 문장 초안

Self-Discover는 CoT와 같은 단일 prompting strategy를 고정하는 대신, LLM이 task examples와 atomic reasoning modules를 바탕으로 `SELECT`, `ADAPT`, `IMPLEMENT` 단계를 거쳐 task-specific reasoning structure를 구성하도록 한다. 이 방법은 BBH, T4D, MATH에서 Direct Prompting, CoT, Plan-and-Solve보다 높은 성능을 보였고, CoT-Self-Consistency나 reasoning-module majority voting보다 훨씬 적은 inference call로 competitive한 성능을 달성했다. 특히 이 논문은 reasoning strategy가 task에 따라 달라져야 한다는 점을 강하게 보여준다.

그러나 Self-Discover는 주로 task-level 또는 instance-level에서 하나의 reasoning structure를 먼저 구성한 뒤, 각 문제를 그 구조에 따라 푸는 방식이다. 즉, reasoning 과정 중 생성된 후보들의 answer distribution, route disagreement, budget remaining, verifier signal을 관찰하면서 다음 reasoning path family를 선택하거나 STOP하는 문제는 직접 다루지 않는다. 본 연구는 Self-Discover와 같은 task-level reasoning-structure composition 연구를 확장하여, SLM mathematical reasoning에서 현재 reasoning state에 조건화된 path acquisition, macro sampling strategy selection, verifier-aware stopping을 다룬다.

## 11. 현재 우선순위와 다음 액션

- 최종 priority: `P0`
- 위협도: 높음
- 지금 바로 반영할 것:
  - Self-Discover를 related work P0로 고정
  - `structured reasoning이 CoT보다 낫다`는 claim을 제거
  - Self-Discover-style structured prompting을 baseline 또는 최소 비교 대상으로 추가
  - macro strategy-card 설계 시 `SELECT-ADAPT-IMPLEMENT` 아이디어 참고
  - 실험 표에 `inference calls`, `token cost`, `accuracy`, `budget-normalized accuracy` 포함
- 나중으로 미뤄도 되는 것:
  - human reasoning pattern 비교
  - OPRO와의 full transferability 비교
  - BBH/T4D 전체 재현
