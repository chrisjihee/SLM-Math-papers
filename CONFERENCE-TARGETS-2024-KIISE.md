# CONFERENCE TARGETS 2024 KIISE

## 14.1 기준

- 정보과학회 2024 소프트웨어 분야 우수학술대회 목록 기준으로 본다.
- `S급 = 최우수학술대회`, `A급 = 우수학술대회`로 해석한다.
- Workshop 논문은 주요 성과로 보지 않는다.
- Full paper 중심으로 본다.
- 현재 연구와 실제 관련성이 있는 venue만 포함한다.
- 현재 연구의 중심은 `Budget-aware / state-conditioned reasoning path selection for small language model mathematical reasoning`이다.
- 따라서 등급이 높더라도 관련성이 낮은 분야는 main target에 넣지 않는다.

## 14.2 현재 연구의 핵심 target venue

| 구분 | 학회 | 등급 | 관련성 | 적합한 논문 형태 | 현재 우선순위 |
| -- | -- | -- | --- | --------- | ------- |
| Core target | ACL | S | 매우 높음 | math reasoning, verifier, self-consistency extension, path selection | 최우선 |
| Core target | EMNLP | S | 매우 높음 | TTC, sampling efficiency, reranker, reasoning analysis | 최우선 |
| Core target | NAACL | S | 매우 높음 | path selection, efficient reasoning, verifier/rationale selection | 최우선 |
| Core target | AAAI | S | 매우 높음 | reasoning methods, adaptive compute, verifier-aware inference | 최우선 |
| Stretch target | ICLR | S | 높음 | adaptive TTC, compute allocation, routing methodology | 조건부 상향 |
| Stretch target | ICML | S | 높음 | stronger methodological contribution, broad generalization | 조건부 상향 |
| Stretch target | NeurIPS | S | 높음 | strong algorithmic novelty, multi-benchmark generalization | 조건부 상향 |
| Realistic fallback | ACL Findings | A | 높음 | strong empirical paper, scoped novelty, careful analysis | 높음 |
| Realistic fallback | EMNLP Findings | A | 높음 | efficient reasoning / routing empirical study | 높음 |
| Realistic fallback | NAACL Findings | A | 높음 | scoped method + strong analysis | 높음 |
| Realistic fallback | COLING | A | 중상 | reasoning evaluation, rationale/path analysis | 중상 |
| Realistic fallback | EACL | A | 중상 | compact but clear path-selection paper | 중상 |
| Realistic fallback | IJCAI | A | 중상 | AI-oriented reasoning / allocation / verifier paper | 중상 |
| Conditional target | SIGIR | S | 조건부 | evidence-grounded reasoning, reranking-heavy paper | 낮음 |
| Conditional target | KDD | S | 조건부 | large-scale routing/ranking analysis, stronger data angle | 낮음 |
| Conditional target | WSDM | S | 조건부 | ranking, selection, retrieval-grounded reasoning | 낮음 |
| Conditional target | CIKM | S | 조건부 | retrieval/knowledge-grounded reasoning systems | 낮음 |
| Conditional target | WWW | S | 조건부 | web-scale evidence/ranking/retrieval reasoning | 낮음 |
| NFM-only conditional target | INFOCOM | S | 조건부 | real network measurement / operations contribution | 매우 낮음 |
| NFM-only conditional target | CoNEXT | S | 조건부 | network experiments + telecom reasoning system insight | 매우 낮음 |
| NFM-only conditional target | NSDI | S | 조건부 | system-building + realistic operational evaluation | 매우 낮음 |
| NFM-only conditional target | SIGCOMM | S | 조건부 | strong network-systems novelty 필수 | 매우 낮음 |
| NFM-only conditional target | IMC | A | 조건부 | measurement-heavy TeleLogs/operations paper | 낮음 |
| NFM-only conditional target | NOMS | A | 조건부 | network management application paper | 낮음 |
| NFM-only conditional target | ICNP | A | 조건부 | protocol/operations reasoning link가 있을 때 | 낮음 |
| NFM-only conditional target | PAM | A | 조건부 | measurement/analysis 중심일 때 | 낮음 |
| NFM-only conditional target | WiOpt | A | 조건부 | optimization-heavy wireless reasoning일 때 | 낮음 |

## 14.3 Paper track별 추천 venue

| Paper track | 주제 | 1차 target | stretch target | fallback | 제외/주의 |
| ----------- | -- | --------- | -------------- | -------- | ----- |
| Main SLM-Math paper | Budget-aware / state-conditioned reasoning path selection for small language model mathematical reasoning | ACL, EMNLP, NAACL, AAAI | ICLR, ICML, NeurIPS | ACL Findings, EMNLP Findings, NAACL Findings, COLING, EACL, IJCAI | CG superiority claim, 무리한 network venue 확장 |
| Extension paper | Heterogeneous reasoning path pool construction + verifier/reranker + compute-accuracy tradeoff | ACL, EMNLP, NAACL, AAAI | ICLR, ICML, NeurIPS | ACL Findings, EMNLP Findings, IJCAI, COLING | PRM/MCTS/RL을 한 번에 다 얹는 과도한 확장 |
| NFM bridge paper | Domain-aware test-time reasoning strategy selection for NFM-LLM | ACL, EMNLP, NAACL, AAAI | IJCAI, 조건부로 ICLR/ICML | ACL Findings, EMNLP Findings, COLING, NOMS | 첫 논문부터 SIGCOMM/NSDI/INFOCOM을 main target으로 두지 않기 |

## 14.4 관련 학회별 보강해야 할 related work

### ACL / EMNLP / NAACL

- self-consistency
- reasoning-aware sampling
- confidence-based SC
- verifier / rationale selection
- self-correction / reflection
- mathematical reasoning
- small language model reasoning

### AAAI / ICLR / ICML / NeurIPS

- test-time compute scaling
- adaptive compute allocation
- MCTS / search
- PRM / verifier
- small-model math reasoning
- self-evolution
- strategy selection

### NFM / network

- telco LLM evaluation
- TeleMath
- TeleTables
- TeleLogs
- RCA
- network automation
- intent-to-configuration

## 한 줄 요약

현재 연구의 현실적인 메인 제출 전략은 **ACL / EMNLP / NAACL / AAAI를 core target으로 두고, ICLR / ICML / NeurIPS는 방법론적 새로움이 충분할 때만 stretch로 올리며, NFM는 TeleMath 중심 bridge로 제한하는 것**이다.
