# s1: Simple test-time scaling review

## 1. Metadata

- Title: s1: Simple test-time scaling
- Authors: Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, Tatsunori Hashimoto
- Year: 2025
- Venue / Status: EMNLP 2025 Proceedings
- Links:
  - Code / Project: https://github.com/simplescaling/s1
  - ACL Anthology: https://aclanthology.org/2025.emnlp-main.1025/
- Code / Data:
  - model, data, code 공개
  - `s1K` 1,000개 reasoning trace 기반 SFT
- Benchmarks: AIME24, MATH500, GPQA Diamond
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

이 논문은 1,000개 고품질 reasoning trace로 `Qwen2.5-32B-Instruct`를 SFT한 뒤, test time에 reasoning 길이를 강제로 줄이거나 `"Wait"`를 삽입해 늘리는 `budget forcing`만으로 명확한 test-time scaling curve를 재현할 수 있음을 보인다.

## 3. 핵심 문제 설정

- o1 이후 `test-time compute를 더 쓰면 reasoning 성능이 오른다`는 현상이 주목받았지만, 공개된 단순 재현법은 부족했다.
- 이 논문은 강한 reasoning 성능과 TTC scaling을 얻기 위한 가장 단순한 공개 방법이 무엇인지 묻는다.
- 기존 RL / MCTS / multi-agent / large-scale replication line은 무겁고 공개 재현성이 낮다고 본다.
- 이 논문의 TTC는 기본적으로 **하나의 reasoning trace를 더 길게 또는 짧게 만드는 sequential scaling**이다.
- 따라서 내 연구와 직접 연결되지만, 초점은 다르다.
  - s1: 단일 path를 얼마나 오래 생각하게 할 것인가
  - 내 연구: 제한된 TTC 안에서 어떤 path family를 추가로 샘플링할 것인가

## 4. 핵심 방법

- 학습:
  - `Qwen2.5-32B-Instruct`를 `s1K` 1,000개 reasoning trace로 SFT해 `s1-32B`를 만든다.
- 추론:
  - 핵심은 `budget forcing`
  - maximum budget: thinking token이 한계를 넘으면 end-of-thinking delimiter를 강제로 붙여 종료
  - minimum budget: 모델이 끝내려 할 때 delimiter를 억제하고 `"Wait"`를 삽입해 더 생각하게 함
- 방법 관점에서 보면:
  - reasoning path: 하나의 긴 sequential natural language trace
  - sampling: 주로 greedy / pass@1
  - self-consistency: 주방법 아님, majority voting은 parallel scaling baseline
  - verifier / PRM: 주방법에는 없음
  - search / MCTS / reflection: 명시적 search 없음. `"Wait"`는 reflection처럼 보일 수 있으나 policy/search는 아님
  - routing / strategy selection: 없음
- 핵심은 **single-path thinking length control**이지, heterogeneous path-family orchestration이 아니다.

## 5. SLM-Math 관점의 재해석

- s1은 현재 연구의 직접 경쟁자라기보다 `single-path sequential TTC scaling`의 강한 baseline이다.
- 공통점:
  - TTC가 reasoning 성능을 바꾼다는 점을 정면으로 다룬다.
  - sequential scaling vs parallel scaling을 직접 비교한다.
- 차이점:
  - s1은 한 reasoning trace를 길게 만드는 방법이다.
  - 내 연구는 `direct`, `CoT`, `prompt-diverse CoT`, `PoT`, `CG`, `verifier-guided path` 등 여러 path family 사이에서 budget을 배분하는 문제를 다뤄야 한다.
- 따라서 내 연구는 `longer single-path reasoning`보다 왜 `heterogeneous path-pool construction`이 필요한지를 보여줘야 한다.

## 6. 우리 연구에 대한 novelty risk

- adaptive TTC 자체는 이미 새롭지 않다.
- `더 오래 생각하게 하면 성능이 오른다`는 주장도 이미 위험하다.
- sequential scaling vs parallel scaling 구도도 이미 정리되어 있다.
- TTC metric 설계 역시 `Control / Scaling / Performance`로 상당 부분 선점되어 있다.
- 단순 SC/MoR가 single long reasoning보다 좋다는 주장은 검증 없이는 위험하다.
- `적은 수의 distilled reasoning trace로 reasoning SFT`도 이미 강한 선행축이다.
- 특히 위험한 claim:
  - `test-time compute를 늘려 reasoning 성능을 높이는 것이 새롭다`
  - `simple inference-time control로 scaling을 보이는 것이 새롭다`
- 안전한 방향:
  - `path-family / strategy-level TTC allocation`
  - `same budget에서 longer single-path vs more diverse path-pool` 비교

