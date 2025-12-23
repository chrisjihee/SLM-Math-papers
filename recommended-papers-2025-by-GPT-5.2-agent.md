ChatGPT의 말:
좋습니다. Structured Rationale Distillation, Test-time Scaling, Model Merging, Math Reasoning & Knowledge Graph 관련해서 2023~2025년 주요 학회 및 arXiv에서 총합 10~15편의 최신 논문을 선별하여 소개드리겠습니다.

각 논문은 제시하신 출력 형식에 맞춰 핵심 아이디어, 연구와의 연관성, 구현 팁과 함께 정리해드릴게요. 결과가 준비되는 동안 계속 대화하셔도 괜찮습니다!


- title: "Skip-Thinking: Chunk-wise Chain-of-Thought Distillation Enable Smaller Language Models to Reason Better and Faster"
  venue: "EMNLP 2025"
  link: "https://aclanthology.org/2025.emnlp-main.610/"
  idea: "제안된 **Skip-Thinking** 기법에서는 긴 추론 과정을 내부적으로 여러 의미 단위로 나누어(Step를 **청크** 단위로 분할) 작은 모델이 한 번에 한 청크씩 학습하도록 합니다:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}. 이를 통해 불필요한 부분 문장을 학습하지 않아 **핵심 추론 토큰**에 대한 학습 비중을 높이고, 추론 중간 단계는 건너뛰며(**skip-thinking**) 답을 바로 예측해 **추론 속도**도 향상시킵니다:contentReference[oaicite:2]{index=2}."
  relevance: "LLM 교사로부터 생성된 장문의 CoT를 SLM이 그대로 학습하면 잡음과 장기 의존성으로 **추론 논리 학습에 어려움**이 있다는 문제를 해결합니다:contentReference[oaicite:3]{index=3}. 청크 단위 학습으로 작은 모델(3B~8B)이 **필수 추론 논리**를 효과적으로 익혀 성능을 높였고, 답안을 얻을 때 **불필요한 단계 생략**으로 응답 시간이 단축되어 RQ1과 RQ2에 모두 부합합니다:contentReference[oaicite:4]{index=4}."
  tips: "논문 **Figure 1**에 제시된 청크 분할 및 학습 과정, **Figure 3**의 결과에서 청크 개수 증가에 따른 **성능-속도 균형**을 참고하세요:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}. 구현 시 **섹션 3**의 청크 분할 알고리즘과 **섹션 4**의 추론 시 Skip 조건을 확인하면 도움이 됩니다."

- title: "Distilling LLM Agent into Small Models with Retrieval and Code Tools"
  venue: "NeurIPS 2025 (Spotlight)"
  link: "https://arxiv.org/abs/2505.17612"
  idea: "**Agent Distillation** 프레임워크로 대형 LLM 에이전트의 **전체 문제해결 행동**(복잡한 CoT + Tool 사용)을 소형 SLM에 이식합니다:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}. 교사 LLM에는 `first-thought prefix` 프롬프트로 **고품질 실행 추론 예시**를 생성하게 하고, 학생은 **자기일관적 행동 생성(Self-Consistent Action Generation)**으로 추론 단계의 신뢰도를 높였습니다:contentReference[oaicite:9]{index=9}. 그 결과 0.5B~3B급 SLM이 단순 CoT 증류로 미세조정한 상위 모델(1.5B, 3B, 7B) 수준의 **경쟁력 있는 성능**을 보였습니다:contentReference[oaicite:10]{index=10}."
  relevance: "도구 활용까지 포함한 복잡한 **추론 추상화**를 소형 모델에 주입하여 SLM의 문제해결 범위를 확장한 연구입니다. CoT만 증류했을 때 나타나는 **희소 지식/계산 한계**(hallucination)를 보완하고, Self-Consistency 기법을 test-time이 아닌 **학습 과정**에 적용해 작은 모델의 **추론 안정성**을 높였다는 점에서 RQ1과 RQ2 모두에 시사점을 줍니다:contentReference[oaicite:11]{index=11}:contentReference[oaicite:12]{index=12}."
  tips: "교사 LLM의 **trajectory** 샘플 질을 높이는 `first-thought prefix` 기법과, 학생의 **액션 검증을 통한 추론 견고화** 방식을 참고하세요:contentReference[oaicite:13]{index=13}. 구현 시 논문 **Section 4**의 프롬프트 설계 및 **Section 5**의 Self-Consistency 활용 방법, 그리고 저자 제공 GitHub 리소스를 확인하면 유용합니다."

