# MUST-READ PLAN

Last updated: 2026-06-14

이 문서는 **지금 당장 읽어야 하는 논문만 압축한 canonical shortlist**다. 자세한 큐는 [READING-QUEUE-202606.md](READING-QUEUE-202606.md)를 본다.

## 운영 원칙

- 메인라인은 math reasoning이다.
- `CG`는 여러 path family 중 하나다.
- 첫 관련연구 묶음은 `math frontier -> TTC/SC -> strategy selection -> verifier -> structured reasoning -> NFM bridge` 순으로 읽는다.
- NFM는 bridge domain이므로, mainline 관련 논문을 읽고 난 뒤에 붙인다.

## P0 묶음 A: Math SLM frontier

1. rStar-Math — ICML 2025
   https://proceedings.mlr.press/v267/guan25f.html
   왜: 현재 strongest small-model math frontier reference.

2. DeepSeekMath — arXiv 2024
   https://arxiv.org/abs/2402.03300
   왜: strong math pretraining + RL + SC baseline.

3. s1: Simple test-time scaling — EMNLP 2025
   https://aclanthology.org/2025.emnlp-main.1025/
   왜: simplest TTC baseline.

4. DeepSeek-R1 — arXiv 2025
   https://arxiv.org/abs/2501.12948
   왜: reasoning RL 계열 positioning.

## P0 묶음 B: Self-consistency와 TTC

5. Self-Consistency — ICLR 2023
   https://openreview.net/forum?id=1PL1NIMMrw
   왜: 모든 sampling-based reasoning의 기본선.

6. Reasoning-Aware Self-Consistency — NAACL 2025
   https://aclanthology.org/2025.naacl-long.184/
   왜: rationale-aware SC와 early stopping.

7. Confidence Improves Self-Consistency in LLMs — ACL 2025 Findings
   https://aclanthology.org/2025.findings-acl.1030/
   왜: confidence-weighted vote baseline.

8. Learning How Hard to Think — ICLR 2025
   https://openreview.net/forum?id=6qUUgw9bAZ
   왜: input-adaptive compute allocation framing.

9. Scaling LLM Test-Time Compute Optimally — ICLR 2025
   https://openreview.net/forum?id=4FWAwZtd2n
   왜: compute-optimal TTC framing.

## P0 묶음 C: Reasoning path pool / strategy selection

10. Self-Discover — official paper page
    https://openreview.net/forum?id=BROvXhmzYK
    왜: reasoning structure composition reference.

11. Automatic Model Selection with Large Language Models for Reasoning — EMNLP 2023 Findings
    https://aclanthology.org/2023.findings-emnlp.55/
    왜: CoT vs PAL routing reference.

12. ToRA — arXiv 2023
    https://arxiv.org/abs/2309.17452
    왜: tool-assisted path family reference.

## P0 묶음 D: Verifier / PRM / reranker

13. Let's Verify Step by Step — ICLR 2024
    https://openreview.net/forum?id=v8L0pN6EOi
    왜: process supervision canonical paper.

14. Math-Shepherd — ACL 2024
    https://aclanthology.org/2024.acl-long.510/
    왜: automatic process supervision reference.

15. Process Reward Models That Think — arXiv 2025
    https://arxiv.org/abs/2504.16828
    왜: generative PRM reference.

16. Training Verifiers to Solve Math Word Problems — arXiv 2021
    https://arxiv.org/abs/2110.14168
    왜: verifier-first math reasoning classic.

## P1 묶음: Structured / graph reasoning

17. UniCoTT — ICLR 2025
    https://openreview.net/forum?id=3baOKeI2EU

18. MAGDi — ICLR 2025 Spotlight
    https://openreview.net/forum?id=ffLblkoCw8

19. InstructGraph — ACL 2024 Findings
    https://aclanthology.org/2024.findings-acl.801/

20. Think-on-Graph — arXiv 2023
    https://arxiv.org/abs/2307.07697

메모:
- 이 묶음은 "CG가 최고"를 입증하기 위한 것이 아니라, **structured family를 얼마나 중립적으로 설명할지** 정리하기 위한 것이다.

## P1 묶음: Search / reflection / RL

21. Tree of Thoughts — arXiv / NeurIPS-era reference
    https://arxiv.org/abs/2305.10601

22. RAP — official paper page
    https://openreview.net/forum?id=VTWWvYtF1R

23. ReST-MCTS* — arXiv 2024
    https://arxiv.org/abs/2406.03816

24. Reflexion — official paper page
    https://openreview.net/forum?id=vAElhFcKW6

메모:
- 이 묶음은 mainline 재현 대상이 아니라, "우리는 어디까지 하지 않는가"를 정리하는 데 필요하다.

## P1 묶음: NFM bridge

25. TeleMath — arXiv 2025
    https://arxiv.org/abs/2506.10674

26. TeleTables — dataset page
    https://huggingface.co/datasets/netop/TeleTables

27. TeleLogs — dataset page
    https://huggingface.co/datasets/netop/TeleLogs

28. TeleQnA — arXiv 2023
    https://arxiv.org/abs/2310.15051

29. ORAN-Bench-13K — arXiv 2024
    https://arxiv.org/abs/2407.06245

30. ORANSight-2.0 — arXiv 2025
    https://arxiv.org/abs/2503.05200

## 실제 읽기 순서 추천

### Week 1

- Self-Consistency
- RASC
- Learning How Hard to Think
- Scaling LLM TTC Optimally

### Week 2

- rStar-Math
- DeepSeekMath
- s1
- DeepSeek-R1

### Week 3

- Let's Verify Step by Step
- Math-Shepherd
- ThinkPRM
- Self-Discover

### Week 4

- Auto Model Selection
- UniCoTT
- MAGDi
- TeleMath

## immediate takeaway

현재 가장 먼저 읽어야 할 것은 `CG` 논문이 아니라,

1. `SC/TTC allocation`
2. `math frontier`
3. `strategy selection`
4. `verifier`

다. `CG`/graph 계열은 그 다음에 읽어도 늦지 않다.
