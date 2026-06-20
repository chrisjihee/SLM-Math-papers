# UNIFIED PAPER LIST

> **Status note (2026-06-20):** This file is a secondary/legacy unified index.
> The canonical paper registry is now `papers.yaml`, and the active reading/status queue is `READING-QUEUE-202606.md` plus root `CURRENT-READING.md`.
> For current claim boundaries and positioning, use `RELATED-WORK-MATRIX.md` and `POSITIONING-NOTES.md`.
> Do not infer unread/read status from this file alone.

Last updated: 2026-06-14

이 문서는 현재 `SLM-Math`의 **post-2026-06 taxonomy**에 맞게 논문을 재분류한 통합 목록이다. 목적은 "CG 관련 논문 모음"이 아니라, **math reasoning mainline + TTC/path selection + selective NFM bridge**를 함께 보는 것이다.

## 1. Math SLM / reasoning frontier

| Paper | Year / Venue | Link | 메모 |
|---|---|---|---|
| rStar-Math | 2025 / ICML | https://proceedings.mlr.press/v267/guan25f.html | small-model math frontier, MCTS + PPM + self-evolution |
| DeepSeekMath | 2024 / arXiv | https://arxiv.org/abs/2402.03300 | math pretraining + GRPO + SC |
| DeepSeek-R1 | 2025 / arXiv | https://arxiv.org/abs/2501.12948 | reasoning RL positioning |
| LIMO | 2025 / arXiv | https://arxiv.org/abs/2502.03387 | few curated examples hypothesis |
| s1 | 2025 / EMNLP | https://aclanthology.org/2025.emnlp-main.1025/ | simple TTC baseline |
| WizardMath | 2023 / arXiv | https://arxiv.org/abs/2308.09583 | classic math SLM baseline |
| MetaMath | 2023 / arXiv | https://arxiv.org/abs/2309.12284 | synthetic math QA bootstrapping |
| MAmmoTH | 2023 / arXiv | https://arxiv.org/abs/2309.05653 | hybrid CoT + PoT training |
| ToRA | 2023 / arXiv | https://arxiv.org/abs/2309.17452 | tool-integrated math reasoning |
| MathCoder | 2023 / arXiv | https://arxiv.org/abs/2310.03731 | code-integrated math reasoning |

핵심 포인트:
- 이 묶음은 "math SOTA를 노리기 위한 체크리스트"이기도 하지만, 동시에 **우리가 raw frontier race를 직접 따라가면 안 되는 이유**를 보여 준다.

## 2. Self-consistency and TTC

| Paper | Year / Venue | Link | 메모 |
|---|---|---|---|
| Self-Consistency | 2023 / ICLR | https://openreview.net/forum?id=1PL1NIMMrw | canonical SC baseline |
| Reasoning-Aware Self-Consistency | 2025 / NAACL | https://aclanthology.org/2025.naacl-long.184/ | rationale-aware SC |
| Confidence Improves Self-Consistency in LLMs | 2025 / ACL Findings | https://aclanthology.org/2025.findings-acl.1030/ | confidence-weighted voting |
| Self-Consistency Boosts Calibration for Math Reasoning | 2024 / EMNLP Findings | https://arxiv.org/abs/2403.09849 | calibration angle |
| Learning How Hard to Think | 2025 / ICLR | https://openreview.net/forum?id=6qUUgw9bAZ | input-adaptive compute allocation |
| Scaling LLM Test-Time Compute Optimally | 2025 / ICLR | https://openreview.net/forum?id=4FWAwZtd2n | compute-optimal TTC framing |
| Can 1B LLM Surpass 405B LLM? | 2025 / arXiv | https://arxiv.org/abs/2502.06703 | small-vs-large TTC claim |
| Kinetics | 2025 / arXiv | https://arxiv.org/abs/2506.05333 | practical scaling-law correction |

핵심 포인트:
- 이 묶음이 현재 mainline related work의 중심이다.

## 3. Reasoning path pool / strategy selection

| Paper | Year / Venue | Link | 메모 |
|---|---|---|---|
| Self-Discover | 2024 / official page | https://openreview.net/forum?id=BROvXhmzYK | reasoning structure composition |
| Automatic Model Selection with LLMs for Reasoning | 2023 / EMNLP Findings | https://aclanthology.org/2023.findings-emnlp.55/ | CoT vs PAL routing |
| PAL | 2022 / arXiv | https://arxiv.org/abs/2211.10435 | code-as-reasoning path |
| Program of Thoughts Prompting | 2022 / arXiv | https://arxiv.org/abs/2211.12588 | PoT path family |
| ToRA | 2023 / arXiv | https://arxiv.org/abs/2309.17452 | tool-integrated path family |

핵심 포인트:
- `Self-Discover`는 graph/KG 쪽보다 **strategy selection**에 두는 것이 맞다.
- `PAL/PoT/ToRA`는 우리 taxonomy에서 **alternative path family**의 대표 사례다.

## 4. Verifier / PRM / reranker

| Paper | Year / Venue | Link | 메모 |
|---|---|---|---|
| Training Verifiers to Solve Math Word Problems | 2021 / arXiv | https://arxiv.org/abs/2110.14168 | verifier-first math reasoning classic |
| Let's Verify Step by Step | 2024 / ICLR | https://openreview.net/forum?id=v8L0pN6EOi | process supervision canonical |
| Math-Shepherd | 2024 / ACL | https://aclanthology.org/2024.acl-long.510/ | automatic PRM |
| Process Reward Models That Think | 2025 / arXiv | https://arxiv.org/abs/2504.16828 | generative verifier |
| Rewarding Progress | 2025 / ICLR | https://openreview.net/forum?id=A6Y7AqlzLW | progress-based automated prover/verifier framing |

