# 한국어 대규모언어모델을 활용한 MMR기반 자가생성 In-Context Learning

---

한국어 대규모언어모델을 활용한 MMR기반 자가생성 In-Context Learning

장규식◦1, 나승훈1, 임준호2, 김태형3, 류휘정3, 장두성3

전북대학교1, 한국전자통신연구원2, KT3

## {jks4880, nash}@jbnu.ac.kr1 joonho.lim@etri.re.kr2,{taehyeong 2019.kim, hwijung.ryu, dschang}@kt.com3

Self-Generated In-Context Learning based on MMR Algorithm using Korean LLMs

## Gyu-sik Jang◦1,Seung-Hoon Na1, Joon-Ho Lim2, Tae-Hyeong Kim3, Hwi-Jung Ryu3, Du-Seong Chang3 Jeonbuk National University1, ETRI2, KT3

요 약

대규모 언어 모델에서 In-context learning을 활용한 성능 향상이 이루어지고 있으나, 대부분의 사람들의 사용에 있어서 원하는 답과 관련된 예제를 모델에게 입력으로 주면서 사용하는 경우가 적다. 따라서 사용자가 입력만을 주어도 모델이 스스로 입력에 대한 생성을 하여 새로운 예제를 만들고, 이를 MMR 알고리즘 기반으로 입력과의 언어의 다양성이 높은 예제를 선택하여 하여 모델의 성능을 향상하는 MMR 기반 자가 생성 In-context learning을 제안하고 Baseline과 비교하여 성능 향상을 보였다.

# 서 론

ChatGPT의 등장 이후 다양한 언어 모델들이 사람들의 일상에 서 널리 사용되고 있다. 대다수의 사용자들은 특별한 예제를 제 공하지 않고 단순한 입력만으로 결과를 얻기를 원한다. 그러나 대규모 언어 모델은 많은 연구들을 바탕으로 특정 예제들을 입력 과 같이 제공하면 성능이 향상된다는 것이 알려져 있지만 그렇게 사용하지는 않는다. 이를 보완하기 위해 모델이 사용자의 입력 과 질문을 분석하여 예제를 생성하고 생성된 예제들을 바탕으로 순위 재설정 후 In-context learning을 수행하면, 사용자의 요구에 더욱 정확하게 응답할 수 있을 것이다. 이러한 접근 방식은 모델 의 성능을 더욱 향상시킬 수 있는 잠재력을 가지고 있다.

본 논문에서는 자가 생성 In-context Learning 방식에 MMR(Maximal Marginal Relevance)[1]알고리즘을 적용하 여 샘플을 선택하는 방식을 소개한다. 이 방식은 영어 데이터 셋과 모델에 대해 이미 연구[2, 3]가 진행되었지만, 한국어에는 적용되지 않았으며, 모델이 입력을 바탕으로 새로운 내용을 생성하여 In-context learning을 수행하면 편향된 예제 생성 및 많은 생성 예제가 노이즈가 될 수 있다. 본 논문은 이러한 기존 방식의 문제점을 해결하기 위해 MMR을 활용한 순위 재설정 방식을 적용하여 생성 예제 중 입력 예제와 다른 값을 활용하는 방식으로 개선하며, 기존의 Baseline과 비교했을 때 일부 데이터셋에서 성능 향상을 확인할 수 있었다.

# 관련 연구

언어 모델

자연어 처리 분야에서는 대용량 코퍼스를 활용한 사전학습 방 식으로 훈련된 디코더 기반의 생성 모델들이 다양한 작업에서 뛰 어난 성능을 보여주고 있다[4]. 이와 같은 언어 모델 연구의 흐름 에 따라, 국내에서도 한국어를 대상으로 한 대규모 언어 모델들

도 개발되었으며[5, 6], 이러한 모델들을 기반으로 추가적인 학습 및 연구가 활발히 진행되고 있다. 본 논문에서는 이 중 KULLM v2[7] 모델을 활용하여 실험을 수행하였다.

## In-context learning

In-context learning은 작업에 대한 예제나 시연이 프롬프트와 같이 주어져 미세조정 없이 모델이 새로운 작업을 수행할 수 있 는 방법이다. 이에 대해 더 좋은 방법의 In-context learning을 수 행하기 위한 여러 방법이 연구가 진행되었다. [8]연구는 각 샘플 이 올바른 예측을 도출할 수 있는 예제 구성을 찾아 성능을 극대 화 하는 방법에 대해 연구를 수행하였다. [2]연구는 모델이 입력 에 대해 새로운 예제를 생성해내어 In-context learning을 수행하 는 방법에 대해 연구를 하였다. 자가 생성과 관련된 연구에서는 제로샷보다 나은 성능을 보였다. 본 논문에서는 자가 생성을 통 한 예제를 MMR 알고리즘을 사용한 방법을 바탕으로 한국어 모 델에 적용 및 자가생성 In-context learning을 적용 및 MMR 알고 리즘을 통한 선택 방법을 적용하였다.

