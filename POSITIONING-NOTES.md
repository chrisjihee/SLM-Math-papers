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

### Chain-of-Thought Prompting (origin baseline / claim boundary)

- risk:
  CoT는 직접적 위협이라기보다, 중간 추론 단계(rationale) 유도라는 가장 기본 형태를 이미 확립한 origin이다. 따라서 `CG > CoT`나 `prompt에 reasoning을 넣으면 좋아진다`, `CoT prompting을 개선한다`를 새 발견·핵심 기여처럼 쓰면 바로 충돌한다.
- response:
  CoT를 모든 path-family 비교의 origin baseline(few-shot CoT greedy)으로 고정하고, CG는 CoT의 replacement가 아니라 auxiliary / structured family 중 하나로 둔다. 우리 기여는 CoT 개선이 아니라 CoT를 포함한 heterogeneous path family의 state-conditioned acquisition과 STOP이다. 특히 prompt-diversity 효과(여러 CoT 변형)와 structural rationale(CG) 효과를 분리하는 ablation을 두어 "다양성 이득"을 "구조 이득"으로 오인하지 않게 한다.

- wording caution:
  `CoT prompting을 개선한다`, `중간 추론 단계 유도가 새롭다`, `CG가 CoT보다 우월하다`, `prompt에 reasoning을 넣으면 좋아진다`만으로 기여를 쓰면 안 된다. raw GSM8K/MATH SOTA 경쟁 프레임도 피한다.

### Self-Consistency (canonical multi-sample baseline / substrate)

- risk:
  Self-Consistency는 CoT 이후 가장 기본적인 multi-sample / majority-vote baseline으로, `여러 reasoning path를 샘플링해서 답을 고른다`, `majority voting`, `homogeneous multi-sample reasoning`, `sample scaling`을 이미 선점했다. RASC/CISC/adaptive-TTC 계열은 모두 이 SC substrate 위의 stopping·weighting·confidence 확장이라, SC 영역에서 새로움을 주장하면 이 강한 인접 선행들과 정면충돌한다.
- response:
  SC는 우리가 반드시 넘어야 할 fixed homogeneous SC baseline(fixed SC@K)으로 고정하고, 우리 기여는 homogeneous same-prompt sampling이 아니라 heterogeneous path family를 state-conditioned하게 구성하고 언제 STOP할지 결정하는 upstream path-pool 구성으로 둔다. RASC/CISC는 aggregation/stopping 개선으로, 우리는 그보다 앞선 어떤 후보 family를 만들지로 분리한다.

- wording caution:
  `self-consistency를 도입한다 / 처음 쓴다`, `majority voting으로 답을 고른다`, `여러 path를 샘플링하면 좋아진다`, `sample 수를 늘리면 좋아진다`만으로 기여를 쓰면 안 된다. `fixed homogeneous SC`와 `heterogeneous path-family allocation + STOP`을 명확히 분리하고, SC를 폄하하는 wording도 피한다(필수 baseline).

### Tree of Thoughts / search-based deliberate reasoning

- risk:
  ToT는 thought를 노드로 한 트리에서 self-evaluation(value/vote)과 BFS/DFS(+backtracking/lookahead) explicit search로 deliberate problem solving을 수행해, `reasoning search`, `tree search`, `lookahead/backtracking`, `state self-evaluation`, `deliberate problem solving`, `multi-path exploration`을 이미 선점했다. GoT, MCTS류(rStar-Math)와 함께 search-heavy cluster를 이룬다.
- response:
  우리는 thought-level explicit tree search가 아니라, 제한된 TTC 안에서 heterogeneous path family를 어떤 순서·budget으로 획득하고 언제 STOP할지 결정하는 lightweight orchestration(route-family / strategy-card / macro action routing)으로 간다. ToT의 state-evaluation은 우리 route/family-level estimator의 개념적 조상으로만 차용하되 node-level이 아니라 route-level로, 그리고 search/evaluation cost를 TTC budget에 명시 계상한다. ToT는 full reproduction 대상이 아니라 search-heavy contrastive boundary reference로 둔다.

