The Thirty-Seventh AAAI Conference on Artificial Intelligence (AAAI-23)

Learning by Applying: A General Framework for Mathematical Reasoning via Enhancing Explicit Knowledge Learning

Jiayu Liu1, 2, Zhenya Huang1, 2*, Chengxiang Zhai3, Qi Liu1, 2

1Anhui Province Key Laboratory of Big Data Analysis and Application, School of Data Science & School of Computer Science and Technology, University of Science and Technology of China

2State Key Laboratory of Cognitive Intelligence

3University of Illinois at Urbana-Champaign jy251198@mail.ustc.edu.cn, {huangzhy, qiliuql}@ustc.edu.cn, czhai@illinois.edu

Abstract

Mathematical reasoning is one of the crucial abilities of gen- eral artificial intelligence, which requires machines to master mathematical logic and knowledge from solving problems. However, existing approaches are not transparent (thus not interpretable) in terms of what knowledge has been learned and applied in the reasoning process. In this paper, we pro-

pose a general Learning by Applying (LeAp) framework to enhance existing models (backbones) in a principled way by explicit knowledge learning. In LeAp, we perform knowledge learning in a novel problem-knowledge-expression paradigm, with a Knowledge Encoder to acquire knowledge from prob- lem data and a Knowledge Decoder to apply knowledge for expression reasoning. The learned mathematical knowledge, including word-word relations and word-operator relations, forms an explicit knowledge graph, which bridges the knowl- edge “learning” and “applying” organically. Moreover, for problem solving, we design a semantics-enhanced module and a reasoning-enhanced module that apply knowledge to improve the problem comprehension and symbol reasoning abilities of any backbone, respectively. We theoretically prove the superiority of LeAp’s autonomous learning mechanism. Experiments on three real-world datasets show that LeAp im- proves all backbones’ performances, learns accurate knowl- edge, and achieves a more interpretable reasoning process.

Introduction

Mathematical reasoning is one of the core abilities and signs of the intelligence level of general artificial intelli- gence (Zhang, Wang et al. 2020). It requires machines to grasp mathematical knowledge and logical thinking from solving several mathematical problems (Lewkowycz et al. 2022; Seo et al. 2015). Among them, we specifically study math word problems (MWP) in this paper, which is a funda- mental reasoning task that has attracted much attention since the 1960s (Feigenbaum, Feldman et al. 1963). Figure 1 il- lustrates a toy example. Generally, a math word problem is represented as a problem sentence (“Amy has ... have?”) that poses a question requesting an unknown quantity. To solve it, the machine needs to understand the verbal description that contains words (e.g.,“Amy”) and quantities (e.g.,“2”),

*Corresponding Author.

Copyright © 2023, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

Figure 1: Learning and applying knowledge for MWP.

and then reason a mathematical expression (i.e.,“3 ×2 +2”), based on which finally get the answer (i.e.,“8”).

In the literature, traditional MWP solvers include rule- based, statistic-based, and semantics parsing-based (Zhang, Wang et al. 2020). In recent years, sequence to sequence (Seq2Seq) framework has thrived in MWP task (Wang, Liu, and Shi 2017; Lan et al. 2022), following a problem- expression paradigm to translate problems into expressions, where the existing work has focused on improving MWP in two ways, including promoting problem understanding (Lin et al. 2021; Kim et al. 2022) and improving expression rea- soning (Zhang et al. 2020a; Cao et al. 2021). However, such a problem-expression paradigm is still far from encompass- ing human-like mathematical reasoning capacity, because it lacks the processes of learning and applying explicit knowl- edge. On one hand, according to the educational theory of cognitivism (Mowrer 1960; Muhajirah 2020), humans ac- quire explicit mathematical knowledge from solving prob- lems (Liu et al. 2019), e.g., the word “times” is related to the operator “×” and “apples” belongs to “fruits” from the problem in Figure 1. On the other hand, humans produce solutions for MWP by applying this knowledge in logical thinking (Liang et al. 2018). It is necessary to integrate these two processes organically into machines to build a stronger AI (Tsatsou et al. 2021; de Penning et al. 2011).

From this perspective, existing MWP solvers have some room for improvement. First, they ignore the learning pro- cess of explicit knowledge. To be specific, the learned knowledge of existing solvers is implicitly contained in the parameters and network architectures, which is not transpar- ent to humans. Second, the lack of applying explicit knowl- edge (e.g., “times” is related to “×” in Figure 1) hinders their reasoning ability and interpretability of how they rea-

son the answers. More importantly, we emphasize that both knowledge learning and applying are general human capa- bilities (Huang et al. 2020a) that can benefit different MWP solvers. To this end, this paper aims to construct a general framework in which different MWP solvers can learn and apply explicit knowledge to achieve better reasoning ability. However, many challenges remain to be confronted. First, there is no clear scheme of how to formalize the explicit knowledge that is helpful for MWP and applicable to dif- ferent solvers. Second, it is challenging to probe a learn- ing mechanism that simulates how humans gain knowledge from solving MWP, which meanwhile should be general to work with different solvers. Third, we need to design a general knowledge application mechanism based on distinct

solver architectures, which is underexplored nowadays.

To address these challenges, we propose a novel frame- work named Learning by Applying (LeAp) for MWP, which adopts a problem-knowledge-expression architecture. In LeAp, we define two types of explicit and general math- ematical knowledge, including word-word relations and word-operator relations. Then, we implement LeAp by a Variational AutoEncoder (VAE) that contains a Knowledge Encoder and a Knowledge Decoder. Specifically, Knowl- edge Encoder acquires knowledge from problem sentences, and Knowledge Decoder applies the learned knowledge to reason corresponding expressions. The combination of these two components constitutes our novel “learning knowledge by applying it” mechanism. The learned knowledge explic- itly forms a knowledge graph in the middle and serves as a bridge connecting the two components, which is transpar- ent. Moreover, for MWP solving, we propose a semantics- enhanced module and a reasoning-enhanced module in Knowledge Decoder, which apply knowledge to promote problem comprehension and symbol reasoning, respectively. Our LeAp is a general framework that benefits existing MWP solvers by improving their reasoning abilities. We conduct extensive experiments by instantiating several back- bone solvers in LeAp. The experimental results on three datasets show the improvements of LeAp on answer reason- ing, effect of knowledge learning, as well as reasoning inter- pretability. The contributions of this paper are as follows:

We propose a general Learning by Applying (LeAp) framework to learn and apply explicit knowledge, where existing MWP solvers can serve as its backbone and ben- efit from it to improve reasoning ability.

We design a novel semantics-enhanced module and a novel reasoning-enhanced module for knowledge appli- cation, which enhance existing MWP solvers on both an- swer accuracy and reasoning interpretability.

We theoretically analyze the superiority of our au- tonomous knowledge learning mechanism in LeAp and experimentally validate its effectiveness.

Related Work

In this section, we summarize the related work as follows.

