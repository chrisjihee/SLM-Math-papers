# Math-Shepherd review stub

## 메타데이터

- 제목: Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations
- 연도: 2024
- venue / status: ACL 2024 Long Paper
- 링크: https://aclanthology.org/2024.acl-long.510/
- 상태: `stub`

## 한 줄 요약

- human step labels 없이 자동으로 process supervision을 만들고, 이를 verification과 RL에 활용한 practical PRM 논문이다.

## 왜 중요한가

- verifier/PRM을 현실적인 자동화 방향으로 확장한 대표 사례다.
- full human-annotated PRM을 하지 않아도 verifier line이 강하다는 점을 보여 준다.

## 우리 연구와의 관계

- method inspiration이다.
- 우리는 step-level PRM 재구현보다는 route-level lightweight reranker/policy 쪽이 더 맞다.

## 빌릴 점

- auto process supervision narrative
- verifier를 reranking과 RL에 나눠 쓰는 구조
- lightweight verifier와 heavy PRM의 대비 문구

## 하면 안 되는 주장

- human-free verifier novelty를 그대로 가져오면 안 된다.
- verifier literature를 지나치게 좁게 인용하면 안 된다.

## target venue 관점에서의 의미

- verifier extension paper를 준비할 때 직접 비교해야 할 주요 reference다.
- main paper에서는 future extension anchor로 다루는 편이 안전하다.

## 아직 확인할 질문

- verification-only 활용과 RL 활용을 우리 scope에서 어떻게 분리할지
- process score를 route-level stopping signal로 약하게 쓸 수 있을지
