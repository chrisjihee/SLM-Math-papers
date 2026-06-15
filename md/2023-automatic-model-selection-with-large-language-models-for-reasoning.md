# Automatic Model Selection with Large Language Models for Reasoning review

## 1. Metadata

- Title: Automatic Model Selection with Large Language Models for Reasoning
- Authors: James Xu Zhao, Yuxi Xie, Kenji Kawaguchi, Junxian He, Michael Qizhe Xie
- Year: 2023
- Venue / Status: Findings of EMNLP 2023
- Links:
  - ACL Anthology: https://aclanthology.org/2023.findings-emnlp.55/
  - arXiv: https://arxiv.org/abs/2305.14333
  - GitHub: https://github.com/XuZhao0/Model-Selection-Reasoning
- Code / Data:
  - code, prompts, dataset 공개
  - Benchmarks: `GSM8K`, `SVAMP`, `ASDIV`, `SingleOP`, `SingleEQ`, `AddSub`, `MultiArith`, `Date Understanding`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

이 논문은 `CoT`와 `PAL`처럼 서로 다른 강점과 약점을 가진 reasoning method를 모두 실행한 뒤, LLM selector가 문제별로 더 나은 해법을 선택하게 하면 self-consistency보다 낮은 비용으로 더 높은 성능을 얻을 수 있음을 보인다.

## 3. 핵심 문제 설정

- 하나의 reasoning method가 모든 문제에 최적이지 않다는 문제에서 출발한다.
- 저자들은 `CoT`와 `PAL`이 서로 다른 error distribution과 강점/약점을 가진다고 본다.
- 기존 한계는 두 가지다.
  - CoT나 PAL 하나만 고정하면 문제별 적합성을 무시한다.
  - self-consistency는 비용이 크고, 서로 다른 method의 강점을 명시적으로 선택하지 않는다.
- 따라서 이 논문은 `어떤 reasoning method가 현재 문제에 더 적합한가`를 고르는 selection 문제를 다룬다.
- 내 연구와의 연결은 매우 직접적이지만, 이 논문은 **one-shot post-hoc model selection**이고, 내 연구는 **state-conditioned path acquisition / stopping**으로 가야 한다.

## 4. 핵심 방법

- reasoning path는 크게 두 종류다.
  - `CoT`: natural language reasoning chain
  - `PAL`: Python program / interpreter 기반 reasoning
- 전체 과정은 두 단계다.
  - 같은 문제에 대해 `CoT` solution과 `PAL` solution을 각각 생성
  - 두 답이 다를 때 LLM selector가 어느 method가 더 맞는지 고름
- selector 입력에는 문제, CoT chain, CoT answer, PAL chain 등이 들어간다.
- selector는 선택과 짧은 explanation을 함께 생성한다.
- 별도 selector 학습 없이 few-shot prompting 기반으로 동작한다.
- self-consistency와도 결합한다.
  - `Ours@k`는 selection 과정을 k회 반복한 뒤 majority voting
- 중요한 이론적 메시지는 method 간 상보성이다.
  - 비슷한 method끼리는 improvement가 작고
  - 성격이 다른 method끼리 묶을 때 gain이 커진다.

## 5. SLM-Math 관점의 재해석

- 이 논문은 route-card / strategy-card reranker의 가장 단순한 원형에 가깝다.
- 공통점:
  - heterogeneous reasoning methods를 결합한다.
  - problem-level selection이 중요하다는 점을 보여 준다.
  - homogeneous SC보다 heterogeneous selection이 더 cost-efficient할 수 있음을 보인다.
- 차이점:
  - 이 논문은 `CoT`와 `PAL` 두 해법을 먼저 모두 생성한 뒤, final answer를 post-hoc으로 선택한다.
  - 내 연구는 warm-start 이후 current reasoning state, answer histogram, disagreement, route history, remaining budget을 보고 다음 path family를 더 acquisition할지 또는 stop할지를 결정해야 한다.
- 안전한 한 문장 차별화:
  - Zhao et al.은 이미 생성된 CoT/PAL 해법 중 무엇을 선택할지 다루고, 내 연구는 **어떤 path family를 다음에 더 생성할지와 언제 멈출지를 다룬다.**

## 6. 우리 연구에 대한 novelty risk

- `reasoning method selection` 자체는 이미 존재한다.
- heterogeneous method selection이 homogeneous self-consistency보다 비용 효율적일 수 있다는 claim도 이미 있다.
- path diversity의 질이 중요하다는 주장도 이미 있다.
- selector prompt / candidate order bias가 결과에 영향을 준다는 점도 이미 확인되었다.
- 따라서 위험한 claim:
  - `문제별로 CoT/CG/PoT 중 하나를 선택하는 것이 새롭다`
  - `heterogeneous reasoning path를 섞는 것이 SC보다 효율적이다`
  - `LLM이 더 나은 reasoning path를 고르게 하는 것이 novelty다`
  - `CoT 변형 몇 개를 섞으면 충분히 heterogeneous하다`