- wording caution:
  `reasoning search`, `tree/graph search`, `BFS/DFS`, `lookahead`, `backtracking`, `self-evaluation`, `deliberate problem solving`을 우리 novelty로 쓰면 ToT/GoT와 정면충돌한다. CG를 ToT/GoT식 tree/graph search처럼 과장하지 말고, 우리를 "search over a reasoning tree"로 서술하지 말 것. ToT 대비 raw SOTA 경쟁 프레임도 피한다.

### Graph of Thoughts / graph-structured reasoning (CG naming boundary)

- risk:
  GoT는 LLM reasoning을 thought=vertex, dependency=edge의 arbitrary directed graph로 모델링하고 generate/aggregate(merge)/refine transformation으로 실행해, `graph-structured reasoning`, `arbitrary thought graph`, `aggregation/merging`, `refinement loop`, `transformation-based reasoning`을 이미 선점했다. 특히 우리 `CG(Concept Graph)` 이름 때문에 reviewer가 GoT를 가장 먼저 연상할 수 있어, graph 관련 claim의 혼동 위험이 가장 크다.
- response:
  우리는 thought graph 내부 변환·실행이 아니라, 제한된 TTC 안에서 heterogeneous path family를 어떤 순서·budget으로 획득하고 언제 STOP할지 결정하는 lightweight orchestration(route-family / strategy-card / macro action routing)으로 간다. GoT는 full reproduction 대상이 아니라 graph-structured / search-heavy contrastive boundary reference로 두고, graph operation cost(generation+aggregation+refinement+scoring)를 TTC budget에 계상한다. GoT 실험 모델은 GPT-3.5로 정확히 기록한다(ToT의 GPT-4와 구분).

- 명문화(필수):
  - `CG is a linearized structured rationale, not GoT-style graph-of-thought search/traversal.`
  - `We should not claim novelty on graph-structured reasoning, arbitrary thought graphs, aggregation/merging, or refinement loops.`

- wording caution:
  `graph reasoning`, `thought graph`, `arbitrary reasoning graph`, `aggregation/merging`, `refinement loop`, `transformation-based reasoning`을 우리 novelty로 쓰면 GoT/ToT와 정면충돌한다. 우리를 "graph search over thoughts"로 서술하지 말고, CG를 GoT식 graph search처럼 과장하지 말 것. GoT 대비 raw SOTA 경쟁 프레임도 피한다.

### Self-Refine / reflection / self-feedback

- risk:
  Self-Refine는 추가 학습 없이 단일 LLM이 generate→self-feedback→refine을 반복하는 iterative self-refinement를 제시해, `reflection`, `self-feedback`, `iterative refinement`를 이미 선점했다.
- response:
  우리는 reflection loop 자체를 기여로 두지 않고, 이를 macro strategy 후보(`self_refine_k`) 중 하나로만 포함한다. 핵심은 제한된 TTC 안에서 heterogeneous path family를 어떻게 획득하고 언제 STOP하며 어떤 voting/verification으로 최종 답을 정할지다. reflection cost(generation+feedback+refine)를 TTC budget에 계상하고, parallel sampling과 budget-matched로 공정 비교한다.

- wording caution:
  `iterative self-refinement / reflection을 우리가 처음 제안한다`, `self-feedback 기반 개선이 우리 기여다`로 쓰면 안 된다. 특히 Self-Refine의 수학(GSM8K) 약세를 근거로 `reflection은 효과 없다`를 일반화하지 말 것(과제·모델·budget 의존).

### rStar-Math

- risk:
  full MCTS + PPM + self-evolution이 현재 우리 line보다 훨씬 강한 math frontier고, `SLM + TTC로 math reasoning을 밀어올린다`는 넓은 claim은 이미 사실상 선점되어 있다.
- response:
  우리는 raw frontier performance 경쟁이 아니라, 제한된 TTC 안에서 heterogeneous reasoning path family를 어떻게 선택·검증·중단할지 다루는 lightweight orchestration으로 가야 한다.

