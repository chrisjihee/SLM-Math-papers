아래는 **아직 추가로 읽고 정리할 논문 목록**을 우선순위별로 정리한 것입니다. 이미 `RASC`, `CISC`, `Self-Discover`, `s1`, `Scaling LLM TTC Optimally`, `Let’s Verify Step by Step`, `Math-Shepherd`, `ThinkPRM`, `Automatic Model Selection`, `PAL`, `PoT`, `rStar-Math`는 전략 독해를 진행했으므로, 여기서는 **다음 라운드에서 읽을 후보** 중심으로 정리했습니다.

## 1순위: main positioning을 닫기 위해 먼저 읽을 논문

| 우선순위 | 전체 논문명                                                                                 | 학술대회/저널/아카이브         | 링크                                                                   | 왜 먼저 읽어야 하는가                                                                                                                                                              |
| ---- | -------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P0   | **DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models** | arXiv, 2024          | [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300) | math-specific pretraining, GRPO, SC까지 포함한 open math model frontier입니다. “우리 방법이 training-heavy math model improvement와 어떻게 다른가”를 닫아야 합니다. ([arXiv][1])                     |
| P0   | **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** | arXiv, 2025          | [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948) | reasoning RL, long CoT, self-verification, distilled small models까지 포함하므로, `SLM + reasoning RL + TTC` 축의 가장 큰 frontier reference입니다. ([arXiv][2])                         |
| P0   | **ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving**           | arXiv, 2023          | [https://arxiv.org/abs/2309.17452](https://arxiv.org/abs/2309.17452) | `PAL`/`PoT` 이후 읽어야 할 tool-integrated reasoning 대표 논문입니다. external tool, symbolic solver, interactive tool-use trajectory를 포함하므로 `RUN_TOOL` family 설계에 중요합니다. ([arXiv][3]) |
| P0   | **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**              | NeurIPS 2022 / arXiv | [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903) | CoT 자체는 이미 기본 배경이지만, related-work repo에는 canonical CoT note가 있어야 합니다. 이후 모든 path family 비교의 기준점입니다. ([arXiv][4])                                                          |
| P0   | **Self-Consistency Improves Chain of Thought Reasoning in Language Models**            | ICLR 2023 / arXiv    | [https://arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171) | 현재 연구의 substrate가 Self-Consistency이므로 원 논문을 별도 전략 독해로 고정해야 합니다. “path pool construction”을 SC 위에 어떻게 얹을지 정리하는 기준입니다. ([arXiv][5])                                          |

## 2순위: search / reflection / tree reasoning 경계 정리

| 우선순위  | 전체 논문명                                                                       | 학술대회/저널/아카이브      | 링크                                                                   | 왜 읽어야 하는가                                                                                                                                                                       |
| ----- | ---------------------------------------------------------------------------- | ----------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P0/P1 | **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**  | arXiv, 2023       | [https://arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601) | ToT는 CoT를 tree search로 확장한 대표 논문입니다. 우리 연구의 selection unit이 `thought/node`가 아니라 `path family / macro strategy / STOP`이라는 차이를 정리해야 합니다. ([arXiv][6])                             |
| P1    | **Graph of Thoughts: Solving Elaborate Problems with Large Language Models** | AAAI 2024 / arXiv | [https://arxiv.org/abs/2308.09687](https://arxiv.org/abs/2308.09687) | CG/graph-like reasoning과 이름상 가까워 reviewer가 연상할 가능성이 있습니다. GoT는 LLM thought를 graph로 구성하는 prompting framework이고, 우리 CG/path-family allocation과 어떻게 다른지 정리할 필요가 있습니다. ([arXiv][7]) |
| P1    | **Self-Refine: Iterative Refinement with Self-Feedback**                     | arXiv, 2023       | [https://arxiv.org/abs/2303.17651](https://arxiv.org/abs/2303.17651) | reflection/refinement baseline을 닫기 위해 필요합니다. 현재 실험에서 reflection이 약했다고 해도 “reflection은 효과 없다”고 말하면 안 되므로, 강한 self-feedback 계열을 확인해야 합니다. ([arXiv][8])                            |
| P1    | **Reflexion: Language Agents with Verbal Reinforcement Learning**            | arXiv, 2023       | [https://arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366) | verbal feedback, episodic memory, trial-and-error 기반 reflection을 다룹니다. `reflection`을 macro strategy card 중 하나로 넣을지 판단하는 데 필요합니다. ([arXiv][9])                                   |

## 3순위: structured prompting / decomposition / rationale learning 축

| 우선순위  | 전체 논문명                                                                                                | 학술대회/저널/아카이브         | 링크                                                                   | 왜 읽어야 하는가                                                                                                                                                   |
| ----- | ----------------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1    | **Least-to-Most Prompting Enables Complex Reasoning in Large Language Models**                        | arXiv, 2022          | [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625) | complex problem을 simpler subproblems로 분해해 순차적으로 푸는 structured prompting baseline입니다. macro strategy card에서 `decompose-first` 계열을 정의할 때 필요합니다. ([arXiv][10]) |
| P1    | **Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models** | arXiv, 2023          | [https://arxiv.org/abs/2305.04091](https://arxiv.org/abs/2305.04091) | `plan first, solve later` 구조를 다룹니다. Self-Discover와 함께 structured prompting / planning strategy 계열의 baseline으로 정리할 필요가 있습니다. ([arXiv][11])                   |
| P1    | **Large Language Models are Zero-Shot Reasoners**                                                     | NeurIPS 2022 / arXiv | [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916) | Zero-shot-CoT의 원 논문입니다. `Let’s think step by step`류 minimal prompting baseline을 명확히 정리하기 위해 필요합니다. ([arXiv][12])                                            |
| P1/P2 | **STaR: Bootstrapping Reasoning With Reasoning**                                                      | arXiv, 2022          | [https://arxiv.org/abs/2203.14465](https://arxiv.org/abs/2203.14465) | rationale generation → correct-answer filtering → fine-tuning loop입니다. CG distillation / rationale distillation 쪽 boundary를 정리하는 데 도움이 됩니다. ([arXiv][13])   |

## 4순위: NFM/ETRI bridge 및 domain benchmark 축

| 우선순위  | 전체 논문명                                                                                      | 학술대회/저널/아카이브 | 링크                                                                   | 왜 읽어야 하는가                                                                                                                                                                                                              |
| ----- | ------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1/P2 | **TeleMath: A Benchmark for Large Language Models in Telecom Mathematical Problem Solving** | arXiv, 2025  | [https://arxiv.org/abs/2506.10674](https://arxiv.org/abs/2506.10674) | NFM/telecom bridge로 가장 직접적인 benchmark 후보입니다. 논문 main experiment보다는 과제 보고/응용 validation bridge로 두는 것이 안전합니다. ([arXiv][14])                                                                                              |
| P2    | **TeleResilienceBench: Quantifying Resilience for LLM Reasoning in Telecommunications**     | arXiv, 2026  | [https://arxiv.org/abs/2605.09929](https://arxiv.org/abs/2605.09929) | 2026년 최신 telecom reasoning resilience benchmark입니다. current reasoning trace를 이어받아 회복하는 설정이라, long-term으로 `state-conditioned reasoning recovery`와 연결될 수 있습니다. 다만 main thesis line보다는 NFM extension 후보입니다. ([arXiv][15]) |

## 링크 확인이 필요한 후보

`UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation`는 이전 queue에 있었지만, 지금 웹 검색으로는 제목/공식 링크를 안정적으로 확인하지 못했습니다. 이 항목은 repo 내부 metadata나 사용자가 가진 PDF 기준으로 다시 확인한 뒤 넣는 것이 좋겠습니다. 확인 전에는 `P1 candidate / link-unverified` 정도로만 두는 편이 안전합니다.

# 추천 독해 순서

바로 다음 라운드는 아래 순서가 가장 좋겠습니다.

1. **DeepSeekMath**
2. **DeepSeek-R1**
3. **ToRA**
4. **Chain-of-Thought Prompting**
5. **Self-Consistency**
6. **Tree of Thoughts**
7. **Self-Refine / Reflexion**
8. **Least-to-Most / Plan-and-Solve**
9. **TeleMath**

이 순서로 읽으면 먼저 **math frontier와 tool-use frontier**를 닫고, 그 다음 **CoT/SC 원전과 search/reflection/structured prompting canonical baseline**을 정리하게 됩니다. 그러면 SLM-Math의 related work boundary는 상당히 단단해질 것입니다.

[1]: https://arxiv.org/abs/2402.03300?utm_source=chatgpt.com "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
[2]: https://arxiv.org/abs/2501.12948?utm_source=chatgpt.com "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
[3]: https://arxiv.org/abs/2309.17452?utm_source=chatgpt.com "ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving"
[4]: https://arxiv.org/abs/2201.11903?utm_source=chatgpt.com "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
[5]: https://arxiv.org/abs/2203.11171?utm_source=chatgpt.com "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
[6]: https://arxiv.org/abs/2305.10601?utm_source=chatgpt.com "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
[7]: https://arxiv.org/abs/2308.09687?utm_source=chatgpt.com "Graph of Thoughts: Solving Elaborate Problems with Large Language Models"
[8]: https://arxiv.org/abs/2303.17651?utm_source=chatgpt.com "Self-Refine: Iterative Refinement with Self-Feedback"
[9]: https://arxiv.org/abs/2303.11366?utm_source=chatgpt.com "Reflexion: Language Agents with Verbal Reinforcement Learning"
[10]: https://arxiv.org/abs/2205.10625?utm_source=chatgpt.com "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
[11]: https://arxiv.org/abs/2305.04091?utm_source=chatgpt.com "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models"
[12]: https://arxiv.org/abs/2205.11916?utm_source=chatgpt.com "Large Language Models are Zero-Shot Reasoners"
[13]: https://arxiv.org/abs/2203.14465?utm_source=chatgpt.com "STaR: Bootstrapping Reasoning With Reasoning"
[14]: https://arxiv.org/abs/2506.10674?utm_source=chatgpt.com "TeleMath: A Benchmark for Large Language Models in Telecom Mathematical Problem Solving"
[15]: https://arxiv.org/abs/2605.09929?utm_source=chatgpt.com "TeleResilienceBench: Quantifying Resilience for LLM Reasoning in Telecommunications"
