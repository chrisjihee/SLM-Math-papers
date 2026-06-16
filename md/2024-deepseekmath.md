# DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models review

## 1. Metadata

- Title: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
- Authors: Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo
- Year: 2024
- Venue / Status: arXiv:2402.03300v3, 2024-04-27 preprint
- Links:
  - Paper: https://arxiv.org/abs/2402.03300
  - GitHub / Code: https://github.com/deepseek-ai/deepseek-math
- Code / Data:
  - GitHub repository 제공
  - DeepSeekMath Corpus는 Common Crawl에서 선별한 120B math-related tokens를 중심으로 구축
- Paper Type:
  - `training-heavy`
  - `math-specialized pretraining + SFT + RL alignment`
  - `inference-time`
  - `homogeneous self-consistency baseline`
- Reading Status: `strategically-read`
- Current Priority: `P0`

## 2. One-line Summary

DeepSeekMath는 7B code-pretrained model에 대규모 math corpus pretraining, CoT/PoT/tool-integrated SFT, GRPO 기반 RL을 적용해 open-source 7B 수학 추론 성능을 크게 끌어올린 training-heavy frontier 논문이다.

## 3. 핵심 문제 설정

- 이 논문은 open-source model이 GPT-4 / Gemini Ultra 같은 closed model에 비해 수학 추론 성능이 크게 뒤처지는 문제를 풀려고 한다.
- 핵심 해법은 model scale만 키우는 것이 아니라,
  - math-specialized corpus pretraining
  - CoT / PoT / tool-integrated reasoning SFT
  - GRPO 기반 RL
  를 7B backbone에 결합하는 것이다.
- 내 연구와의 연결은 직접적이면서도 간접적이다.
  - 직접적으로는 여러 reasoning path를 test-time에 선택하는 논문은 아니다.
  - 그러나 강한 7B math backbone과 strong SC baseline을 제시한다.
- 특히 중요한 연결점:
  - CoT / PoT / tool-use path를 training stage에서 이미 흡수한 model이라는 점
  - `Pass@K`와 `Maj@K`를 구분해 분석한다는 점
  - self-consistency 64 samples를 강한 baseline으로 제시한다는 점

## 4. 핵심 방법

- math pretraining:
  - Common Crawl에서 fastText classifier와 반복 mining으로 math-related corpus를 선별한다.
  - 35.5M pages, 120B tokens를 수집하고 benchmark contamination도 줄이려 한다.
- SFT:
  - 776K mathematical instruction-tuning examples를 사용한다.
  - CoT, PoT, tool-integrated reasoning format이 포함된다.
- GRPO:
  - PPO와 달리 value model을 제거하고, 같은 question의 sampled outputs group 평균 reward를 baseline으로 사용한다.
  - memory/computation burden을 줄이는 RL design이다.
- self-consistency / Pass@K / Maj@K:
  - self-consistency over 64 samples를 보고한다.
  - RL은 Pass@K보다 Maj@K를 더 크게 개선한다고 분석한다.
- 내 연구 관점에서 핵심 포인트:
  - DeepSeekMath는 여러 sampled outputs를 **training signal**로 사용한다.
  - 내 연구는 여러 reasoning paths를 **test-time acquisition / selection / stopping 대상**으로 사용한다.

## 5. SLM-Math 관점의 재해석

- DeepSeekMath는 내 연구의 직접 경쟁자라기보다 **강한 backbone / 강한 SC baseline / Pass@K-Maj@K 분석 기준점**이다.
- 공통점:
  - small/open math model의 reasoning 성능을 중시한다.
  - CoT, PoT, tool-integrated reasoning을 모두 중요하게 본다.
  - sampling-based aggregation의 효과를 정면으로 다룬다.
- 차이점:
  - DeepSeekMath의 핵심은 model parameter를 training-heavy하게 개선하는 것이다.
  - 내 연구의 핵심은 주어진 model에서 heterogeneous reasoning path pool을 제한된 TTC 안에서 어떻게 구성할지다.
- 안전한 한 문장 차별화:
  - DeepSeekMath는 strong math-specialized backbone과 homogeneous SC baseline을 제공하고, 내 연구는 **그 위에서 서로 다른 path family에 budget을 어떻게 나눌지**를 다룬다.

## 6. 우리 연구에 대한 novelty risk

- `작은 모델도 수학 reasoning을 잘할 수 있다`는 넓은 claim은 이미 약하다.
- CoT / PoT / tool-integrated reasoning을 섞는 것 자체도 새롭지 않다.
- RL로 math reasoning을 강화하는 것도 새롭지 않다.
- self-consistency over many samples는 이미 강한 baseline이다.
- `Pass@K / Maj@K` 분석을 빼면 pool-quality 논의가 약해 보일 수 있다.
- 따라서 위험한 framing:
  - `sLLM math 성능 향상` 자체를 novelty로 쓰기
  - `SC가 성능을 올린다`를 기여처럼 쓰기
  - `tool-use route를 섞으면 좋아진다`를 새 관찰처럼 쓰기

## 7. 우리가 빌릴 수 있는 것

