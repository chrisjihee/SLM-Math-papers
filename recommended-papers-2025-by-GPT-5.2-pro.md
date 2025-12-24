```yaml
- title: "Symbolic Chain-of-Thought Distillation: Small Models Can Also \"Think\" Step-by-Step"
  venue: "ACL 2023"
  link: "https://arxiv.org/abs/2306.14050"
  idea: "대형 교사(teacher)가 생성한 다양한 CoT rationalization을 샘플링해 데이터로 만들고, 학생(student)이 이를 생성·답변하도록 학습(SCoTD)해 125M~1.3B급에서도 step-by-step 추론 이득을 끌어냅니다."
  relevance: "RQ1(서술형 CoT의 데이터 효율) 관점에서 '많이 샘플링한 CoT를 증류하면 작은 모델에서도 CoT가 작동'한다는 강한 근거입니다. 또한 CoT 샘플의 '다양성/선택 기준/샘플 수'가 성능을 좌우한다는 분석은 CG/ RP 증류에서도 그대로 적용 가능합니다."
  tips: "교사 CoT를 k개 이상 다중 샘플링→(필요 시) 필터링/선택→SFT 파이프라인을 그대로 복제해보세요. 특히 '샘플 수(k)·다양성·교사 확률'의 trade-off를 다룬 실험/분석 파트를 집중적으로 보시면 좋습니다."

- title: "Learning to Maximize Mutual Information for Chain-of-Thought Distillation"
  venue: "Findings of ACL 2024"
  link: "https://aclanthology.org/2024.findings-acl.577/"
  idea: "학생이 '정답'과 'CoT(추론 과정)'을 함께 학습할 때, 두 과제 사이의 결합을 약하게 두면 CoT가 단순 장식이 되기 쉬운데, 이를 보완하기 위해 Mutual Information(MI) 기반 목표를 넣어 CoT 학습이 실제 정답 예측에 기여하도록 만듭니다."
  relevance: "RQ1에서 CoT를 auxiliary loss로 둘 때 '어떻게 결합시키면 데이터 효율이 좋아지는가'에 대한 힌트를 줍니다. CG/JSON 같은 구조화 표현을 auxiliary head로 두는 경우에도 MI/정보병목류 결합을 그대로 응용할 수 있습니다."
  tips: "목표함수(정답 loss + CoT loss + MI 항) 정의/추정 방식과 ablation(각 항 제거/가중치 변화)을 그대로 재현해보세요. CG 버전이라면 '정답↔그래프' 간 MI를 최대화하는 변형을 설계하기 좋습니다."

- title: "Teaching Small Language Models Reasoning through Counterfactual Distillation"
  venue: "EMNLP 2024"
  link: "https://aclanthology.org/2024.emnlp-main.333/"
  idea: "기존 CoT 증류가 OOD에서 약하고 CoT 다양성이 부족하다는 문제를 겨냥해, (1) 입력은 유사하지만 라벨이 바뀌는 counterfactual 데이터를 LLM으로 생성하고, (2) multi-view CoT로 reasoning 샘플 다양성을 늘려 SLM의 견고성을 높입니다."
  relevance: "RQ1에서 '같은 데이터 예산으로 더 많은 학습 신호를 뽑는' 전형적인 데이터 효율 트릭입니다(특히 OOD 강건성). CG 증류에서도 counterfactual(관계/엣지 일부만 바꾼 그래프) 생성으로 '관계 민감도'를 학습시키는 설계가 가능합니다."
  tips: "counterfactual 생성 규칙(입력 유사도 유지 + 라벨 전환)과 multi-view CoT 생성/필터링 파이프라인을 그대로 가져오되, 그래프 표현이라면 '엣지/관계 최소 변경' 제약을 추가해보세요. OOD 실험 설정을 함께 복제하면 효과를 빨리 확인할 수 있습니다."

- title: "Distilling Mathematical Reasoning Capabilities into Small Language Models"
  venue: "arXiv (2024)"
  link: "https://arxiv.org/abs/2401.11864"
  idea: "수학 추론을 자연어 CoT로만 증류하지 않고, 방정식 형태로 중간표현을 만드는 Equation-of-Thought Distillation(EoTD)를 제안하며, CoT·PoT·EoT 등을 섞어 더 다양한 사고흐름을 제공하는 Ensemble Thoughts Distillation(ETD)로 SLM 수학 성능을 끌어올립니다."
  relevance: "RQ1의 '서술형 vs 구조화(수식/그래프) 표현' 비교에 딱 맞는 레퍼런스입니다. 특히 중간표현을 더 '검증 가능/정규화'된 형태(수식, 트리플, 그래프)로 만들면 학습 효율이 좋아질 수 있다는 실증 근거로 쓰기 좋습니다."
  tips: "EoT(수식 기반) 표현 정의와 ETD(여러 thought 타입 혼합) 데이터셋 구성 절차를 그대로 재현해보세요. CG 증류에서도 '정규화된 그래프 스키마'를 먼저 고정해 ETD처럼 다양한 reasoning 스타일(CoT/CG/RP)을 혼합하는 실험을 설계하기 좋습니다."

- title: "Distilling Structured Rationales from Large Language Models to Small Language Models for Abstractive Summarization"
  venue: "AAAI 2025"
  link: "https://doi.org/10.1609/aaai.v39i24.34727"
  idea: "LLM이 생성한 구조화 rationale(예: 핵심 측면/근거 문장/삼중(triple) 관계 등)를 ‘다단계 평가+선별’로 정제해 SLM 학습에 쓰는 프레임워크를 제안합니다(Structured Rationale-guided 학습)."
  relevance: "당신의 핵심 주제(Structured Rationale Distillation, JSON/Triple/Graph 증류)와 거의 정면으로 겹칩니다. 특히 '구조화 rationale을 그대로 넣되, 품질 평가/선별을 붙여 데이터 효율을 높이는' 설계는 CG 증류에서 매우 실용적입니다."
  tips: "구조화 rationale 스키마(무엇을 필드로 두는지)와 '선별/게이팅/멀티뷰 결합' 아이디어를 CG 증류 파이프라인에 이식해보세요. 구현 관점에서는 (1) rationale 생성, (2) 평가/필터링, (3) student 학습(멀티태스크/게이팅) 3단계로 분리해 재현하는 게 깔끔합니다."

- title: "Let’s Verify Step by Step"
  venue: "ICLR 2024"
  link: "https://arxiv.org/abs/2305.20050"
  idea: "최종 정답(outcome)만 평가하는 ORM과 달리, 중간 과정(process) 단계별 피드백을 주는 process supervision이 수학 추론에서 더 효과적임을 실험적으로 보이고, 대규모 step-level 피드백 데이터(PRM800K)를 공개합니다."
  relevance: "RQ2(Verifier/PRM vs ORM)와 직접 연결됩니다. SLM에서도 '후보 생성기(generator) + 과정 검증기(PRM)' 조합이 test-time scaling의 핵심이므로, PRM 설계/데이터 수집·활용의 기준점으로 쓰기 좋습니다."
  tips: "PRM800K 같은 step-level 라벨을 직접 구축하기 어렵다면, 논문에서 강조하는 'active learning로 process supervision 효율을 높이는' 관점을 참고해 라벨링 비용을 줄이는 설계를 해보세요(예: 불확실 step만 라벨)."

- title: "Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving"
  venue: "arXiv (2024)"
  link: "https://arxiv.org/abs/2408.00724"
  idea: "추론 시 계산량(FLOPs) 예산을 고정했을 때, (모델 크기, 샘플링/투표, best-of-N, 트리서치 등) 다양한 inference 전략의 비용-성능 곡선을 대규모로 비교해 compute-optimal 조합을 찾고, 작은 모델+고급 inference가 더 좋은 구간이 있음을 보입니다."
  relevance: "RQ2의 break-even point를 ‘실제로 계산 예산 기준’으로 정의/실험하는 데 가장 바로 쓰기 좋습니다. 특히 7B급이 34B급보다 같은 FLOPs 예산에서 유리한 구간이 있다는 관찰은 SLM test-time scaling의 정당화를 강화합니다."
  tips: "논문 TOC 기준으로 Section 3(Compute-Optimal Inference 정의/전략) + Section 4(실험 설정, 모델/리워드모델, FLOPs 계산) + Appendix(하이퍼파라미터)을 그대로 따라가면 재현이 쉽습니다. 당신의 세팅에서는 generator=SLM(3B~8B), verifier=작은 RM 또는 규칙 기반으로 대체해 동일한 곡선을 그려보세요."

- title: "Small Language Models Need Strong Verifiers to Self-Correct Reasoning"
  venue: "arXiv (2024)"
  link: "https://arxiv.org/abs/2404.17140"
  idea: "SLM이 스스로 오류를 고치는(self-correction) 능력을 갖추려면, 단순 자기반성 프롬프트보다 ‘강한 검증 신호(정답/정답해설 기반의 critique)’로 self-correction 데이터를 만들고 이를 SFT하는 파이프라인이 중요하다고 주장합니다."
  relevance: "RQ2에서 'SLM × N회 추론 + 선택'을 할 때, 선택기의 품질(Verifier)이 성능을 좌우한다는 메시지입니다. 작은 verifier(또는 룰/정답검증기)를 따로 키우는 방향이 비용 효율적일 수 있습니다."
  tips: "핵심은 (1) 틀린 풀이에 대해 정답을 이용해 critique 생성, (2) critique 필터링, (3) refinement SFT입니다. 당신의 수학 세팅에서는 ‘최종 답 검증(계산/단위/식 일관성)’을 자동화해 필터링 단계 품질을 올리는 게 효율적입니다."

- title: "s1: Simple test-time scaling"
  venue: "EMNLP 2025"
  link: "https://aclanthology.org/2025.emnlp-main.1025/"
  idea: "1k 규모의 s1K(문제-추론트레이스)로 SFT한 뒤, 생성 도중 강제로 더 ‘생각’을 하게 만드는 budget forcing(예: \"Wait\"를 덧붙여 reasoning을 연장/또는 조기 종료)로 test-time compute를 제어해 성능을 끌어올립니다."
  relevance: "RQ2에서 '정교한 verifier 없이도' test-time compute를 늘려 이득을 얻는 가장 단순한 베이스라인으로 좋습니다. SLM에서도 token-budget을 강제로 늘려 self-check를 유도하는 방식은 구현이 매우 쉽고, 비용 대비 효과를 빠르게 측정할 수 있습니다."
  tips: "s1K 구성 기준(난이도/다양성/품질)과 budget forcing 구현(종료 방지/연장 규칙)을 그대로 실험해보세요. SLM(3B~8B)에서는 ‘연장 토큰 수’와 ‘정답률 상승’의 한계효용 곡선을 먼저 그려 break-even 분석에 바로 연결하는 게 좋습니다."

- title: "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning"
  venue: "ICLR 2025 Spotlight"
  link: "https://openreview.net/forum?id=A6Y7AqlzLW"
  idea: "PRM을 자동 라벨로 키울 때 성능이 제한적이었던 이유를 분석하고, 각 step의 보상을 '정답으로 갈 가능성이 얼마나 진전(progress)했는가'로 정의해 process advantage verifier(PAV)를 학습·활용하는 방법을 제안합니다."
  relevance: "RQ2의 PRM vs ORM 논의에서 한 단계 더 나아가, 사람 라벨 없이도(또는 적게) process verifier를 스케일하는 설계 원리를 제공합니다. 특히 search/RL과 결합할 때 compute 효율이 중요하므로, SLM 기반 test-time search 설계에 직접 연결됩니다."
  tips: "‘progress’ 정의(보상 설계)와 prover policy(베이스와 다른 정책) 설정이 핵심입니다. 당신의 경우 prover를 더 큰 LLM로 두고, SLM generator의 search(예: beam/MCTS)에서 PAV로 가지치기하는 형태로 바로 실험해볼 수 있습니다."

- title: "Process Reward Models That Think"
  venue: "arXiv (2025)"
  link: "https://arxiv.org/abs/2504.16828"
  idea: "단계별 라벨이 많이 필요한 기존 PRM 대신, 검증 자체를 '긴 CoT 생성'으로 수행하는 생성형 PRM(THINKPRM)을 제안해, PRM800K의 극히 일부 라벨(예: 1%)로도 강한 검증 성능과 test-time scaling 효과를 냅니다."
  relevance: "RQ2에서 가장 실용적인 포인트는 'PRM 라벨 비용'입니다. 당신이 SLM에 verifier를 붙일 때, 작은 데이터로도 강해지는 생성형 verifier 설계는 비용 효율을 크게 바꿀 수 있습니다."
  tips: "Figure 1(데이터 효율/서치 성능 비교)와 best-of-N 선택 및 reward-guided search 설정을 그대로 따라가 보세요. 특히 '동일 token budget에서 verifier compute를 어떻게 스케일할지' 비교하는 실험 설정이 break-even 분석에 유용합니다."

- title: "LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition"
  venue: "COLM 2024"
  link: "https://arxiv.org/abs/2307.13269"
  idea: "여러 태스크로 학습된 LoRA 모듈들을 ‘가중치 조합’으로 합성하고, 소수 예시로 그 가중치를 gradient-free로 조정해 보지 못한 태스크에 빠르게 적응하는 LoRA 조합 프레임워크를 제안합니다."
  relevance: "RQ3(서로 다른 추론 스타일/어댑터 병합)에서, ‘LoRA들을 그냥 평균내지 않고 태스크별로 조합 가중치를 학습’하는 아이디어를 제공합니다. CoT/CG 스타일 LoRA를 모듈 풀로 만들고, 소수 검증 샘플로 조합을 학습하는 실험을 설계하기 좋습니다."
  tips: "핵심은 (1) LoRA 후보 풀 구성, (2) Compose(가중치로 합성), (3) Adapt(gradient-free로 w 최적화) 3단계입니다. 당신의 세팅에서는 작은 dev-set(수학/다교과)으로 w를 맞추는 방식이 깔끔합니다."

- title: "LoRA Soups: Merging LoRAs for Practical Skill Composition Tasks"
  venue: "COLING 2025 Industry Track (arXiv 2024)"
  link: "https://arxiv.org/abs/2410.13025"
  idea: "타깃 태스크 데이터가 없거나 적을 때, 여러 LoRA(각각 단일 스킬 학습)를 합쳐 스킬 합성을 수행하는 setting을 체계화하고, LoRA concatenation(CAT) 기반 병합이 기존 모델/데이터 병합보다 유리함을 보입니다."
  relevance: "RQ3에서 '서로 다른 추론 스타일 LoRA를 합치면 능력이 합산되는가'를 실험적으로 다루는 데 매우 좋은 레퍼런스입니다. 특히 수학 MWP 같은 복합 스킬 태스크를 스킬 조합 관점으로 재정의할 때 바로 쓸 수 있습니다."
  tips: "CAT(LoRA 가중/결합 방식)과 '모델 병합 vs 데이터 믹싱' 비교 프로토콜을 그대로 가져와 CoT-LoRA, CG-LoRA, Verifier-LoRA 조합을 비교해보세요. 타깃 데이터가 부족할수록 병합의 강점이 드러나는지 확인하는 구성이 좋습니다."

- title: "Understand, Solve and Translate: Bridging the Multilingual Mathematical Reasoning Gap"
  venue: "arXiv (2025)"
  link: "https://arxiv.org/abs/2501.02448"
  idea: "영-한 수학 병렬 벤치마크 HRM8K(8,011문항)를 제안하고, 한국어에서의 성능 격차가 ‘추론 능력’보다 ‘비영어 입력 이해’ 문제에서 비롯된다는 분석을 바탕으로, 영어를 앵커로 활용하는 UST(Understand→Solve→Translate) 학습을 제안합니다."
  relevance: "당신의 GSM8k-kor/다국어 수학 추론 연구에 바로 꽂힙니다. 특히 ‘한국어 성능 하락 원인이 무엇인가’를 실증적으로 분해해주므로, CG 증류가 어느 부분(이해 vs 추론)에 도움을 주는지 분석 설계에 유용합니다."
  tips: "HRM8K 데이터 구성(병렬/이중언어)과 UST 파이프라인(영어 앵커 추론 후 번역)을 그대로 베이스라인으로 두고, CG/RP 증류가 UST의 어느 단계(Understand/Solve/Translate)를 개선하는지 모듈별 ablation을 권합니다."

- title: "Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models"
  venue: "ICML 2025"
  link: "https://arxiv.org/abs/2410.13080"
  idea: "KG 기반 추론에서 환각을 줄이기 위해 KG 구조를 디코딩에 직접 통합하는 graph-constrained reasoning(GCR)을 제안하며, KG-Trie로 KG 추론 경로를 인덱싱해 디코딩을 제약(constrained decoding)함으로써 ‘KG에 근거한 경로’만 생성하도록 만듭니다."
  relevance: "RQ1의 ‘구조화 표현(그래프)을 중간표현으로 쓰는 것’뿐 아니라, RQ2에서 verifier 없이도 ‘검색 공간을 구조로 제한’해 추론 효율/신뢰성을 올리는 접근입니다. 또한 lightweight KG-specialized LLM을 쓰는 설정은 SLM 연구와 잘 맞습니다."
  tips: "핵심 구현은 KG-Trie(경로 인덱싱) + constrained decoding 입니다. 당신의 Concept Graph 증류에서도, 그래프 스키마가 정해져 있다면 ‘허용되는 엣지 전이만 디코딩’하도록 제약을 넣는 방식으로 바로 응용 가능하고, 환각(잘못된 관계 생성) 감소를 정량화하기 좋습니다."
```

### 각 항목의 1차 출처(위 YAML 순서대로)

1. SCoTD
2. MI 기반 CoT Distillation
3. Counterfactual Distillation
4. EoTD/ETD 수학 증류
5. AAAI 2025 Structured Rationale Distillation(요약)
6. Let’s Verify Step by Step (ICLR 2024, PRM800K/Process vs Outcome)
7. Inference Scaling Laws (compute-optimal, best-of-N/투표/트리서치, 작은 모델 우위 구간)
8. s1: Simple test-time scaling (s1K + budget forcing)
9. Strong Verifiers for SLM Self-Correction
10. Rewarding Progress (ICLR 2025 Spotlight, PAV/progress)
11. Process Reward Models That Think (THINKPRM, 저라벨 PRM)
12. LoraHub (COLM 2024)
13. LoRA Soups (CAT, COLING 2025 Industry track)
14. HRM8K + UST (Korean bilingual math benchmark)
15. Graph-constrained Reasoning (KG-Trie constrained decoding, ICML 2025)
