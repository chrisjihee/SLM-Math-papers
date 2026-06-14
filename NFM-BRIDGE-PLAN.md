# NFM BRIDGE PLAN

## 1. 왜 NFM가 현재 연구와 연결되는가

현재 SLM-Math의 핵심은 "수학에서 CG를 증명하기"가 아니라, **문제와 현재 state를 보고 어떤 reasoning path를 더 쓸지 고르는 것**이다. 이 framing은 telecom domain에도 자연스럽게 연결된다.

- `TeleMath`는 domain-specific mathematical reasoning이다.
- `TeleTables`는 table interpretation + structured reasoning이다.
- `TeleLogs`는 root cause analysis(RCA)와 diagnostic reasoning이다.
- `TeleYAML / Intent-to-Recipe`는 schema-constrained planning/output generation으로 이어진다.

즉 NFM는 완전히 다른 thesis가 아니라, **math mainline에서 개발한 path selection / verifier / stopping 아이디어를 다른 high-value reasoning domain으로 옮겨 보는 selective bridge**다.

## 2. 우선순위

1. `TeleMath`
   가장 직접적이다. 현재 math line을 거의 그대로 옮길 수 있다.

2. `TeleTables`
   structured/table reasoning으로 확장하기 좋다.

3. `TeleLogs`
   verifier, RCA consistency, diagnosis path selection으로 연결된다.

4. `TeleYAML / Intent-to-Recipe`
   흥미롭지만 evaluation 설계가 더 어렵다. 초기에 무리해서 넣지 않는다.

5. `TeleQnA / 3GPP TSG`
   retrieval/knowledge anchor로는 유용하지만, thesis 핵심 novelty로는 약하다.

## 3. SLM-Math 개념과 NFM 개념 매핑

### reasoning path family

- math mainline:
  `direct`, `CoT`, `prompt-diverse CoT`, `CG-style structured rationale`, `PoT`

- NFM bridge:
  `direct`, `RAG`, `CoT`, `PoT`, `table-structured prompt`, `log-diagnostic path`, `recipe generation path`

### route-card

- math에서의 route-card는 path family의 성격을 요약한다.
- NFM에서는 이를 `strategy-card`, `tool-card`, `recipe-card`로 확장할 수 있다.

예시:

- TeleMath:
  `direct`, `CoT`, `PoT`, `RAG+CoT`

- TeleTables:
  `direct`, `table-focused extraction`, `table+reasoning`, `retrieval+table selection`

- TeleLogs:
  `direct RCA`, `structured RCA checklist`, `symptom-first diagnosis`, `retrieval-supported diagnosis`

### verifier

- math:
  answer consistency, rationale plausibility, step-level reward

- NFM:
  schema validation, unit validation, evidence faithfulness, RCA consistency, standards-groundedness

### STOP

- math:
  더 샘플링할지 멈출지

- NFM:
  latency/cost/safety-aware stopping, 더 긴 reasoning이나 retrieval이 필요한지 판단

### TTC allocation

- math:
  문제별 route/budget allocation

- NFM:
  task별 reasoning/retrieval/tool budget allocation

## 4. 최소 브리지 실험

핵심 원칙은 **heavy training 없이 평가부터**다.

### Stage 0: 경량 평가 러너

- 내부 작업명은 `NFM-Eval-Harness`로 둔다.
- 초기 구현은 `lm-evaluation-harness` 또는 Open Telco evaluation framework 위에 얇게 얹는 수준으로 충분하다.
- 목적은 "새 모델 개발"이 아니라 **path-family baseline 비교**다.

### Stage 1: benchmark 선택

- `TeleMath`
- `TeleTables`
- `TeleLogs`
- 필요하면 `TeleQnA`를 retrieval anchor로 추가

### Stage 2: baseline 비교

#### TeleMath

- `direct`
- `CoT`
- `RAG+CoT`
- `PoT`

#### TeleTables

- `direct`
- `table-structured prompt`
- `retrieval/table selection`

#### TeleLogs

- `direct RCA`
- `structured diagnostic path`
- `retrieval-supported RCA`

### Stage 3: 무엇을 볼 것인가

- accuracy
- majority-vote gain
- cost/latency proxy
- failure mode
- 어떤 task에서 어떤 path family가 유리한지

## 5. 1차 paper story 후보

NFM 첫 논문은 아래처럼 작아야 한다.

> telecom reasoning tasks에서도 하나의 universal prompting recipe가 정답이 아니며, task type에 따라 direct / CoT / RAG / structured path의 utility가 다르고, lightweight strategy selection이 성능-비용 tradeoff를 개선할 수 있다.

이 메시지는 math mainline과 정합적이다.

## 6. 하지 말아야 할 것

- 박사 thesis를 telecom-only thesis로 바꾸지 않는다.
- Open Telco 전체 benchmark를 한 번에 다 풀려고 하지 않는다.
- GSMA leaderboard alignment 없이 NFM SOTA를 주장하지 않는다.
- math mainline이 안정되기 전에 dataset을 너무 많이 섞지 않는다.
- 첫 단계에서 heavy NFM training부터 열지 않는다.

## 7. 추천 일정

- 1단계:
  `TeleMath` baseline comparison

- 2단계:
  `TeleTables` structured reasoning extension

- 3단계:
  `TeleLogs` verifier/RCA extension

## 8. 한 줄 권고

NFM는 **math TTC/path selection mainline을 유지한 채, task-specific reasoning path selection이 실제 고부가가치 도메인에서도 통하는지 확인하는 selective bridge**로만 운영하는 것이 가장 안전하다.
