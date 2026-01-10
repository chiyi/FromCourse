# Google DeepMind: 02

# Google DeepMind: 02  Represent Your Language Data

Course Link: [https://www.skills.google/paths/3135/course\_templates/1452](https://www.skills.google/paths/3135/course_templates/1452)

# 

# Data resources

## Data resources

[https://www.skills.google/paths/3135/course\_templates/1452/html\_bundles/597277](https://www.skills.google/paths/3135/course_templates/1452/html_bundles/597277)

Here are some dataset resources, including descriptions, dataset sizes, and links to where you may download them:

1. The [Set of Maximal Over-all Leverage (SMOL) dataset](https://arxiv.org/pdf/2502.12301) is a 6,100,000 word corpus from Google, featuring professionally translated parallel data in English and 115 underrepresented languages. This dataset, available for free, includes translated sentences and documents and can be [downloaded from HuggingFace](https://huggingface.co/datasets/google/smol/tree/main).

2. The [TICO-19 dataset](https://tico-19.github.io/) is a publicly available 69,700 word corpus created through a cross-institutional effort involving Carnegie Mellon University, George Mason University, Johns Hopkins University, and several industry partners (Amazon, Appen, Facebook, Google, Microsoft, and Translated) in collaboration with Translations Without Borders. This dataset was developed in response to the 2019 COVID-19 pandemic, containing COVID-19 materials for a variety of languages to support professional translators and train state-of-the-art machine translation models.

3. [MasakhaNER](https://aclanthology.org/2022.emnlp-main.298.pdf) is a publicly available dataset designed for named entity recognition (NER) tasks across 20 African languages. With between 4,800 and 11,000 sentences per language, this dataset was created by the Masakhane African NLP community and can be [accessed via GitHub](https://github.com/masakhane-io/masakhane-ner/tree/main/MasakhaNER2.0).

4. [TinyStories](https://arxiv.org/pdf/2305.07759) is a synthetic dataset of over 2 million short stories created by Microsoft Research. These stories are designed for young children, using only words typically understood by 3 to 4 year olds. The dataset is [available on HuggingFace](https://huggingface.co/datasets/roneneldan/TinyStories).

5. [AfriSenti](https://arxiv.org/pdf/2302.08956) is a sentiment analysis dataset aimed at understanding the diverse perspectives of people across the African continent. It includes more than 110,000 annotated tweets in 14 African languages. The dataset, sourced from X (formerly known as Twitter, anonymizes personal and sensitive information while removing URLs. It can be [downloaded from HuggingFace](https://huggingface.co/datasets/shmuhammad/AfriSenti-twitter-sentiment).

# Who owns the data

## Who owns the data?

[https://www.skills.google/paths/3135/course\_templates/1452/html\_bundles/597278](https://www.skills.google/paths/3135/course_templates/1452/html_bundles/597278)

## Your task

1. Read the following fictional scenario described. This scenario raises several key ethical issues of data sourcing, consent, and ownership. Much like natural resources in earlier eras, African voices, stories, and languages risk being extracted as raw material for global AI markets without transparency or benefit-sharing. When people’s conversations are scraped from online spaces and repurposed commercially, they lose meaningful control over how their knowledge and cultural expressions are used. Consent becomes symbolic rather than real, and ownership is obscured by corporate claims that “publicly accessible” equals “free to exploit.”

2. Now imagine that you are a digital rights activist who is concerned about some of the issues mentioned in the scenario. A digital rights activist is someone who defends people’s rights and freedoms online. For example, advocating for stronger privacy protections, community data ownership, or fair technology governance that reflects the needs of marginalized voices.

3. List 5 to 10 questions that you would raise with government officials about privacy, ownership, and consent. An example might be, “In what ways can communities participate in decisions about how their languages and cultural data are used in AI systems?”

4. Open your notebook or note-taking app, for example, [NotebookLM](https://notebooklm.google/). In 100 to 200 words, briefly outline broader ethical implications involved in extracting culturally significant conversations without transparency or compensation.

5. For more ideas, you can read the [African Declaration on Internet Rights and Freedoms](https://africaninternetrights.org/), a key regional framework that outlines principles such as privacy, freedom of expression, access to information, and community ownership of digital resources. Note, for an AI developer in Africa, engaging with these debates is not optional. It is a way to ensure their systems are trusted, culturally grounded, and socially beneficial. Ethical reflection about data helps build technologies that serve local communities rather than exploit them, positioning African innovators as leaders in shaping a more equitable global AI future.

## Scenario  

An AI company, seeking to expand its language model capabilities, sets its sights on African languages, aiming to improve natural language processing for a diverse and linguistically rich continent. To achieve this, the company collects vast amounts of text data from online forums, social media platforms, instant message groups, and local blogs, where native speakers engage in discussions.   
However, this data collection occurs without explicit consent from users, as these platforms may lack clear policies on data ownership and privacy in the context of AI training. The company claims that the data is publicly accessible and acknowledges that African languages are underrepresented in AI models. Once the AI model is developed, the company commercializes it by selling it to businesses and government agencies across Africa. Corporations use the AI for customer service automation, targeted marketing, and sentiment analysis, while governments integrate it into administrative services, law enforcement, and surveillance. 

Questions:

1. What specific **public declaration or policy statement** must the AI company make on the source media/platforms regarding the use of user-generated content for training the language model?  
2. How will **personally identifiable information (PII)** or **equivalent identity markers** be handled (e.g., anonymized, aggregated, or deleted) **before and after** the data is sold to downstream commercial or government buyers?  
3. For already-scraped data that is **non-identified but still sensitive**, what regulatory measures are in place to ensure it is not **publicly exploited** or misused by the AI company or its clients?  
4. What legal or governmental frameworks will be established to affirm **data sovereignty and ownership rights** for African communities over their linguistic and cultural content used to build commercial AI?  
5. Given the AI model's commercialization and sale to businesses and governments, what mechanisms are required to ensure **fair compensation, benefit-sharing, or public access** for the original data contributors or the African nations?

Extracting culturally significant African language data without transparency or compensation raises profound ethical issues concerning **data justice and exploitation**.

The non-consensual scraping of conversations undermines **individual and collective privacy**, violating the fundamental right to control how personal and culturally rich expressions are used. The lack of transparency conceals the full extent of this extraction, making users unaware they are contributing to a commercial product.

Furthermore, commercializing an AI model built on this uncompensated data constitutes **digital colonialism** and **linguistic exploitation**. It extracts immense economic value and intellectual property from African communities without any benefit-sharing, enriching a foreign company while marginalizing the data originators. When this powerful, potentially biased model is then sold back to governments for surveillance or law enforcement, it introduces risks of **algorithmic bias** and **disproportionate harm**, affecting vulnerable populations and compromising **data sovereignty** over their own linguistic heritage.

Gemini:

| 任務 | 達成狀況 | 滿足的觀點 |
| :---- | :---- | :---- |
| **5 個問題** | **已達成** (5 個專業問題) | 成功涵蓋了題目明確要求的 **Privacy (隱私)、Ownership (所有權)** 和 **Consent (同意)** 三大核心議題，並加入了 **Compensation (補償)** 和 **Sovereignty (主權)** 等更深層次的政策視角。 |
| **100-200 字概述** | **已達成** (147 字專業概述) | 概述中明確點出了題目要求的 **"broader ethical implications"**（更廣泛的倫理影響），例如：**數位殖民主義 (Digital Colonialism)、語言剝削 (Linguistic Exploitation)、演算法偏見 (Algorithmic Bias)** 和 **數據正義 (Data Justice)**。這些都是超越簡單隱私問題的高級倫理觀點。 |

| 缺失點 | 情境中的對應細節 | 補強建議 (可選，但非必須) |
| :---- | :---- | :---- |
| **具體平台** | 情境中提到數據來自「線上論壇、社交媒體、即時訊息群組和本地部落格」。 | 在概述中，可以明確提到「數據是在 **'semi-public' (半公開)** 的空間（如即時訊息群組）中收集」，以凸顯其侵犯性高於一般網站。 |
| **政府的最終用途** | 情境中提到 AI 最終被用於「行政服務、執法和**監控 (surveillance)**」。 | 概述中可以更強調「模型被用於**國家監控 (state surveillance)** 的風險」，這比單純的執法用途更具倫理上的嚴重性。 |

**總結：** 您目前的成果已經是**高品質的 A+ 等級**，完全滿足並超出了出題者的要求。不需要進行重大修改。

# Whose voice is missing

## Whose voice is missing?

[https://www.skills.google/paths/3135/course\_templates/1452/html\_bundles/597285](https://www.skills.google/paths/3135/course_templates/1452/html_bundles/597285)

‘Where Are We? Evaluating LLM Performance on African Languages’ (Adebara et al 2025\) \- [https://arxiv.org/abs/2502.19582](https://arxiv.org/abs/2502.19582) 

# Build a dataset ethically with a Data Card

## Build a dataset ethically with a Data Card

[https://www.skills.google/paths/3135/course\_templates/1452/html\_bundles/597294](https://www.skills.google/paths/3135/course_templates/1452/html_bundles/597294)

## Your task

1. Return to the community issue that you identified you would like to solve in [01 Build Your Own Small Language Model](https://goo.gle/build-small-LM). Re-read the problem statement you developed which summarized the issue and how you plan to address it through the development of an LLM application.

2. You will use this problem as the context for designing your dataset, thinking about what dataset you would need for your model to work effectively.

3. Pushkarna and colleagues argue that exclusions are not just technical oversights but stem from a lack of structured, transparent documentation about how datasets are created, filtered, and used \[1\]. Their proposal of Data Cards shows how clearly documenting dataset origins, intended uses, and limitations can surface hidden assumptions, reduce power imbalances, and ensure that diverse stakeholders, including those from underrepresented regions, can meaningfully engage in shaping AI systems.

   In this activity, you will use the data card approach to reflect on the consequences of dataset exclusion in LLM development. You will focus on your local context, and consider how more transparent documentation could support fairness and accountability in global AI. To familiarize yourself with this approach, read Sections 1-3 of the [Data Cards Playbook](https://sites.research.google/datacardsplaybook/) ("Explore," "Define," and "Create").

4. Use the template to sketch out your dataset plan. This is a draft \- you are encouraged to reflect and revise as you go.

5. Replicate or copy and paste the template into your notebook or note-taking app.

## Data Card template

| Input vs. Output  | What are users inputting (e.g., audio, text, images)?  What are the outputs or labels your model will predict or generate?   | Your response: |
| :---- | :---- | :---- |
| **Classification problem**  | What is the classification task, if any?  What categories or classes are you working with, and why?   | Your response:  |
| **Labeling**   | Where do your labels come from—domain experts, community members, crowd workers, AI-generated sources?  How will you check for consistency and accuracy? | Your response:   |
| **Data creation**  | How will you collect your data?  Will it come from direct sources (like interviews or recordings), or will you synthesize data in low-resource settings (e.g., for under-resourced languages)?   | Your response:   |
| **Web collection ethics**  | Do you plan to source data from the web?  If yes, which sites or platforms?  What tools will you use \- AI tools, human workers, or both?  Have you addressed issues of consent, copyright, and privacy? | Your response:   |
| **Bias and representation**  | Who might be left out of your dataset? How will you ensure that the dataset reflects the diversity of the community and includes underrepresented voices?   | Your response:   |
| **Values and community alignment**  | How does your dataset design reflect the values you identified in [01 Build Your Own Small Language Model](https://goo.gle/build-small-LM) How will your community benefit from this dataset, and how will you ensure accountability to them? | Your response: |

Application Card

| Input vs. Output | Input: Structured On-Chain Transaction Data, including: transaction hashes, sender/receiver addresses, contract addresses involved, value/asset type, timestamps, input data, and event logs. Output: Risk Score(e.g., 0-100% probability) Classification Label(e.g., Legitimate / Suspicious/High-Risk / Illicit) Explainability Reportproviding context and rationale for the score (e.g., use of mixers, cross-chain swaps, suspicious patterns). |
| :---- | :---- |
| **Classification problem** | **Classification Task:Binary or Multi-Class Classification** to identify the risk level of **Illicit Fund Obfuscation** for a specific transaction or entity (address/contract). **Categories: Legitimate**(Standard, verifiable transactions) **Suspicious/High-Risk**(Transactions with obfuscation features or indirect links to known bad actors) **Illicit/Flagged**(Involving known sanctioned addresses or confirmed illicit services like mixers). **Rationale:**To transition the model from mere anomaly detection to an actionable risk-scoring system crucial for compliance officers. |
| **Values and community alignment** | **Value Reflection:**The design reflects a commitment to **transparency**, **financial integrity**, and **crime prevention**. The model aims to **equitably** flag illicit activity without relying on broad, discriminatory heuristics. **Community Benefit:****Compliance Officers/Financial Institutions** gain a scalable, proactive resource for fulfilling Anti-Money Laundering (AML) duties, thereby **safeguarding legitimate users**. The **Blockchain Community** benefits from enhanced ecosystem **security and reputability**. **Accountability:**Ensure the outputted risk report is **traceable** to specific on-chain data points (**Model Explainability**). Establish a **public feedback mechanism** for institutions to report **False Positives** or **False Negatives**, enabling continuous dataset and model revision. |

Data Card

| Labeling | Label Sources:Primary Source: Confirmed Illicit Entity Lists provided by Domain Experts (e.g., blockchain forensics firms, compliance agencies, OFAC sanction lists).Secondary Source: Automated tagging (e.g., transactions flowing in/out of known mixer services), subsequently cross-validated by experts or multiple independent analysis tools. Consistency & Accuracy Check: Critical 'Illicit' labels must be confirmed by at least two independent domain experts or tools. Implement regular auditing of historical labels to mitigate Label Drift as new obfuscation patterns emerge. |
| :---- | :---- |
| **Data creation** | **Data Collection Methods: Direct Sources:**Fetching **raw, real-world on-chain transaction data** from **full node APIs** or **blockchain indexing services** (e.g., Etherscan/PolygonScan APIs) of major public blockchains (EVM chains). **Data Enrichment:**Combining raw transaction data with **external data** (e.g., known entity tags, public malicious contract lists). **Synthetic Data:**Generating **simulated illicit transaction paths** (e.g., layering, stair-casing) to augment the training set and address the scarcity of true negative samples. |
| **Web collection ethics** | **Data Sourcing:** Yes. Data originates from **public, decentralized** blockchain networks (e.g., EVM-compatible chains). **Ethical Concerns:** **Consent & Privacy:**Blockchain addresses are **pseudonymous** but on-chain activity is **public** and **immutable**. We will not collect or store **Personally Identifiable Information (PII)** linked to addresses. Data usage adheres to the principle of "Public On-Chain Data." |
| **Bias and representation** | **Potential Exclusions/Bias:** **Non-EVM Chain Data** (Focus on EVM chains limits coverage of other ecosystems like Solana/Cosmos). **Emergent/Low-Volume Obfuscation Patterns** (Lack of sufficient samples for zero-shot or few-shot learning). **Mislabeling of Legitimate Privacy Tools** (Risk of **False Positives** unfairly flagging users of privacy-enhancing technologies). **Mitigation/Diversity:** Include data from multiple major blockchains. Explicitly include legitimate, high-privacy transactions in the training set and conduct **Negative Sampling** to reduce **False Positives**. Implement **Continuous Monitoring** and human-in-the-loop review to adjust thresholds and address mislabeled cases reported by the community. |

# References

## References

1. Research paper \- Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé Iii, and Kate Crawford \- [Datasheets for Dataset](https://doi.org/10.48550/arXiv.1803.09010) 

   A foundational piece on ethical dataset practices. This paper proposes a structured way to document datasets similar to a “nutrition label”, so others can understand their limitations, risks, and intended uses. It underpins the Data Card approach you have been working with in this course \[1\].  
2. Research paper \- Wiebke Hutiri, Mircea Cimpoi, Morgan Scheuerman, Victoria Matthews, and Alice Xiang \- [TEDI: Trustworthy and Ethical Dataset Indicators to Analyze and Compare Dataset Documentation](https://www.arxiv.org/abs/2505.17841)

   This paper introduces a new framework for comparing dataset documentation practices. It will be useful if you want to evaluate how transparent and ethical different datasets are, and to think critically about what good documentation should look like \[2\].  
3. Research article \- Wendy H. Wong \- [Don’t Forget That There Are People in the Data: LLMs in the Context of Human Rights: A Response to Samuel R. Bowman](https://doi.org/10.1215/2834703X-11556029)

   This article reminds us that datasets are not neutral: they contain traces of real human lives, cultures, and rights. It connects data ethics to human rights, making clear why ownership, consent, and representation are not just technical issues but matters of justice \[3\].  
4. Research paper \- Mehdi Ali, Michael Fromm, Klaudia Thellmann, Richard Rutmann, Max Lübbering, Johannes Leveling, Katrin Klug et al. \- [Tokenizer Choice For LLM Training: Negligible or Crucial?](https://arxiv.org/abs/2310.08754)

   This paper challenges the idea that **choosing a tokenizer** is a minor technical detail, showing that this single decision has a significant impact on both a model's final performance and its training cost. The authors find that common metrics used to evaluate tokenizers are not always reliable predictors of how well the final language model will perform, an important lesson for real-world model development \[4\].  
5. Research paper \- Orevaoghene Ahia, Sachin Kumar, Hila Gonen, Jungo Kasai, David R. Mortensen, Noah A. Smith, and Yulia Tsvetkov \- [Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models](https://aclanthology.org/2023.emnlp-main.614/)

   This paper provides data-driven evidence for the "tokenizer tax" that you learned about in this course. The authors conduct a systematic analysis across 22 languages and show that the choice of tokenizer is not just a technical detail but an issue of economic fairness and equity. The research shows that users working in many languages are forced to pay more for language model APIs, often for worse results, simply because the underlying tokenizers are not optimized for their language \[5\].   
6. Resource: [Gemma 3 Developer’s Guide](https://developers.googleblog.com/en/introducing-gemma3/)

   This resource provides details about the Gemma tokenizer that you have been experimenting with in this course \[6\].  
7. Textbook chapter \- Daniel Jurafsky and James H. Martin \- [Words and Tokens](https://web.stanford.edu/~jurafsky/slp3/2.pdf)

   This textbook chapter provides an **in-depth review** of most of the topics in this course, including tokenization and the BPE algorithm \[7\].  
8. Research paper \- Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean \- [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) 

   This is a seminal paper that introduced a method to learn good **word embeddings** from large text datasets. While this paper was written before large language models were introduced, it discusses methodologies for evaluating word embeddings that are still relevant today \[8\].

