# 세분화된 LLM 피드백을 활용한 요약문 평가 모델 학습

---

세분화된 LLM 피드백을 활용한 요약문 평가 모델 학습

오지환◦1, 최정환2, 윤태원2, 민향숙1, 송환준1,2†

한국과학기술원 산업및시스템공학과1	한국과학기술원 데이터사이언스대학원2

{jh.oh, hwani.choi, ytaewon0415, hyangsuk.min, songhwanjun}@kaist.ac.kr

## Training Summary Evaluation Model with Fine-Grained LLM Feedback

Jihwan Oh◦1, Jeonghwan Choi2, Taewon Yun2, Hyangsuk Min1, Hwanjun Song1,2† ISysE KAIST1	GSDS KAIST2

요 약

자동 요약문 평가 모델을 학습하기 위해서는 인간이 라벨링한 대량의 데이터가 필요하지만, 고품질의 요약문 라벨을 대량으로 얻는 것은 많은 비용이 든다. 본 연구에서는 이러한 한계를 극복하기 위해 대형 언어 모델(LLM)이 생성한 피 드백을 활용하는 방법을 탐구한다. 10개의 LLM으로 다양한 요약문을 생성한 후, Llama-3-70B-Instruct를 사용하여 문장 단위로 추론 근거 및 오류 유형이 포함된 LLM 피드백을 생성한다. 적은 계산 비용을 유지하면서 높은 성능을 이끌어내기 위해, 소형 오픈소스 모델인 Llama-3-8B-Instruct를 학습에 사용한다. 실험 결과, LLM이 생성한 대규모 데이터셋으로 학습한 모델이 인간이 라벨링한 소규모 데이터셋으로 학습한 모델보다 높은 성능을 보였다. 요약문 평가 모델 학습에서 LLM 피드백을 활용하는 것이 인간 피드백을 사용하는 것보다 성능 측면에서 더 효과적이고 비용 효율적임을 보였다.

# 서론

최근 대규모 언어 모델(LLM)의 발전은 텍스트 요약 성능을 크 게 향상시켰다[1]. 그러나, 요약문 내 환각(Hallucination) 문제는 여전히 발생하고 있으며, 이로 인해 요약문 사실 검증의 중요성 이 더욱 부각되고 있다[2]. 요약문의 사실성을 사람이 검증하기 위해서는 많은 시간과 비용이 소모된다. 특히 오류 유형 탐지와 설명 가능한 평가와 같은 세분화된 수준의 평가에서는 비용이 더 욱 증가하고 재현성 또한 확보하기 어려운 문제가 있다. 이러한 비용을 줄이기 위해 LLM이 생성한 라벨을 활용한 언어 모델 학 습 방법인 지식 증류(Knowledge distillation)가 대안으로 제시되 고 있다[3, 4]. 그러나 요약문 평가 모델에 세분화된 LLM 피드백 을 적용하여 학습하는 연구는 아직 충분히 탐구되지 않았다.

본 논문에서는 LLM이 생성한 세분화된 피드백을 활용하여 효 율적이고 효과적인 사실 검증 모델을 학습할 수 있는 가능성을 제시한다. 그림 1과 같이, 제안된 파이프라인은 다음 네 단계로 구성된다: (1) 요약문 생성: 10개의 언어 모델을 사용하여 다양 한 요약문을 생성한다. (2) 피드백 생성: 사전 학습된 평가 모델 Llama-3-70B-Instruct을 사용하여 문장 단위의 사실 검증 라벨 및 오류 유형이 포함된 세분화된 LLM 피드백을 FineSurE[5] 프롬 프트를 통해 생성한다. (3) LLM 피드백을 활용한 모델 학습: 생 성된 LLM 피드백을 활용하여 자동 요약문 평가 모델(Llama-3- 8B-Instruct)을 지식 증류[6] 기법으로 미세 조정한다. (4) 추론: 학습된 모델의 성능을 확인하기 위해 문서-요약문 쌍에 대해 생 성된 피드백과 사람 평가와의 일치도를 확인한다.

0) 이 논문은 2024년도 정부(과학기술정보통신부)의 재원으로 정보통신기획평가 원의 지원을 받아 수행된 연구임 (No. RS-2024-00445087, 도메인 특화 자동 가치 연계 평가를 통한 AI 모델 신뢰성 향상). 또한 부분적으로 정부 (과학기술 정보통신부)의 재원으로 한국연구재단의 지원을 받아 수행된 연구임 (No. RS- 2024-00334343).