- title: "UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation"
  venue: "ICLR 2025"
  link: "https://openreview.net/forum?id=HJY_fJieOJ"
  idea: "**체인, 트리, 그래프** 등 다양한 형태의 중간 추론과정을 하나의 **통합 포맷(UniCoT)**으로 변환하여 LLM 교사의 지식을 SLM에 전달하는 방법을 제시합니다:contentReference[oaicite:14]{index=14}. LLM이 답과 함께 **정확한 설명**을 반복적으로 생성하도록 프롬프트하여 다단계 구조화된 rationale을 만들고, 학생은 이에 대해 **통합 지도 학습 + 구조 일치 학습(Structural Consistency)**을 수행해 **내부 표현까지 구조를 반영**하도록 합니다:contentReference[oaicite:15]{index=15}."
  relevance: "RQ1의 핵심인 **서술형 CoT vs 구조화된 표현** 비교에 직접 응답하는 연구입니다. 다양한 형태의 추론 과정을 활용해 SLM의 성능을 **여러 태스크 전반에서 향상**시켰으며, 특히 **환각 감소**와 **합리적 추론** 정합성을 동시에 잡았습니다:contentReference[oaicite:16]{index=16}:contentReference[oaicite:17]{index=17}. 이는 작은 모델일수록 **구조적인 피드백**이 학습에 유리함을 시사합니다."
  tips: "논문에서 제시하는 **iterative prompting** 기법으로 LLM이 구조적 rationale을 생성하는 방식을 참고하세요. 또 **Section 3**의 Unified CoT 구성 및 **Section 4**의 Structural Consistency 손실 정의를 보면, 서로 다른 구조의 정보를 학생 모델에 주입하는 구현 세부를 얻을 수 있습니다. (코드는 공개됨:contentReference[oaicite:18]{index=18}.)"

- title: "Towards Efficient CoT Distillation: Self-Guided Rationale Selector for Better Performance with Fewer Rationales"
  venue: "EMNLP 2025 (Findings)"
  link: "https://aclanthology.org/2025.findings-emnlp.413/"
  idea: "대형 LLM 교사가 만든 CoT 중 **노이즈가 적고 유용한 소수의 rationales**만 선별하여 증류 효율을 높이는 **MoRSD** 기법을 소개합니다:contentReference[oaicite:19]{index=19}. 학생 모델이 **자신의 정답률로 rationale 품질을 평가**하는 **자체 평가지표(Rationale Difficulty)**를 도입하고, 정밀도(Accuracy), 다양성(Diversity), 난이도(Difficulty)를 충족하는 소수의 rationale만 학습에 사용해 **7개 데이터셋 평균 +4.6%** 성능 향상을 달성했습니다:contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21}."
  relevance: "많은 양의 CoT 데이터보다 **엄선된 양질의 CoT**가 SLM 성능 향상에 더 효과적임을 보였습니다:contentReference[oaicite:22]{index=22}. 이는 소형 모델 증류 시 **데이터 효율성**이 관건이라는 점을 부각하며, RQ1의 관점에서 구조화된 중간표현의 **품질 관리**가 학습 효과를 좌우함을 시사합니다."
  tips: "논문 **Figure 2**에 교사가 생성한 rationales를 **학생 모델 평가지표**로 걸러내는 4단계 파이프라인이 그려져 있습니다:contentReference[oaicite:23]{index=23}. **Section 3**의 Rationale Difficulty 계산법과 Accuracy/Diversity 필터 설계를 참조하면, 자체 점검을 통해 학생에 맞춘 데이터 선택을 구현할 수 있습니다."

- title: "Soft Self-Consistency Improves Language Models Agents"
  venue: "ACL 2024 (Short)"
  link: "https://aclanthology.org/2024.acl-short.28/"
  idea: "기존 Self-Consistency(SC)의 **과반수 득표** 방식 대신, 생성된 각 후보 답안의 **확률값(신뢰도)**로 가중치를 주어 투표하는 **Soft Self-Consistency (SOFT-SC)**를 제안합니다:contentReference[oaicite:24]{index=24}. 답안 분포가 넓거나 행동 시퀀스가 긴 **복잡한 작업**에서 소수의 샘플로도 높은 성능을 내며, 동일 샘플 수 대비 SC보다 **1~6%p 정확도 향상**을 이뤘습니다:contentReference[oaicite:25]{index=25}. 특히 장기 멀티스텝 문제에서 SOFT-SC는 SC 대비 **절반 이하 샘플**로 동등 성능을 달성했습니다:contentReference[oaicite:26]{index=26}."
  relevance: "이는 **SLM의 추론 신뢰도**를 활용해 test-time 투표 효율을 극대화한 방법으로, RQ2의 ‘가장 비용 효율적인 추론 스케일링’에 부합합니다. 후보 개수가 적을 때도 효과가 크므로, 대형 모델보다 샘플 생성 비용 대비 성능향상이 중요한 **소형 모델 추론**에 유용합니다:contentReference[oaicite:27]{index=27}."
  tips: "모델이 출력한 log-likelihood로 **confidence score**를 계산해 가중 투표하는 구현을 참고하세요. 논문 수식에 제시된 **연속형 스코어 계산 방식**과, Bash 실행/웹 쇼핑 등 **사례 연구**(Table 1)에 나타난 성능 개선폭을 보면 SOFT-SC의 실전 적용 이점을 파악할 수 있습니다."

