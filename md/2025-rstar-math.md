# rStar-Math review stub

## 메타데이터

- 제목: rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking
- 연도: 2025
- venue / status: ICML 2025
- 링크: https://proceedings.mlr.press/v267/guan25f.html
- 코드: https://github.com/microsoft/rStar
- 상태: `stub`

## 한 줄 요약

- small math SLM에 `MCTS + process preference model + self-evolution`을 결합해 frontier급 성능을 만든 heavy search 계열 논문이다.

## 왜 중요한가

- 현재 small-model math frontier를 설명할 때 빠질 수 없는 기준점이다.
- 우리가 왜 raw frontier race 대신 lightweight TTC/path selection 쪽으로 가야 하는지 보여 준다.

## 우리 연구와의 관계

- 직접 baseline이라기보다 contrastive positioning에 가깝다.
- 공통점은 math reasoning과 test-time reasoning orchestration을 본다는 점이다.
- 차이점은 우리는 massive self-evolution이 아니라 제한된 TTC 안의 lightweight path/strategy allocation을 다룬다는 점이다.

## 빌릴 점

- introduction에서 frontier reference로 사용
- search-heavy line과의 차이를 설명하는 related work 문구
- `policy model / verifier / search`를 분리해서 보는 framing

## 하면 안 되는 주장

- 우리 방법이 rStar-Math보다 강하다고 말하면 안 된다.
- MCTS/self-evolution novelty를 우리가 처음 하는 것처럼 쓰면 안 된다.

## target venue 관점에서의 의미

- ACL/EMNLP/NAACL/AAAI mainline 논문화 시, 가장 큰 novelty risk 중 하나다.
- ICLR/ICML/NeurIPS stretch를 노릴 때는 이 논문과의 차별화가 훨씬 더 선명해야 한다.

## 아직 확인할 질문

- PPM의 실제 lightweight 대체 가능 요소는 무엇인가
- main gain이 MCTS인지 self-evolution인지 synthetic data 규모인지
- 우리 논문에서 어느 정도까지 비교/언급하면 충분한지