# 방법

본 논문에서는 제안 하는 방법은 [2]에서와 같이 대규모 언어 모델이 자가생성을 수행을 진행하되, MMR 알고리즘을 사용하 여 생성해낸 예제 중 다양성이 높은 값을 선택하여 예제로 사용 하게 된다.

입력 형태

제안된 방법에 대해 모델에게 입력에 대한 내용을 각각 분할하

여 다음의 수식(1)과 같이 모델이 생성해낸 예제를 얻는다.

Qgen = f (Q),	Cgen = f (C),	Rgen = f (Q′, C′)	(1)

그림 1: 모델이 생성된 예제들을 MMR 알고리즘을 바탕으로 가장 점수가 높은 예제를 선택 하여 In-context learning을 통해 원래의

테스트 입력에 대한 최종적인 출력을 생성하는 과정

빨간색 : test 입력, 파란색 : 생성된 예제, 초록색 : 생성 예제의 답변, 보라색 : 최종 답변

수식(1)에서 Q는 질문, C는 내용이며 각각 Qgen, Cgen, Rgen는 Q, C를 바탕으로 모델이 생성해낸 답변이다. 이러한 생성 과정 을 그림1과 같다.

MMR을 활용한 re-rank 과정

모델에 의해 생성된 예제들은 입력 값에 매우 가까우며, 그 결 과 예제들이 특정한 값에 편향될 수 있다. 이를 보완하기 위해, 우리는 여러 개의 Qgen, Cgen, Rgen 예제를 생성하고, MMR 알 고리즘(2)을 활용하여 점수가 높은 예제들을 추출하여 In-context learning으로 사용하였다.

모델이 제공한 테스트 입력을 기반으로 생성된 예제들은 동일 한 원본 값에서 파생되었기 때문에, 이들 사이의 관련성은 자연 스럽게 높다. 따라서 MMR 알고리즘을 통해 이러한 예제들 사이 의 다양성이 높은 값을 In-context learning에 사용한다.

MMR = λ × relevance − (1 − λ) × max similarity	(2)

추론 과정

MMR 알고리즘을 통해서 생성된 예제 간의 다양성이 높은 값 을 바탕으로 In-context learning을 하게 된다. 생성된 예제들은 퓨샷 학습과 동일한 방법을 사용하여, 답변은 도출하게 된다. 이 때 퓨샷 학습은 다음 수식(3)과 같다.

p(yi|xtest ) = P C(yi) | T (x1 , y1 ), . . . , T (xk , yk ), T (xtest )

laswag를 사용하였다. 각 데이터셋은 boolq는 주어진 내용과 질 문을 바탕으로 질문의 진위여부를 선택하는 데이터셋이며, Hel- laswag 데이터셋은 내용을 바탕으로 4가지의 선택지중 가장 적 절한 결말을 선택하며 마지막으로 NSMC 감성 분류 평가 데이터 셋[10]를 이용하여 주어진 문장에 대한 감성 분류를 하는 실험을 진행하였다.

실험 설계 언어 모델을 활용하여서 들어온 입력에 대한 예제들 을 만들어 낸 뒤 MMR 알고리즘을 기반으로 다양성이 가장 높 은 값을 선택해 In-context learning을 수행한다. 실험에서는 각각 3,5개를 생성해낸뒤 MMR 알고리즘으로 1,3개를 선택한다. 이 때 MMR의 λ값은 0.5이며, 모든 생성의 temperature 는 1.0으로 하여 실험을 진행하였다.

모델 본 실험에서 사용이 된 모델은 Polyglot-ko[5]을 기반으로 지시 학습을 한 모델인 Kullm v2(5.8b) 모델[7]을 사용하여 진행 하였으며,실험에 사용된 모델은 공개가 되어 있는 한국어 지시학 습이 진행된 모델이다. 본 연구에서는 추가적인 학습을 하지 않 은 채 실험을 진행하였다.

Baseline 본 논문에서의 비교 대상은 제로샷을 이용한 방법 과 퓨샷 학습을 사용하였다. 퓨샷을 진행하는데 있어서 예제를 1,3,5개를 주고 실험을 진행하였으며, 기존의 self-icl 방법과 비교 를 진행하기 위해 3shot, 5shot을 주어 성능을 비교하였다.

i

# 실험

실험 설정

gen

gen

gen

gen

i

(3)

Dataset 본 논문에서는 자가 생성 in-context learning을 평가

하기 위하여kobest[9] 데이터셋을 활용하여 한국어 boolq, hel-

표 1: 제로샷 및 퓨샷에 대한 성능


|  | nsmc | boolq | Hellaswag |
| --- | --- | --- | --- |
| 1self-icl | 0.65 | 0.54 | 0.17 |
| 3self-icl | 0.65 | 0.60 | 0.21 |
| 5self-icl | 0.66 | 0.58 | 0.21 |
| 3gen 1sel (ours) | 0.55 | 0.62 | 0.17 |
| 5gen 3sel (ours) | 0.68 | 0.52 | 0.28 |