Math Word Problems. Early efforts to solve MWP range from rule-based methods (Bakman 2007; Fletcher 1985), statistic-based methods (Hosseini et al. 2014; Mitra and

Baral 2016), to semantics parsing-based methods (Koncel- Kedziorski et al. 2015; Shi et al. 2015). They are character- ized by relying on manually crafted rules, machine learn- ing models, and semantic structure of problems, respec- tively. Recently, Wang et al. (2017) first proposed a seq2seq model that translated the problem sentence into expression, following a problem-expression paradigm. Based on such a manner, we summarize advanced methods into two cat- egories: semantics-focused and reasoning-focused. Specifi- cally, semantics-focused methods aim to promote the com- prehension of problems with advanced networks (e.g., graph neural networks (Zhang et al. 2020b), pre-trained language models (Liang et al. 2021; Shen et al. 2021; Kim et al. 2022; Yu et al. 2021; Huang et al. 2021)), or additional informa- tion (Lin et al. 2021; Wu, Zhang, and Wei 2021; Huang et al. 2020b). For example, Zhang et al. (2020b) proposed Graph2Tree to capture the relationships and order informa- tion among quantities. Reasoning-focused methods aim to improve the expression reasoning process (Wang et al. 2019; Shen and Jin 2020; Cao et al. 2021; Jie, Li, and Lu 2022), such as GTS (Xie and Sun 2019) that applied the goal-driven decomposition mechanism to reason an expression tree. Be- sides, Shen et al. (2020) produced an ensemble of multiple encoders and decoders, combining their advantages in both semantic understanding and reasoning.

Knowledge Learning and Applying. One of our most crucial targets is that LeAp can learn and apply explicit knowledge for MWP. Thus, we summarize the related work regarding knowledge learning and knowledge applying, re- spectively. For knowledge learning, it expects machines to gain knowledge from data (de Penning et al. 2011; Lab- hishetty et al. 2022). Since our knowledge in LeAp forms an explicit knowledge graph, a relevant task is link predic- tion (Chen et al. 2021; Cai and Ji 2020) (or knowledge graph completion (Bansal et al. 2019; Cheng et al. 2021)), which generally learns unknown knowledge (edges) in a knowl- edge graph with the existing edges. For example, Bordes et al. (2013) considered the semantics of knowledge and inter- preted it as translation operation. Pei et al. (2019) captured the structure information and the long-range dependencies via a novel geometric perspective. Some researchers also investigate learning other types of knowledge, e.g., back- ground knowledge (Peyrard and West 2020), logic knowl- edge (Dai and Muggleton 2021), and implicit knowledge in pre-trained language models (Petroni et al. 2019). For knowledge applying, various types of knowledge have been applied in many machine learning tasks, such as conversa- tion generation (Zhou et al. 2018), question answering (Liu et al. 2021), and recommender systems (Xia et al. 2021). Some special forms of knowledge (e.g., logic rules (Qu and Tang 2019), mathematical property (Pei et al. 2020)) have also played an important role in many studies. We refer the readers to a more detailed survey conducted by Laura von Rueden et al. (2021). Especially, Wu et al. (2020) made a ba- sic attempt to incorporate an external manually constructed knowledge base for MWP task.

Different from previous studies on knowledge learning, our LeAp gains mathematical knowledge by applying it to reason answers. Compared with existing work on MWP,

Knowledge Encoder ࡼ࣐ሺࢆȁࢄሻ

Prior ࡼሺࢆሻ

Knowledge Decoderࡼࣂሺࢅȁࢆǡ ࢄሻ

Figure 2: The architecture of LeAp, which operates in a problem-knowledge-expression paradigm.

it is a general framework that empowers different solvers with explicit knowledge learning and applying in a novel problem-knowledge-expression paradigm, further improving their reasoning abilities. Besides, we propose a semantics- enhanced module and a reasoning-enhanced module in LeAp to apply knowledge for MWP solving, which bring better answer accuracy and reasoning interpretability.

LeAp: Learning by Applying

In this section, we first formally define our problem and then introduce the architecture of our LeAp in details.

Problem Definition

A MWP dataset is denoted as D = (X, Y ), where X is the set of problem sentences and Y is the set of corresponding expressions. Specifically, XP = {w1, ..., wn} ∈ X is a se- quence of n word tokens and numeric values of problem P , where wi is either a word token (e.g., “Amy” in Figure 1) or a numeric value (e.g., “2”). YP = {y1, ..., ym} ∈ Y is a sequence of m symbols. Each symbol yi comes from a tar- get vocabulary VP composed of the operator set VO (e.g.,

{+, ×, −, ÷}), numeric constant set VN (e.g., π), and nu- meric values NP in XP , i.e., VP = VO ∪VN ∪NP . Note that different problems may have different VP since NP varies with P . The goal of MWP is to train a solver that reads the problem sentence XP , generates a valid mathematical ex- pression YP , and gets a numeric answer aP based on YP .

The knowledge Z we consider is explicitly represented as

a mathematical knowledge graph. Its vertices include words

Our goal is to build a framework that (1) learns mathemat- ical knowledge Z from solving MWP; (2) applies knowl- edge Z to reason the answers for MWP. These two goals are coupled with each other and achieved collaboratively.

LeAp Architecture

Intuitively, the educational theory of cognitivism (Mowrer 1960; Muhajirah 2020) indicates that a learner fosters a strong connection to the knowledge (e.g., “times” is re- lated to “×”) by directly applying it (e.g., solve the problem in Figure 1). Drawing this insight, we construct our LeAp framework with a novel problem-knowledge-expression ar- chitecture to achieve the mechanism of “learning knowl- edge by applying it”. Specifically, the problem-knowledge process acquires knowledge from problem data, and the knowledge-expression process applies this knowledge to rea- son expressions for answers, which further guides to learn reasonable knowledge autonomously. To this end, we for- malize LeAp as a Variational AutoEncoder (VAE) (Kingma and Welling 2013), which is shown in Figure 2. It consists of three main parts: (1) a Knowledge Encoder Pφ(Z|X) that acquires knowledge Z from problem sentences X =

{XP } (problem-knowledge); (2) a Knowledge Decoder

Pθ(Y |Z, X) that reasons the expressions Y = {YP } based on X and Z (knowledge-expression); (3) a knowledge prior P (Z) of Z. The training objective of LeAp is to maximize the Evidence Lower Bound (ELBO):

L = EPφ(Z|X) [log Pθ(Y |Z, X)] − KL (Pφ(Z|X) P (Z)), (1)

and operators, and the knowledge we focus on is the exis-

`	˛¸	x	`	˛¸	x

tence of its edges. Specifically, we formalize Z as word- word relation wwi,j and word-operator relation woi,c, i.e.,

where the first term L1 optimizes the performance of MWP

