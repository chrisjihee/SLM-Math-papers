# POSITIONING NOTES

## 1. 한 문장 thesis candidate

소형 언어모델의 수학 추론에서 핵심은 특정 rationale 포맷의 우월성보다, **heterogeneous reasoning path pool을 제한된 테스트타임 계산량 안에서 어떻게 선택·검증·중단하느냐**에 있다.

## 2. 메인 contribution 후보

- problem-conditioned test-time compute allocation
- heterogeneous reasoning path family selection
- route-card / strategy-card 기반 lightweight reranking
- answer selection / verification을 포함한 budget-aware inference orchestration

## 3. 우리의 contribution이 아닌 것

- 새로운 대규모 math pretraining corpus
- rStar-Math 급 MCTS self-evolution 재현
- PRM 자체의 SOTA 학습법
- graph reasoning 자체의 근본적 돌파
- telecom foundation model 전체를 새로 만드는 것

## 4. 현재 safe claim

- `CG`는 여러 reasoning path family 중 하나다.
- 현재 strongest student result는 multiple-CoT 축에 있다.
- 다음 병목은 route generation보다 route/budget selection과 answer/path verification이다.
- adaptive TTC는 여전히 중요하지만, novelty는 단순 budget allocation보다 path-family / strategy-level allocation 쪽에 있어야 한다.
- query-only difficulty prediction보다 current reasoning state를 읽는 policy가 필요하다는 점을 전면에 세우는 것은 안전하다.

## 5. 현재 forbidden claim

- "CG가 CoT보다 우수하다"
- "graph reasoning superiority"
- "sequential routing is solved"
- "reflection is ineffective in general"
- "NFM에서 곧바로 SOTA를 낼 수 있다"
- "이 연구의 main novelty는 CG 자체다"

## 제출 전략상 가장 위험한 선행연구

### rStar-Math

- risk:
  full MCTS + PPM + self-evolution이 현재 우리 line보다 훨씬 강한 math frontier다.
- response:
  우리는 raw frontier performance 경쟁이 아니라, 제한된 TTC 안에서 lightweight path/strategy selection을 다룬다.

### Learning How Hard to Think

- risk:
  adaptive TTC 자체는 새롭지 않고, query-level difficulty prediction 기반 compute allocation도 이미 수행되었다.
- response:
  우리의 contribution은 단순 budget allocation이 아니라 path-family / strategy-level allocation이어야 하며, query-only predictor가 아니라 current reasoning pool을 보는 state-conditioned policy여야 한다.

- wording caution:
  `adaptive test-time compute allocation for mathematical reasoning`만 전면에 두면 정면충돌 위험이 크다. `state-conditioned allocation over heterogeneous reasoning path families`처럼 더 좁고 구체적으로 써야 한다.

### Scaling LLM Test-Time Compute Optimally

- risk:
  difficulty-conditioned compute-optimal scaling, sequential vs parallel trade-off, verifier / PRM search, revision strategy selection까지 이미 강하게 정리되어 있다.
- response:
  우리는 difficulty-only strategy selection이 아니라 current reasoning state를 보고 heterogeneous path family 또는 macro strategy를 다음에 무엇으로 확장할지, 그리고 언제 stop할지를 다뤄야 한다.

- wording caution:
  `problem-dependent TTC strategy selection`, `compute-optimal inference`, `best-of-N보다 효율적인 adaptive allocation`만으로 contribution을 쓰면 이 논문과 지나치게 겹친다. `state-conditioned reasoning path pool construction`과 `path-family / strategy-level acquisition`을 더 앞에 둬야 한다.

### Reasoning-Aware Self-Consistency / Confidence Improves Self-Consistency

- risk:
  SC efficiency, early stopping, confidence-weighted voting은 이미 연구되어 있고, RASC는 reasoning-level quality feature까지 사용해 sample-level stopping과 rationale selection을 수행한다.
