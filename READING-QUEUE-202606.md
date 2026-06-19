# READING QUEUE 2026-06

현재 읽기 큐는 "CG를 살릴 논문"이 아니라, **math reasoning mainline + TTC/path selection + verifier + selective NFM bridge** 순서로 재편한다.

## P0: 지금 바로 읽기

### 1. rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking

- Year / Venue: 2025 / ICML 2025
- Link: https://proceedings.mlr.press/v267/guan25f.html
- Status: strategically-read
- Theme: math_slm_frontier, search_reflection_rl, verifier_prm
- 왜 중요한가: small-model math frontier에서 가장 강한 heavy System 2 reference 중 하나이며, `MCTS + PPM + self-evolution`이 어디까지 밀어올릴 수 있는지 보여준다.
- 뽑을 것: trajectory scaling curve, step-level verifier/PPM, pairwise preference supervision, heavy search와 lightweight orchestration의 경계.
- 우리와의 관계: direct 경쟁보다는 contrastive positioning. 우리는 heavy search reproduction이 아니라 lighter-weight path-family / strategy-level allocation 쪽으로 가야 한다.
- Priority: P0
- Track: main math research

### 2. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- Year / Venue: 2024 / arXiv-only
- Link: https://arxiv.org/abs/2402.03300
- Status: strategically-read
- Theme: math_slm_frontier, sc_efficiency, tool_use
- 왜 중요한가: strong 7B math backbone과 homogeneous self-consistency baseline, 그리고 `Pass@K / Maj@K` 해석 기준을 함께 제공하는 training-heavy frontier reference다.
- 뽑을 것: math-specialized pretraining, GRPO, CoT/PoT/tool-integrated SFT, `Pass@K`와 `Maj@K`의 분리.
- 우리와의 관계: direct baseline reference이자 backbone reference. 우리는 training recipe보다 heterogeneous path pool allocation과 stopping으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 3. s1: Simple test-time scaling

- Year / Venue: 2025 / EMNLP 2025
- Link: https://aclanthology.org/2025.emnlp-main.1025/
- Status: strategically-read
- Theme: adaptive_ttc, sc_efficiency
- 왜 중요한가: 가장 단순한 test-time scaling replication line이다.
- 뽑을 것: budget forcing, simple long-thinking recipe, minimal TTC recipe.
- 우리와의 관계: direct TTC baseline이자 single-path sequential scaling의 강한 기준선이다. 우리는 single long reasoning이 아니라 heterogeneous path family / strategy-level allocation으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 4. Self-Consistency Improves Chain of Thought Reasoning in Language Models

- Year / Venue: 2023 / ICLR 2023 (arXiv 2203.11171는 2022-03 공개)
- Link: https://openreview.net/forum?id=1PL1NIMMrw
- Status: strategically-read
- Target file: `md/2023-self-consistency.md`
- Theme: sc_efficiency
- 왜 중요한가: CoT 이후 canonical multi-sample / majority-vote baseline이며, RASC/CISC/adaptive-TTC가 그 위에 쌓이는 homogeneous SC substrate다.
- 뽑을 것: self-consistency의 unit(sample/answer), marginalization intuition, fixed SC@K(1/4/8/16/32/64) origin baseline, Maj@K, sample-scaling curve.
- 우리와의 관계: 반드시 넘어야 할 fixed homogeneous SC baseline. 우리 기여는 SC 개선이 아니라 heterogeneous path-family를 state-conditioned하게 acquire/STOP하는 upstream path-pool 구성이고, `self-consistency / majority vote 자체`는 우리 novelty가 아니다.
- Priority: P0
- Track: main math research

### 5. Reasoning-Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling

- Year / Venue: 2025 / NAACL 2025
- Link: https://aclanthology.org/2025.naacl-long.184/
- Status: strategically-read
- Theme: sc_efficiency, adaptive_ttc
- 왜 중요한가: sample 수를 고정하지 않고 rationale quality까지 보며 SC를 조정한다.
- 뽑을 것: early stopping rule, rationale-aware weighting, sample-efficiency framing.
- 우리와의 관계: 매우 가깝고 필수 baseline이다. 다만 이 논문은 homogeneous CoT-style sample scoring과 stopping에 초점이 있고, 우리는 heterogeneous path family / macro strategy allocation으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 6. Confidence Improves Self-Consistency in LLMs