## 7. 우리가 빌릴 수 있는 것

- 문제 framing:
  - test-time scaling vs train-time scaling
  - sequential scaling vs parallel scaling
  - thinking token을 TTC proxy로 쓰는 방식
- baseline:
  - single CoT + budget forcing
  - `"Wait"` forcing
  - majority voting
  - rejection sampling by length
  - token / step / class conditional control
- metric:
  - `Control`
  - `Scaling`
  - `Performance`
  - average thinking tokens
  - accuracy / pass@1
  - budget-matched comparison
- ablation:
  - budget sweep
  - `"Wait"` vs 다른 continuation cue
  - sequential scaling vs parallel SC vs hybrid
  - repetition / flattening 분석
- figure idea:
  - x축 generated tokens, y축 accuracy
  - longer single CoT vs SC CoT vs heterogeneous MoR 비교
  - single-path budget forcing vs path-pool scaling 비교

## 8. 우리가 하면 안 되는 주장

- test-time compute를 늘려 reasoning 성능을 높이는 것이 새롭다는 주장
- thinking length를 제어하는 간단한 inference-time 방법이 없었다는 주장
- `"Wait"` 같은 cue로 더 생각하게 하는 것이 새롭다는 주장
- parallel Self-Consistency가 항상 sequential long reasoning보다 낫다는 주장
- TTC allocation metric은 accuracy만 보면 된다는 주장
- longer reasoning은 항상 좋다는 주장
- SLM에서 test-time scaling을 처음 보였다는 주장
- 적은 distilled reasoning trace로 reasoning SFT를 향상시키는 것이 새롭다는 주장

## 9. baseline / ablation 반영 아이디어

- `single CoT + budget forcing` baseline 추가
- 기존 SC/MoR 결과를 sample 수가 아니라 generated token budget 기준으로 다시 정리
- `single long CoT` vs `SC CoT` vs `Multiple-CoT` vs `CG-inclusive MoR` budget-matched 비교
- `Control / Scaling / Performance` metric 구현
- `"Wait"` forcing 1x/2x/4x와 route switching 비교
- early STOP policy가 repetition / flattening을 줄이는지 분석
- macro strategy catalog에 `long_single_cot_wait_k` 같은 s1-inspired strategy 추가

## 10. Related Work에 넣을 문장 초안

`s1: Simple test-time scaling`은 1,000개의 carefully curated reasoning traces로 `Qwen2.5-32B-Instruct`를 SFT하고, test time에 end-of-thinking delimiter를 강제로 삽입하거나 `"Wait"`를 추가해 thinking length를 조절하는 `budget forcing`을 제안하였다. 이 연구는 단순한 decoding-time intervention만으로도 `AIME24`, `MATH500`, `GPQA Diamond`에서 test-time scaling curve를 얻을 수 있음을 보였고, sequential scaling과 majority-voting 기반 parallel scaling을 직접 비교하였다. 특히 `Control`, `Scaling`, `Performance`를 통해 test-time scaling method를 accuracy뿐 아니라 controllability와 scaling slope 관점에서 평가한 점은 이후 연구의 중요한 기준이 된다.

그러나 s1은 주로 단일 reasoning trace의 길이를 조절하는 방법이며, 여러 reasoning path family 중 어떤 path를 추가로 생성할지, 현재 answer distribution과 disagreement 상태를 보고 언제 stop하거나 diversify할지의 문제는 직접 다루지 않는다. 본 연구는 s1의 single-path sequential scaling과 달리, 제한된 TTC 안에서 `direct`, `CoT`, `prompt-diverse CoT`, `PoT`, `structured rationale`, `verifier-guided path` 등 heterogeneous reasoning path pool을 동적으로 구성하고, state-conditioned 방식으로 path acquisition과 stopping을 결정하는 문제를 다룬다.

## 11. 현재 우선순위와 다음 액션

- 최종 priority: `P0`
- 위협도: 중간~높음
- 지금 바로 반영할 것:
  - s1-style `budget forcing`을 baseline으로 구현
  - 기존 Axis 2 결과를 token budget 기준으로 재평가
  - `SC CoT`, `Multiple-CoT`, `CG-inclusive MoR`, `Adaptive MoR`, `Sequential TTC Router`가 `single long CoT + Wait forcing`보다 언제 나은지 보이기
  - `adaptive TTC` 자체를 novelty로 쓰지 말고 `path-family / strategy-level allocation`으로 좁히기
- 나중으로 미뤄도 되는 것:
  - `s1K` 재학습 full reproduction
  - `REBASE` full reproduction
  - token / step / class conditional control의 full comparison