표 2: 자가 생성 및 MMR 알고리즘을 통한 선택 시 성능

실험 결과

실험 결과는 표 1 및 2에 요약되어 있습니다. nsmc 및 boolq 데 이터셋에서 제안 방식을 적용하면, 자가생성 예제를 모두 활용하 는 전략과 퓨샷 방식보다 우수한 성능을 보였다. 이 결과는 본 논 문의 방식을 통해 자가 생성된 예제가 입력 데이터와의 관련성이 높아, 랜덤하게 선택된 퓨샷 방식보다 좋은 생성을 할 수 있음을 보여준다. 또한, MMR 알고리즘을 활용하여 생성된 예제 중 문 장 간 다양성이 높은 예제를 선택하여, 성능 향상을 할 수 있음을 보여준다.

반면 Hellaswag 데이터셋의 경우 자가생성을 통한 결과가 제 로샷 및 퓨샷보다 전반적으로 부족한 성능을 보여준다. 이는 해 당 작업이 In-context learning에 대해 약한 모습을 보여주며, 퓨샷 에서 예제 수에 따른 성능 추이에서도 알 수 있다.

그럼에도 불구하고 논문이 제안한 MMR알고리즘을 통해 선 택한 경우 단순히 자가생성을 이용한 in-context learning을 하는 방법보다 높은 점수를 보여주고 있으며, 이는 자가 생성을 통한 퓨샷을 늘림으로써 성능을 향상하던 기존 방법과 달리 MMR알 고리즘을 통한 예제 선택이 모든 예제를 사용할때보다 뛰어남을 보여준다.

# 한계

모델은 자가생성 기능을 통해 예제를 생성한다. 이 과정에서 추가적인 리소스가 필요하며, 대규모의 생성 작업은 상당한 시간 과 연산 리소스를 요구한다. 또한 기존의 논문에서 설명하였던 것과 같은 성능 향상은 본 연구에서는 어려웠으며, 이는 작업의 종류의 차이 및 학습된 모델의 작업에 대한 이해 차이로 인하여 발생한 것으로 보인다.

# 결론 및 향후 연구

자가 생성 방식의 In-context learning 방식을 한국어에 적용하 여 일부 작업에서 제로샷에 비해 성능이 향상 될 수 있음을 보 였으며, MMR알고리즘을 사용하여 예제를 선택함으로써 자가 생성된 예제간 가장 다양성이 높은 형태의 예제를 선택하여 in- context learning을 함으로써 성능이 향상 될 수 있음을 보여준다. 향후 연구는 자가 생성예제를 통한 in-context learning이 제로샷

보다 부족한 데이터셋이 존재함에 따라 분석하고 더 나은 예제 생성 및 검색을 통해 in-context learning을 수행하는 방법론을 향 후 연구하고자 한다.

# 참고 문헌

J. Carbonell and J. Goldstein, “The use of mmr, diversity-based reranking for reordering documents and producing summaries,” in Proceedings of the 21st Annual International ACM SIGIR Confer- ence on Research and Development in Information Retrieval, SIGIR ’98, (New York, NY, USA), p. 335–336, Association for Computing Machinery, 1998.

H. J. Kim, H. Cho, J. Kim, T. Kim, K. M. Yoo, and S. goo Lee, “Self- generated in-context learning: Leveraging auto-regressive language models as a demonstration generator,” 2022.

W.-L. Chen, C.-K. Wu, and H.-H. Chen, “Self-icl: Zero-shot in- context learning with self-generated demonstrations,” 2023.

T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhari- wal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal,

A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh,

D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler,

M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish,

A. Radford, I. Sutskever, and D. Amodei, “Language models are few-shot learners,” 2020.

H. Ko, K. Yang, M. Ryu, T. Choi, S. Yang, jiwung Hyun, and S. Park, “A technical report for polyglot-ko: Open-source large-scale korean language models,” 2023.

L. Junbum, “llama-2-ko-7b (revision 4a9993e),” 2023.

S. Lee, T. Lee, J. Lee, Y. Jang, and H. Lim, “Kullm: Learning to construct korean instruction-following large language models,” in Annual Conference on Human and Language Technology, pp. 196– 202, Human and Language Technology, 2023.

Z. Wu, Y. Wang, J. Ye, and L. Kong, “Self-adaptive in-context learn- ing: An information compression perspective for in-context example selection and ordering,” in Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), (Toronto, Canada), pp. 1423–1436, Association for Com- putational Linguistics, July 2023.

D. Kim, M. Jang, D. S. Kwon, and E. Davis, “Kobest: Korean bal- anced evaluation of significant tasks,” 2022.

L. Park, “Naver sentiment movie corpus,” 2016.
