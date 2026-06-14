# DeepSeekMath review stub

## 메타데이터

- 제목: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
- 연도: 2024
- venue / status: arXiv / unverified
- 링크: https://arxiv.org/abs/2402.03300
- 코드: https://github.com/deepseek-ai/deepseek-math
- 상태: `stub`

## 한 줄 요약

- math-specific continued pretraining과 GRPO를 통해 7B open model의 수학 추론을 크게 끌어올린 training-heavy baseline이다.

## 왜 중요한가

- raw math performance를 논할 때 자주 비교되는 대표 baseline이다.
- self-consistency와 training-side gain을 같이 보여 준다.

## 우리 연구와의 관계

- direct baseline reference다.
- 우리는 large-scale math pretraining/RL이 아니라 inference-time orchestration 쪽에 초점이 있다.

## 빌릴 점

- math mainline background
- self-consistency baseline 서술
- small open model math reasoning frontier 비교축

## 하면 안 되는 주장

- simple routing/TTC만으로 DeepSeekMath류 training gain을 대체한다고 과장하면 안 된다.
- raw math SOTA 경쟁으로 프레임을 옮기면 안 된다.

## target venue 관점에서의 의미

- ACL/EMNLP/NAACL/AAAI용 메인 논문에서도 반드시 언급해야 할 strong baseline 축이다.
- 우리 novelty는 training recipe가 아니라 path/strategy allocation임을 분명히 해야 한다.

## 아직 확인할 질문

- SC가 성능에 기여한 비중을 얼마나 크게 해석해야 하는가
- 우리 benchmark와 직접적으로 맞닿는 비교 문구는 어디까지가 적절한가