Z = {wwi,j, woi,c|i, j = 1, ..., N ; c = 1, ..., C}, where N and C are the number of words and operators in MWP task. wwi,j describes the relationship between words wi and wj (e.g., “apples” belongs to “fruits”), while woi,c captures the one between word wi and operator oc (e.g., “times” is related to “×”). Both wwi,j and woi,c are set as binary variables, which equal 1 if there exists knowledge between word wi and word wj (or operator oc), and 0 otherwise. Please note that our formulation can be easily extended to incorporate multiple relationships (edges) between words and operators, such as hypernymy and antonymy (Shehata 2009).

solving, and the second term L2 regularizes the knowledge

learning results. In the following, we will introduce the de- tails of Knowledge Encoder Pφ(Z|X), Knowledge Decoder Pθ(Y |Z, X), and the knowledge prior P (Z) in turn.

Knowledge Encoder. Knowledge Encoder Pφ(Z|X) aims at acquiring explicit knowledge Z from the problem sentence set X as shown in Figure 2, which operates the problem-knowledge process. Since wwi,j, woi,c ∈ Z are bi- nary, we map each word wi and operator oc to the vector wi, oc ∈ Rd respectively (d is the dimension), and feed

wi, wj, oc into different networks to encode their Bernoulli

distributions. Formally, we model Knowledge Encoder as:

After generating symbol yt, the backbone solver derives the next reasoning state st+1 with another solver-specific

Pφ(wwi,j |X) = Bernoulli (σ (f1 ([wi, wj ]))) ,

Pφ(woi,c|X) = Bernoulli (σ (f2 ([wi, oc]))) ,

(2)

network f3 (e.g., f3 represents the forget gate in Seq2Seq):

st+1 = f3(st, e(yt), options).	(6)

where σ is the sigmoid function, f1 and f2 are neural net- works that transform the concatenation [·] of wi, wj and wi, oc, respectively. Note that f1, f2 can be implemented ranging from MLP to pre-train language models (Petroni et al. 2019). Since we focus more on learning knowledge from MWP, we do not emphasize their difference and adopt MLP (Kipf et al. 2018) for simplicity.

During training, Knowledge Encoder Pφ(Z|X) needs to

Readers can refer to the original papers for more details of different backbone solvers summarized in Section 2.

Semantics-enhanced Module. LeAp improves problem comprehension with a semantics-enhanced module for ap- plication of word-word knowledge wwi,j ∈ Z (e.g., under- stand “how many fruits” in Figure 1 via the knowledge “ap- ples” belongs to “fruits”), which is independent of specific backbone solvers. Specifically, for problem P , (1) we con-

sample Z to estimate E

Pφ(Z|X)

[log Pθ(Y |Z, X)], i.e., L1

struct a graph SEP as shown in Figure 2 by taking the words

in P as vertices and their knowledge {wwi,j|i, j = 1, ..., n}

in Eq. (1). However, it is hard to use reparameterization to backpropagate the derivatives since wwi,j, woi,c ∈ Z are binary (Kipf et al. 2018). Therefore, we adopt a continuous approximation of Eq. (2) when optimizing Eq. (1):

wwi,j = σ ((f1 ([wi, wj ]) + gi,j )/τ ) ,

from Z as edges. Thus, SEP can be seen as a subgraph of our overall explicit knowledge Z; (2) we get word represen- tations H by the original backbone according to Eq. (4); (3) we utilize a GCN to pass the message on SEP to obtain H′ that fuses the relational knowledge:

woi,c = σ ((f

2 ([wi, oc]) + g

i,c

(3)

)/τ ) ,

H′ = AE · ReLU(AE · H · W1 + b1) · W2 + b2,	(7)

where AE  ∈  Rn×n is the adjacency matrix of SEP ,

where {gi,j, gi,c} are i.i.d. sampled from Gumbel(0, 1) dis- tribution (Jang, Gu, and Poole 2016). τ is a temperature pa- rameter that controls the degree of approximation.

Knowledge Decoder.  Knowledge Decoder P (Y |Z, X)

W1, W2, b1, b2 are trainable parameters.

Reasoning-enhanced Module. Now, we introduce how LeAp improves symbol reasoning with our proposed reasoning-enhanced module that applies both word-word

applies the knowledge

θ

Z acquired by Knowledge Encoder

knowledge and word-operator knowledge wwi,j, woi,c ∈ Z. Intuitively, word “times” in a problem sentence can encour-

to reason expressions Y , which operates the knowledge-

expression process in Figure 2. Here, we aim to design a general knowledge application mechanism that benefits dif- ferent solvers (e.g., Seq2Seq, GTS), rather than propose a special solver architecture. Specifically, we contribute

age a solver to correctly reason symbol “×” through the re- lational knowledge woi,c between “times” and “×”, whose location in the expression can be refined based on how fo- cused the solver is on “times”. Thus, to guide the reasoning at step t, we first establish temporary relationships wst be-

a semantics-enhanced module and a reasoning-enhanced

tween current reasoning state st and all words in P by:

module in Knowledge Decoder, which apply knowledge to

t	exp (f4 (st, h′ ))

improve problem understanding and symbol reasoning, re-

wsi = Σ

exp  f   s , h′    ,

(8)

spectively. In the following, we first unify the architecture of most existing solvers into “Backbone Solver”. Then, we

f4 st, h′

j

= v⊤ tanh

j

W3 · st, h′	,

explain the details of our proposed modules.

Backbone Solver. Given problem P , a backbone solver

where v, W3 are learnable parameters.

Then, combining st and knowledge Z, we construct an-

first reads the problem sentence XP = {w1, ..., wn}, and

then generates word representations H = {h1, ..., hn} and

other graph REt for problem P . As depicted in Figure 2,

′

an initial reasoning state s1 by:

(H, s ) = Sol-Enc({w , i = 1, ..., n}).	(4)

its vertex set contains reasoning state st, words H	=

{h′ , ..., h′ } of P , and all operators O = {o1, ..., oC}. The

edge set is composed of wst and knowledge wwi,j, woi,c.

1	i	i

On REt , we propagate the information from st to enhance

Sol-Enc conducts problem understanding and captures

operator representations by:

many existing models in different solvers. It can be formal- ized ranging from RNN (e.g., GTS, TSN-MD), BERT (e.g.,

Ht = AE · ReLU(AE · [wst · st, H′] · W4 + b4) · W5 + b5,

MWP-BERT), to specific MWP encoder (e.g., Graph2Tree). Then, the backbone solver generates the expression YP =

{y1, ..., ym} for P step by step. Specifically, at step t (t =

Hˆ t = Ht + LayerNorm(Ht),

Ot = LayerNorm(ReLU(AD · Hˆ t·W6 + b6)),	(9)

1, ..., m), it reasons symbol yt by:

Pθ(yt | y1, ..., yt−1, P ) = Sol-Dec(st, e(yt), options).	(5)

