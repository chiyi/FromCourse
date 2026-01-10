# Google DeepMind: 01

# Google DeepMind: 01  Build Your Own Small Language Model

Course Link: [https://www.skills.google/paths/3135/course\_templates/1341](https://www.skills.google/paths/3135/course_templates/1341) 

# Anticipating benefits

## Anticipating benefits

[https://www.skills.google/paths/3135/course\_templates/1341/html\_bundles/597262](https://www.skills.google/paths/3135/course_templates/1341/html_bundles/597262) 

* Law   
* Arts and culture   
* Media and entertainment   
* Languages   
* Business administration   
* Government services   
* Communications  
* Manufacturing   
* Agriculture  
* Education  
* Healthcare  
* Politics   
* Security and policing

2\. Write roughly 300 words (100 words for each) explaining how these benefits can address a local problem. Keep a record in your notebook or note-taking app.

### Law

AI applications in law can be **highly user-friendly**. General users can easily search for relevant legal provisions by inputting specific demands into a prompt. The AI can then list applicable provisions and summarize them into an accessible overview, providing **convenient initial guidance** before consulting a paid advisor. This significantly improves efficiency, allowing people to quickly review essential legal texts rather than sifting through unrelated documents. **Although AI enhances public familiarity, real-life legal scenarios still require consultation with a professional advisor.** Crucially, this serves as a powerful preliminary tool, **always emphasizing the need for professional verification.**

### Manufacturing

**AI applications in manufacturing are driving significant efficiency gains.** While modern factories utilize automated pipelines with robotics and AGVs, AI further **optimizes the utilization** of these assets. Instead of devices being limited to a single, pre-defined function, AI-trained robots **have the potential to be tuned dynamically** within predefined parameters based on the manufacturing environment. This transformation **may lead to a reduction in long-term operational costs** rather than immediate capital outlay, and it **expands the scope of automated workflows.** Consequently, this flexibility pushes working hour limitations further and **significantly boosts overall production agility and capacity where bottlenecks are software-based.**

### Education

AI applications are poised to **significantly advance education through deep personalization**. Intelligent tutoring systems analyze performance data to recommend **customized learning paths**, allowing students to receive valuable, instantaneous feedback for concept mastery. Furthermore, AI tools automate routine grading and administrative tasks, significantly **reducing educators' operational burden**. This reallocation of time enables teachers to focus more on mentorship and **guiding complex critical thinking skills**. Crucially, learners also **independently harness AI** for research, querying, verification, and review processes. Ultimately, this transformation facilitates a more effective and **truly student-centered learning environment.**

# Develop statement

## Challenge: Develop your problem statement

[https://www.skills.google/paths/3135/course\_templates/1341/html\_bundles/597263](https://www.skills.google/paths/3135/course_templates/1341/html_bundles/597263)

1. Reflect on the values you have identified as important to you and the sectors you recognized that may benefit from language models. Thinking about these, generate at least two potential problems in your local community that you are interested in solving through language models. 

   If you need some inspiration, reflect on some of the problems you have encountered in this course. Along with AlphaFold, you considered the integrated AI and literacy initiative from RobotsMali which empowers African language speakers to develop and use AI tools that preserve linguistic heritage, improve literacy, and reflect local cultural realities. You also learned about Google DeepMind’s LearnLM system, which supports learners with chat experiences based on learning science principles.

2. Evaluate each of your ideas against your values framework to see which closely aligns with your personal and community values.

3. Based on your evaluation, choose an idea to take forward.

4. Develop a problem statement for the problem you wish to solve in 150-200 words in your notebook or note-taking app.

   Remember, it should:

   * Clearly define the core issue that the research aims to address.

   * Provide context and background.

   * Be specific and set the boundaries and scope of the work.

   * Be feasible and something that can be realistically addressed.

   * Justify the need for the research.

### Improving Visibility into Obfuscated Cryptographic Transactions

The pseudonymous nature of public blockchains facilitates sophisticated criminal operations seeking to **commingle illicit funds with legitimate transactions to evade detection**. The core problem is the current lack of a **unified, intelligent system** capable of proactively identifying and mapping these obfuscation attempts across **diverse ledger architectures**. Existing detection methods, often reliant on **traditional, rule-based systems**, struggle to adapt to the **rapidly evolving tactics** used by threat actors, such as complex cross-chain swaps and the illicit leveraging of **NFTs for value transfer**. This rigidity creates significant, exploitable blind spots in financial oversight.  
This research aims to solve the challenge of **generalized illicit fund tracing** in a dynamic environment. Our scope is focused: to develop a tool applicable to **major public blockchain ecosystems (especially EVM-like chains)** providing accessible on-chain data. The objective is to create an **adaptive, integrated model**—combining LLM contextual awareness with robust distinction algorithms—to analyze all relevant data points (wallet interactions, contract calls, and asset messages). Critically, the model must be designed for **continuous performance monitoring and parameter updating** to maintain efficacy against new criminal patterns. This will allow the system to **automatically score and preliminarily flag** high-risk entities, providing compliance officers with a vital, scalable, and **proactive analytical resource**.

# References

## References

[TinyStories: How Small Can Language Models Be and Still Speak Coherent English?](https://arxiv.org/pdf/2305.07759)

[Supervised Learning](https://developers.google.com/machine-learning/intro-to-ml/supervised) 

[Prepare Your Data](https://developers.google.com/machine-learning/guides/text-classification/step-3)

# My Lab TmpSaved

tokens \= list(text) \# Add your code here.

text \= ''.join(tokens) \# Add your code here.

    n \= 1 \+ len(list(ngram\_model.keys())\[0\]) \# Size of n-grams.  
    print('ngram n=',n)  
    for \_ in range(n\_tokens):  
      context \= generated\_tokens\[-(n \- 1):\]  
      context \= tokenizer.join\_text(context)  
      if context in ngram\_model:  
        if sampling\_mode \== 'random':  
          next\_word \= random.choices(  
              list(ngram\_model\[context\].keys()),  
              weights=ngram\_model\[context\].values()  
          )\[0\]  
        else:  
          idx\_max \= argmax(ngram\_model\[context\].values())  
          next\_word \= list(ngram\_model\[context\].keys())\[idx\_max\]  
        generated\_tokens \+= \[next\_word\]  
      else:  
        print(  
            "⚠️ No valid continuation found. Change the prompt or"  
            " try sampling another continuation.\\n"  
        )  
        break

    tmp\_list \= \[\]  
    for number in sequence:  
      if len(tmp\_list) \< max\_length:  
        tmp\_list \+= \[number\]  
      else:  
        subsequences \+= \[tmp\_list\]  
        tmp\_list \= tmp\_list\[-n\_overlap:\] \+ \[number\]  
    if len(tmp\_list) \> 0:  
      subsequences \+= \[tmp\_list\]

    for text in dataset:  
      sequence \= enhanced\_tokenizer.encode(text)  
      subsequences \= segment\_encoded\_sequence(sequence, segmentation\_length, n\_overlap)  
      encoded\_tokens \+= subsequences  