- wording caution:
  `SLM math reasoning with test-time compute`, `search-based reasoning`, `verifier-guided selection`, `small models can do deep thinking`만으로 contribution을 쓰면 rStar-Math와 정면충돌한다. `step-level MCTS/PPM`이 아니라 `path-family / macro-strategy allocation under limited budget`을 더 앞에 둬야 한다.

### DeepSeekMath

- risk:
  strong 7B math backbone, CoT/PoT/tool-integrated training, GRPO, SC@64, `Pass@K / Maj@K` 분석까지 이미 제시되어 있어 `small model math improvement`나 `SC gain` 자체를 novelty로 쓰기 어렵다.
- response:
  우리는 더 강한 math-specialized model을 학습하는 대신, 주어진 backbone 위에서 heterogeneous reasoning path pool을 제한된 TTC 안에서 어떻게 구성하고 멈출지에 집중해야 한다.

- wording caution:
  `sLLM math reasoning improvement`, `self-consistency helps`, `tool-integrated reasoning is useful`만으로 기여를 쓰면 DeepSeekMath와 지나치게 겹친다. `fixed homogeneous SC`와 구분되는 `state-conditioned path-pool construction and stopping`을 더 앞에 둬야 한다.

### DeepSeek-R1

- risk:
  human reasoning label 없이 pure RL(GRPO)만으로 long CoT·self-verification·dynamic strategy adaptation이 창발함을 보이고, 이를 1.5B~70B 소형 모델로 distill까지 했기 때문에 `SLM + 강한 reasoning`, `long CoT`, `self-verification`, `RL로 reasoning capability 유도`, `distilled small reasoner` 같은 claim은 이미 강하게 선점되어 있다.
- response:
  우리는 RL/distillation으로 reasoner 자체를 학습하는 training-time 경쟁이 아니라, 그렇게 얻은 fixed/given backbone 위에서 제한된 TTC 안의 heterogeneous reasoning path pool을 state-conditioned하게 구성·선택·중단하는 lightweight inference-time orchestration으로 가야 한다. R1-distilled 모델은 경쟁 대상이 아니라 strong backbone / contrastive frontier로 둔다.

- wording caution:
  `RL incentivizes reasoning`, `long chain-of-thought`, `self-verification / reflection`, `small distilled reasoner`, `small models can reason with test-time compute`만으로 contribution을 쓰면 DeepSeek-R1과 정면충돌한다. 이 행동들은 R1이 emergent behavior로 이미 보고했으므로, 우리는 `state-conditioned path-family / macro-strategy acquisition and stopping`을 더 앞에 두고 raw math SOTA 경쟁 프레임을 피해야 한다.

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

### ToRA / tool-interleaved paths

- risk:
  ToRA는 자연어 reasoning과 program 실행·tool 호출을 한 trajectory 안에서 interleave하는 tool-integrated agent를 imitation learning과 output space shaping으로 7B~70B에 학습해, `tool-use reasoning`, `reasoning↔execution interleaving`, `작은 모델이 도구로 MATH를 푼다`를 PAL/PoT보다 강하게 선점했다.
- response:
  우리는 ToRA-like tool-interleaved path를 새로 제안하는 것이 아니라, 그것을 heterogeneous path pool의 강한 한 family로 수용하고, `CoT / CG / direct / PAL / PoT / ToRA-like / verifier-guided` 중 무엇을 현재 reasoning state와 남은 budget에서 더 호출하고 언제 STOP할지 결정하는 state-conditioned orchestration으로 가야 한다. 특히 tool-interleaved path는 generation cost뿐 아니라 tool execution cost가 들므로, 이를 TTC budget에 명시적으로 포함해야 한다.

- wording caution:
  `tool-integrated reasoning`, `reasoning-execution interleaving`, `program execution으로 math를 푼다`만으로 기여를 쓰면 ToRA와 바로 겹친다. `ToRA-like path는 강한 path family`이고, 우리 기여는 `state-conditioned path acquisition / stopping과 tool-cost-aware budget allocation`이라는 점을 분리해서 써야 하며, ToRA 대비 raw MATH/GSM8K SOTA 경쟁 프레임은 피해야 한다.

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