- Year / Venue: 2025 / ACL 2025 Findings
- Link: https://aclanthology.org/2025.findings-acl.1030/
- Status: strategically-read
- Theme: sc_efficiency, adaptive_ttc
- 왜 중요한가: confidence-weighted voting으로 SC cost를 줄이는 strong recent baseline이다.
- 뽑을 것: confidence signal 종류, P(True), within-question confidence, weighted voting.
- 우리와의 관계: 필수 aggregation baseline이다. 다만 이 논문은 homogeneous path pool 위의 confidence-weighted aggregation을 다루고, 우리는 heterogeneous path-family / macro strategy allocation으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 7. Learning How Hard to Think: Input-Adaptive Allocation of LM Computation

- Year / Venue: 2025 / ICLR 2025
- Link: https://openreview.net/forum?id=6qUUgw9bAZ
- Status: strategically-read
- Theme: adaptive_ttc
- 왜 중요한가: 입력별로 computation budget을 적응적으로 배정하는 가장 직접적인 reference다.
- 뽑을 것: allocation policy, reward prediction, fixed-budget vs adaptive-budget comparison.
- 우리와의 관계: 우리 framing과 매우 가깝지만, 이 논문은 query-level budget allocation과 weak/strong routing에 초점이 있고 우리는 state-conditioned reasoning path family / macro strategy allocation으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 8. Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning

- Year / Venue: 2025 / ICLR 2025
- Link: https://openreview.net/forum?id=4FWAwZtd2n
- Theme: adaptive_ttc, verifier_prm
- Status: strategically-read
- 왜 중요한가: difficulty-conditioned compute-optimal TTC와 verifier/search/revision trade-off를 가장 직접적으로 정리한 핵심 framing paper다.
- 뽑을 것: search vs revision decomposition, difficulty-only compute-optimal baseline, verifier overhead accounting, budget-accuracy curve.
- 우리와의 관계: 메인 framing reference지만, 이 논문은 problem difficulty 기반 strategy selection이고 우리는 current reasoning state 기반 heterogeneous path-family / macro-strategy allocation으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 9. Let's Verify Step by Step

- Year / Venue: 2024 / ICLR 2024
- Link: https://openreview.net/forum?id=v8L0pN6EOi
- Theme: verifier_prm
- Status: strategically-read
- 왜 중요한가: process-supervised PRM이 majority voting과 outcome-style verifier보다 강한 downstream selector가 될 수 있음을 보여주는 canonical paper다.
- 뽑을 것: process vs outcome supervision, PRM800K, best-of-N + verifier selection, fixed-pool-after-generation framing.
- 우리와의 관계: verifier-related positioning의 기준선이며, 우리는 PRM 자체보다 upstream path acquisition / heterogeneous pool construction 쪽으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 10. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations

- Year / Venue: 2024 / ACL 2024
- Link: https://aclanthology.org/2024.acl-long.510/
- Theme: verifier_prm, search_reflection_rl
- Status: strategically-read
- 왜 중요한가: human step labels 없이 자동 process supervision으로 strong PRM을 만들고 best-of-N verification / step-level PPO까지 연결한 대표 verifier baseline이다.
- 뽑을 것: automatic process supervision, best-of-N verification, PRM final-score aggregation, verifier cost accounting.
- 우리와의 관계: verifier line의 현실적인 자동화 reference이자, 우리는 PRM 자체보다 candidate pool construction / upstream path acquisition 쪽으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 11. Self-Discover: Large Language Models Self-Compose Reasoning Structures

- Year / Venue: 2024 / NeurIPS 2024
- Link: https://openreview.net/forum?id=BROvXhmzYK
- Status: strategically-read
- Theme: path_pool_construction
- 왜 중요한가: reasoning structure 자체를 선택/조합하는 대표 paper다.
- 뽑을 것: module selection, structure composition, inference cost comparison.
- 우리와의 관계: strategy-card / path-family framing의 직접 참고문헌이자 P0 related work다. 다만 이 논문은 task-level one-shot structure composition에 가깝고, 우리는 state-conditioned path-family / macro strategy acquisition으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 12. TeleMath: A Benchmark for Large Language Models in Telecom Mathematical Problem Solving

- Year / Venue: 2025 / arXiv-only
- Link: https://arxiv.org/abs/2506.10674
- Theme: nfm_telco_bridge
- 왜 중요한가: math mainline을 NFM로 연결하는 가장 자연스러운 첫 benchmark다.
- 뽑을 것: task type, answer format, pass@1 vs majority-vote 성격, direct/CoT 차이.
- 우리와의 관계: NFM bridge의 1순위.
- Priority: P0
- Track: NFM bridge