그림 1: 실험 흐름도

# 관련 연구

요약문 평가 데이터

여러 연구에서 요약문 사실 검증 모델 학습을 위해 인간이 라 벨링한 데이터셋을 수집하였다. SummEval[7]은 크라우드소싱 과 전문가 라벨링을 모두 포함한 종합적인 벤치마크 데이터셋 을 제시한다. 벤치마크 데이터셋의 규모를 확장하려는 연구로 는 AggreFact[8]가 있으며, 기존의 뉴스 도메인의 벤치마크 데 이터셋을 통합하여 대량의 인간 라벨 데이터를 제공한다. 한편, TofuEval[1]은 사실 오류를 다양한 유형으로 분류하고, 문장 단 위의 사실성 평가를 제공하는 더 세분화된 라벨링 프레임워크를 제안한다.

요약문 평가 방법

문서와 요약문 간의 사실적 일관성을 검증하기 위한 다양한 평 가 방법이 연구되었다. FalseSum[9]은 문서 수준의 자연어 추론 (NLI) 예제에 의도적으로 사실적 불일치를 추가하여 평가 모델 을 학습시키는 접근법을 제시한다. QAFactEval[10]은 요약문에 서 정보 단위를 추출하고, 이를 기반으로 질문을 생성하여 일관 성을 검증하는 QA 기반 메트릭이다. 가장 최근 연구들 중에서 는 G-Eval[11] 및 FineSurE[5]와 같이 제로샷(Zero-shot) 추론만 을 활용하는 방법도 있다.

기존 연구와 달리, 본 연구에서는 최신 LLM 모델을 활용하여 사람의 개입 없이 데이터셋을 구축하고, 이를 통해 모델을 학습 시킨다. 이를 통해 LLM 기반의 세분화된 피드백이 요약 평가 성 능 향상시키는 것을 확인한다.

# 방법론

우리는 다양한 입력 맥락에서 일반화할 수 있는 요약 평가 모 델를 학습시키기 위해 LLM 피드백을 포함한 대규모 데이터셋을 구축하였다. 본 데이터셋은 다중 도메인, 다양한 길이 및 두 가지 유형(비대화형, 대화형)을 포함하는 10,877개의 문서로 구성되어 있다. 이러한 원본 문서들은 LLM 피드백을 기반으로 라벨링된 데이터를 생성하여 사실 검증 모델을 학습시키는 데 사용되며, 이는 다음 세 단계로 이루어진다:

요약문 생성

우리는 사실 오류 유형의 다양성을 확보하기 위해 10개의 서 로 다른 LLM을 사용하여 요약을 생성하였으며, 이를 통해 다 양한 분포의 요약을 확보하였다. 사용된 모델로는 Non-LLM (BART-large-CNN, FLAN-T5-large, Pegasus-Large), 오픈 소스 LLM (Phi-2, Llama-2-13B-Chat, Mistral-7B-Instruct, Mixtral-7B- Instruct), 및 상업용 LLM (Claude-Instant, GPT-3.5-Turbo, GPT- 4-Turbo)이 있다.

피드백 생성

LLM을 통해 피드백을 생성할때, 높은 품질의 사실 검증 피드 백을 확보하는 것이 중요하다. 이를 위해 우리는 FineSurE[5]라 는 기존의 LLM 기반 사실 검증기준을 채택하였으며, 이는 다양 한 오류 유형을 식별하고, 각 결정에 대한 근거를 제공한다. 이 때 문장 수준의 사실 검증에서 92.0%의 정확도를 보인 Llama- 3-70B-Instruct을 통해 피드백을 생성하였다. 우리는 “오류 없음 (NoE)”, “외부 지식 오류(OutE)”, “개체 오류(EntE)”, “서술 오

류(PredE)”, “상황 오류(CirE)”, “문법 오류(GramE)”, “연결 오류 (LinkE)”, “참조 오류(CorefE)” 및 “기타 오류(OtherE)”와 같은 아 홉 가지 오류 범주와 이에 대한 판단 근거를 포함하는 피드백을

획득하였다. 결과적으로, 우리는 총 102,640개의 문서-요약 쌍에

대한 LLM 피드백을 학습 데이터로 수집하였다.

LLM 피드백을 활용한 학습