- problem framing:
  - parameter count만이 수학 추론 능력의 핵심은 아니다
  - sampling-based aggregation의 효과를 분리해서 봐야 한다
  - training gain과 test-time gain을 구분해야 한다
- baseline:
  - DeepSeekMath-Base / Instruct / RL 7B
  - Top1
  - self-consistency @ 1 / 4 / 8 / 16 / 32 / 64
  - tool-integrated reasoning
  - majority vote
- metric:
  - Accuracy
  - Pass@K
  - Maj@K
  - budget-normalized accuracy
  - tool-use allowed vs disallowed accuracy
- ablation:
  - backbone ablation: general vs code-pretrained vs math-specialized
  - route ablation: CoT vs PoT/PAL vs tool-use vs structured rationale
  - aggregation ablation: Top1 vs majority vs verifier/reranker
  - exploration vs aggregation: Pass@K vs Maj@K
- figure/table idea:
  - route family별 `Pass@K`, `Maj@K`, `Oracle@K`, `Verifier@K`
  - cost-accuracy frontier
  - homogeneous SC vs heterogeneous pool 비교표

## 8. 우리가 하면 안 되는 주장

- `sLLM도 수학 reasoning을 잘할 수 있다는 것을 처음 보였다`고 쓰면 안 된다.
- `CoT / PoT / tool-use를 섞으면 수학 성능이 오른다`를 novelty로 쓰면 안 된다.
- `RL로 수학 reasoning을 향상시키는 것이 새롭다`고 쓰면 안 된다.
- `self-consistency로 성능이 오른다`를 기여처럼 쓰면 안 된다.
- `raw MATH accuracy SOTA` 프레임으로 가면 안 된다.
- `Pass@K 향상 = reasoning capability 향상`으로 단순화하면 안 된다.

## 9. baseline / ablation 반영 아이디어

- fixed `SC@K` baseline을 `K=1/4/8/16/32/64`로 강화한다.
- `Pass@K / Maj@K` 평가를 추가한다.
- `Top1 / SC / oracle path pool / verifier-reranker selection` table을 분리한다.
- `PoT / PAL / tool-integrated route`를 route universe에 포함할지 검토한다.
- homogeneous SC와 heterogeneous path pool을 직접 비교한다.
- code-pretrained backbone vs general backbone을 비교한다.
- `RL은 Maj@K를 올린다`는 관점에서, 우리 routing이 exploration을 실제로 늘리는지 본다.

## 10. Related Work에 넣을 문장 초안

DeepSeekMath는 open-source 7B model의 수학 추론 성능을 크게 끌어올린 대표적인 training-heavy 접근이다. 이 논문은 DeepSeek-Coder-Base-v1.5 7B를 기반으로 Common Crawl에서 선별한 120B math-related tokens를 이용해 continual pretraining을 수행하고, CoT, PoT, tool-integrated reasoning 형식의 instruction tuning과 GRPO 기반 reinforcement learning을 결합하여 GSM8K와 MATH에서 강한 성능을 보였다. 특히 DeepSeekMath-RL 7B는 self-consistency with 64 samples까지 보고하며, Pass@K와 Maj@K 분석을 통해 RL이 주로 output distribution을 안정화하여 majority-vote 성능을 높인다는 점을 보여준다.

그러나 DeepSeekMath의 핵심은 model parameter를 대규모 math data와 RL로 개선하는 데 있으며, 제한된 test-time budget 안에서 서로 다른 reasoning path family를 어떻게 동적으로 구성하고 선택할지는 다루지 않는다. 본 연구는 DeepSeekMath와 같은 math-specialized backbone 및 self-consistency baseline을 강한 비교 대상으로 삼되, 주어진 small language model이 현재 reasoning state, answer distribution, disagreement, remaining budget을 바탕으로 CoT, prompt-diverse CoT, PoT/PAL, structured rationale, verifier-guided path 등 heterogeneous reasoning paths 중 무엇을 추가로 샘플링하고 언제 멈출지를 결정하는 **state-conditioned test-time compute allocation** 문제에 초점을 둔다.

## 11. 현재 우선순위와 다음 액션

- 현재 우선순위: `P0`
- 위협도: 높음
- 지금 당장 해야 할 일:
  - DeepSeekMath를 P0 related work로 고정
  - fixed `SC@K`, `Pass@K`, `Maj@K`를 main evaluation에 포함
  - `Top1 vs SC vs heterogeneous path pool vs oracle path pool vs verifier/reranker selection` table을 설계
  - `PoT / PAL / tool-integrated` route를 route universe에 포함할지 결정
  - claim을 `sLLM 수학 성능 향상`이 아니라 `heterogeneous path pool construction under limited TTC`로 고정
- 나중으로 미뤄도 되는 일:
  - DeepSeekMath backbone full reproduction
  - GRPO 직접 재현
  - reward model / PRM 재학습
  - 120B corpus pipeline 재현
- 한 문장 결론:
  - DeepSeekMath는 training-heavy frontier와 strong homogeneous SC baseline을 보여주는 기준점이며, 내 연구는 그 위에서 **state-conditioned heterogeneous path-pool construction과 budget-aware stopping**으로 차별화해야 한다.