- title: "Boosting the Power of Small Multimodal Reasoning Models to Match Larger Models with Self-Consistency Training"
  venue: "ECCV 2024"
  link: "https://arxiv.org/abs/2311.14109"
  idea: "대형 모델의 성능을 작은 모델에서 달성하기 위해, **학습 단계**에서 Self-Consistency 아이디어를 도입한 **MC-CoT** 방법을 제안합니다:contentReference[oaicite:28]{index=28}. 하나의 입력에 대해 학생이 **여러 개의 rationale과 답안을 생성**하고, 교사가 이를 **투표로 정답 선택**하여 피드백으로 사용함으로써, 학생이 **고품질 추론 경로**를 학습하도록 유도합니다:contentReference[oaicite:29]{index=29}. 이 방식으로 작은 Vision+Language 모델이 훨씬 큰 모델에 필적하는 **강력한 추론 성능**을 보였으며, rationale의 정확도가 향상되고 답안의 **견고성**도 증가했습니다:contentReference[oaicite:30]{index=30}:contentReference[oaicite:31]{index=31}."
  relevance: "SLM을 여러 번 돌려 성능을 높이는 **test-time SC**를 **train-time**으로 끌어와서, 작은 모델도 **다회 추론**의 이점을 학습 내재화하여 큰 모델 1회 추론에 맞먹는 성능을 얻었습니다. 이는 RQ2의 **SLM × N회 vs LLM × 1회 break-even** 관점에서, 학습 기법으로 그 격차를 좁힌 흥미로운 사례입니다."
  tips: "모델 학습 시 한 질문당 다중 해결 경로를 생성하는 **Algorithm 1**을 참고하세요. 또한 **코드 공개**되어 있으므로:contentReference[oaicite:32]{index=32}, self-consistency training 구현 시 해당 저장소의 데이터 생성 및 투표 절차를 확인하면 좋습니다."

- title: "General Purpose Verification for Chain of Thought Prompting"
  venue: "arXiv 2024 (under review)"
  link: "https://arxiv.org/abs/2405.00204"
  idea: "LLM 스스로 자신의 추론 과정을 **검증자(Verifier)**로 활용하여 잘못된 추론 단계를 걸러내는 방법입니다. 구체적으로, 각 추론 스텝에 대해 **관련성**, **수리적 정확성**, **논리적 일관성** 세 가지 원칙을 정의하고, 해당 조건을 만족하는지 모델에게 검사시킵니다:contentReference[oaicite:33]{index=33}. 추가로 **퍼플렉서티(난이도)** 기준 검증을 병행하여 **여러 CoT 경로 중 최적 해답**을 선택했으며, 그 결과 일반적인 생성보다 항상 성능이 향상되었고, 9개 데이터셋 중 6개에서 **best-of-N(최소 퍼플렉시티 경로)**보다도 성능이 우수했습니다:contentReference[oaicite:34]{index=34}:contentReference[oaicite:35]{index=35}."
  relevance: "추론 과정 자체를 평가하는 **Process-based Verifier**를 활용해 LLM의 출력 신뢰성을 높이는 접근으로, RQ2에서 언급한 **Verifier/Reward Model을 통한 후보 선택**에 해당합니다. 특히 이 방법은 **여러 후보 중 다수결**에 의존하기보다, **한 번의 검증 패스**로 잘못된 경로를 제거해 작은 모델에서도 효율적인 추론 성능 향상을 기대할 수 있습니다."
  tips: "제시된 세 가지 **검증 기준**은 실제 구현 시 프롬프트로 활용 가능합니다 (예: '이 단계의 계산이 정확한가?' 등을 LLM에게 질의). 또한 논문에서 **perplexity 기반 최종 선택**을 사용하였는데, 이는 OpenAI API 등 **black-box 모델**에도 적용 가능하므로, 모델 점수가 없는 경우 **언어모델의 확률값**으로 후보를 rerank하는 아이디어를 응용할 수 있습니다."

