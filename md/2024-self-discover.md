# SELF-DISCOVER review stub

## 메타데이터

- 제목: SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures
- 연도: 2024
- venue / status: NeurIPS 2024 poster
- 링크: https://openreview.net/forum?id=BROvXhmzYK
- 상태: `stub`

## 한 줄 요약

- LLM이 seed set의 reasoning modules를 바탕으로 task-specific reasoning structure를 스스로 조합하게 하는 strategy composition 논문이다.

## 왜 중요한가

- reasoning strategy selection/composition 자체가 이미 새롭지 않다는 점을 보여 준다.
- path-family framing과 strategy-card framing의 직접 참고문헌이다.

## 우리 연구와의 관계

- direct novelty risk다.
- 우리는 one-shot structure composition이 아니라 dynamic budgeted path acquisition, stopping, verifier/reranker 결합으로 차별화해야 한다.

## 빌릴 점

- reasoning structure / strategy language
- strategy-card 류 표현
- path-family를 구조 수준에서 설명하는 방식

## 하면 안 되는 주장

- reasoning strategy selection general idea를 우리가 처음 한다고 말하면 안 된다.
- strategy selection과 sequential TTC allocation을 구분하지 않으면 안 된다.

## target venue 관점에서의 의미

- core target venue용 related work에서 매우 중요하다.
- 특히 `strategy selection`을 메인 contribution으로 쓰려면 이 논문과의 차이를 먼저 써야 한다.

## 아직 확인할 질문

- 우리 route-card를 SELF-DISCOVER의 reasoning module/structure와 어떻게 구별할지
- one-shot structure selection과 sequential re-allocation의 차이를 어떤 예시로 보여 줄지
