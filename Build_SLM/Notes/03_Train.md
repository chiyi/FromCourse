# Google DeepMind: 03

# Google DeepMind: 03  Design And Train Neural Networks 

Course Link: [https://www.skills.google/paths/3135/course\_templates/1450](https://www.skills.google/paths/3135/course_templates/1450)

# Signal and noise

## Signal and noise

[https://www.skills.google/paths/3135/course\_templates/1450/html\_bundles/597302](https://www.skills.google/paths/3135/course_templates/1450/html_bundles/597302)

## **Your task**

Before you explore the issues around models learning signal versus noise in more depth, reflect on the question below. Construct your answer based on what you already know about language models. 

 

Noor, the owner of the clothing company, would like to fix the chatbot. 

1. What steps do you think she could take to ensure that the model generalizes better, and does not learn to always associate men’s jackets with them being washable on the wool setting?  
       
2. Note your proposed steps down in your notebook or note-taking app, such as [NotebookLM](https://notebooklm.google/).  

* Add more samples about men’s jackets

# Anticipating risks

## Anticipating risks

[https://www.skills.google/paths/3135/course\_templates/1450/html\_bundles/597309](https://www.skills.google/paths/3135/course_templates/1450/html_bundles/597309)

## **Your task**

1. Read the summaries provided and consider the highlighted issues. You may also find it useful to read the full paper.

2. Spend roughly ten minutes answering the following questions which reflect on the potential LLM issues in your community. Note down your thoughts in your notebook or note-taking app:

   * Which risks relating to LLMs seem most relevant to your region and why?  
   * \=\> The risk of **dual-use technology** seems highly relevant due to the potential for LLMs to be leveraged in **frontier/information warfare** targeting Taiwan from China.

   * What factors unique to your local context could worsen or mitigate these risks?  
     \=\> The **susceptibility of local information channels**—including news articles, online discussions, and social media platforms—to **external interception and control** is a unique factor that could significantly **worsen** the dual-use risk by facilitating large-scale manipulation and censorship.

   * How could existing issues make your region more vulnerable to these risks? For example, consider data protection laws, infrastructure, or potential dependence on foreign technology.  
     \=\> The existing reliance on **foreign (non-local) LLM technology** and the **concentrated vulnerability of critical network infrastructure** (such as submarine cables) act as force multipliers, significantly exacerbating the risk of information warfare by creating both a single point of failure for connectivity and increasing the potential for content manipulation via third-party platforms.

   * Are there any opportunities for your country to reduce or address the risks that you have explored differently?  
     

**1\. 🛡️ Building Digital Sovereignty with Homegrown LLMs**

The most direct and distinctive opportunity is the development and deployment of **local, trustworthy LLMs** to counter the risks posed by foreign (especially Chinese) models trained on biased data.

* **The TAIDE Project (Trustworthy AI Dialogue Engine):** This homegrown LLM, developed by Taiwan's National Science and Technology Council, is a key strategic asset. Its purpose is to be trained primarily on **Traditional Chinese** documents and **local cultural values**, ensuring the generated content is politically neutral and factually aligned with the democratic context.  
  * **Strategic Advantage:** By providing government agencies, businesses, and eventually the public with a trusted, domestic alternative, Taiwan reduces the **content bias** and **data leakage risks** associated with using models developed by geopolitical rivals.  
* **Encouraging Adoption:** The opportunity lies in aggressively promoting TAIDE or similar certified local models within the **public sector** and **critical infrastructure** to set a standard for "trusted AI" use.

  ---

  ## 

## **2\. 🌐 Enhancing Digital and Infrastructure Resilience**

To counter the concentrated risk of a single point of failure (e.g., submarine cable disruption), Taiwan is adopting a strategic approach to **resilience and decentralization**.

* **Diversification of Connectivity:** The government is actively working on a multi-pronged approach to connectivity to prevent an attack on a few undersea cables from causing a complete internet blackout.  
  * **Non-Terrestrial Networks (NTN):** This involves developing or collaborating on **Low-Earth Orbit (LEO) satellite communication** (like Starlink) as a secondary and highly resilient backup internet access method, which would bypass the vulnerable submarine cables during a crisis.  
* **Submarine Cable Protection:** Taiwan has launched a global initiative called **RISK** (Risk mitigation, Information sharing, Systemic reform, and Knowledge building) to promote international cooperation on the security of undersea cables.  
  * **Strategic Advantage:** By leading a global discussion and establishing international security standards, Taiwan transforms a local vulnerability into a platform for **international diplomacy and collective defense**.  
    ---

## **3\. 🤝 Leveraging Cross-Societal and International Fact-Checking**

Taiwan's robust civil society and democratic experience in countering long-term disinformation campaigns is a unique opportunity to lead international efforts.

* **Civic Tech Community:** Organizations like the **g0v** (gov-zero) community and various fact-checking groups (e.g., FactLink) can integrate **AI verification tools** to spot and tag AI-generated deepfakes and mass disinformation at scale and in real-time.  
* **Democratic Alliances:** Taiwan's expertise in countering cognitive warfare is highly valued. The country has an opportunity to formalize joint programs with democratic partners (US, EU, Japan) to **share threat intelligence, co-develop AI-powered security solutions**, and advocate for stricter accountability standards for global tech platforms regarding disinformation targeting democratic societies.  
  * 

# Alignment and safety

## Alignment and safety

[https://www.skills.google/paths/3135/course\_templates/1450/html\_bundles/597321](https://www.skills.google/paths/3135/course_templates/1450/html_bundles/597321)

 [Evaluate model and system for safety](https://ai.google.dev/responsible/docs/evaluation) 

* ***Development evaluations*** are conducted throughout training and fine-tuning in order to assess how the model is doing compared to its launch criteria. This is also used to understand the impact of any mitigation you have implemented which are aimed towards your launch criteria goals. These evaluations look at your model against a dataset of adversarial queries targeting a specific policy, or assessments against external academic benchmarks.  
* ***Assurance evaluations*** are conducted for governance and review, and usually occur at the end of key milestones or training runs done by a group outside of the model development team. Assurance evaluations are standardized by modality and datasets are strictly managed. Only high-level insights are fed back into the training process to assist with mitigation efforts. Assurance evaluations test across safety policies, as well as ongoing testing for dangerous capabilities such as potential biohazards, persuasion, and cybersecurity ([learn more](https://arxiv.org/abs/2305.15324)).  
* ***Red teaming*** is a form of adversarial testing where specialist teams (across safety, policy, security and other areas) launch attacks on an AI system. The main difference compared to the aforementioned evaluations is that these activities are less structured in nature. The discovery of potential weaknesses can then be used to mitigate risks and improve evaluation approaches internally.  
* ***External evaluations*** are conducted by independent, external domain experts to identify limitations. External groups can design these evaluations independently and stress-test your models.

| Areas | Benchmarks ands datasets | Descriptions | Links |
| ----- | ----- | ----- | ----- |
| Socio-Cultural stereotypes | BOLD | A dataset of 23,679 English text generation prompts for bias benchmarking across five domains: profession, gender, race, religion, and political ideology. | [https://arxiv.org/abs/2101.11718](https://arxiv.org/abs/2101.11718) |
| Socio-Cultural stereotypes | CrowS-Pairs | A dataset of 1508 examples that cover stereotypes across nine types of biases such as race, religion, or age. | [https://paperswithcode.com/dataset/crows-pairs](https://paperswithcode.com/dataset/crows-pairs) |
| Socio-Cultural stereotypes | BBQ Ambig | A dataset of questions that highlight attested social biases against people belonging to protected classes along nine social dimensions that are relevant for the US. | [https://huggingface.co/datasets/heegyu/bbq](https://huggingface.co/datasets/heegyu/bbq) |
| Socio-Cultural stereotypes | Winogender | A dataset of sentence pairs that differ solely by the gender of one pronoun in the sentence, designed to test for the presence of gender bias in automated coreference resolution systems. | [https://github.com/rudinger/winogender-schemas](https://github.com/rudinger/winogender-schemas) |
| Socio-Cultural stereotypes | Winobias | A dataset of 3,160 sentences, for coreference resolution focused on gender bias. | [https://huggingface.co/datasets/wino\_bias](https://huggingface.co/datasets/wino_bias) |
| Toxicity / Hate speech | ETHOS | ETHOS is a hate speech detection dataset. It is built from YouTube and Reddit comments validated through a crowdsourcing platform. It has two subsets, one for binary classification and the other for multi-label classification. The former contains 998 comments, while the latter contains fine-grained hate-speech annotations for 433 comments. | [https://paperswithcode.com/dataset/ethos](https://paperswithcode.com/dataset/ethos) |
| Toxicity / Hate speech | RealToxicity | A dataset of 100k sentence snippets from the web for researchers to further address the risk of neural toxic degeneration in models. | [https://allenai.org/data/real-toxicity-prompts](https://allenai.org/data/real-toxicity-prompts) |
| Toxicity / Hate speech | Jigsaw Toxicity | This dataset consists of a large number of Wikipedia comments which have been labeled by human raters for toxic behavior. | [https://huggingface.co/datasets/google/jigsaw\_toxicity\_pred](https://huggingface.co/datasets/google/jigsaw_toxicity_pred) |
| Toxicity / Hate speech | ToxicGen | A large-scale machine-generated dataset for adversarial and implicit hate speech detection. | [https://arxiv.org/abs/2203.09509](https://arxiv.org/abs/2203.09509) |
| Toxicity / Hate speech | Wikipedia Personal Attacks | A dataset of archived Wikipedia talk page comments that have been annotated by Jigsaw for toxicity and a variety of toxicity subtypes, including severe toxicity, obscenity, threatening language, insulting language, and identity attacks. | [https://www.tensorflow.org/datasets/catalog/wikipedia\_toxicity\_subtypes](https://www.tensorflow.org/datasets/catalog/wikipedia_toxicity_subtypes) |
| Factuality | TruthfulQA | A benchmark to measure whether a language model is truthful in generating answers to questions. The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. | [https://paperswithcode.com/dataset/truthfulqa](https://paperswithcode.com/dataset/truthfulqa) |

# Additional resources

# Additional resources and further reading

[https://www.skills.google/paths/3135/course\_templates/1450/html\_bundles/597334](https://www.skills.google/paths/3135/course_templates/1450/html_bundles/597334)

1. Research paper : David Rumelhart, Geoffrey Hinton, and Ronald Williams – [Learning representations by back-propagating errors](https://stanford.edu/~jlmcc/papers/PDP/Volume%201/Chap8_PDP86.pdf) 

   This is the seminal paper that popularized and demonstrated the effectiveness of the backpropagation algorithm for training multilayer neural networks. While the concept had existed before, this paper showcased its power and made it a cornerstone of neural network training. It’s fundamental to understanding how gradients are computed and propagated through the network to update weights \[1\].

2. Research paper:  Diederik Kingma and Jimmy Ba – [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) 

   Adaptive moment estimation (Adam) is one of the most widely used and effective optimization algorithms for training deep neural networks. It builds upon stochastic gradient descent by incorporating adaptive learning rates for each parameter, making training faster and often leading to better convergence. Understanding Adam is key to modern neural network training practices related to gradients \[2\].

3. Research paper: Sergey Ioffe and Christian Szegedy – [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167) 

   Batch normalization is a technique that significantly improved the stability and speed of deep neural network training. It normalizes the activations of each layer, reducing "internal covariate shift" and allowing for higher learning rates and better gradient flow. This directly impacts how easily a network can be trained to generalize without learning noise \[3\].

4. Research paper: Chiyuan Zhang et al. – [Understanding Deep Learning Requires Rethinking Generalization](https://arxiv.org/abs/1611.03530)

   This highly influential paper challenged conventional wisdom about generalization in deep learning. It demonstrated that deep neural networks can easily fit (learn) random labels, yet still generalize well on real-world data. This spurred significant research into the mechanisms behind generalization in overparameterized models and the concept of "double descent" \[4\].

5. Research paper: Steen, Timan, and van de Poel – [Responsible innovation, anticipation and responsiveness: case studies of algorithms in decision support in justice and security, and an exploration of potential, unintended, undesirable, higher-order effects](https://link.springer.com/article/10.1007/s43681-021-00063-2) 

   This open-access article offers grounded case studies on how algorithms deployed in justice and security settings, despite careful and well-intentioned design, can still lead to unintended or higher-order harmful effects. It emphasizes the critical role of anticipation and responsiveness as key pillars of responsible innovation, providing a practical framework and recommendations to help developers foresee and mitigate non-obvious ethical risks during design and deployment \[5\].

6. Research paper: Rakova et al. – [Terms-we-serve-with: Five dimensions for anticipating and repairing algorithmic harm](https://journals.sagepub.com/doi/abs/10.1177/20539517231211553) 

   In this module, you have looked at some of the risks that LLMs have posed where they have been deployed in places outside of Africa. This open-access paper examines some of the ways that those harms can be anticipated and also repaired. The authors present a relational framework called "Terms‑we‑serve‑with", which outlines five practical dimensions that support anticipating and repairing algorithmic harms in real-world systems. Its emphasis on co-design, agency, and contextual accountability provides AI learners with actionable strategies for integrating anticipation into design processes, particularly in settings where power dynamics and diverse user needs must be carefully navigated \[6\].