In Sol-Dec, st is the reasoning state at step t (s1 at step 1

Oˆ t = ReLU([Ot, O] · W7+b7),

O′ = O + LayerNorm(Oˆ t),

where AD  ∈  RC×n is the adjacency matrix of REt ,

comes from Eq. (4)). e(yt) is the embedding of symbol yt, which equals oc if yt is operator oc, or hi if yt is a num- ber wi ∈ NP . options are some optional terms. Specifically,

W∗, b∗ are weight matrices and biases.

When reasoning symbol yt in Eq. (5), e(yt) is chosen as

o′ ∈ O′ in Eq. (9) if yt is operator oc, or h′ ∈ H′ in Eq. (7)

c	i

the meanings of Sol-Dec, st, and options vary with differ- ent solvers. For example, in Seq2Seq, Sol-Dec represents the

if yt is number wi. Finally, the symbol representation e(yt)

enhanced with knowledge Z is used to generate the next rea-

output gate of LSTM, st is the hidden state, and options = ∅.

soning state st+1 by Eq. (6), and REt evolves to REt+1.

Prior of Knowledge. The prior P (Z) controls the known information for LeAp. Since knowledge wwi,j, woi,c ∈ Z is binary, it is natural to take the following Bernoulli distri- bution as the prior of Z and set δ1 = 0.1 for sparsity.

wwi,j ∼ Bernoulli(δ1), woi,c ∼ Bernoulli(δ1).	(10)

We design the prior P (Z) to simulate a real learner. In practice, a learner may obtain different reasoning perfor- mances for MWP with different knowledge backgrounds. For example, a junior high school student has better reason- ing ability than a primary school student. Thus, we can set a higher δ1 = 0.5 for knowledge that a learner has mas- tered, which we can simulate by introducing part of (e.g., α = 20%) edges of an external knowledge base. With such prior, LeAp can also be guided to learn similar knowledge, thus alleviating the problem of capturing false correlations.

In summary, our LeAp framework has the following ad- vantages. First, LeAp is general to take different MWP solvers as the backbone, enabling them not only to learn reasonable knowledge but also to gain better reasoning abil- ity. Second, LeAp adopts a problem-knowledge-expression architecture, where knowledge Z explicitly forms a knowl- edge graph. Therefore, both its learning results and apply- ing methods are more interpretable compared with previ- ous methods that follow the problem-expression paradigm.

knowledge (i.e., ri,j = 0) as true (i.e., zi,j = 1), and thus

Pθ(Y |zi,j = 1, X) < Pθ(Y |zi,j = 0, X) at this time. Based on the “Effective knowledge” assumption, we an-

alyze the difference between our LeAp and LP. Recall that LP learns knowledge with a model Pφ(zi,j|X), which calcu- lates the posterior probability of Z given X from a Bayesian perspective. Comparatively, LeAp learns knowledge from reasoning expressions Y based on X. Thus, we investigate

(1) Whether the optimization objective of LeAp in Eq. (1) optimizes the posterior Pφ(zi,j|X, Y )

(2) If (1) holds, whether Pφ(zi,j|X, Y ) is larger (i.e., more accurate) than Pφ(zi,j|X)

Here, we consider a simplified setting to train LeAp with parameters being initialized with φLP , XLP from a trained LP model. Under such setting, we have two theorems that answer the two questions above, respectively.

Theorem 1. Assume Pφ(zi,j = ri,j|X) > δ(X)

holds in a neighborhood U of (φLP , XLP ) and knowl- edge Z is effective. Then, for each zi,j ∈ Z, maximiz- ing the objective of MWP solving in Eq. (1), i.e., L1 = EPφ(zi,j |X)[log Pθ(Y |zi,j, X)], is equivalent to maximizing

L3 = ri,j · Pθ(Y |zi,j = 1, X) · Pφ(zi,j = 1|X)+

(1 − ri,j) · Pθ(Y |zi,j = 0, X) · Pφ(zi,j = 0|X)	(12)

in U , where δ(X) ≜ max { 	1     }|c=θ,x ∈X ,

Third, in the prior of knowledge Z, we can set different α to investigate problem solving effects of learners with variable

1+ β(1−ri,j,ri,j,c)	i

β(ri,j,1−ri,j,c)

and β(a, b, c) ≜ Pθ(Y |zi,j = a, X) ·  ∂Pθ (Y |zi,j =b,X)  .

background, which is further visualized in Section 5.3.

Theoretical Analyses

In brief, our LeAp learns mathematical knowledge from problems and applies it to solve MWP, naturally construct- ing an explicit knowledge graph (KG) as shown in Figure 2. Comparatively, a straightforward way to learn a KG is the link prediction task (LP) (Chen et al. 2021; Cai and Ji 2020),

∂c

Proof. The basic idea is to verify that the inner product of

the derivatives of L1 and L3 is positive for each parameter in LeAp. Thus, under a first order Taylor approximation, the gradient direction of L1 implicitly optimizes L3. On this ba- sis, the entire proof consists of three parts of verification for Knowledge Encoder φ, Knowledge Decoder θ, and vertex embeddings X respectively. Here ⟨, ⟩ represents the inner

which predicts the edge between each pair of vertices di-

product of two vectors.

For φ in Knowledge Encoder, ⟨

∂L1 , ∂L3 ⟩ =

rectly. In this section, we investigate deeper into how LeAp

∂φ	∂φ

is superior in its autonomous learning mechanism compared

(2r

— 1) · ln Pθ(Y |zi,j = 1, X) · ∂Pφ(zi,j = 1|X)

2. (13)

with LP. Here, we unify some important notations without

i,j

Pθ(Y |z

i,j

= 0, X)	∂φ

loss of generality. Specifically, we use zi,j ∈ Z to represent the knowledge between vertices i and j in the KG, including word-word relation wwi,j and word-operator relation woi,c.

According to the definition of “Effective knowledge” in Eq. (11), ⟨ ∂L1 , ∂L3 ⟩ ≥ 0 always holds.

For

X represents the embeddings of vertices, including words

θ in Knowledge Decoder, when ri,j = 1, we can

derive that ⟨ ∂L1 , ∂L3 ⟩ =

{wi} and operators {oc}.

∂θ	∂θ

Before detailed derivation, we first assume that the knowl-

∂Pθ(Y |zi,j = 1, X) 2	Pφ(zi,j = 1|X)2

edge Z is helpful for solving MWP, because we cannot ex-

·

∂θ	Pθ(Y |z

i,j

+

= 1, X)

pect to gain knowledge irrelevant to mathematical reason- ing (e.g., chemistry knowledge) from solving mathematical

⟨ ∂Pθ(Y |zi,j = 0, X) ,

∂θ

∂Pθ(Y |zi,j = 1, X) ⟩·

∂θ

problems. Thus, we give the following definition:

Pφ(zi,j = 0|X) · Pφ(zi,j = 1|X)

Definition 1. Effective knowledge Z: ∀zi,j ∈ Z,

Pθ(Y |z

i,j

>

= 0, X)

