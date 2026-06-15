# Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks review

## 1. Metadata

- Title: Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks
- Authors: Wenhu Chen, Xueguang Ma, Xinyi Wang, William W. Cohen
- Year: 2023
- Venue / Status: TMLR, 10/2023
- Links:
  - OpenReview: https://openreview.net/forum?id=YfZ4ZPt8zd
  - Paper / PDF: https://openreview.net/forum?id=YfZ4ZPt8zd
  - GitHub: https://github.com/wenhuchen/Program-of-Thoughts
- Code / Data:
  - existing metadata lists GitHub: `https://github.com/wenhuchen/Program-of-Thoughts`
  - Benchmarks: `GSM8K`, `AQuA`, `SVAMP`, `MultiArith`, `TabMWP`, `FinQA`, `ConvFinQA`, `TATQA`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

PoT는 LLM이 계산까지 직접 하게 두는 CoT의 한계를 지적하고, Python program을 생성한 뒤 계산은 interpreter에 맡기는 방식으로 numerical reasoning 성능을 크게 높인 tool-use prompting이다.

## 3. 핵심 문제 설정

- CoT는 reasoning과 computation을 한 path 안에서 같이 수행해야 해서 산술 실수, 복잡한 수식 처리, 반복 계산에서 자주 무너질 수 있다.
- PoT는 이를 `LLM은 reasoning과 program synthesis를 담당하고, computation은 외부 실행기에 맡긴다`로 분해한다.
- 특히 large-number arithmetic, equation-heavy task, state tracking이 필요한 문제에서 유리하다.
- 내 연구와의 연결은 매우 직접적이다.
  - PoT는 `CoT / CG / direct`와 다른 강한 path family다.
  - 따라서 내 후보 pool에는 반드시 `PoT / PAL / executable path`가 들어가야 한다.
- 다만 이 논문은 문제별로 `PoT를 쓸지 CoT를 쓸지`, 혹은 `언제 멈출지`를 학습하는 것이 아니라, 고정 prompting + fixed SC 비교에 가깝다.

## 4. 핵심 방법

- PoT의 reasoning path는 자연어 rationale이 아니라 **executable program**이다.
- program은 중간 계산을 담는 multi-step code이며, 의미 있는 variable binding을 통해 계산과 reasoning을 분리한다.
- 기본 설정은 few-shot prompting 후 Python 3.8 + SymPy execution이다.
- sampling은 greedy decoding과 self-consistency를 모두 사용한다.
  - SC는 temperature 0.4, `K=40`
- verifier나 reward model은 없다.
  - Python execution이 deterministic computation executor 역할을 한다.
- search / MCTS / reflection은 없다.
- routing은 제한적이다.
  - AQuA에서 PoT 결과를 보고 추가 CoT를 이어가는 형태가 있지만, 동적 path selection이 핵심은 아니다.

## 5. SLM-Math 관점의 재해석

- PoT는 `tool-executable reasoning path family`를 보여주는 canonical reference다.
- 공통점:
  - computation을 외부화해 arithmetic/symbolic error를 줄인다.
  - SC와 결합 가능한 path family다.
  - 일부 문제유형에서 CoT보다 marginal utility가 크다.
- 차이점:
  - PoT는 path family 자체를 제시하지만, 여러 family 사이의 budget-aware selection은 하지 않는다.
  - 내 연구는 `CoT`, `PoT/PAL`, `CG`, `direct`, `verifier-guided path` 중 무엇을 언제 더 뽑을지 결정해야 한다.
- 안전한 한 문장 차별화:
  - PoT는 executable path family를 열어주고, 내 연구는 **이 executable path를 포함한 heterogeneous pool에서 현재 state와 budget에 맞는 것을 고르는 문제**를 다룬다.

## 6. 우리 연구에 대한 novelty risk

- PoT / tool-use reasoning 자체는 이미 선점되어 있다.
- `CoT의 계산 오류를 줄이기 위해 외부 도구를 쓴다`는 claim도 새롭지 않다.
- `program-based reasoning`만으로 novelty를 주장하면 약하다.
- `PoT+SC`가 강하므로, SC baseline에서 PoT를 빼면 바로 지적받을 수 있다.
- 문제 유형별로 PoT가 유리한 영역을 이미 분석했으므로, 단순한 `problem-type analysis`는 새롭지 않다.
- SLM에서는 오히려 위험이 있다.
  - open-source 7B/16B code model의 PoT 성능이 낮아, SLM이 PoT를 안정적으로 생성한다는 주장은 실험 없이는 위험하다.

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - computation과 reasoning을 분리한다
  - reasoning path는 자연어만이 아니라 executable program도 포함한다