- response:
  우리는 homogeneous SC가 아니라 heterogeneous path pool construction과 state-conditioned strategy selection을 강조해야 하며, sample-level stopping이 아니라 path-family / macro-strategy acquisition 문제를 전면에 세워야 한다.

- wording caution:
  `efficient self-consistency`, `reasoning-aware stopping`, `weighted voting`, `rationale quality scoring`, `confidence-based aggregation`만 전면에 두면 RASC/CISC와 지나치게 겹친다.

### Self-Discover / Automatic Model Selection

- risk:
  reasoning strategy selection 자체도 새롭지 않고, Self-Discover는 task-level reasoning-structure composition을, Automatic Model Selection은 `CoT`와 `PAL` 사이의 one-shot post-hoc method selection을 이미 강하게 제시했다.
- response:
  우리는 dynamic budgeted path acquisition, stopping, verifier/reranker를 결합한 방향으로 차별화해야 하며, one-shot structure composition이 아니라 current reasoning state를 읽는 sequential decision problem이라는 점을 전면에 세워야 한다.

- wording caution:
  `self-compose reasoning structure`, `structured prompting over CoT`, `strategy composition`, `method selection`만으로 기여를 쓰면 Self-Discover / Automatic Model Selection과 지나치게 겹친다. `state-conditioned acquisition before full generation`을 더 앞에 둬야 한다.

### PAL / Tool-use paths

- risk:
  program-aided reasoning, Python interpreter execution, CoT의 arithmetic/state-tracking failure 보완, `SC-PAL`류 tool-use path 강화는 이미 PAL/PoT 계열이 대표적으로 제시했다.
- response:
  우리는 PAL 자체를 새로 제안하는 것이 아니라, `CoT`, `CG`, `direct`, `PAL/PoT`, verifier-guided path 중 어떤 family를 현재 reasoning state와 남은 budget에서 더 호출할지 결정하는 orchestration 문제로 가야 한다.

- wording caution:
  `tool-use reasoning`, `natural language + symbolic execution`, `structured path가 CoT보다 낫다`만으로 기여를 쓰면 PAL과 바로 겹친다. `tool-executed path는 강한 baseline family`이고, 우리의 기여는 `state-conditioned path acquisition / stopping`이라는 점을 분리해서 써야 한다.

### PoT / executable paths

- risk:
  executable program path, computation offloading, `SC-PoT`, arithmetic/state-tracking utility는 이미 PoT가 canonical하게 보여줬다.
- response:
  우리는 PoT를 강한 executable path family로 수용하고, 그 위에서 CoT / PAL / CG / direct와의 budget-aware allocation을 다뤄야 한다.

- wording caution:
  `program-based reasoning`, `computation offloading`, `PoT가 CoT보다 낫다`만 전면에 두면 PoT와 지나치게 겹친다. `PoT는 path family`, `우리 기여는 state-conditioned path-family allocation`으로 분리해야 한다.

### s1

- risk:
  single-path sequential test-time scaling, thinking-length control, sequential vs parallel scaling 비교는 이미 강하게 제시되었다.
- response:
  우리는 얼마나 오래 같은 path를 생각하게 할지보다, 현재 reasoning state를 보고 어떤 path family를 더 샘플링할지와 언제 stop/diversify할지를 다뤄야 한다.

- wording caution:
  `test-time scaling`, `simple inference-time reasoning improvement`, `longer thinking helps`만 전면에 두면 s1과 지나치게 겹친다.

### Verifier / PRM papers

- risk:
  answer/path selection은 verifier/PRM literature에서 강하게 다뤄졌고, `Let's Verify Step by Step`은 process-supervised PRM이 majority voting 및 outcome-style verifier보다 강할 수 있음을 canonical하게 보여준다.
- response:
  우리의 route/strategy reranker는 step-level PRM과 다르게 path acquisition 전/중간의 lightweight policy/value estimator로 위치시킨다.