[Pθ(Y |zi,j = 1, X)−Pθ(Y |zi,j = 0, X)]·(2ri,j −1) > 0. (11)

ri,j is the ground-truth label of zi,j, equalling 1 if there exists true knowledge (i.e., edge) between i and j, and 0

∂Pθ (Y |zi,j = 1, X)  · P (z	= 1|X) · β(1, 0, θ)·

∂θ	φ  i,j

Pφ(zi,j = 1|X) · β(0,1,θ) − Pφ(zi,j = 0|X)

otherwise. Pθ is the Knowledge Decoder of LeAp. In Def-

β(1,0,θ)	 .	(14)

Pθ(Y |zi,j = 1, X) · Pθ(Y |zi,j = 0, X)

inition 1, if there exists knowledge between i and j (i.e.,

Given the condition Pφ(zi,j = ri,j|X) > δ(X), it is easy to

ri,j = 1), Knowledge Decoder can better reason the ex- pressions Y by applying zi,j = 1 than zi,j = 0. On the

verify that Pφ

(zi,j

β(0,1,θ)

β(1,0,θ)

φ(z

i,j

= 0|X), and

contrary, it will introduce redundancy if we treat the false	thus ⟨ ∂L1 , ∂L3 ⟩ > 0 in U . The proof for ri,j = 0 is similar.

∂θ	∂θ

For xi ∈ X , we also report the result of ri,j = 1. Since LeAp is initialized with a trained LP model, (φLP , XLP ) can be seen as a locally optimal solution of Pφ(zi,j = 1|X),

and thus ∂Pφ(zi,j =1|X) ≈ 0 holds in U . Based on it, we can

i

derive that ⟨ ∂L1 , ∂L3 ⟩ ≈

Experiments

Experimental Setup

Datasets. We use three datasets in experiments: Math23K, MAWP, and SVAMP. Specifically, Math23K (Wang, Liu, and Shi 2017) is a Chinese dataset that contains 23, 162

∂xi  ∂xi

problems that have only one variable. We use its the pub-

∂Pθ(Y |zi,j = 1, X) 2 ·

∂xi

Pφ(zi,j = 1|X)2

+

Pθ(Y |zi,j = 1, X)

lished dataset partition for experiments. MAWPS (Roy and Roth 2017) is an English dataset. We select 2, 373 prob-

⟨ ∂Pθ(Y |zi,j = 1, X) , ∂Pθ(Y |zi,j = 0, X) ⟩·

lems with only one unknown variable and conduct 5-fold

∂xi

∂xi

cross-validation. SVAMP (Patel, Bhattamishra, and Goyal

Pφ(zi,j = 0|X) · Pφ(zi,j = 1|X)

2021) is a test dataset that contains 1, 000 more difficult

Pθ(Y |z

i,j

>

= 0, X)

problems than MAWPS. Following Patel et al. (2021), mod-

∂Pθ(Y |zi,j = 1, X)

∂xi

· Pφ(zi,j = 1|X) · β(1, 0, xi)·

els are trained on the combination of MAWPS and another ASDiv-A dataset and tested on the problems in SVAMP.

Baselines. We take the following SOTA models as the

Pφ(zi,j = 1|X) · β(0,1,xi) − Pφ(zi,j = 0|X)

β(1,0,xi)	 .	(15)

Pθ(Y |zi,j = 1, X) · Pθ(Y |zi,j = 0, X)

Similar to Eq. (14), it is easy to verify that Eq. (15) is

larger than 0, and thus ⟨ ∂L1 , ∂L3 ⟩ > 0 in U . □

baselines, i.e., the basic Seq2Seq, semantics-focused meth- ods (Graph2Tree, HMS), reasoning-focused methods (GTS, TSN-MD), and ensemble-based method (Multi-E/D). Our LeAp is a general framework, and thus we take all of them

∂xi  ∂xi

In Theorem 1, we further notice that L3 can be rewritten as P (Y |zi,j = ri,j, X)· P (zi,j = ri,j|X) if Pφ(zi,j|X) and Pθ(Y |zi,j, X) reconstruct the true distribution P (zi,j|X) and P (Y |zi,j, X) behind dataset D. Thus, L3 is equivalent to the following posterior, answering our question (1):

P (zi,j = ri,j |X, Y )

as the backbones to evaluate its effectiveness and generality.

Seq2Seq (Luong, Pham, and Manning 2015) adopts a BiLSTM encoder and a LSTM decoder with attention to translate a problem sentence into an expression.

Graph2Tree (Zhang et al. 2020b) builds and encodes two quantity-related graphs to enrich problem under-

P (Y |z	= r  , X) · P (z	= r  |X) · P (X)	(16)

standing with quantity information.

=	i,j

i,j

i,j

P (X, Y )

i,j	.

HMS (Lin et al. 2021) captures problem semantics fol- lowing a word-clause-problem hierarchy.

Theorem 2. Under the assumption of “Effective knowl- edge”, the following inequality holds:

P (Y |zi,j = ri,j , X) · P (X) > 1.	(17)

P (X, Y )

Proof. P (X, Y ) can be rewritten as

GTS (Xie and Sun 2019) proposes a goal-driven decom- position mechanism to reason the expression tree.

TSN-MD (Zhang et al. 2020a) generates diverse candi- date expressions with a multiple-decoder network.

Multi-E/D (Shen and Jin 2020) is an ensemble of sequence-based encoder/decoder with graph-based en-

P (X) · [P (Y |zi,j = ri,j , X) · P (zi,j = ri,j |X)+

P (Y |zi,j = 1 − ri,j , X) · P (zi,j = 1 − ri,j |X)].

(18)

coder/decoder to obtain better semantics and reasoning.

Implementation Details. For Knowledge Encoder Pφ, the

According to the “Effective knowledge” assumption, P (Y |zi,j = 1 − ri,j, X) < P (Y |zi,j = ri,j, X). There- fore, Eq. (18) is less than

P (X) · [P (Y |zi,j = ri,j , X) · P (zi,j = ri,j |X)+

dimension of embeddings d is 128. The temperature parame- ter τ in Eq. (3) decreases from 0.5 to 0.1 during training. For Knowledge Decoder Pθ, all backbone solvers are optimized with their original parameter settings. Other parameters are initialized randomly and trained with Adam (Kingma and

P (Y |zi,j = ri,j , X) · P (zi,j = 1 − ri,j |X)]

= P (X) · P (Y |zi,j = ri,j , X),

i.e., inequality. (17) holds. □

(19)

Ba 2014) with dropout probability 0.5. Words with less than 5 occurrences are converted to a special token “UNK”. All experiments are run on a Linux server with four 2.30GHz

Based on Theorem 2 and Eq. (16), P (zi,j = ri,j|X, Y ) > P (zi,j = ri,j|X), supporting our question (2). In summary, we conclude that: According to Theorem 1, in LeAp, the autonomous mechanism of learning knowledge from solv- ing MWP is to optimize the posterior P (zi,j = ri,j|X, Y ) by L1 in Eq. (1). Such a mechanism is more accurate than a straightforward link prediction model P (zi,j = ri,j|X) since it achieves a higher probability according to Theo- rem 2. Notably, LeAp’s superiority lies in the mechanism to calculate the posterior probability based on the informa- tion (i.e., Y ) provided by solving MWP, instead of obtaining better parameters φ, X.

Intel Xeon Gold 5218 CPUs and a Tesla V100 GPU. Our codes are available at https://github.com/bigdata-ustc/LeAp.

Performance on Answer Reasoning

We verify the effectiveness of LeAp in improving the rea- soning ability of backbones for MWP, using answer accu- racy as the metric since there may be many correct expres- sions for the same problem. The predicted expression is con- sidered correct if its calculated value equals the true answer. In Table 1, we first report the performances of all back- bones in their original version (“ORI”) and with our LeAp framework (“LeAp”). From Table 1, we observe that LeAp

Table 1: Answer accuracy (∗ ∗ ∗ : p ≤ 0.001, ∗∗ : p ≤ 0.01, ∗ : p ≤ 0.05). †: implemented by MTPToolkit (Lan et al. 2022).

Table 2: Ablation study on reducing semantics-enhanced module (“w/o SE”) or reasoning-enhanced module (“w/o RE”). The performance of LeAp is referred in Table 1.

improves the answer accuracy of all backbones, and by ap- plying paired t-test, the improvements are statistically signif- icant with p ≤ 0.001 ∼ 0.05. It demonstrates that LeAp can enhance the mathematical reasoning ability of MWP solvers

by enabling them to autonomously learn explicit knowledge from problem solving and apply it to generate answers.

Second, to assess the effect of knowledge application, we design a variation of LeAp, named “LeAp-EK”, by directly applying knowledge Z from external knowledge bases in Knowledge Decoder. We select HowNet (Dong and Dong 2006) as the knowledge base for Math23K and Con- ceptNet (Speer, Chin, and Havasi 2017) for MAWPS and SVAMP. As we can see, the performances of “LeAp-EK” are also significantly better than “ORI”. It shows the appli- cability of Knowledge Decoder that applies knowledge for different solvers and further verifies the reasonability of our “Effective knowledge” assumption in Section 4.

Third, “LeAp” outperforms “LeAp-EK” in almost all cases. That is probably because LeAp learns additional word-operator knowledge and our theoretical results guar- antee that effective knowledge for MWP can be acquired. Thus, it reflects the importance and benefits of LeAp’s learn- ing mechanism to gain knowledge autonomously.

Ablation Study. Here, we highlight the advantages of our semantics-enhanced module in Eq. (7) and reasoning- enhanced module in Eq. (9) for knowledge application. Combing Table 1 and Table 2, the accuracy of reduc- ing semantics-enhanced (“w/o SE”) or reasoning-enhanced (“w/o RE”) degrades for all models, proving that they are necessary for LeAp to solve MWP while also having su- perior generality. Besides, the performances of LeAp “w/o SE” are higher than “w/o RE” for semantics-focused meth- ods (e.g., Graph2Tree). It indicates that the learned knowl- edge may be more useful to reason symbols for methods that have captured strong semantics. The opposite results appear for reasoning-focused solvers (e.g., TSN-MD). Thus, these

Table 3: Top 3 knowledge (word-word/operator pairs) of LeAp with different backbones on MAWPS.

two modules are suitable for different types of backbones.

LeAp Analysis

Knowledge learning. Now, we assess the quality of ex- plicit knowledge Z learned by LeAp. Our idea is to rank wwi,j, woi,c ∈ Z after training and expect the reason- able one to be at the top. We visualize the top 3 word- word/operator pairs in Table 3 and clearly see that LeAp gains reasonable knowledge with different backbones (e.g., LeAp (Seq2Seq) learns that “house” is related to “home” and “total” is related to “+”).

Further, we conduct a quantitative evaluation by introduc- ing α = 20% of external knowledge bases (i.e., HowNet and ConceptNet) as the prior for word-word knowledge wwi,j (there is no external knowledge base for woi,c) and calculat- ing Precision@50 based on the rest 80%, because we fo-

Co-occur	TF-IDF	LP

Figure 3: Precision@50 of word-word relations wwi,j.

Figure 4: Answer accuracy with α = 0%, 20%, 40%, 60%.

cus more on the knowledge accuracy. Here, We introduce three classic baselines. “Co-occur” determines the weight between two words by their co-occurrence frequency in all problems. “TF-IDF” calculates the cosine similarity be- tween words by their TF-IDF values. “LP” is a model with the same architecture as Knowledge Encoder. It is trained on the same 20% knowledge in the prior of LeAp.

From Figure 3, our LeAp performs better than all base- lines, no matter taking which backbone solver. It reflects the superiority and robustness of LeAp’s autonomous learning mechanism. Especially, LeAp outperforms LP, justifying the rationality of our theoretical analyses in Section 4.

Knowledge prior. To simulate learners with different backgrounds, we take α = 0%, 20%, 40%, 60% of exter- nal knowledge bases in the prior P (Z) and evaluate the performance of LeAp on MWP solving, with Seq2Seq, Graph2Tree, and GTS as the backbone. From Figure 4, with the increase of α, the answer accuracy of LeAp shows an in- creasing trend, just as a human learner with a richer knowl- edge foundation can better carry out mathematical reason- ing. Besides, when α = 0%, LeAp still outperforms the original backbones (“ORI”) in Table 1. It demonstrates the flexibility of our LeAp to learn knowledge from scratch.

Case Study. Further, we conduct case study to illustrate the interpretable reasoning process of LeAp (Graph2Tree as the backbone). In Figure 5, we report the problem sentence, the prefix expressions reasoned by Graph2Tree and LeAp (Graph2Tree), and the word-operator knowledge woi,c learned by LeAp. For both cases, we can see that the original Graph2Tree makes mistakes at reasoning step t = 1. Comparatively, by applying the learned knowledge woi,c be- tween “times” and “×”, “more” and “+”, LeAp corrects such errors and reasons “×” and “+” accurately. Notably, the knowledge woi,c is fixed during the reasoning process. When to use this knowledge is controlled by how focused LeAp is on the words “times” and “more”, measured by wst in our proposed reasoning-enhanced module (Eq. (8) in Sec- tion 3.2). Therefore, we can conclude that in LeAp, not only

Figure 5: Case study.

does the learned explicit knowledge benefit existing MWP solvers on answer accuracy, but the knowledge application mechanism can also explain how to reason the correspond- ing answers, showing superior interpretability.

Conclusion and Future Work

In this paper, we proposed a Learning by Applying (LeAp) framework for explicit knowledge learning and applying in a novel general problem-knowledge-expression paradigm that can be added to existing solvers to improve their reason- ing ability. We also designed semantics/reasoning-enhanced modules in LeAp to strengthen problem understanding and symbol reasoning by applying knowledge effectively. We theoretically proved the superiority of LeAp’s autonomous learning mechanism from a Bayesian perspective. Experi- ments showed the effectiveness of LeAp in answer reason- ing, knowledge learning, and interpretability. In the future, we will extend LeAp to other types of knowledge/problems, and explore its potential to enrich external knowledge bases. Acknowledgement. This research was partially sup- ported by grants from the National Natural Science Foun-

dation of China (Grants No. 62106244, and 61922073).

References

Bakman, Y. 2007. Robust understanding of word problems with extraneous information. arXiv preprint math/0701393.

Bansal, T.; Juan, D.-C.; Ravi, S.; and McCallum, A. 2019. A2N: Attending to neighbors for knowledge graph infer- ence. In Proceedings of the 57th annual meeting of the as- sociation for computational linguistics, 4387–4392.

Bordes, A.; Usunier, N.; Garcia-Duran, A.; Weston, J.; and Yakhnenko, O. 2013. Translating embeddings for modeling multi-relational data. Advances in neural information pro- cessing systems, 26.

Cai, L.; and Ji, S. 2020. A multi-scale approach for graph link prediction. In Proceedings of the AAAI conference on artificial intelligence, volume 34, 3308–3315.

Cao, Y.; Hong, F.; Li, H.; and Luo, P. 2021. A Bottom-Up DAG Structure Extraction Model for Math Word Problems. In AAAI, volume 35, 39–46.

Chen, J.; He, H.; Wu, F.; and Wang, J. 2021. Topology-aware correlations between relations for inductive link prediction in knowledge graphs. In Proceedings of the AAAI Confer- ence on Artificial Intelligence, volume 35, 6271–6278.

Cheng, K.; Yang, Z.; Zhang, M.; and Sun, Y. 2021. UniKER: A Unified Framework for Combining Embedding and Defi- nite Horn Rule Reasoning for Knowledge Graph Inference. In Proceedings of the 2021 Conference on Empirical Meth- ods in Natural Language Processing, 9753–9771.

Dai, W.-Z.; and Muggleton, S. H. 2021. Abductive knowl- edge induction from raw data. In IJCAI, 1845–1851.

de Penning, H. L. H.; Garcez, A. S. d.; Lamb, L. C.; and Meyer, J.-J. C. 2011. A neural-symbolic cognitive agent for online learning and reasoning. In Twenty-Second Interna- tional Joint Conference on Artificial Intelligence.

Dong, Z.; and Dong, Q. 2006. Hownet and the Computation of Meaning. World Scientific.

Feigenbaum, E. A.; Feldman, J.; et al. 1963. Computers and thought. New York McGraw-Hill.

Fletcher, C. R. 1985. Understanding and solving arithmetic word problems: A computer simulation. Behavior Research Methods, Instruments, & Computers, 17(5): 565–571.

Hosseini, M. J.; Hajishirzi, H.; Etzioni, O.; and Kushman,

N. 2014. Learning to solve arithmetic word problems with verb categorization. In EMNLP, 523–533. Citeseer.

Huang, Z.; Lin, X.; Wang, H.; Liu, Q.; Chen, E.; Ma, J.; Su, Y.; and Tong, W. 2021. Disenqnet: Disentangled represen- tation learning for educational questions. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discov- ery & Data Mining, 696–704.

Huang, Z.; Liu, Q.; Chen, Y.; Wu, L.; Xiao, K.; Chen, E.; Ma, H.; and Hu, G. 2020a. Learning or forgetting? a dy- namic approach for tracking the knowledge proficiency of students. ACM Transactions on Information Systems (TOIS), 38(2): 1–33.

Huang, Z.; Liu, Q.; Gao, W.; Wu, J.; Yin, Y.; Wang, H.; and Chen, E. 2020b. Neural mathematical solver with enhanced formula structure. In Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval, 1729–1732.

Jang, E.; Gu, S.; and Poole, B. 2016. Categorical reparameterization with gumbel-softmax. arXiv preprint arXiv:1611.01144.

Jie, Z.; Li, J.; and Lu, W. 2022. Learning to Reason Deduc- tively: Math Word Problem Solving as Complex Relation Extraction. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics, 5944–5955.

Kim, H.; Hwang, J.; Yoo, T.; and Cheong, Y.-G. 2022. Im- proving a Graph-to-Tree Model for Solving Math Word

Problems. In 2022 16th International Conference on Ubiq- uitous Information Management and Communication (IM- COM), 1–7. IEEE.

Kingma, D. P.; and Ba, J. 2014.	Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980.

Kingma, D. P.; and Welling, M. 2013. Auto-encoding varia- tional bayes. arXiv preprint arXiv:1312.6114.

Kipf, T.; Fetaya, E.; Wang, K.-C.; Welling, M.; and Zemel,

R. 2018. Neural relational inference for interacting systems. In International Conference on Machine Learning, 2688– 2697. PMLR.

Koncel-Kedziorski, R.; Hajishirzi, H.; Sabharwal, A.; Et- zioni, O.; and Ang, S. D. 2015. Parsing algebraic word problems into equations. Transactions of the Association for Computational Linguistics, 3: 585–597.

Labhishetty, S.; Zhai, C.; Xie, M.; Gong, L.; Sharnagat, R.; and Chembolu, S. 2022. Differential Query Semantic Anal- ysis: Discovery of Explicit Interpretable Knowledge from E-Com Search Logs. In Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining, 535–543.

Lan, Y.; Wang, L.; Zhang, Q.; Lan, Y.; Dai, B. T.; Wang, Y.; Zhang, D.; and Lim, E.-P. 2022. Mwptoolkit: an open- source framework for deep learning-based math word prob- lem solvers. In Proceedings of the AAAI Conference on Ar- tificial Intelligence, volume 36, 13188–13190.

Lewkowycz, A.; Andreassen, A.; Dohan, D.; Dyer, E.; Michalewski, H.; Ramasesh, V.; Slone, A.; Anil, C.; Schlag, I.; Gutman-Solo, T.; et al. 2022. Solving Quantitative Rea- soning Problems with Language Models. arXiv preprint arXiv:2206.14858.

Liang, X.; Hu, Z.; Zhang, H.; Lin, L.; and Xing, E. P. 2018. Symbolic graph reasoning meets convolutions. Advances in Neural Information Processing Systems, 31.

Liang, Z.; Zhang, J.; Shao, J.; and Zhang, X. 2021. Mwp- bert: A strong baseline for math word problems. arXiv preprint arXiv:2107.13435.

Lin, X.; Huang, Z.; Zhao, H.; Chen, E.; Liu, Q.; Wang, H.; and Wang, S. 2021. Hms: A hierarchical solver with dependency-enhanced understanding for math word prob- lem. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, 4232–4240.

Liu, L.; Du, B.; Ji, H.; Zhai, C.; and Tong, H. 2021. Neural- Answering Logical Queries on Knowledge Graphs. In Pro- ceedings of the 27th ACM SIGKDD Conference on Knowl- edge Discovery & Data Mining, 1087–1097.

Liu, Q.; Huang, Z.; Yin, Y.; Chen, E.; Xiong, H.; Su, Y.; and Hu, G. 2019. Ekt: Exercise-aware knowledge tracing for student performance prediction. IEEE Transactions on Knowledge and Data Engineering, 33(1): 100–115.

Luong, M.-T.; Pham, H.; and Manning, C. D. 2015. Effec- tive Approaches to Attention-based Neural Machine Trans- lation. In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, 1412–1421.

Mitra, A.; and Baral, C. 2016. Learning to use formulas to solve simple arithmetic problems. In Proceedings of the

54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2144–2153.

Mowrer, O. 1960. Learning theory and behavior. John Wiley & Sons Inc.

Muhajirah, M. 2020. Basic of Learning Theory: (Behavior- ism, Cognitivism, Constructivism, and Humanism). Inter- national Journal of Asian Education, 1(1): 37–42.

Patel, A.; Bhattamishra, S.; and Goyal, N. 2021. Are NLP Models really able to Solve Simple Math Word Problems? In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 2080–2094.

Pei, H.; Wei, B.; Chang, K.; Zhang, C.; and Yang, B. 2020. Curvature regularization to prevent distortion in graph em- bedding. Advances in Neural Information Processing Sys- tems, 33: 20779–20790.

Pei, H.; Wei, B.; Chang, K. C.-C.; Lei, Y.; and Yang, B. 2019. Geom-GCN: Geometric Graph Convolutional Net- works. In International Conference on Learning Represen- tations.

Petroni, F.; Rockta¨schel, T.; Riedel, S.; Lewis, P.; Bakhtin, A.; Wu, Y.; and Miller, A. 2019. Language Models as Knowledge Bases? In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), 2463–2473.