우리는 QLoRA[12]를 사용하여 Llama-3-8B-Instruct를 LLM 피드백이 포함된 학습 데이터셋으로 미세조정하였다. 이때 JSON 형식(예: [“SENTENCE”: “SUMMARY SENTENCE 1”, “REASONING”: “REASON”, “CATEGORY”: “ERROR TYPE”, ...])

으로 출력하도록 설정하였고, 이는 FineSurE[5] 프롬프트를 기반 하여 작성하였다. 우리는 4개의 NVIDIA H100 GPU를 사용하여 Batch size 32, Iteration 8,000 설정으로 학습을 진행하였다.

# 실험

요약문 평가 모델의 성능을 측정하기 위해 다음 세가지 평가 지표를 사용한다: (1) bAcc(Balanced-Accuracy): 문장 단위로 사실 여부를 판단 하도록 하여 인간의 이진(Binary) 피드백으로 구성된 검증 데이터와 비교하여 클래스 불균형을 고려한 일치도

(2) Pearson Correlation: 요약문 단위로 사실 일치도를 계산하 여 예측된 일치도와 검증 데이터에서 계산된 일치도 사이의 피어 슨 상관계수 (3) Rank Correlation: 요약문 생성 모델을 단위로 사실 일치도를 순위로 계산하여 검증 데이터에서 계산된 순위 사 이의 스피어만 순위 상관계수 (Spearman’s rank correlation).


| Method | bAcc | Pearson Corr | Rank Corr |
| --- | --- | --- | --- |
| Zero-shot(Baseline) | 54.7% | 0.246 | 0.663 |
| Human Feedback | 69.8% | 0.534 | 0.684 |
| LLM Feedback(Ours) | 73.4% | 0.625 | 0.865 |


표 1: 피드백 종류에 따른 사실 검증의 성능 비교

표 1은 학습 없이 제로샷(Zero-shot) 추론으로만 요약문을 평가 한 결과(Baseline), 5,853개의 인간 피드백 및 102,640 개의 LLM 피드백을 사용해 모델을 학습한 결과를 나타낸다. 이때 검증 데 이터로는 무작위 추출된 693개의 인간 피드백이 사용되었다. 대 규모 LLM 피드백을 활용한 학습이 소규모의 인간 피드백을 사 용하는 것보다 우수하다는 것을 보여준다. 인간의 이진(Binary) 피드백을 사용하여 미세 조정한 모델은 제로샷 추론에 비해 높 은 성능을 보이지만, LLM 피드백을 통한 학습이 훨씬 큰 성능 향상을 보인다. 또한 대량의 LLM 피드백은 인간 피드백에 비해 비교적 쉽게 획득할 수 있기 때문에, 이는 LLM 피드백의 우수한 실용성과 효율성을 나타낸다.

우리는 LLM 피드백의 세분화 수준을 세 가지 방식으로 조정 하였다: (1) 각 문장이 사실적으로 올바른지 여부를 나타내는 이 진(Binary) 라벨만 사용하는 경우, (2) 프롬프트 엔지니어링의 연 쇄적 사고(Chain-of-thought)와 같은 추론 단계(Reasoning step)


| Setting | bAcc | Pearson Corr | Rank Corr |
| --- | --- | --- | --- |
| Binary Label | 73.0% | 0.628 | 0.649 |
| + Reasoning | 71.9% | 0.628 | 0.825 |
| + Error Localization | 73.4% | 0.625 | 0.865 |


표 2: LLM 기반 사실 검증의 성능을 평가한 소거 실험 결과

를 추가하는 경우 (3) 오류 유형 탐지(Error localization)로 추론 단계를 고도화한 경우. 표 2는 위에서의 세 가지 세분화 수준에 따른 LLM 기반 사실 검증의 성능을 평가하기 위한 소거 실험 결 과이다. 이때 이진(Binary) 피드백만을 사용한 경우는 bAcc가 상 대적으로 높았으나, 순위 상관계수는 가장 낮게 나타났다. 추론 정보를 추가했을 때는 bAcc가 다소 감소했지만, 두 상관계수는 개선되었다. 오류 유형 탐지(Error localization)를 추가했을 때는 추론 정보와의 시너지 효과로 인해 가장 높은 bAcc와 순위 상관 계수를 달성하였다. 따라서, LLM 피드백에 설명 가능한 정보를 추가하여 미세조정을 진행하면 인간과의 일치도가 높아진다는 것을 확인할 수 있다.


