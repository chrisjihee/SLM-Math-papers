# PHD STRATEGY 2026-2027

## 1. 현재 상태 진단

현재 SLM-Math는 아래 세 축을 이미 갖고 있다.

- Axis 1: CoT vs CG 직접 비교
- Axis 2: SC / Static / Adaptive MoR evidence
- Axis 1-next: sequential TTC router / reranker / offline simulator line

즉 thesis core는 더 이상 teacher 데이터 생성 자체가 아니라, **문제별 reasoning path selection과 TTC allocation**에 가깝다.

## 2. 가장 현실적인 큰 방향

- 첫 top-tier submission은 **math mainline**이어야 한다.
- NFM은 첫 논문의 핵심이 아니라, application/bridge 또는 후속 논문으로 둔다.
- 2026 Q3에는 관련연구 / 포지셔닝 / 실험 질문을 고정해야 한다.
- 2026 Q4에는 benchmark와 baseline을 줄이고, 하나의 명확한 contribution으로 제출 가능성을 만들어야 한다.
- 2027에는 extension paper 또는 NFM bridge paper를 dissertation chapter로 발전시킨다.
- 실패 시 compromise venue나 domestic/industry-aligned output도 고려하되, 목표는 정보과학회 S급/A급 우수학술대회 기준으로 유지한다.

## 3. umbrella thesis

> Efficient and Reliable Reasoning Path Selection for Small Language Models

이 umbrella 아래에서 `math mainline`과 `selective NFM bridge`를 함께 다루되, priority는 항상 math mainline에 둔다.

## 4. Main SLM-Math paper

### 1차 target

- ACL
- EMNLP
- NAACL
- AAAI

### stretch target

- ICLR
- ICML
- NeurIPS

### fallback

- ACL Findings
- EMNLP Findings
- NAACL Findings
- COLING
- EACL
- IJCAI

### 요구되는 contribution

- budget-aware / state-conditioned reasoning path selection
- heterogeneous path pool construction
- verifier/reranker 또는 stopping policy 중 최소 하나의 선명한 add-on
- compute-accuracy tradeoff와 failure mode 분석

## 5. Extension paper

- verifier/reranker, strategy-card, compute-accuracy tradeoff가 강해지면 `ACL / EMNLP / NAACL / AAAI`를 다시 노린다.
- retrieval/ranking/evidence-grounded reasoning이 중심이 되면 `SIGIR / KDD / WSDM / CIKM / WWW`를 조건부로 고려한다.
- 단, mainline이 그쪽으로 실제 이동하기 전에는 target venue를 섣불리 바꾸지 않는다.

## 6. NFM bridge paper

- 우선은 NLP/AI venue에서 domain reasoning application으로 가져간다.
- network venue는 `TeleLogs / RCA / operation / measurement / system contribution`이 강해졌을 때만 고려한다.
- immediate NFM bridge는 `TeleMath` 중심으로 제한한다.
- `TeleTables`, `TeleLogs`는 second-phase candidate다.

## 7. 정보과학회 2024 S/A 목록 기준 target venue 전략

- core S급 main target:
  `ACL / EMNLP / NAACL / AAAI`
- stretch S급:
  `ICLR / ICML / NeurIPS`
- realistic A급 fallback:
  `ACL Findings / EMNLP Findings / NAACL Findings / COLING / EACL / IJCAI`
- conditional target:
  `SIGIR / KDD / WSDM / CIKM / WWW`
- NFM-only conditional target:
  `INFOCOM / CoNEXT / NSDI / SIGCOMM / IMC / NOMS / ICNP / PAM / WiOpt`

## 8. 분기별 마일스톤

### 2026 Q3

- related work / positioning / title 방향 고정
- P0 논문 읽기와 review stub 정리
- main experiment question을 1개로 압축
- held-out selection protocol 확정

### 2026 Q4

- benchmark와 baseline을 줄여 메인 테이블 고정
- main contribution을 `path selection + TTC allocation`으로 선명하게 유지
- 첫 top-tier submission 시도

### 2027 Q1

- reviewer-risk가 큰 선행연구 대응 보강
- verifier/reranker 또는 stronger held-out generalization extension 진행

### 2027 Q2

- extension paper 또는 bridge paper 제출
- NFM는 이 시점에도 `TeleMath` 중심으로만 유지

### 2027 Q3-Q4

- accepted / under-review paper를 dissertation chapter로 정리
- 필요하면 compromise venue 또는 domestic/industry-aligned output 추가

## 9. 실패 방지용 scope control

- `CG`, verifier, NFM, ranking, retrieval, tool use를 한 번에 다 열지 않는다.
- rStar-Math 재현이나 full PRM 재구현을 immediate next action으로 두지 않는다.
- 첫 논문 단계에서 NFM benchmark를 여러 개 섞지 않는다.
- main novelty를 `CG`로 되돌리지 않는다.

## 10. blunt recommendation

가장 현실적인 전략은 아래와 같다.

1. thesis core는 math reasoning + TTC/path selection으로 고정한다.
2. 첫 논문은 math mainline으로 간다.
3. 두 번째 논문은 verifier/path-pool extension 또는 stronger generalization으로 간다.
4. NFM는 `TeleMath` 중심의 small bridge로만 붙인다.
5. network venue는 실제 system contribution이 생기기 전까지 secondary concern으로 둔다.

## 11. 한 줄 결론

2026-2027 전략의 핵심은 **math mainline에서 top-tier 수준의 첫 논문을 만든 뒤, 같은 umbrella 안에서 extension과 selective NFM bridge를 차례로 붙이는 것**이다.