Peyrard, M.; and West, R. 2020. KLearn: Background Knowledge Inference from Summarization Data. In EMNLP (Findings).

Qu, M.; and Tang, J. 2019. Probabilistic logic neural net- works for reasoning. Advances in neural information pro- cessing systems, 32.

Roy, S.; and Roth, D. 2017. Unit dependency graph and its application to arithmetic word problem solving. In AAAI, volume 31.

Seo, M.; Hajishirzi, H.; Farhadi, A.; Etzioni, O.; and Mal- colm, C. 2015. Solving geometry problems: Combining text and diagram interpretation. In EMNLP, 1466–1476.

Shehata, S. 2009. A wordnet-based semantic model for en- hancing text clustering. In 2009 IEEE International Confer- ence on Data Mining Workshops, 477–482. IEEE.

Shen, J.; Yin, Y.; Li, L.; Shang, L.; Jiang, X.; Zhang, M.; and Liu, Q. 2021. Generate & Rank: A Multi-task Framework for Math Word Problems. In Findings of the Association for Computational Linguistics: EMNLP 2021, 2269–2279.

Shen, Y.; and Jin, C. 2020. Solving math word problems with multi-encoders and multi-decoders. In Proceedings of the 28th International Conference on Computational Lin- guistics, 2924–2934.

Shi, S.; Wang, Y.; Lin, C.-Y.; Liu, X.; and Rui, Y. 2015. Automatically solving number word problems by semantic parsing and reasoning. In EMNLP, 1132–1142.

Speer, R.; Chin, J.; and Havasi, C. 2017. Conceptnet 5.5: An open multilingual graph of general knowledge. In Thirty- first AAAI conference on artificial intelligence.

Tsatsou, D.; Karageorgos, K.; Dimou, A.; Carbo´, J.; Lo´pez,

J. M. M.; and Daras, P. 2021. Towards Unsupervised Knowl- edge Extraction. In AAAI Spring Symposium: Combining Machine Learning with Knowledge Engineering.

von Rueden, L.; Mayer, S.; Beckh, K.; Georgiev, B.; Giessel- bach, S.; Heese, R.; Kirsch, B.; Walczak, M.; Pfrommer, J.; Pick, A.; et al. 2021. Informed Machine Learning-A Taxon- omy and Survey of Integrating Prior Knowledge into Learn- ing Systems. IEEE Transactions on Knowledge & Data En- gineering, (01): 1–1.

Wang, L.; Zhang, D.; Zhang, J.; Xu, X.; Gao, L.; Dai, B. T.; and Shen, H. T. 2019. Template-based math word problem solvers with recursive neural networks. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 33, 7144–7151.

