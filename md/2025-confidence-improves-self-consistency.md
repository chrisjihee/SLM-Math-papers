# CISC review stub

## 메타데이터

- 제목: Confidence Improves Self-Consistency in LLMs
- 연도: 2025
- venue / status: ACL 2025 Findings
- 링크: https://aclanthology.org/2025.findings-acl.1030/
- 코드: https://github.com/taubenfeld/CISC
- 상태: `stub`

## 한 줄 요약

- self-consistency의 majority vote를 confidence-weighted vote로 바꿔 sample 수를 줄이는 answer-level efficiency baseline이다.

## 왜 중요한가

- confidence-weighted voting이 이미 강한 baseline임을 보여 준다.
- answer selection과 path selection을 분리해서 생각하게 해 준다.

## 우리 연구와의 관계

- direct baseline이다.
- 우리는 answer weighting을 부정하는 것이 아니라, 그 위에 path-family acquisition과 strategy allocation을 추가로 다룬다.

## 빌릴 점

- confidence signal usage
- weighted vote baseline
- sample efficiency reporting 방식

## 하면 안 되는 주장

- answer weighting만으로는 안 된다는 식의 과도한 단정
- confidence baseline을 무시한 채 route-level novelty만 강조하는 서술

## target venue 관점에서의 의미

- ACL/EMNLP/NAACL 쪽 related work에서 매우 직접적으로 맞닿는다.
- `homogeneous answer-level weighting` 대 `heterogeneous path-level allocation` 대비가 필요하다.

## 아직 확인할 질문

- within-question confidence를 우리 state feature로 넣을지
- confidence와 verifier/reranker의 경계를 어떻게 둘지
