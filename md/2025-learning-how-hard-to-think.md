# Learning How Hard to Think review stub

## 메타데이터

- 제목: Learning How Hard to Think: Input-Adaptive Allocation of LM Computation
- 연도: 2025
- venue / status: ICLR 2025 Poster
- 링크: https://openreview.net/forum?id=6qUUgw9bAZ
- 상태: `stub`

## 한 줄 요약

- 입력마다 필요한 계산량이 다르다는 가정 아래 test-time compute를 적응적으로 배정하는 input-adaptive allocation 논문이다.

## 왜 중요한가

- adaptive TTC 자체는 새롭지 않다는 가장 직접적인 근거다.
- 우리 problem statement와 매우 가깝다.

## 우리 연구와의 관계

- method inspiration이자 strong novelty risk다.
- 우리는 단순 budget allocation이 아니라 path-family/strategy-level allocation으로 차별화해야 한다.

## 빌릴 점

- input-adaptive compute framing
- fixed-budget vs adaptive-budget 비교 프레임
- allocation policy vocabulary

## 하면 안 되는 주장

- adaptive TTC를 우리가 처음 문제화했다는 주장
- compute allocation 자체를 novelty의 핵심으로만 두는 주장

## target venue 관점에서의 의미

- ICLR/ICML/NeurIPS stretch를 생각하면 반드시 정면 대응해야 하는 선행연구다.
- ACL/EMNLP/NAACL/AAAI에서도 framing risk가 큰 편이다.

## 아직 확인할 질문

- 이 논문의 allocation unit과 우리 strategy-level action space를 어떻게 정확히 구분할지
- stopping policy와 route-family policy를 어느 수준에서 통합할지
