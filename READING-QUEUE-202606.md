# READING QUEUE 2026-06

현재 읽기 큐는 "CG를 살릴 논문"이 아니라, **math reasoning mainline + TTC/path selection + verifier + selective NFM bridge** 순서로 재편한다.

## P0: 지금 바로 읽기

### 1. rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking

- Year / Venue: 2025 / ICML 2025
- Link: https://proceedings.mlr.press/v267/guan25f.html
- Theme: math_slm_frontier, search_reflection_rl, verifier_prm
- 왜 중요한가: 현재 small-model math frontier에서 가장 강한 reference 중 하나다.
- 뽑을 것: policy model, PPM, MCTS, self-evolution이 각각 얼마나 무거운지와 무엇이 main gain인지.
- 우리와의 관계: 직접 경쟁보다는 contrastive positioning. 우리는 lighter-weight orchestration 쪽.
- Priority: P0
- Track: main math research

### 2. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- Year / Venue: 2024 / arXiv-only
- Link: https://arxiv.org/abs/2402.03300
- Theme: math_slm_frontier
- 왜 중요한가: strong math pretraining + GRPO + self-consistency의 대표 baseline이다.
- 뽑을 것: 7B scale에서 pretraining, RL, SC가 각각 얼마나 기여하는지.
- 우리와의 관계: direct baseline reference. "math SOTA"를 노리지 말아야 하는 이유를 준다.
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

- Year / Venue: 2023 / ICLR 2023
- Link: https://openreview.net/forum?id=1PL1NIMMrw
- Theme: sc_efficiency
- 왜 중요한가: 모든 sampling-based reasoning의 canonical baseline이다.
- 뽑을 것: self-consistency의 unit, marginalization intuition, sample scaling curve.
- 우리와의 관계: 반드시 이 baseline을 넘거나 확장해야 한다.
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
- 왜 중요한가: process supervision / PRM의 canonical paper다.
- 뽑을 것: step-level supervision이 왜 outcome-level보다 강한지, PRM800K의 역할.
- 우리와의 관계: full PRM을 안 하더라도 verifier-related positioning의 기준선이다.
- Priority: P0
- Track: main math research

### 10. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations

- Year / Venue: 2024 / ACL 2024
- Link: https://aclanthology.org/2024.acl-long.510/
- Theme: verifier_prm, search_reflection_rl
- 왜 중요한가: human step labels 없이 math PRM을 만드는 대표 사례다.
- 뽑을 것: auto process supervision, reranking vs PPO usage.
- 우리와의 관계: verifier line의 현실적인 자동화 reference.
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

## P1: 포지셔닝과 baseline 보강에 중요

### 13. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- Year / Venue: 2025 / arXiv-only
- Link: https://arxiv.org/abs/2501.12948
- Theme: math_slm_frontier, search_reflection_rl
- 왜 중요한가: reasoning RL 계열의 대표 reference다.
- 뽑을 것: cold-start + RL recipe, readability issue, distillation story.
- 우리와의 관계: 우리가 직접 재현할 대상은 아니지만 RL-heavy line과의 차이를 분명히 해 준다.
- Priority: P1
- Track: main math research

### 14. LIMO: Less is More for Reasoning

- Year / Venue: 2025 / arXiv-only
- Link: https://arxiv.org/abs/2502.03387
- Theme: math_slm_frontier
- 왜 중요한가: few high-quality examples만으로도 reasoning을 끌어낼 수 있다는 반례다.
- 뽑을 것: data efficiency claim, curated examples의 역할.
- 우리와의 관계: "대규모 새 데이터 생성"이 반드시 immediate next step이 아니라는 근거.
- Priority: P1
- Track: main math research

### 15. WizardMath

- Year / Venue: 2023 / arXiv-only
- Link: https://arxiv.org/abs/2308.09583
- Theme: math_slm_frontier
- 왜 중요한가: classic open math SLM baseline이다.
- 뽑을 것: RLEIF, dataset evolution, 7B/70B scaling.
- 우리와의 관계: older frontier baseline.
- Priority: P1
- Track: main math research

### 16. MetaMath

- Year / Venue: 2023 / arXiv-only
- Link: https://arxiv.org/abs/2309.12284
- Theme: math_slm_frontier
- 왜 중요한가: synthetic math QA bootstrapping의 대표.
- 뽑을 것: question rewriting pipeline, 7B/70B gains.
- 우리와의 관계: main novelty가 data bootstrapping이 아님을 보여 주는 contrastive reference.
- Priority: P1
- Track: thesis background

