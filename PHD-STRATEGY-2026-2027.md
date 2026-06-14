# PHD STRATEGY 2026-2027

## 1. 현재 상태

현재 SLM-Math는 다음 세 가지 자산을 이미 갖고 있다.

- Axis 1: CoT vs CG 직접 비교와 fair comparison evidence
- Axis 2: SC / Static / Adaptive MoR evidence
- Axis 1-next: sequential TTC router / oracle / heuristic / reranker/listwise scaffold

즉, thesis core는 아직 "새로운 teacher 데이터 생성"보다 **문제별 reasoning path selection과 TTC allocation**에 더 가깝다.

## 2. 지도교수님이 사실상 요구하는 목표

- AAAI / NAACL / ACL 급 top-tier를 진지하게 시도할 것
- 안 되면 현실적인 compromise path를 준비할 것
- 내년까지 top-tier 수준 논문 2편 안팎을 dissertation backbone으로 만들 것

## 3. 추천 umbrella thesis

> Efficient and Reliable Reasoning Path Selection for Small Language Models

이 umbrella 아래에 math mainline과 NFM bridge를 함께 넣을 수 있다.

## 4. 추천 paper tracks

### Track 1. Main paper

- 주제:
  math reasoning, TTC allocation, heterogeneous path pool, route/strategy reranker

- 핵심 질문:
  어떤 reasoning path family를 어떤 문제에 얼마나 배정할 것인가

- 우선 벤치마크:
  `GSM8K-kor`, `GSM8K`, 가능하면 `MATH500`

### Track 2. Extension paper

- 주제:
  verifier-guided selection, path-pool construction, stronger held-out selection

- 가능 방향:
  `MATH/MATH500` 확장, verifier 결합, tool-assisted family 추가

### Track 3. Application / bridge paper

- 주제:
  `TeleMath`, `TeleTables`, `TeleLogs`에서 reasoning strategy selection

- 원칙:
  math mainline이 선행이고, NFM는 selective application으로 둔다.

## 5. 분기별 마일스톤

### 2026 Q3

- related work / positioning 완성
- current mainline claim 정제
- held-out selector / reranker line 정리
- 최소 1개 paper outline 완성

### 2026 Q4

- math main paper 실험 고정
- main benchmark table + ablation + case study 완성
- 1차 top-tier 제출 시도

### 2027 Q1

- reviewer-risk가 큰 부분 보강
- verifier/path-pool extension 또는 stronger generalization paper 준비

### 2027 Q2

- 2번째 top-tier-level paper 제출
- NFM bridge는 이 시점에 small but crisp하게 정리

### 2027 Q3-Q4

- accepted / under-review paper들을 dissertation chapter로 정리
- 부족하면 bridge paper 또는 journal/transactions compromise path 준비

## 6. minimum viable top-tier submission package

- clear research question
- strong related work positioning
- `GSM8K/GSM8K-kor + MATH/MATH500` 또는 동등한 setup
- 가능하면 multiple model sizes
- strong baselines
- path family ablation
- compute-accuracy tradeoff
- error analysis
- case studies
- reproducible code/data description

## 7. 리스크 관리

### scope creep

- path family, verifier, NFM, multimodal, merging을 동시에 다 열지 않는다.

### too much CG emphasis

- current evidence상 main message는 CG superiority가 아니다.

### weak novelty vs rStar / search / verifier papers

- heavy search를 따라가려 하지 말고 lightweight orchestration으로 차별화한다.

### too many datasets

- math mainline이 안정되기 전에는 benchmark를 크게 늘리지 않는다.

### unstable agent-generated code

- code path를 넓히기 전에 offline simulator / held-out evaluation을 우선한다.

### NFM workload fragmentation

- NFM는 mainline 이후의 bridge로만 둔다.

## 8. blunt recommendation

가장 현실적인 전략은 아래와 같다.

1. thesis core는 math reasoning + TTC/path selection으로 고정한다.
2. 첫 논문은 math mainline으로 간다.
3. 두 번째 논문은 verifier/path-pool extension 또는 stronger generalization으로 간다.
4. NFM는 `TeleMath -> TeleTables -> TeleLogs` 순서의 carefully scoped bridge로 둔다.
5. NFM가 예상보다 매우 강한 결과를 주지 않는 이상, thesis core를 telecom으로 바꾸지 않는다.

## 9. 한 줄 결론

2026-2027 졸업 전략의 핵심은 **math reasoning 메인라인을 흔들지 않고, TTC/path selection을 중심으로 두 편 수준의 논문화 가능한 축을 만든 뒤, NFM를 application bridge로 제한적으로 붙이는 것**이다.
