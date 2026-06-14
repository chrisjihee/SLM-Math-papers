# s1 review stub

## 메타데이터

- 제목: s1: Simple test-time scaling
- 연도: 2025
- venue / status: EMNLP 2025
- 링크: https://aclanthology.org/2025.emnlp-main.1025/
- 코드: https://github.com/simplescaling/s1
- 상태: `stub`

## 한 줄 요약

- 복잡한 search 없이도 long-thinking과 budget forcing만으로 강한 test-time scaling을 만들 수 있음을 보인 simple TTC baseline이다.

## 왜 중요한가

- "복잡한 router 없이도 gain이 난다"는 가장 직접적인 반례다.
- 우리 연구가 꼭 지나가야 하는 baseline이다.

## 우리 연구와의 관계

- direct TTC baseline이다.
- 우리는 single-family long thinking이 아니라 heterogeneous path family selection으로 차별화해야 한다.

## 빌릴 점

- minimal TTC baseline framing
- compute-forcing/length-forcing discussion
- simple but strong baseline 설계 원칙

## 하면 안 되는 주장

- 단순 long-thinking baseline이 주는 이득을 우리의 고유 novelty로 착각하면 안 된다.

## target venue 관점에서의 의미

- ACL/EMNLP/NAACL/AAAI mainline에서 반드시 비교해야 할 TTC baseline이다.
- ICLR/ICML/NeurIPS stretch를 노릴 때는 `왜 simple long-thinking보다 heterogeneous routing이 필요한가`를 더 강하게 보여 줘야 한다.

## 아직 확인할 질문

- `budget forcing`를 우리 route-family framing과 어떻게 정합적으로 비교할지
- simple TTC baseline을 어느 budget까지 포함할지
