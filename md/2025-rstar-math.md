# rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking review

## 1. Metadata

- Title: rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking
- Authors: Xinyu Guan, Li Lyna Zhang, Yifei Liu, Ning Shang, Youran Sun, Yi Zhu, Fan Yang, Mao Yang
- Year: 2025
- Venue / Status: ICML 2025, Proceedings of the 42nd International Conference on Machine Learning
- Links:
  - Paper: https://proceedings.mlr.press/v267/guan25f.html
  - Code / Data: https://github.com/microsoft/rStar
- Paper Type:
  - `training-heavy`
  - `inference-time`
  - `verifier`
  - `search`
  - `tool-use`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

rStar-Math는 1.5B~7B SLM을 policy model로 두고 code-augmented CoT, Python execution, MCTS, SLM 기반 Process Preference Model(PPM), 4-round self-evolution을 결합해 작은 모델도 frontier급 수학 추론 성능에 접근할 수 있음을 보인 강한 System 2 math reasoning 논문이다.

## 3. 핵심 문제 설정

- 이 논문이 푸는 질문은 **frontier teacher distillation 없이도 small language model이 강한 수학 추론 능력을 가질 수 있는가**이다.
- 기존 한계로 보는 것은 다음과 같다.
  - System 1 single-pass inference는 빠르지만 오류가 많다.
  - strong teacher CoT distillation은 teacher quality에 묶이고, intermediate step 오류를 직접 줄이지 못한다.
  - PRM은 유망하지만 step-level annotation이 비싸고 Q-value regression은 noisy하다.
- 내 연구와의 연결은 매우 직접적이다.
  - 이 논문도 `test-time compute`를 전면에 둔다.
  - 여러 reasoning step과 trajectory를 생성하고 reward/verifier 기반으로 좋은 해를 선택한다.
- 하지만 차이도 명확하다.
  - rStar-Math는 **step-level MCTS search + PPM-guided verification + self-evolved training**이 중심이다.
  - 내 연구는 **CoT / CG / prompt-diverse CoT / PoT / direct / verifier-guided route** 중 무엇을 어느 시점에 더 추가할지 고르는 **path-family / strategy-level TTC allocation**이 중심이다.

## 4. 핵심 방법

- reasoning path:
  - 일반 CoT가 아니라 **code-augmented CoT trajectory**다.
  - 각 step은 자연어 설명과 Python code를 함께 생성하고, code가 실행 가능한 step만 유효 node로 남긴다.
- sampling:
  - 단순 repeated sampling이 아니라 **MCTS**로 step 후보를 탐색한다.
  - policy SLM이 candidate node를 만들고, Python execution과 PPM score로 filtering 및 selection을 수행한다.
- self-consistency:
  - 전통적인 independent-sample majority voting이 아니라, verifier/reward-guided solution selection에 가깝다.
- test-time compute:
  - trajectory 수를 명시적으로 늘리며 scaling을 본다.
  - 기본은 benchmark별로 8/16 trajectories, 확장 설정은 `rStar-Math64`
- verifier / reward model:
  - 핵심은 **PPM(Process Preference Model)**이다.
  - Q-value를 직접 회귀하지 않고, MCTS에서 얻은 signal로 positive/negative step preference pair를 구성해 pairwise ranking으로 학습한다.
- search / MCTS / reflection:
  - 핵심 search는 MCTS다.
  - 명시적 reflection prompt는 없지만, search 과정에서 backtracking/self-correction-like behavior가 나타난다.
- training data / self-evolution:
  - 747k math word problems와 4 rounds self-evolution을 사용한다.
  - bootstrap round에서는 DeepSeek-Coder-V2-Instruct 236B도 활용한다.

## 5. SLM-Math 관점의 재해석

- rStar-Math는 내 연구의 **상위 위협 논문**이다.
- 공통점:
  - SLM math reasoning을 다룬다.
  - test-time compute와 verifier/search의 중요성을 인정한다.
  - code/Python execution을 적극적으로 활용한다.
- 차이점:
  - rStar-Math의 selection unit은 **step / trajectory**다.
  - 내 연구가 잡아야 할 selection unit은 **route / path family / macro strategy / STOP**이다.
  - rStar-Math는 heavy MCTS + self-evolution이고, 내 연구는 existing SLM과 route bank를 전제로 한 **lightweight orchestration**이어야 한다.
- 안전한 한 문장 차별화:
  - rStar-Math는 code-augmented reasoning paradigm 내부에서 step-level search를 강화하고, 내 연구는 **heterogeneous reasoning path family pool을 제한된 예산 안에서 state-conditionally 구성하는 문제**를 다룬다.

## 6. 우리 연구에 대한 novelty risk

- `SLM math reasoning + TTC scaling` 자체는 이미 새롭지 않다.
- `MCTS 기반 reasoning search`도 이미 강한 선행축이다.
- `verifier / reward model 기반 candidate selection`도 새롭지 않다.
- `Python/code-augmented reasoning`은 강한 baseline 축이다.
- raw math SOTA 경쟁은 매우 위험하다.
- `CG vs CoT`처럼 rationale format 중심 프레임은 rStar-Math 앞에서 약해 보일 수 있다.
- reflection에 대한 단정도 위험하다.
  - search + verifier 구조 안에서 self-correction-like behavior가 나타날 수 있기 때문이다.

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - System 1 vs System 2 reasoning
  - policy model + reward model + search
  - TTC scaling의 marginal utility는 benchmark/problem마다 다르다