- baseline:
  - Direct
  - CoT
  - CoT + calc
  - PoT
  - PoT + SC
  - PoT as intermediate step + CoT
  - PAL
- metric:
  - exact match
  - option accuracy
  - budget-matched accuracy
  - accuracy vs number of samples
  - tool execution success rate
  - parse / runtime failure rate
- ablation:
  - PoT vs CoT
  - PoT vs CoT + calc
  - PoT vs direct equation generation
  - semantic binding on/off
  - greedy vs SC
  - backend model ablation
- figure/table idea:
  - problem category별 PoT utility breakdown
  - execution failure taxonomy
  - PoT vs CoT 사례 비교

## 8. 우리가 하면 안 되는 주장

- `PoT가 reasoning에 Python을 처음 도입했다`고 쓰면 안 된다.
- `CoT의 계산 오류를 외부 도구로 처음 해결했다`고 쓰면 안 된다.
- `PoT는 단순 CoT 변형이라 비교할 필요가 없다`고 쓰면 안 된다.
- `PoT는 항상 CoT보다 좋다`고 쓰면 안 된다.
- `SLM도 PoT를 안정적으로 생성할 수 있다`고 실험 없이 말하면 안 된다.
- `계산은 interpreter가 하므로 PoT는 verifier가 필요 없다`고 쓰면 안 된다.

## 9. baseline / ablation 반영 아이디어

- `PoT`를 action space에 공식 추가한다.
- `SC-PoT`를 budget-matched baseline으로 둔다.
- `Mixed CoT + PoT`와 `Mixed CoT + PAL + PoT`를 비교한다.
- PoT가 유리한 problem subset을 정의한다.
  - arithmetic-heavy
  - equation-heavy
  - symbolic
  - iterative
  - state-tracking
- `LLM simulating runtime` ablation을 넣는다.
- route-card에 PoT의 strengths, failure modes, cost를 적는다.
- budget-accuracy curve에서 CoT / PoT / Mixed를 함께 본다.

## 10. Related Work에 넣을 문장 초안

Program of Thoughts Prompting은 numerical reasoning에서 CoT가 reasoning과 computation을 함께 내부적으로 처리해야 한다는 한계를 지적하고, LLM이 Python program을 생성한 뒤 계산은 external interpreter에 위임하는 방식으로 성능을 높였다. 이 접근은 `GSM8K`, `AQuA`, `SVAMP`, `MultiArith`, `TabMWP`, `FinQA`, `ConvFinQA`, `TATQA`에서 CoT와 CoT+SC보다 강한 결과를 보였고, 특히 symbolic, iterative, equation-heavy 문제에서 executable reasoning path의 장점을 보여주었다. 그러나 PoT는 주로 하나의 executable path family를 고정적으로 사용하는 방식이며, 제한된 test-time budget 안에서 CoT, PoT, direct solving, structured rationale, verifier-guided path 중 무엇을 언제 더 샘플링할지 결정하는 문제는 다루지 않는다. 따라서 본 연구는 PoT를 heterogeneous reasoning pool의 핵심 구성요소로 포함하되, 현재 reasoning state와 남은 budget을 조건으로 path-family / strategy-level allocation을 수행하는 문제에 초점을 둔다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 높음
- 지금 당장 해야 할 일:
  - `PoT / PAL`을 path family 목록에 공식 추가
  - `SC-PoT`와 `Mixed CoT+PoT`를 budget-matched baseline으로 설계
  - tool execution cost를 TTC accounting에 포함
  - PoT route-card에 strengths, failure modes, cost를 작성
- 나중으로 미뤄도 되는 일:
  - FinQA / ConvFinQA / TATQA full 재현
  - more general tool ecosystem 확장
  - 더 복잡한 symbolic solver 확장
- 한 문장 결론:
  - PoT는 경쟁자가 아니라, **내 method가 반드시 선택·조합해야 하는 executable reasoning path family**다.
