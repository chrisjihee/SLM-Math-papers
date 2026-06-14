# NFM BRIDGE PLAN

## 1. 기본 원칙

- NFM은 박사논문 main thesis replacement가 아니다.
- NFM은 **math mainline에서 만든 TTC/path selection 아이디어를 제한적으로 옮겨 보는 selective bridge**다.
- immediate bridge candidate는 `TeleMath` 하나로 제한한다.
- `TeleTables`, `TeleLogs`는 second-phase candidate다.
- `TeleYAML`은 structured-output evaluation이 명확해지기 전까지 future work다.
- `TeleQnA / ORANBench`는 domain QA baseline으로는 유용하지만 thesis novelty로는 약하다.

## 2. 왜 bridge가 필요한가

현재 SLM-Math의 중심 질문은 특정 rationale 포맷의 승부가 아니라, **제한된 테스트타임 계산량 안에서 어떤 reasoning path를 더 쓸지 결정하는 문제**다. 이 framing은 telecom domain에도 옮길 수 있지만, 처음부터 넓게 펼치면 mainline이 흔들린다.

그래서 bridge는 아래처럼 아주 좁게 잡는다.

- 먼저 `TeleMath`에서 math mainline과 가장 가까운 형태의 path-family 비교만 한다.
- 그 다음에야 `TeleTables`, `TeleLogs`를 second-phase로 검토한다.

## 3. NFM task scope control

| NFM task | 지금 사용할지 | 이유 | 주의점 |
|---|---|---|---|
| TeleMath | 예 | math mainline과 가장 직접적으로 연결되는 immediate bridge candidate | main paper를 대체하지 말 것 |
| TeleTables | 아직 아님 | structured/table reasoning으로는 유망하지만 task form이 이미 달라진다 | table interpretation novelty를 별도 contribution처럼 부풀리지 말 것 |
| TeleLogs | 아직 아님 | verifier/RCA 관점에서는 흥미롭지만 telecom-specific adaptation 부담이 크다 | thesis core가 RCA로 이동하지 않게 주의 |
| TeleYAML / Intent-to-Recipe | 아니오 | evaluation contract가 아직 불안정하다 | structured-output novelty를 섣불리 주장하지 말 것 |
| TeleQnA | 제한적 참고만 | retrieval anchor나 domain QA sanity check로는 유용하다 | thesis novelty로는 약함 |
| ORANBench / ORAN-Bench-13K | 제한적 참고만 | domain QA baseline으로는 유용하다 | reasoning path selection 연구와 직접 연결은 약함 |
| srsRANBench | 나중 | code/system 이해가 섞여 scope가 커진다 | mainline에서 멀어짐 |

## 4. immediate bridge story

현재 가장 작은 bridge story는 아래 정도가 적절하다.

> telecom mathematical reasoning에서도 하나의 universal prompting recipe가 정답이 아니며, direct / CoT / PoT / RAG-like path family의 utility가 문제 유형에 따라 다르고, lightweight strategy selection이 성능-비용 tradeoff를 개선할 수 있다.

이 스토리는 math mainline과 정합적이고, 불필요하게 network-systems claim으로 커지지 않는다.

## 5. 하지 말아야 할 것

- 박사 thesis를 telecom-only thesis로 바꾸지 않는다.
- Open Telco benchmark 전부를 한 번에 다루지 않는다.
- 첫 단계에서 heavy NFM training부터 열지 않는다.
- `TeleTables + TeleLogs + TeleYAML + TeleQnA + ORANBench`를 한 논문에 묶지 않는다.
- 처음부터 `SIGCOMM / NSDI / INFOCOM / CoNEXT`를 main target으로 놓지 않는다.

## 6. venue 전략

- 우선은 `ACL / EMNLP / NAACL / AAAI` 같은 NLP/AI venue에서 domain reasoning application으로 붙이는 것이 안전하다.
- `IJCAI`, `COLING`, `Findings`는 realistic fallback이 될 수 있다.
- network venue는 실제 network operations / measurement / system contribution이 생겼을 때만 고려한다.

## 7. 추천 순서

1. `TeleMath` baseline comparison
2. math mainline에서 path-family selection story가 선명해진 뒤 bridge 초안 작성
3. 필요하면 `TeleTables` 또는 `TeleLogs` 중 하나만 second-phase로 확장

## 8. 한 줄 결론

NFM는 **TeleMath 중심의 좁은 bridge/application**으로만 운영하고, `TeleTables`와 `TeleLogs`는 후속 단계로 미루는 것이 현재 박사과정 전략상 가장 안전하다.
