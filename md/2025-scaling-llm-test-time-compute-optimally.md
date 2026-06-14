# Scaling LLM Test-Time Compute Optimally review stub

## 메타데이터

- 제목: Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning
- 연도: 2025
- venue / status: ICLR 2025 Oral
- 링크: https://openreview.net/forum?id=4FWAwZtd2n
- 상태: `stub`

## 한 줄 요약

- search, revision, verifier를 포함한 compute-optimal TTC 관점에서 reasoning 성능을 분석한 대표 framing paper다.

## 왜 중요한가

- compute-optimal TTC framing의 핵심 anchor다.
- search와 revision을 분해해 보는 관점을 준다.

## 우리 연구와의 관계

- method inspiration이자 contrastive positioning 대상이다.
- 우리는 heavier verifier/search가 아니라 smaller-model lightweight orchestration 쪽으로 가야 한다.

## 빌릴 점

- compute-optimal framing
- search vs revision decomposition
- compute-accuracy tradeoff narrative

## 하면 안 되는 주장

- compute-optimal TTC framing 자체를 새로 제안한다고 쓰면 안 된다.
- verifier/search-heavy setting을 그대로 우리 기여처럼 말하면 안 된다.

## target venue 관점에서의 의미

- stretch venue를 보든 core NLP/AI venue를 보든 introduction에서 핵심 reference가 된다.
- 우리 논문은 이 선행연구보다 더 가벼운 setting에서 어떤 차별화가 있는지 분명해야 한다.

## 아직 확인할 질문

- route-family selection을 search/revision taxonomy 안에서 어떻게 배치할지
- verifier 없이도 유지되는 gain을 어떻게 설득력 있게 보일지