- baseline:
  - Best-of-N
  - ORM Best-of-N
  - PRM/PPM-guided search
  - code-augmented CoT / PoT / PAL route
  - MCTS-style search upper/reference baseline
- metric:
  - pass@1
  - pass@N
  - cost-normalized accuracy
  - trajectory count vs accuracy curve
  - verifier / reranker ablation accuracy
- ablation:
  - trajectory 수 1/2/4/8/16/32/64
  - route family ablation: CoT only / CG only / PoT-code only / mixed
  - voting vs verifier/reranker selection
  - hard label vs pairwise / soft utility target
- figure/table idea:
  - budget-scaling curve
  - voting/ORM/PRM/reranker 비교표
  - pool construction -> scoring -> selection -> stop 도식화

## 8. 우리가 하면 안 되는 주장

- `SLM 수학 추론에서 test-time compute allocation을 처음 제안한다`고 쓰면 안 된다.
- `작은 모델도 TTC를 쓰면 강해질 수 있음을 처음 보인다`고 쓰면 안 된다.
- `MCTS 또는 search-based reasoning을 처음 적용한다`고 쓰면 안 된다.
- `verifier / reward model candidate selection`이 새롭다고 쓰면 안 된다.
- `process-level verification 없이도 route selection만으로 충분하다`고 단정하면 안 된다.
- `CG가 CoT/PoT/search보다 본질적으로 우월한 representation`이라고 쓰면 안 된다.
- `reflection은 효과가 없다`고 쓰면 안 된다.
- `sample 수를 늘리면 항상 성능이 오른다`고 쓰면 안 된다.

## 9. baseline / ablation 반영 아이디어

- `PoT / PAL / code-augmented CoT` route를 path family 후보에 포함한다.
- trajectory budget별 scaling curve를 `1, 2, 4, 8, 16, 32, 64` 형태로 다시 설계한다.
- majority voting vs answer-frequency vs confidence-weighted voting vs verifier/reranker selection을 비교한다.
- route selection supervision을 hard top-1 class보다 pairwise / soft utility ranking으로 설계한다.
- strategy-card에 cost, route composition, expected diversity, verifier compatibility를 추가한다.
- answer correctness와 trace correctness를 분리한 case study를 둔다.
- `heavy MCTS + PPM`은 direct reproduction target이 아니라 strong upper/reference baseline으로 둔다.

## 10. Related Work에 넣을 문장 초안

rStar-Math는 작은 언어모델의 수학 추론 능력을 System 2-style reasoning으로 크게 끌어올린 대표적인 연구다. 이들은 code-augmented CoT를 생성하는 policy SLM, Python execution 기반 step filtering, MCTS 기반 trajectory search, 그리고 step-level preference pair로 학습한 Process Preference Model(PPM)을 결합하여 1.5B~7B 규모의 SLM이 MATH, AIME, Olympiad Bench 등에서 frontier model에 근접하거나 일부 경우 능가할 수 있음을 보였다. 특히 이 연구는 단순 outcome-level Best-of-N보다 step-level reward signal과 search가 복잡한 수학 추론에서 더 효과적일 수 있음을 보여준다.

그러나 rStar-Math의 핵심 초점은 code-augmented reasoning paradigm 안에서 step-level MCTS search와 self-evolved policy/reward model을 학습하는 데 있다. 반면 본 연구는 heavy MCTS나 대규모 self-evolution을 재현하기보다, 제한된 test-time compute budget 안에서 CoT, prompt-diverse CoT, structured rationale, direct solving, PoT/PAL, verifier-guided path 등 heterogeneous reasoning path family를 어떻게 구성하고 선택하며 언제 멈출지를 다룬다. 따라서 본 연구는 rStar-Math와 경쟁적으로 raw math SOTA를 추구하기보다, rStar-Math류 heavy System 2 search와 상보적인 **state-conditioned path-pool construction and budget allocation** 문제에 위치한다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 높음
- 지금 당장 해야 할 일:
  - rStar-Math를 P0 related work의 최상위 축으로 고정
  - 논문 claim에서 `SLM + TTC로 math 성능 향상` 같은 일반 주장을 제거
  - `PoT / PAL / code-augmented CoT`를 baseline path family 후보로 포함
  - strategy-card supervision을 hard class label보다 pairwise / utility-aware ranking으로 재설계
  - budget curve와 saturation 분석을 프로토콜에 포함
- 나중으로 미뤄도 되는 일:
  - full MCTS / PPM / self-evolution reproduction
  - 747k급 data synthesis
  - Olympiad-level raw SOTA 경쟁
- 한 문장 결론:
  - rStar-Math는 우리가 따라가야 할 direct implementation target이 아니라, **heavy System 2 search와 구분되는 lightweight path-family allocation 논문으로 포지셔닝해야 한다는 사실을 가장 강하게 알려주는 논문**이다.