### 13. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- Year / Venue: 2025 / arXiv
- Link: https://arxiv.org/abs/2501.12948
- Status: strategically-read
- Theme: math_slm_frontier, search_reflection_rl
- 왜 중요한가: human reasoning label 없이 pure RL(GRPO)로 long CoT·self-verification을 창발시키고 1.5B~70B로 distill까지 한 training-heavy / reasoning-RL frontier reference다. 직접 구현할 inference-time allocation baseline은 아니지만, `RL reasoning 유도 / long CoT / self-verification / distilled small reasoner` claim boundary를 강하게 제한한다.
- 뽑을 것: cold-start + multi-stage RL recipe, GRPO, readability/language-mixing issue, distillation story, R1-Distill backbone baseline, AIME/MATH-500 + thinking-token budget.
- 우리와의 관계: 직접 재현 대상이 아니라 P0 contrastive frontier reference이자 strong backbone. 우리는 fixed/given backbone 위 state-conditioned heterogeneous path-pool construction / STOP / lightweight orchestration으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 14. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

- Year / Venue: 2022 / NeurIPS 2022 (arXiv 2201.11903는 2022-01 공개)
- Link: https://arxiv.org/abs/2201.11903
- Status: strategically-read
- Target file: `md/2022-chain-of-thought.md` (CURRENT-READING.md target_file 우선)
- Theme: math_reasoning, prompting, reasoning_path_baseline
- 왜 중요한가: 중간 추론 단계(rationale)를 유도하는 reasoning prompting의 canonical origin이며, 모든 reasoning path-family 비교의 기준점이다.
- 뽑을 것: few-shot CoT greedy origin baseline, direct vs CoT 기준선, GSM8K/SVAMP/ASDiv/AQuA/MAWPS, prompt-diversity vs structural(CG) 분리 ablation, emergent-ability-at-scale framing.
- 우리와의 관계: 개선/대체 대상이 아니라 P0 origin baseline / claim boundary. 우리 기여는 CoT 포함 heterogeneous path family를 제한된 TTC 안에서 state-conditioned하게 acquire/STOP하는 것이고, CG는 auxiliary structured family로 둔다. `CG > CoT`, `CoT prompting novelty` 주장 금지.
- Priority: P0
- Track: main math research

## P1: 포지셔닝과 baseline 보강에 중요

### 15. LIMO: Less is More for Reasoning

- Year / Venue: 2025 / arXiv-only
- Link: https://arxiv.org/abs/2502.03387
- Theme: math_slm_frontier
- 왜 중요한가: few high-quality examples만으로도 reasoning을 끌어낼 수 있다는 반례다.
- 뽑을 것: data efficiency claim, curated examples의 역할.
- 우리와의 관계: "대규모 새 데이터 생성"이 반드시 immediate next step이 아니라는 근거.
- Priority: P1
- Track: main math research

### 16. WizardMath

- Year / Venue: 2023 / arXiv-only
- Link: https://arxiv.org/abs/2308.09583
- Theme: math_slm_frontier
- 왜 중요한가: classic open math SLM baseline이다.
- 뽑을 것: RLEIF, dataset evolution, 7B/70B scaling.
- 우리와의 관계: older frontier baseline.
- Priority: P1
- Track: main math research

### 17. MetaMath

- Year / Venue: 2023 / arXiv-only
- Link: https://arxiv.org/abs/2309.12284
- Theme: math_slm_frontier
- 왜 중요한가: synthetic math QA bootstrapping의 대표.
- 뽑을 것: question rewriting pipeline, 7B/70B gains.
- 우리와의 관계: main novelty가 data bootstrapping이 아님을 보여 주는 contrastive reference.
- Priority: P1
- Track: thesis background

### 18. MAmmoTH

- Year / Venue: 2023 / arXiv-only
- Link: https://arxiv.org/abs/2309.05653
- Theme: math_slm_frontier, path_pool_construction
- 왜 중요한가: CoT와 PoT를 같이 쓰는 hybrid rationale reference다.
- 뽑을 것: hybrid rationales, MathInstruct, tool-use mix.
- 우리와의 관계: heterogeneous path pool의 training-side reference.
- Priority: P1
- Track: main math research

### 19. ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving

- Year / Venue: 2024 / ICLR 2024 (arXiv 2309.17452는 2023-09 공개)
- Link: https://arxiv.org/abs/2309.17452
- Status: strategically-read
- Target file: `md/2023-tora.md` (CURRENT-READING.md target_file 우선)
- Theme: math_slm_frontier, path_pool_construction, tool_use
- 왜 중요한가: 자연어 reasoning과 program 실행·tool 호출을 한 trajectory에서 interleave하는 tool-integrated agent의 대표로, PAL/PoT보다 강한 tool-interleaved path family reference다.
- 뽑을 것: interactive tool trajectories, output space shaping, ToRA/ToRA-Code 7B~70B baseline, GSM8K/MATH + tool-call·exec cost.
- 우리와의 관계: 직접 재학습 대상이 아니라 P0 tool-use baseline 후보. ToRA-like path를 heterogeneous pool의 한 family로 수용하고, 무엇을 제한 TTC 안에서 언제 추가 획득/STOP할지 결정하는 state-conditioned orchestration으로 차별화한다. tool execution cost를 TTC budget에 포함해야 한다.
- Priority: P0
- Track: main math research

### 20. PAL

- Year / Venue: 2023 / ICML 2023
- Link: https://openreview.net/forum?id=M1fd9Z00sj
- Status: strategically-read
- Theme: path_pool_construction, tool_use
- 왜 중요한가: `PAL / PoT / code-interpreter` route를 heterogeneous reasoning path pool의 필수 family로 고정하게 만드는 canonical tool-use baseline이다.
- 뽑을 것: natural language decomposition과 runtime execution 분리, arithmetic/state-tracking 강점, `SC-PAL` 및 mixed path budget 비교 축.
- 우리와의 관계: direct/CoT/CG와 다른 tool-executed path family를 언제 추가 샘플링할지 결정해야 한다는 점을 선명하게 만든다.
- Priority: P0
- Track: main math research

### 21. Program of Thoughts Prompting

- Year / Venue: 2023 / TMLR
- Link: https://openreview.net/forum?id=YfZ4ZPt8zd
- Status: strategically-read
- Theme: path_pool_construction, tool_use
- 왜 중요한가: executable program path인 `PoT`를 numerical reasoning의 핵심 baseline으로 고정해주는 대표 tool-use prompt다.
- 뽑을 것: computation offloading, `SC-PoT`, mixed CoT+PoT budget comparison, state-tracking / equation-heavy utility.
- 우리와의 관계: `PoT`를 path family taxonomy에 넣고, CoT/PAL/CG와 함께 heterogeneous pool을 구성해야 한다는 근거를 준다.
- Priority: P0
- Track: main math research

### 22. Process Reward Models That Think

- Year / Venue: 2025 / preprint; GitHub metadata TMLR / unverified
- Link: https://arxiv.org/abs/2504.16828
- Status: strategically-read
- Theme: verifier_prm, adaptive_ttc, generative_verifier
- 왜 중요한가: generative PRM과 verifier compute scaling을 결합해, generation compute뿐 아니라 verification compute도 TTC에 포함해야 함을 보여주는 최근 강한 reference다.
- 뽑을 것: data efficiency, long verification CoT, best-of-N verifier selection, compute-matched comparison, verifier budget split.
- 우리와의 관계: lightweight verifier를 path-level에 붙일 아이디어를 주지만, 이 논문은 verifier가 이미 있는 상황의 downstream selector이며 우리는 state-conditioned path acquisition before verification으로 차별화해야 한다.
- Priority: P1
- Track: main math research

### 23. Automatic Model Selection with Large Language Models for Reasoning

- Year / Venue: 2023 / EMNLP 2023 Findings
- Link: https://aclanthology.org/2023.findings-emnlp.55/
- Status: strategically-read
- Theme: path_pool_construction, routing, sc_efficiency
- 왜 중요한가: `CoT`와 `PAL`처럼 서로 다른 reasoning method를 post-hoc으로 선택하는 대표 selection baseline이며, heterogeneous method selection이 homogeneous SC보다 cost-efficient할 수 있음을 보여준다.
- 뽑을 것: `Delta UpperBound`, `Success Rate`, heterogeneous-vs-similar method contrast, option-order bias, selection+SC 결합.
- 우리와의 관계: reasoning strategy selection의 직접 선행연구지만, 이 논문은 full generation 이후의 one-shot selection이고 우리는 state-conditioned path acquisition / stopping으로 차별화해야 한다.
- Priority: P0
- Track: main math research

### 24. TeleTables

- Year / Venue: 2025 / dataset page + paper link
- Link: https://huggingface.co/datasets/netop/TeleTables
- Theme: nfm_telco_bridge
- 왜 중요한가: structured/table reasoning bridge의 핵심 benchmark다.
- 뽑을 것: table interpretation 유형, multi-step table reasoning difficulty.
- 우리와의 관계: strategy-card를 `table prompt / retrieval-table selection`으로 확장하기 좋다.
- Priority: P1
- Track: NFM bridge