- title: "Beyond the First Error: Process Reward Models for Reflective Mathematical Reasoning"
  venue: "EMNLP 2025 (Findings)"
  link: "https://aclanthology.org/2025.findings-emnlp.253/"
  idea: "기존 **Outcome Reward Model (ORM)**이 최종 답만 맞히면 보상을 주는 반면, **Process Reward Model (PRM)**은 추론 **각 단계의 정확성**을 평가해 세밀한 피드백을 제공할 수 있습니다:contentReference[oaicite:36]{index=36}. 본 논문에서는 수학 장문 문제에서 LLM이 **잘못된 부분을 스스로 수정**하기도 한다는 점에 착안해, 첫 오답 이후에도 올바른 추론이 이어질 수 있음을 반영하는 **Error Propagation/Cessation** 규칙으로 PRM 학습 데이터를 자동 구축했습니다:contentReference[oaicite:37]{index=37}:contentReference[oaicite:38]{index=38}. 약 170만 개의 단계별 평가 데이터를 LLM으로 레이블링해 7B 규모 PRM을 학습시킨 결과, 기존 ORMs 및 공개 PRM들을 뛰어넘는 **솔루션 선택 및 단계 평가 성능**을 보였습니다:contentReference[oaicite:39]{index=39}:contentReference[oaicite:40]{index=40}."
  relevance: "수학 추론에서 **과정 기반 평가**(PRM)가 **결과만 평가**하는 ORM보다 효과적이라는 것을 실증하여 RQ2의 취지에 부합합니다. PRM을 활용하면 SLM이 여러 단계로 이뤄진 풀이 중 **정확한 경로를 식별**하고 잘못된 계산 경로를 배제하는 데 활용할 수 있어, Self-Consistency나 Tree-of-Thought 탐색 시 **효율적인 후보 축소**가 가능합니다."
  tips: "PRM을 실제 활용하려면, 논문의 **데이터 구성 방법(Section 4)**을 참고해 유사하게 **자동 채점 데이터**를 만들 수 있습니다. 또한, PRM으로 Best-of-N 답안을 고를 때뿐 아니라, **단계별 탐색**에 점진적 피드백을 주는 방법(논문 제안 metric)을 적용하면 SLM의 긴 이유열 출력에도 **부분 점검**을 수행할 수 있습니다."

- title: "LoRA Soups: Merging LoRAs for Practical Skill Composition Tasks"
  venue: "COLING 2025 (Industry Track)"
  link: "https://aclanthology.org/2025.coling-industry.55/"
  idea: "각기 다른 **스킬/태스크**에 대해 훈련된 LoRA 어댑터들을 조합하여, 복합 태스크에 필요한 능력을 모두 갖춘 **합성 모델**을 만드는 기법을 연구합니다:contentReference[oaicite:41]{index=41}. 제안하는 **CAT (Concatenation of LoRAs)** 방식은 여러 LoRA의 가중치를 **학습을 통해 최적 조합**하는 것으로, 단순 가중치 평균이나 데이터 재미세조정보다 훨씬 뛰어난 성능을 보였습니다. 예를 들어 **수학 단어 문제 + 코드 실행** 복합 태스크에서 기존 병합 기법 대비 **43%p 높은 정확도**를 달성했습니다:contentReference[oaicite:42]{index=42}."
  relevance: "서로 다른 추론 스타일이나 영역 전문 지식을 가진 Adapter들을 병합할 때 **최적 가중치로 합산**하면 **능력이 상호 보완**됨을 보였다는 점에서 RQ3에 해당합니다. 특히 CAT 방법은 TIES, DARE 등의 선행 연구보다 일관되게 우수하여, Adapter 병합 시 발생하는 **성능 간섭** 문제를 최소화하는 방안으로 활용될 수 있습니다:contentReference[oaicite:43]{index=43}."
  tips: "논문에서는 **이질적인 LoRA 간의 레이어별 가중치 조정**을 학습시키는데, Appendix의 수식과 **Figure 1**의 CAT vs 기존 방법 비교 그림을 참고하면 구현에 도움이 됩니다. 또한 **Section 5**의 테이블에서 다양한 스킬 조합 실험 결과와 **LoRA 가중치 학습 스케줄**을 제공하니, 실제 모델 병합 전에 예상 개선폭을 가늠할 수 있습니다."