### 17. MAmmoTH

- Year / Venue: 2023 / arXiv-only
- Link: https://arxiv.org/abs/2309.05653
- Theme: math_slm_frontier, path_pool_construction
- 왜 중요한가: CoT와 PoT를 같이 쓰는 hybrid rationale reference다.
- 뽑을 것: hybrid rationales, MathInstruct, tool-use mix.
- 우리와의 관계: heterogeneous path pool의 training-side reference.
- Priority: P1
- Track: main math research

### 18. ToRA

- Year / Venue: 2023 / arXiv-only
- Link: https://arxiv.org/abs/2309.17452
- Theme: math_slm_frontier, path_pool_construction, tool_use
- 왜 중요한가: tool-integrated math reasoning의 대표다.
- 뽑을 것: interactive tool trajectories, output space shaping.
- 우리와의 관계: 향후 `PoT/PAL/tool-assisted` family를 path pool에 넣을 때 중요하다.
- Priority: P1
- Track: main math research

### 19. PAL

- Year / Venue: 2022 / arXiv-only
- Link: https://arxiv.org/abs/2211.10435
- Theme: path_pool_construction, tool_use
- 왜 중요한가: code-as-reasoning 계열의 고전이다.
- 뽑을 것: natural language reasoning vs runtime execution 분리.
- 우리와의 관계: direct/CoT와 다른 path family의 정의 기준을 준다.
- Priority: P1
- Track: main math research

### 20. Program of Thoughts Prompting

- Year / Venue: 2022 / arXiv-only
- Link: https://arxiv.org/abs/2211.12588
- Theme: path_pool_construction, tool_use
- 왜 중요한가: PoT 계열의 대표 prompt-level baseline이다.
- 뽑을 것: computation offloading, SC와의 결합.
- 우리와의 관계: `PoT`를 path family taxonomy에 넣을 근거.
- Priority: P1
- Track: main math research

### 21. Process Reward Models That Think

- Year / Venue: 2025 / arXiv-only
- Link: https://arxiv.org/abs/2504.16828
- Theme: verifier_prm
- 왜 중요한가: generative PRM / verbalized verifier의 최근 강한 reference다.
- 뽑을 것: data efficiency, long-CoT verifier, same-token-budget comparison.
- 우리와의 관계: lightweight verifier를 path-level에 어떻게 붙일지 아이디어를 준다.
- Priority: P1
- Track: main math research

### 22. Automatic Model Selection with Large Language Models for Reasoning

- Year / Venue: 2023 / EMNLP 2023 Findings
- Link: https://aclanthology.org/2023.findings-emnlp.55/
- Theme: path_pool_construction, routing
- 왜 중요한가: CoT와 PAL 사이의 method routing을 다룬다.
- 뽑을 것: selection signal, method choice framing, failure cases.
- 우리와의 관계: reasoning strategy selection의 직접 선행연구다.
- Priority: P1
- Track: main math research

### 23. TeleTables

- Year / Venue: 2025 / dataset page + paper link
- Link: https://huggingface.co/datasets/netop/TeleTables
- Theme: nfm_telco_bridge
- 왜 중요한가: structured/table reasoning bridge의 핵심 benchmark다.
- 뽑을 것: table interpretation 유형, multi-step table reasoning difficulty.
- 우리와의 관계: strategy-card를 `table prompt / retrieval-table selection`으로 확장하기 좋다.
- Priority: P1
- Track: NFM bridge

### 24. TeleLogs

- Year / Venue: 2025 / dataset page + paper link
- Link: https://huggingface.co/datasets/netop/TeleLogs
- Theme: nfm_telco_bridge
- 왜 중요한가: RCA, verifier, diagnosis path selection 문제로 바로 연결된다.
- 뽑을 것: symptom-root-cause structure, majority-vote/maj@4 성격, schema needs.
- 우리와의 관계: math 이후 bridge paper의 2순위 또는 3순위.
- Priority: P1
- Track: NFM bridge

## P2: 유용한 배경

- Tree of Thoughts — 2023 / NeurIPS 2023 / https://arxiv.org/abs/2305.10601
  왜: search framing reference. 우리와는 heavier search 대비군.

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