| Setting | bAcc | Pearson Corr | Rank Corr |
| --- | --- | --- | --- |
| 100.0% | 73.4% | 0.625 | 0.865 |
| 50.0% | 69.4% | 0.601 | 0.902 |
| 25.0% | 71.6% | 0.588 | 0.787 |
| 12.5% | 68.6% | 0.509 | 0.589 |
| 0.0% | 57.4% | 0.246 | 0.663 |


표 3: LLM 피드백의 규모에 따른 소거 실험

표 3에서 LLM 피드백의 규모 효과를 평가하기 위해, 우리는 미세조정 시 사용되는 학습 데이터의 크기를 변경하여 성능 변화 를 분석하였다. 학습 데이터의 25.0% (총 25,660개의 LLM 피드 백)를 사용한 경우, 5,853개의 인간 피드백을 사용해 미세조정한 모델보다 더 높은 인간과의 일치도를 확보할 수 있었다. 이는 5 개의 LLM 피드백이 1개의 인간 피드백에 대응될 수 있음을 설명 해준다. 또한, LLM 피드백을 사용하여 학습 데이터의 양을 늘 림에 따라 사실 검증 성능이 점진적으로 향상되는 효과를 확인할 수 있었다.

# 결론

본 연구에서는 다양한 도메인의 문서로부터 대규모 LLM 피드 백을 생성하고, 이를 통해 요약문 평가 모델을 효과적으로 미세 조정 할 수 있음을 보인다. 우리는 LLM 피드백의 세분화 수준 및 규모를 고려하여 LLM을 미세조정하는 다양한 전략을 실험하 였다. 그 결과, LLM 피드백을 활용한 미세조정이 인간 피드백의 부족 문제를 해결하고, 자동화된 요약 평가 모델 학습에서 인간 피드백 보다 적은 비용으로 성능을 향상시킬 수 있음을 보였다.

# 참고 문헌

L. Tang, I. Shalyminov, A. W.-m. Wong, J. Burnsky, J. W. Vincent, Y. Yang, S. Singh, S. Feng, H. Song, H. Su, et al., “TofuEval: Evaluating hallucinations of llms on topic- focused dialogue summarization,” in NAACL, 2024.

M. Cao, Y. Dong, and J. C. K. Cheung, “Hallucinated but fac- tual! inspecting the factuality of hallucinations in abstractive summarization,” in ACL, 2022.

S. Wang, Y. Liu, Y. Xu, C. Zhu, and M. Zeng, “Want to reduce labeling cost? gpt-3 can help,” in EMNLP, 2021.

N. Pangakis and S. Wolken, “Knowledge distillation in au- tomated annotation: Supervised text classification with llm- generated training labels,” in NLP+ CSS, 2024.

H. Song, H. Su, I. Shalyminov, J. Cai, and S. Man- sour, “FineSurE: Fine-grained summarization evaluation us- ing llms,” in ACL, 2024.

Y. Kim and A. M. Rush, “Sequence-level knowledge distilla- tion,” in EMNLP, 2016.

A. R. Fabbri, W. Krys´cin´ski, B. McCann, C. Xiong,

R. Socher, and D. Radev, “Summeval: Re-evaluating sum- marization evaluation,” Transactions of the Association for Computational Linguistics, vol. 9, pp. 391–409, 2021.

L. Tang, T. Goyal, A. R. Fabbri, P. Laban, J. Xu, S. Yavuz,

W. Krys´cin´ski, J. F. Rousseau, and G. Durrett, “Understand- ing factual errors in summarization: Errors, summarizers, datasets, error detectors,” in ACL, 2022.

P. Utama, J. Bambrick, N. S. Moosavi, and I. Gurevych, “Falsesum: Generating document-level nli examples for rec- ognizing factual inconsistency in summarization,” in ACL, 2022.

A. R. Fabbri, C.-S. Wu, W. Liu, and C. Xiong, “QAFactEval: Improved qa-based factual consistency evaluation for sum- marization,” in NAACL, 2022.

Y. Liu, B. Deb, M. Teruel, A. Halfaker, D. Radev, and A. Has- san, “On improving summarization factual consistency from natural language feedback,” in ACL, 2023.

T. Dettmers, A. Pagnoni, A. Holtzman, and L. Zettlemoyer, “Qlora: Efficient finetuning of quantized llms,” in NeurIPS, 2024.
