# Self-Consistency review stub

## 메타데이터

- 제목: Self-Consistency Improves Chain of Thought Reasoning in Language Models
- 연도: 2023
- venue / status: ICLR 2023 poster
- 링크: https://openreview.net/forum?id=1PL1NIMMrw
- 상태: `stub`

## 한 줄 요약

- diverse reasoning paths를 여러 개 샘플링하고 majority vote로 집계하는 canonical sampling baseline이다.

## 왜 중요한가

- 모든 sampling-based reasoning 논문의 출발점이다.
- 우리가 확장하거나 넘어야 할 가장 기본적인 baseline이다.

## 우리 연구와의 관계

- direct baseline이다.
- 우리는 same-prompt homogeneous sampling이 아니라 heterogeneous path family pool을 본다.

## 빌릴 점

- majority-vote baseline
- diverse reasoning path intuition
- sampling curve discussion

## 하면 안 되는 주장

- self-consistency 자체를 부정하는 듯한 문구
- heterogeneous routing을 self-consistency와 무관한 완전히 새로운 문제처럼 포장하는 문구

## target venue 관점에서의 의미

- 어떤 venue를 가든 빠질 수 없는 baseline이다.
- 우리 contribution은 `SC 이후의 후보 풀 설계와 문제별 allocation`으로 표현해야 안전하다.

## 아직 확인할 질문

- 우리 논문에서 homogeneous SC와 heterogeneous pool SC를 어떤 그림으로 대비할지
- answer-level vote와 path-level selection의 경계를 어떻게 정리할지
