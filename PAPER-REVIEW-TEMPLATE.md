# 논문 리뷰 템플릿

## 1. 메타데이터

- 제목:
- 저자:
- 연도:
- venue / status:
- 링크:
- 코드 / 데이터:
- 읽은 날짜:
- 상태: `unread | skimming | read | summarized | implemented | baseline`

## 2. 한 줄 요약

- 이 논문은 무엇을 하며, 왜 중요한가:

## 3. 문제 설정

- 어떤 task를 푸는가:
- 입력/출력은 무엇인가:
- main benchmark는 무엇인가:
- online inference 문제인가, train-time 문제인가:

## 4. 방법

- 핵심 아이디어:
- 모델/파이프라인 개요:
- supervision source:
- training recipe:

## 5. test-time compute 관점

- compute를 늘리는 단위는 무엇인가:
- sample 수 / reasoning length / search depth / tool use / model routing 중 무엇을 제어하는가:
- stopping이 있는가:
- budget-aware policy가 있는가:

## 6. reasoning path family 관점

- path family:
- homogeneous pool인가, heterogeneous pool인가:
- path 선택 시점:
  - reasoning 전
  - reasoning 중
  - candidate 생성 후
- selection unit:
  - sample
  - answer
  - rationale
  - step
  - strategy
  - model
  - tool

## 7. verifier / search / routing 관점

- verifier를 쓰는가:
- verifier 종류:
  - outcome
  - process
  - preference
  - generative
  - schema
  - evidence
- search를 쓰는가:
  - none
  - best-of-n
  - tree
  - mcts
  - reflection
- reranker / router / policy model이 있는가:

## 8. 평가 설정

- 모델 크기:
- 데이터 규모:
- 벤치마크:
- 메트릭:
- cost/latency 보고 여부:

## 9. 핵심 결과

- 대표 수치:
- strongest baseline 대비 개선:
- 무엇이 실제로 main gain을 만들었는가:

## 10. 우리 연구와의 관계

- 직접 baseline인가:
- 상한선 참고인가:
- method inspiration인가:
- contrastive positioning인가:

## 11. 빌려올 것

- 아이디어:
- 실험 디자인:
- 지표:
- ablation 방식:

## 12. 우리가 하면 안 되는 주장

- 이 논문 앞에서 약해지는 주장:
- novelty가 겹치는 주장:
- 표현상 주의점:

## 13. 구현 아이디어

- 우리 코드베이스에 바로 옮길 수 있는 것:
- low-cost pilot 가능 여부:
- heavy experiment가 필요한지:

## 14. math mainline 관련성

- `GSM8K/GSM8K-kor/MATH`와의 직접 관련성:
- TTC/path selection과의 관련성:
- 메인 논문에서 인용할 위치:

## 15. NFM bridge 관련성

- `TeleMath`:
- `TeleTables`:
- `TeleLogs`:
- bridge paper에서 쓸 수 있는지:

## 16. 남는 질문

- 아직 이해 안 된 점:
- 더 확인할 표/부록:
- follow-up으로 읽을 논문:
