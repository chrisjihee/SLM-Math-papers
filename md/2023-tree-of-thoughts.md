# Tree of Thoughts: Deliberate Problem Solving with Large Language Models review

## 1. Metadata

- Title: Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- Authors: Shunyu Yao(Princeton), Dian Yu(Google DeepMind), Jeffrey Zhao(Google DeepMind), Izhak Shafran(Google DeepMind), Thomas L. Griffiths(Princeton), Yuan Cao(Google DeepMind), Karthik Narasimhan(Princeton)
- Year: 2023
- Venue / Status: NeurIPS 2023 (arXiv 2305.10601, 2023-05 공개; PDF CreationDate 2023-12-05)
- Links:
  - Paper: https://arxiv.org/abs/2305.10601
  - GitHub / Code (official): https://github.com/princeton-nlp/tree-of-thought-llm
- Source PDF (local): `paper/2023-tree-of-thoughts.pdf`
  - grounding: pypdf/pymupdf 기준 14 pages, sha256 `79c5237e3f63953a73f2b0d6894327702ee1f7e981450c251bb1b5cb4f8d7b8f`
  - title/authors/abstract/method(BFS/DFS·value/vote·backtracking·state evaluation)/benchmarks/74% vs 4%/code URL을 PDF 본문에서 직접 확인
- Paper Type:
  - `inference-time` / `prompting`
  - `explicit tree search over thoughts` (deliberate reasoning, search-heavy)
  - `contrastive search-boundary reference`
- Reading Status: `strategically-read`
- Current Priority: `P1`

## 2. One-line Summary

ToT는 LLM의 단일 경로(token-level, left-to-right) 디코딩 한계를, 중간 단위인 "thought"를 노드로 하는 트리 위에서 thought 생성 + self-evaluation 상태평가(value/vote) + BFS/DFS(backtracking/lookahead) explicit search로 확장해, 탐색이 본질인 과제에서 큰 향상을 보인 deliberate problem-solving 논문이다.

## 3. 핵심 문제 설정

- 이 논문이 푸는 질문은 **단일 left-to-right 디코딩으로는 약한, exploration·strategic lookahead·초기 결정이 중요한 과제를 LLM이 어떻게 풀 수 있는가**이다.
- 기존 한계로 보는 것:
  - CoT/CoT-SC는 한 번 생성한 경로(또는 그 다중 샘플의 majority)에 의존해, 중간에서 탐색·되돌리기·전역 비교를 하지 못한다.
- 해법은 reasoning을 **트리 탐색 문제로 일반화**: 각 노드에서 thought 후보를 생성하고, self-evaluation으로 상태 가치를 매겨, BFS/DFS로 유망 분기를 확장하고 막힌 분기는 backtracking한다.
- 내 연구와의 연결:
  - ToT는 "여러 후보를 만들어 평가·탐색"한다는 점에서 우리 candidate-pool 서사와 표면적으로 겹치지만, **통제 단위가 thought/node(미시)** 이고 **heavy explicit search**라는 점이 다르다.
  - 우리는 thought-level 탐색이 아니라, 제한된 TTC 안에서 **heterogeneous path family**를 어떤 순서·budget으로 획득하고 언제 STOP할지 결정하는 **lightweight orchestration**이다. ToT는 search-heavy 대비점.

## 4. 핵심 방법 (PDF 본문 grounding)

- thought (선택/탐색 단위):
  - 한 reasoning step에 해당하는 일관된 텍스트 조각(노드). ToT의 통제 단위는 **thought / state / node**.
- thought generation:
  - `sample`(동일 prompt에서 i.i.d. 다중 샘플) 또는 `propose`(한 prompt로 서로 다른 후보를 한 번에 제안).
- state evaluation V(pθ, S) (self-evaluation):
  - (a) `value`: 각 상태를 독립적으로 점수화 — `V(s) ∼ p_value(v|s)`.
  - (b) `vote`: 여러 상태를 비교 투표해 가장 유망한 상태 선택.
  - 외부 verifier/PRM이 아니라 **동일 LM의 self-evaluation**.
- search:
  - `BFS`(폭 유지 단계 확장) / `DFS`(깊이 우선 + threshold 미달 시 prune/backtrack), lookahead·backtracking 포함.
- 실험 모델/과제:
  - base model **GPT-4**, planning/search가 본질인 과제 — **Game of 24, Creative Writing, Mini Crosswords**.