### 25. TeleLogs

- Year / Venue: 2025 / dataset page + paper link
- Link: https://huggingface.co/datasets/netop/TeleLogs
- Theme: nfm_telco_bridge
- 왜 중요한가: RCA, verifier, diagnosis path selection 문제로 바로 연결된다.
- 뽑을 것: symptom-root-cause structure, majority-vote/maj@4 성격, schema needs.
- 우리와의 관계: math 이후 bridge paper의 2순위 또는 3순위.
- Priority: P1
- Track: NFM bridge

### 26. Tree of Thoughts: Deliberate Problem Solving with Large Language Models

- Year / Venue: 2023 / NeurIPS 2023 (arXiv 2305.10601는 2023-05 공개)
- Link: https://arxiv.org/abs/2305.10601
- Status: strategically-read
- Target file: `md/2023-tree-of-thoughts.md`
- Source PDF: `paper/2023-tree-of-thoughts.pdf`
- Theme: search_reflection_rl, path_pool_construction
- 왜 중요한가: thought/node 단위 explicit BFS/DFS search + self-evaluation(value/vote)의 search-heavy deliberate reasoning 대표. GoT·MCTS류(rStar-Math)와 같은 search cluster다.
- 뽑을 것: IO/CoT/CoT-SC/ToT(-lite) deliberation-spectrum baseline, generation(sample/propose)·evaluation(value/vote) framing, LM-call/tree-node cost accounting, budget-matched comparison.
- 우리와의 관계: 직접 baseline이 아니라 search-boundary contrastive reference. 우리는 thought-level search가 아니라 heterogeneous path-family acquisition + STOP의 lightweight orchestration으로 분리하고, search/eval cost를 TTC budget에 계상한다. full reproduction 비대상(필요 시 budget-matched ToT-lite).
- Priority: P1
- Track: main math research

## P2: 유용한 배경

- Graph of Thoughts — 2023 / arXiv-only / https://arxiv.org/abs/2308.09687
  왜: graph claim을 어디까지 해야 하는지 구분하는 데 도움.

- RAP: Reasoning via Planning — 2023 / official paper / https://openreview.net/forum?id=VTWWvYtF1R
  왜: planning-style reasoning과의 차이를 정리할 때 유용.

- ReST-MCTS* — 2024 / arXiv-only / https://arxiv.org/abs/2406.03816
  왜: PRM-guided tree search self-training reference.

- Reflexion — 2023 / official paper / https://openreview.net/forum?id=vAElhFcKW6
  왜: reflection negative evidence를 너무 일반화하지 않기 위해 읽어야 한다.

- UniCoTT — 2025 / ICLR 2025 / https://openreview.net/forum?id=3baOKeI2EU
  왜: structured rationale distillation reference.

- MAGDi — 2025 / ICLR 2025 Spotlight / https://openreview.net/forum?id=ffLblkoCw8
  왜: graph-based distillation이 실제로 무엇을 의미하는지 참고.

- InstructGraph — 2024 / ACL 2024 Findings / https://aclanthology.org/2024.findings-acl.801/
  왜: graph-centric instruction tuning과 preference alignment reference.

## Skim only

- Kinetics: Rethinking Test-Time Scaling Laws — 2025 / https://arxiv.org/abs/2506.05333
  왜: 최신 scaling law 관점 참고. immediate mainline은 아님.

- Can 1B LLM Surpass 405B LLM? — 2025 / https://arxiv.org/abs/2502.06703
  왜: compute-optimal TTS 주장 참고.

- ORAN-Bench-13K — 2024 / https://arxiv.org/abs/2407.06245
  왜: NFM 지식 benchmark 맥락 참고.

- ORANSight-2.0 — 2025 / https://arxiv.org/abs/2503.05200
  왜: telecom-specialized model line 참고.

- Think-on-Graph — 2023 / https://arxiv.org/abs/2307.07697
  왜: graph-preserving reasoning과 현재 CG의 차이 확인용.

## Deprioritized for now

- LoRA Soups, LoRA interference, model merging 계열
  이유: 현재 메인라인이 path selection/TTC이며, merging은 중장기 축이다.

- broad KG completion / graph QA only papers
  이유: 현재 thesis core가 KG reasoning 자체가 아니다.

- full telecom QA sweep papers
  이유: NFM는 bridge domain이지 mainline이 아니다.

- giant self-evolution replication papers
  이유: 현재 immediate next step이 아니다.