Wang, Y.; Liu, X.; and Shi, S. 2017. Deep neural solver for math word problems. In Proceedings of the 2017 Confer- ence on Empirical Methods in Natural Language Process- ing, 845–854.

Wu, Q.; Zhang, Q.; Fu, J.; and Huang, X.-J. 2020. A knowledge-aware sequence-to-tree network for math word problem solving. In EMNLP, 7137–7146.

Wu, Q.; Zhang, Q.; and Wei, Z. 2021. An edge-enhanced hierarchical graph-to-tree network for math word problem solving. In Findings of the Association for Computational Linguistics: EMNLP 2021, 1473–1482.

Xia, L.; Huang, C.; Xu, Y.; Dai, P.; Zhang, X.; Yang, H.; Pei, J.; and Bo, L. 2021. Knowledge-enhanced hierarchical graph transformer network for multi-behavior recommenda- tion. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, 4486–4493.

Xie, Z.; and Sun, S. 2019. A Goal-Driven Tree-Structured Neural Model for Math Word Problems. In IJCAI, 5299– 5305.

Yu, W.; Wen, Y.; Zheng, F.; and Xiao, N. 2021. Improv- ing Math Word Problems with Pre-trained Knowledge and Hierarchical Reasoning. In Proceedings of the 2021 Confer- ence on Empirical Methods in Natural Language Process- ing, 3384–3394.

Zhang, D.; Wang, L.; et al. 2020. The Gap of Semantic Pars- ing: A Survey on Automatic Math Word Problem Solvers. IEEE Transactions on Pattern Analysis and Machine Intelli- gence, 42(9): 2287–2305.

Zhang, J.; Lee, R. K.-W.; Lim, E.-P.; Qin, W.; Wang, L.;

Shao, J.; and Sun, Q. 2020a. Teacher-student networks with multiple decoders for solving math word problem. In IJCAI.

Zhang, J.; Wang, L.; Lee, R. K.-W.; et al. 2020b. Graph-to- Tree Learning for Solving Math Word Problems. In Associ- ation for Computational Linguistics, 3928–3937.

Zhou, H.; Young, T.; Huang, M.; Zhao, H.; Xu, J.; and Zhu,

X. 2018. Commonsense knowledge aware conversation gen- eration with graph attention. In IJCAI, 4623–4629.