- cost 특성:
  - thought 생성 + 상태 평가 + 분기 탐색이 모두 LM 호출 → 단일 CoT 대비 **LM call이 크게 증가**(search-heavy).

## 5. SLM-Math 관점의 재해석

- ToT는 직접 baseline 경쟁자라기보다, **search-heavy deliberate reasoning의 대비점(boundary reference)** 이다.
- 공통점:
  - 여러 reasoning 후보를 만들어 평가·선택하는 multi-candidate 사고.
  - 추가 학습 없이 inference-time 행동을 바꿈.
- 차이점(핵심):
  - **granularity**: ToT는 thought/node 내부 explicit search(미시). 우리는 path family / route / macro strategy / STOP(거시) 획득·배분.
  - **homogeneous tree vs heterogeneous pool**: ToT 노드는 대체로 동질 thought. 우리는 `direct / CoT / prompt-diverse CoT / CG / PAL / PoT / verifier-guided` 이질 family pool.
  - **heavy search vs lightweight orchestration**: ToT는 폭·깊이·backtracking으로 LM call 급증. 우리는 route/strategy-card 수준의 가벼운 추정 + macro action routing + STOP을 budget allocation으로 프레이밍.
  - **large/interactive vs small/offline**: ToT는 GPT-4 + 상호작용 탐색. 우리는 small LM + fixed sample bank / offline simulator.
- 보완 포인트:
  - ToT의 state-evaluation(value/vote)은 우리 lightweight route/strategy estimator의 **개념적 조상**으로 차용 가능 — 단 node-level이 아니라 **route/family-level**로, 그리고 **budget에 산입**해서.
- 안전한 한 문장 차별화:
  - ToT는 하나의 reasoning process를 thought 트리로 explicit search하고, 내 연구는 **제한된 TTC 안에서 이질적 path family를 언제·얼마나 획득하고 멈출지 결정**한다.

## 6. 우리 연구에 대한 novelty risk

- "여러 후보를 만들어 평가·탐색한다"는 **multi-path exploration + evaluation** 프레임을 강하게 선점.
- **self-evaluation(value/vote)으로 후보/상태를 고른다**는 lightweight scoring 아이디어 선점 → 우리 route/strategy estimator를 "처음"이라 말하기 어려움.
- **lookahead / backtracking / BFS-DFS** 이미 존재 → "reasoning search 자체"는 novelty 불가.
- "후보 풀을 만들고 그중 고른다"가 표면적으로 겹쳐, **선택 단위(thought vs path-family)를 명확히 안 하면 ToT 재탕으로 읽힐 위험**.
- 단, 위협 성격은 micro-level 탐색(GPT-4, puzzle, 단일 process의 트리 확장)이라 RASC/Scaling-TTC 같은 inference-time allocation 직접 baseline과는 결이 다름.

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - 단일 경로는 exploration/lookahead가 필요한 과제에 취약하다.
  - generation cost뿐 아니라 **state-evaluation cost / search cost(LM call·tree node)** 도 TTC budget이다.
- baseline:
  - `IO / CoT / CoT-SC / ToT(-lite)` 를 **deliberation 정도(single→sample-vote→explicit search)** 축으로 배치. ToT는 search-heavy 상한/대비군.
- metric:
  - accuracy + **LM call 수 / 생성 token / 노드 확장 수**를 cost로 보고 → **budget-matched comparison** 필수.
- ablation:
  - generation `sample` vs `propose` → 우리 path 다양화(표현 다양화 vs family 다양화)와 분리.
  - evaluation `value` vs `vote` → 우리 route/strategy estimator 설계 참조.
  - search budget(폭 b, 깊이) sweep → 우리 budget-accuracy 곡선과 같은 축에 정렬.
- terminology(차용):
  - `thought`, `deliberate problem solving`, `thought generation (sample/propose)`, `state evaluation (value/vote)`, `lookahead`, `backtracking`, `BFS/DFS search`.
- 주의: ToT 과제(Game of 24/Crosswords)는 우리 mainline(GSM8K/MATH500)과 달라 **수치 차용이 아니라 framing/metric/ablation 설계만 차용**.

## 8. 우리가 하면 안 되는 주장