- wording caution:
  `verifier로 후보를 고른다`, `reward model reranking을 도입한다`, `candidate selection을 개선한다`만으로 contribution을 쓰면 PRM literature와 지나치게 겹친다. `fixed pool after generation`과 `state-conditioned pool construction before verification`을 분리해서 써야 한다.

### Math-Shepherd

- risk:
  automatic process supervision, step-level PRM, best-of-N verification, step-level PPO까지 이미 강한 verifier baseline이 있다.
- response:
  우리는 PRM을 새 contribution으로 주장하지 말고, PRM이 평가할 candidate pool을 어떻게 state-conditionally 만들지에 집중해야 한다.

- wording caution:
  `best-of-N verification`, `process supervision`, `automatic process annotation`만으로 기여를 쓰면 Math-Shepherd와 너무 겹친다. `candidate pool construction before verification`을 전면에 둬야 한다.

### Process Reward Models That Think

- risk:
  generative PRM, long verification CoT, compute-matched verifier scaling, best-of-N verifier selection까지 이미 강한 최신 reference가 있다.
- response:
  우리는 verifier를 새로 제안하지 말고, generation budget과 verification budget을 어떻게 나눌지, 그리고 verifier가 평가할 pool을 어떻게 만들지에 집중해야 한다.

- wording caution:
  `generative verifier`, `verifier compute scaling`, `best-of-N verification`만으로 기여를 쓰면 ThinkPRM과 너무 겹친다. `state-conditioned path acquisition before verification`을 전면에 둬야 한다.

## 정보과학회 S/A 우수학술대회 기준 제출 전략

- 현재 연구의 1차 target은 `ACL / EMNLP / NAACL / AAAI`다.
- `ICLR / ICML / NeurIPS`는 stretch target이다.
- `ACL Findings / EMNLP Findings / NAACL Findings / COLING / EACL / IJCAI`는 realistic fallback이다.
- `SIGIR / KDD / WSDM / CIKM / WWW`는 ranking, retrieval, evidence-grounding이 중심이 될 때만 고려한다.
- NFM bridge는 처음부터 `SIGCOMM / NSDI / INFOCOM`을 노리지 말고, `TeleMath` 중심의 domain reasoning application을 NLP/AI venue에 붙이는 것이 우선이다.
- network venue는 실제 network-system contribution이 생겼을 때만 고려한다.

## 8. graph / structured reasoning papers와의 포지셔닝

- 공통점:
  structured intermediate representation에 관심이 있다.

- 차이점:
  현재 우리 `CG`는 graph-preserving traversal보다 **linearized structured rationale**에 가깝다.

- 안전한 문장:
  "CG-style rationale은 structured path family 중 하나로 평가된다."

- 금지 문장:
  "우리는 graph reasoning을 했다."

## 9. NFM를 어떻게 붙일 것인가

- NFM는 메인 thesis topic이 아니라 application/bridge다.
- 가장 좋은 immediate bridge는 `TeleMath`다.
- `TeleTables`, `TeleLogs`는 second-phase candidate다.
- `TeleQnA`는 retrieval/knowledge anchor로는 유용하지만 thesis core novelty로는 약하다.

## 10. paper title 방향

- State-Conditioned Test-Time Compute Allocation for Small Language Model Reasoning
- Budget-Aware Reasoning Path Pool Construction for Small Language Models
- Heterogeneous Reasoning Path Selection for Efficient Self-Consistency
- Macro-Action Routing for Budget-Efficient Mathematical Reasoning
- Strategy-Card Reranking for Small Language Model Reasoning
- Domain-Aware Reasoning Strategy Selection for Telecom Mathematical Reasoning

## 11. blunt recommendation

첫 논문은 **math reasoning mainline**으로 가야 한다.

- 주제:
  path pool + TTC allocation + reranking/verification
- 벤치마크:
  `GSM8K-kor`, `GSM8K`, 가능하면 `MATH500`
- CG:
  auxiliary structured family
- NFM:
  후속 bridge paper