- 안전한 방향:
  - `one-shot post-hoc selection`이 아니라
  - **state-conditioned path acquisition / macro strategy allocation / STOP decision**

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - different reasoning methods have different strengths and weaknesses
  - choosing the better reasoning method is itself a selection problem
  - heterogeneous method combination can beat homogeneous sampling
- baseline:
  - CoT
  - PAL / PoT
  - CoT-SC
  - PAL-SC
  - CoT + PAL selector
  - similar-method selector
  - option-order randomized selector
- metric:
  - Accuracy
  - Average budget
  - Total tokens
  - Cost-normalized accuracy
  - `Delta UpperBound`
  - `Success Rate`
  - Improvement over best single route
- ablation:
  - heterogeneous pair vs similar pair
  - with explanation vs without explanation
  - selector model size
  - same backbone vs different backbone
  - option order randomization
  - selection only on disagreement vs always select
- figure/table idea:
  - route pair별 `Delta UpperBound`
  - pairwise disagreement / complementary correct count
  - one-shot selector vs state-conditioned router comparison

## 8. 우리가 하면 안 되는 주장

- `reasoning method selection은 거의 다뤄지지 않았다`고 쓰면 안 된다.
- `heterogeneous path를 섞는 것이 self-consistency와 결합될 수 있다는 점이 새롭다`고 쓰면 안 된다.
- `LLM으로 더 나은 reasoning path를 고르게 하는 것이 novelty다`라고 쓰면 안 된다.
- `CoT 변형 여러 개를 섞으면 충분한 diversity가 생긴다`고 가정하면 안 된다.
- `selector prompt를 잘 쓰면 robust하게 선택할 수 있다`고 쉽게 쓰면 안 된다.
- `CG route는 CoT route와 다르므로 자동으로 유용하다`고 쓰면 안 된다.

## 9. baseline / ablation 반영 아이디어

- `CoT + PAL / PoT selector` baseline을 넣는다.
- route pair별 `Delta UpperBound`, `Success Rate`, complementary correct count를 계산한다.
- `prompt-diverse CoT`와 truly heterogeneous family를 구분하는 ablation을 한다.
- candidate order randomization을 넣는다.
- selector accuracy와 final accuracy를 분리해서 보고한다.
- one-shot selector와 state-conditioned sequential router를 같은 budget에서 비교한다.
- selection after full generation과 acquisition before generation을 method section에서 분리한다.

## 10. Related Work에 넣을 문장 초안

`Automatic Model Selection with Large Language Models for Reasoning`은 `CoT`와 `PAL`이 서로 다른 강점과 약점을 가진 reasoning method라는 점에 주목하고, 동일한 문제에 대해 두 해법을 모두 생성한 뒤 LLM selector가 더 적절한 해법을 선택하는 방식으로 reasoning 성능을 개선하였다. 이 연구는 model selection이 self-consistency와 complementary하며, heterogeneous reasoning methods를 결합할 경우 homogeneous self-consistency보다 낮은 비용으로 더 높은 성능을 얻을 수 있음을 보였다. 또한 `CoT`와 `CoT` 변형처럼 유사한 method 조합은 이득이 제한적이라는 분석을 통해, method 간 상보성과 problem-dependent performance gap이 중요함을 제시하였다.

그러나 이 연구는 주어진 문제에 대해 `CoT`와 `PAL` 해법을 먼저 모두 생성한 뒤 final answer를 선택하는 **post-hoc model selection**에 가깝다. 반면 본 연구는 제한된 test-time compute budget 아래에서 현재까지 관찰된 reasoning state, answer distribution, route history, disagreement, remaining budget을 바탕으로 어떤 reasoning path family 또는 macro sampling strategy를 추가로 선택할지, 그리고 언제 중단할지를 결정하는 **state-conditioned path acquisition and stopping** 문제를 다룬다. 따라서 본 연구는 기존 model selection 연구를 확장하여, self-consistency 후보 풀을 동적으로 구성하고 path-family / strategy-level compute allocation을 수행하는 lightweight orchestration framework로 위치한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 높음
- 지금 당장 해야 할 일:
  - `CoT + PAL / PoT selector`를 baseline으로 포함
  - route pair별 `Delta UpperBound`, `Success Rate`, complementary correct count 도입
  - `CoT_Lv1/2/3/CG`가 실제로 heterogeneous한지 검증
  - candidate order randomization을 reranker 평가에 추가
  - one-shot selector와 state-conditioned router를 구분해서 서술
- 나중으로 미뤄도 되는 일:
  - GPT-4 기반 full reproduction
  - symbolic benchmark 확장
  - Codex 기반 PAL 재현
- 한 문장 결론:
  - 이 논문 이후 내 연구는 `strategy selection을 한다`가 아니라, **one-shot post-hoc model selection을 state-conditioned path acquisition, macro strategy allocation, STOP decision으로 확장한다**고 써야 한다.