- `reasoning을 트리/그래프로 탐색하는 것이 새롭다`고 쓰면 안 된다(ToT/GoT 선점).
- `deliberate problem solving / 중간 상태 self-evaluation(value/vote)을 우리가 처음 도입한다`고 쓰면 안 된다.
- `lookahead·backtracking·BFS/DFS 기반 reasoning search가 우리 기여다`라고 쓰면 안 된다.
- `multi-path exploration 자체가 novelty다`라고 쓰면 안 된다.
- `우리 CG가 ToT/GoT식 graph/tree search와 같다`고 과장하면 안 된다.
- ToT 대비 raw 성능 SOTA 경쟁 프레임으로 가면 안 된다.
- ToT의 search 비용을 무시한 채 정확도만 비교하면 안 된다.

## 9. baseline / ablation 반영 아이디어

- `IO / CoT / CoT-SC / ToT(-lite)` 를 deliberation-spectrum baseline으로 같은 budget 곡선에 배치.
- **search cost(LM call·node 수)를 TTC budget에 명시 산입**하고, ToT는 budget-matched로만 비교.
- generation(sample/propose)·evaluation(value/vote) 축을 우리 path 다양화·route estimator 설계와 분리하는 ablation.
- 우리 route/family-level estimator를 ToT node-level self-eval과 명확히 구분(개념 차용은 하되 단위·비용을 분리).
- **full ToT 재현은 비대상**: search-heavy contrastive reference로 두고, 필요 시에만 작은 폭/깊이의 **budget-matched ToT-lite** 1개를 상한 대비군으로.

## 10. Related Work에 넣을 문장 초안

Tree of Thoughts(Yao et al., NeurIPS 2023)는 언어모델의 단일 경로 디코딩 한계를 극복하기 위해, 중간 추론 단위인 thought를 노드로 하는 트리 위에서 thought 생성과 self-evaluation 기반 상태 평가(value/vote), 그리고 BFS/DFS 탐색(backtracking/lookahead 포함)을 결합한 deliberate problem-solving 프레임워크다. 이 방법은 Game of 24, Creative Writing, Mini Crosswords처럼 탐색·계획이 본질인 과제에서 CoT/CoT-SC 대비 큰 향상을 보였다(예: Game of 24에서 CoT 4% 대비 ToT 74%).

그러나 ToT의 초점은 하나의 reasoning process를 thought 노드 수준에서 명시적으로 탐색하는 heavy search이며, 제한된 test-time compute 안에서 서로 다른 reasoning path family를 어떤 순서·budget으로 획득하고 언제 멈출지는 다루지 않는다. 본 연구는 ToT를 thought-level explicit search의 대비점으로 삼되, 주어진 small language model이 현재 reasoning state와 남은 budget(생성·평가·탐색 비용 포함)을 바탕으로 heterogeneous reasoning path family 중 무엇을 추가로 획득하고 언제 STOP할지 결정하는 **state-conditioned, lightweight test-time orchestration**으로 구분된다. 즉 탐색 단위가 thought가 아니라 path-family/macro-strategy라는 점이 핵심 차이다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P1`
- 위협도: 중간 (claim 경계·wording 측면; 직접 baseline 경쟁 아님)
- 구현 결정:
  - **full reproduction 비대상.** ToT는 conceptual / search-heavy contrastive reference로 둔다.
  - 필요 시에만 작은 폭·깊이의 **budget-matched ToT-lite**(LM-call 계상)를 상한 대비군으로 1개 추가하는 선택지. full BFS/DFS + GPT-4 재현은 mainline·비용 규칙상 비권장.
- 지금 당장 해야 할 일:
  - ToT를 `search-based / deliberate reasoning` cluster(GoT·MCTS류·rStar-Math)와 묶어 **P1 search-boundary reference**로 고정.
  - `reasoning search / BFS·DFS / lookahead·backtracking / self-evaluation / deliberate solving`을 novelty로 쓰지 않도록 wording 가드.
  - **search cost를 TTC budget에 계상**하는 원칙 명문화.
  - 우리 route/family-level estimator를 ToT node-level self-eval과 분리.
- 나중으로 미뤄도 되는 일:
  - ToT full search 재현, puzzle benchmark(Game of 24/Crosswords) 평가, MCTS류와의 정량 대결.
- 한 줄 결론:
  - ToT는 우리가 재현·경쟁할 대상이 아니라, "reasoning을 트리로 explicit search"하는 heavy search의 대비점으로 두고, 우리를 **path-family acquisition & STOP under limited TTC**로 분리하게 만드는 P1 search-boundary reference다.