핵심 포인트:
- 현재 route-card reranker line은 step-level PRM과 동일하지 않다.
- 하지만 verifier literature와 끊어 읽으면 positioning이 약해진다.

## 5. Search / reflection / RL

| Paper | Year / Venue | Link | 메모 |
|---|---|---|---|
| Tree of Thoughts | 2023 / arXiv | https://arxiv.org/abs/2305.10601 | deliberate tree search |
| Graph of Thoughts | 2023 / arXiv | https://arxiv.org/abs/2308.09687 | graph search / thought graph |
| RAP | 2023 / official page | https://openreview.net/forum?id=VTWWvYtF1R | planning with world model |
| ReST-MCTS* | 2024 / arXiv | https://arxiv.org/abs/2406.03816 | PRM-guided tree search self-training |
| Reflexion | 2023 / official page | https://openreview.net/forum?id=vAElhFcKW6 | reflection / verbal RL |
| DeepSeek-R1 | 2025 / arXiv | https://arxiv.org/abs/2501.12948 | RL-heavy reasoning line |
| rStar-Math | 2025 / ICML | https://proceedings.mlr.press/v267/guan25f.html | search-heavy frontier |

핵심 포인트:
- 이 묶음은 "future work"와 "we are lighter-weight" positioning 둘 다에 필요하다.

## 6. Structured / graph reasoning

| Paper | Year / Venue | Link | 메모 |
|---|---|---|---|
| UniCoTT | 2025 / ICLR | https://openreview.net/forum?id=3baOKeI2EU | unified structured CoT distillation |
| MAGDi | 2025 / ICLR Spotlight | https://openreview.net/forum?id=ffLblkoCw8 | graph distillation |
| InstructGraph | 2024 / ACL Findings | https://aclanthology.org/2024.findings-acl.801/ | graph-centric IT + preference alignment |
| Think-on-Graph | 2023 / arXiv | https://arxiv.org/abs/2307.07697 | KG-guided graph reasoning |
| Graph of Thoughts | 2023 / arXiv | https://arxiv.org/abs/2308.09687 | graph-structured thought dependency |

핵심 포인트:
- legacy CG/KG 자료는 유지하되, 현재는 **structured reasoning path family** 또는 **background**로 읽는다.
- `graph reasoning`이라는 표현은 조심해서 쓴다.

## 7. NFM / telco reasoning bridge

| Paper / Resource | Year / Venue | Link | 메모 |
|---|---|---|---|
| TeleQnA | 2023 / arXiv | https://arxiv.org/abs/2310.15051 | telecom QA benchmark |
| TeleMath | 2025 / arXiv | https://arxiv.org/abs/2506.10674 | telecom math reasoning benchmark |
| TeleTables | 2025 / dataset + paper | https://huggingface.co/datasets/netop/TeleTables | table interpretation |
| TeleLogs | 2025 / dataset + paper | https://huggingface.co/datasets/netop/TeleLogs | RCA / diagnostics |
| ORAN-Bench-13K | 2024 / arXiv | https://arxiv.org/abs/2407.06245 | O-RAN knowledge benchmark |
| ORANBench | 2025 / HF dataset | https://huggingface.co/datasets/prnshv/ORANBench | 1,500-question streamlined set |
| srsRANBench | 2025 / HF dataset | https://huggingface.co/datasets/prnshv/srsRANBench | code understanding / codegen |
| ORANSight-2.0 | 2025 / arXiv | https://arxiv.org/abs/2503.05200 | specialized O-RAN LLM |
| GSMA Open Telco AI | 2026 / initiative | https://www.gsma.com/solutions-and-impact/technologies/artificial-intelligence/open-telco-ai/ | official initiative |
| GSMA leaderboard hub | 2026 / HF org | https://huggingface.co/GSMA | benchmark roster, models, scores |

핵심 포인트:
- NFM는 breadth가 넓다. `TeleMath -> TeleTables -> TeleLogs`만 우선 본다.

## 8. Long-term / background / lower priority

| Paper | Year / Venue | Link | 메모 |
|---|---|---|---|
| Self-Instruct | 2023 / ACL | https://aclanthology.org/2023.acl-long.754/ | old data-generation background |
| Distilling Step-by-Step! | 2023 / ACL Findings | https://aclanthology.org/2023.findings-acl.507/ | rationale distillation background |
| Phased Instruction Fine-Tuning | 2024 / ACL Findings | https://aclanthology.org/2024.findings-acl.341/ | curriculum background |
| LoRA Soups | 2025 / COLING Industry | https://aclanthology.org/2025.coling-industry.55/ | long-term merging |
| Unraveling LoRA Interference | 2025 / ACL | https://aclanthology.org/2025.acl-long.1284/ | long-term merging |

핵심 포인트:
- model merging / LoRA merging은 현재 mainline을 직접 지지하지 않으므로 long-term으로 내린다.

## 짧은 정리

현재 taxonomy의 중심축은 아래 세 개다.

1. `math frontier`
2. `TTC / SC / verifier / strategy selection`
3. `selective NFM bridge`

`CG/KG`는 이제 중심축이 아니라 structured family/background 축이다.
