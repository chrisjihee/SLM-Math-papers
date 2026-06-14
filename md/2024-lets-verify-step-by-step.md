# Let's Verify Step by Step review stub

## 메타데이터

- 제목: Let's Verify Step by Step
- 연도: 2024
- venue / status: ICLR 2024 poster
- 링크: https://openreview.net/forum?id=v8L0pN6EOi
- 코드/데이터: https://github.com/openai/prm800k
- 상태: `stub`

## 한 줄 요약

- process supervision이 outcome supervision보다 math reasoning 검증에 더 유효함을 보인 canonical PRM 논문이다.

## 왜 중요한가

- verifier / PRM literature의 기준점이다.
- path selection과는 다른 step-level verification 축을 명확히 보여 준다.

## 우리 연구와의 관계

- direct background이자 novelty boundary다.
- 우리는 full PRM을 다시 만드는 대신 path acquisition 전/중간의 lightweight policy/value estimator로 위치시켜야 한다.

## 빌릴 점

- process supervision vs outcome supervision distinction
- verifier section canonical citation
- answer selection과 path selection을 구분하는 문장

## 하면 안 되는 주장

- path-level reranking과 PRM을 동일시하면 안 된다.
- verifier literature를 건너뛴 채 route selection만 독립 novelty처럼 쓰면 안 된다.

## target venue 관점에서의 의미

- verifier-aware extension paper를 쓸 때 핵심 기준선이다.
- main paper에서도 verifier를 안 하더라도 이 문헌에 대한 위치 설명은 필요하다.

## 아직 확인할 질문

- 우리 route-card reranker를 PRM과 어떤 그림으로 구분할지
- step-level supervision이 없는 setting에서 어떤 lightweight 대안을 제안할지