- title: "Graph of Thoughts: Solving Elaborate Problems with Large Language Models"
  venue: "AAAI 2024"
  link: "https://arxiv.org/abs/2308.09687"
  idea: "기존 Chain-of-Thought이나 Tree-of-Thought을 확장하여, LLM이 생성하는 정보를 임의의 **그래프** 구조로 표현하는 **Graph-of-Thought (GoT)** 프레임워크를 제안합니다. 각 중간 생성 단위를 노드로, **아이디어 간 의존 관계**를 엣지로 연결함으로써, 여러 경로의 부분 해법을 **병합**하거나 **피드백 루프**로 개선할 수 있습니다:contentReference[oaicite:44]{index=44}. 이러한 그래프적 사고를 통해 정렬 문제 등에서 기존 ToT 대비 **정확도 62% 향상, 비용 31% 절감** 등의 성과를 보였으며, 새로운 변환 규칙(생각 확장 방식) 추가에도 유연합니다:contentReference[oaicite:45]{index=45}."
  relevance: "LLM의 **복잡 문제 해결**을 인간처럼 **네트워크형 사고**에 가깝게 구현한 것으로, RQ4의 그래프 구조 통합 및 RQ2의 추론 최적화 모두와 연관됩니다. 특히 작은 모델의 경우도, Graph-of-Thought 개념을 적용하면 **다양한 경로 탐색 후 통합**하는 방식으로 1회 대형 모델 추론 이상의 성능을 낼 **단서 제공**을 받을 수 있습니다."
  tips: "Graph-of-Thought은 **프롬프트 전략**으로도 구현 가능하며, 저자들이 공개한 예시는 알고리즘 문제 해결에 응용되었습니다. 논문의 **알고리즘 1** 및 **Fig. 2**를 보면, LLM이 스스로 그래프를 형성하며 탐색하는 절차가 단계별로 나와 있으니 이를 참고해보세요:contentReference[oaicite:46]{index=46}. 또한, GoT에서 언급된 **생각 결합 및 정제(distillation)** 절차는 추론 엔진을 설계할 때 흥미로운 아이디어로 활용될 수 있습니다."

- title: "Self-attention-based Graph-of-Thought for Math Problem Solving"
  venue: "ACL 2025 (Findings)"
  link: "https://aclanthology.org/2025.findings-acl.317/"
  idea: "수학 문제에서 인간이 머릿속에 개념들의 **관계 그래프**를 그리며 추론하는 것에 착안해, LLM의 디코딩 과정 자체를 **그래프 형태**로 바꾸는 **SaGoT** 기법을 제안합니다:contentReference[oaicite:47]{index=47}:contentReference[oaicite:48]{index=48}. Transformer 내부의 self-attention을 변형하여, 각 단계의 **이전 단계 참조 여부**를 토글함으로써 모델이 **필요한 노드만 이어주는** 그래프식 추론을 수행합니다. 추가 훈련 없이 작은 LLM에도 적용 가능한 decoding 기법으로, 수학 추론 정확도가 향상되었고 불필요한 간섭이 감소하여 **작은 모델도 복잡한 prompt를 이해**하는 데 도움을 주었습니다:contentReference[oaicite:49]{index=49}."
  relevance: "Chain-of-Thought의 **선형 구조 한계**(앞뒤 단steps 간 간섭)를 극복하기 위한 것으로, RQ1의 **구조적 중간표현 우수성**을 보여줍니다. 특히 수학 문제처럼 단계별로 분기/합류가 필요한 경우, 작은 모델도 SaGoT를 통해 **그래프형 내부 추론**을 수행하면 성능이 개선될 수 있음을 입증하여 RQ4(수학 추론+그래프 활용)에 부합합니다:contentReference[oaicite:50]{index=50}:contentReference[oaicite:51]{index=51}."
  tips: "SaGoT는 모델의 **내부 Attention 제어**를 필요로 하므로 바로 구현 난도가 있지만, 아이디어 차용은 가능합니다. 예를 들어, 하나의 프롬프트에서 여러 질의(노드)를 한꺼번에 생성하고, 이를 참조해 다음 스텝을 발전시키는 방식으로 **그래프적 추론흐름**을 흉내낼 수 있습니다. 논문 **Figure 1(b)**의 사례(모래껍질 셈 문제)를 보면 SaGoT가 어떻게 단계별로 관계를 맺는지 시각화되어 있으니 개념 이해에 활용하세요."
