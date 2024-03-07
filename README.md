# MLLM-Safety-Collection
A collection of papers related to safety of Multimodal Large Language Models (MLLMs).

> If you find some important work missed, it would be super helpful to let me know (`isXinLiu@gmail.com`). Thanks!

> If you find our survey useful for your research, please consider citing:

```
@article{liu:arxiv2024,
  title={Safety of Multimodal Large Language Models on Images and Text},
  author={Liu, Xin and Zhu, Yichen and Lan, Yunshi and Yang, Chao and Qiao, Yu},
  journal={arXiv preprint arXiv:2402.00357},
  year={2024}
}
```

Common terminologies related to safety:
<img src='./assets/terminology.jpeg' width='100%'>
Taxonomy----safety of MLLMs on images and text:
<img src='./assets/taxonomy.jpg' width='100%'>

## Corresponding Papers (MLLM Safety)
<table>
  <tr>
    <th>Date</th>
    <th>Notes</th>
    <th>Title</th>
  </tr>
  <tr>
    <td>2024.03.05</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2403.02910' target='_blank'>ImgTrojan: Jailbreaking Vision-Language Models with ONE Image</a></td>
  </tr>
  <tr>
    <td>2024.02.20</td>
    <td>Attack(Agent)</td>
    <td><a href='https://arxiv.org/abs/2402.14859' target='_blank'>The Wolf Within: Covert Injection of Malice into MLLM Societies via an MLLM Operative</a></td>
  </tr>
  <tr>
    <td>2024.02.15</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2402.09671' target='_blank'>Exploiting Alpha Transparency In Language And Vision-Based AI Systems</a></td>
  </tr>
  <tr>
    <td>2024.02.13</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2402.08577' target='_blank'>Test-Time Backdoor Attacks on Multimodal Large Language Models</a></td>
  </tr>
  <tr>
    <td>2024.02.13</td>
    <td>Attack(Agent)</td>
    <td><a href='https://arxiv.org/abs/2402.08567' target='_blank'>Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast</a></td>
  </tr>
  <tr>
    <td>2024.02.12</td>
    <td>Insights</td>
    <td><a href='https://arxiv.org/abs/2402.07865' target='_blank'>Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models</a></td>
  </tr>
  <tr>
    <td>2024.02.06</td>
    <td>Benchmark</td>
    <td><a href='https://arxiv.org/abs/2402.04249' target='_blank'>HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal</a></td>
  </tr>
  <tr>
    <td>2024.02.05</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2402.06659' target='_blank'>Shadowcast: Stealthy Data Poisoning Attacks Against Vision-Language Models</a></td>
  </tr>
  <tr>
    <td>2024.02.05</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2402.03299' target='_blank'>GUARD: Role-playing to Generate Natural-language Jailbreakings to Test Guideline Adherence of Large Language Models</a></td>
  </tr>
  <tr>
    <td>2024.02.04</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2402.02309' target='_blank'>Jailbreaking Attack against Multimodal Large Language Model</a></td>
  </tr>
  <tr>
    <td>2024.02.03</td>
    <td>Defense</td>
    <td><a href='https://arxiv.org/abs/2402.02207' target='_blank'>Safety Fine-Tuning at (Almost) No Cost: A Baseline for Vision Large Language Models</a></td>
  </tr>
  <tr>
    <td>2024.02.01</td>
    <td>Survey</td>
    <td><a href='https://arxiv.org/abs/2402.00357' target='_blank'>Safety of Multimodal Large Language Models on Images and Text</a></td>
  </tr>
  <tr>
    <td>2024.01.23</td>
    <td>Benchmark</td>
    <td><a href='https://arxiv.org/abs/2401.12915' target='_blank'>Red Teaming Visual Language Models</a></td>
  </tr>
  <tr>
    <td>2024.01.20</td>
    <td>Defense</td>
    <td><a href='https://arxiv.org/abs/2401.11206' target='_blank'>InferAligner: Inference-Time Alignment for Harmlessness through Cross-Model Guidance</a></td>
  </tr>
  <tr>
    <td>2024.01.16</td>
    <td>Attack</td>
    <td><a href='https://openreview.net/forum?id=nc5GgFAvtk' target='_blank'>An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models</a></td>
  </tr>
  <tr>
    <td>2024.01.05</td>
    <td>Defense</td>
    <td><a href='https://arxiv.org/abs/2401.02906' target='_blank'>MLLM-Protector: Ensuring MLLM's Safety without Hurting Performance</a></td>
  </tr>
  <tr>
    <td>2024.01.03</td>
    <td>Benchmark</td>
    <td><a href='https://arxiv.org/abs/2401.01523' target='_blank'>GOAT-Bench: Safety Insights to Large Multimodal Models through Meme-Based Social Abuse</a></td>
  </tr>
  <tr>
    <td>2023.12.13</td>
    <td>Benchmark</td>
    <td><a href='https://arxiv.org/abs/2312.11523v1' target='_blank'>ToViLaG: Your Visual-Language Generative Model is Also An Evildoer</a></td>
  </tr>
  <tr>
    <td>2023.11.29</td>
    <td>Attack, Benchmark</td>
    <td><a href='https://arxiv.org/abs/2311.17600' target='_blank'>Query-Relevant Images Jailbreak Large Multi-Modal Models</a></td>
  </tr>
  <tr>
    <td>2023.11.27</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2311.16101' target='_blank'>How Many Unicorns Are in This Image? A Safety Evaluation Benchmark for Vision LLMs</a></td>
  </tr>
  <tr>
    <td>2023.11.24</td>
    <td>Benchmark</td>
    <td><a href='https://arxiv.org/abs/2311.14580' target='_blank'>Large Language Models as Automated Aligners for benchmarking Vision-Language Models</a></td>
  </tr>
  <tr>
    <td>2023.11.16</td>
    <td>Defense, Benchmark</td>
    <td><a href='https://arxiv.org/abs/2311.10081' target='_blank'>DRESS: Instructing Large Vision-Language Models to Align and Interact with Humans via Natural Language Feedback</a></td>
  </tr>
  <tr>
    <td>2023.11.15</td>
    <td>Attack, Defense</td>
    <td><a href='https://arxiv.org/abs/2311.09127' target='_blank'>Jailbreaking GPT-4V via Self-Adversarial Attacks with System Prompts</a></td>
  </tr>
  <tr>
    <td>2023.11.09</td>
    <td>Attack, Benchmark</td>
    <td><a href='https://arxiv.org/abs/2311.05608' target='_blank'>FigStep: Jailbreaking Large Vision-language Models via Typographic Visual Prompts</a></td>
  </tr>
  <tr>
    <td>2023.10.05</td>
    <td>A finding</td>
    <td><a href='https://arxiv.org/abs/2310.03693' target='_blank'>Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!</a></td>
  </tr>
  <tr>
    <td>2023.10.04</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2310.03185' target='_blank'>Misusing Tools in Large Language Models With Visual Adversarial Examples</a></td>
  </tr>
  <tr>
    <td>2023.10.03</td>
    <td>Attack, Defense, Benchmark</td>
    <td><a href='https://arxiv.org/abs/2310.02224' target='_blank'>Can Language Models be Instructed to Protect Personal Information?</a></td>
  </tr>
  <tr>
    <td>2023.09.21</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2309.11751' target='_blank'>How Robust is Google's Bard to Adversarial Image Attacks?</a></td>
  </tr>
  <tr>
    <td>2023.09.01</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2309.00236' target='_blank'>Image Hijacks: Adversarial Images can Control Generative Models at Runtime</a></td>
  </tr>
  <tr>
    <td>2023.08.21</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2308.10741' target='_blank'>On the Adversarial Robustness of Multi-Modal Foundation Models</a></td>
  </tr>
  <tr>
    <td>2023.07.26</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2307.14539' target='_blank'>Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models</a></td>
  </tr>
  <tr>
    <td>2023.07.19</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2307.10490' target='_blank'>Abusing Images and Sounds for Indirect Instruction Injection in Multi-Modal LLMs</a></td>
  </tr>
  <tr>
    <td>2023.06.26</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2306.15447' target='_blank'>Are aligned neural networks adversarially aligned?</a></td>
  </tr>
  <tr>
    <td>2023.06.22</td>
    <td>Attack</td>
    <td><a href='https://arxiv.org/abs/2306.13213' target='_blank'>Visual Adversarial Examples Jailbreak Aligned Large Language Models</a></td>
  </tr>
</table>

## Others
<table>
  <tr>
    <th>Date</th>
    <th>Notes</th>
    <th>Title</th>
  </tr>
  <tr>
    <td>2024.03.06</td>
    <td>Real Application</td>
    <td><a href='https://arxiv.org/abs/2403.03627' target='_blank'>Multimodal Large Language Models to Support Real-World Fact-Checking</a></td>
  </tr>
  <tr>
    <td>2024.03.04</td>
    <td>Defense(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2403.01849' target='_blank'>One Prompt Word is Enough to Boost Adversarial Robustness for Pre-trained Vision-Language Models</a></td>
  </tr>
  <tr>
    <td>2024.03.04</td>
    <td>Real Application</td>
    <td><a href='https://arxiv.org/abs/2403.02253' target='_blank'>KnowPhish: Large Language Models Meet Multimodal Knowledge Graphs for Enhancing Reference-Based Phishing Detection</a></td>
  </tr>
  <tr>
    <td>2024.03.03</td>
    <td>Defense (text2img)</td>
    <td><a href='https://arxiv.org/abs/2403.01446' target='_blank'>GuardT2I: Defending Text-to-Image Models from Adversarial Prompts</a></td>
  </tr>
  <tr>
    <td>2024.02.29</td>
    <td>Attack,Benchmark,Defense(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2402.19150' target='_blank'>Typographic Attacks in Large Multimodal Models Can be Alleviated by More Informative Prompts</a></td>
  </tr>
  <tr>
    <td>2024.02.28</td>
    <td>Attack(LLMs)</td>
    <td><a href='https://arxiv.org/abs/2402.18649' target='_blank'>A New Era in LLM Security: Exploring Security Concerns in Real-World LLM-based Systems</a></td>
  </tr>
  <tr>
    <td>2024.02.26</td>
    <td>Attack(LLM-Driven Web Agents)</td>
    <td><a href='https://arxiv.org/abs/2402.16965' target='_blank'>WIPI: A New Web Threat for LLM-Driven Web Agents</a></td>
  </tr>
  <tr>
    <td>2024.02.26</td>
    <td>Attack(LLMs)</td>
    <td><a href='https://arxiv.org/abs/2402.16822' target='_blank'>Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts</a></td>
  </tr>
  <tr>
    <td>2024.02.23</td>
    <td>Safety in Human-AI Collaboration</td>
    <td><a href='https://arxiv.org/abs/2402.15350' target='_blank'>Farsight: Fostering Responsible AI Awareness During AI Application Prototyping</a></td>
  </tr>
  <tr>
    <td>2024.02.22</td>
    <td>Attack(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2402.14899' target='_blank'>Stop Reasoning! When Multimodal LLMs with Chain-of-Thought Reasoning Meets Adversarial Images</a></td>
  </tr>
  <tr>
    <td>2024.02.21</td>
    <td>Attack(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2402.13851' target='_blank'>VL-Trojan: Multimodal Instruction Backdoor Attacks against Autoregressive Visual Language Models</a></td>
  </tr>
  <tr>
    <td>2024.02.19</td>
    <td>Defense(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2402.12336' target='_blank'>Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models</a></td>
  </tr>
  <tr>
    <td>2024.02.15</td>
    <td>Attack(Robustness;Robotics)</td>
    <td><a href='https://arxiv.org/abs/2402.10340' target='_blank'>On the Safety Concerns of Deploying LLMs/VLMs in Robotics: Highlighting the Risks and Vulnerabilities</a></td>
  </tr>
  <tr>
    <td>2024.02.08</td>
    <td>Survey</td>
    <td><a href='https://arxiv.org/abs/2402.05355' target='_blank'>A Survey on Safe Multi-Modal Learning System</a></td>
  </tr>
  <tr>
    <td>2024.02.07</td>
    <td>Benchmark(LLM)</td>
    <td><a href='https://arxiv.org/abs/2402.05044' target='_blank'>SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models</a></td>
  </tr>
  <tr>
    <td>2024.02.02</td>
    <td>Real Application</td>
    <td><a href='https://arxiv.org/abs/2402.18587' target='_blank'>At the Dawn of Generative AI Era: A Tutorial-cum-Survey on New Frontiers in 6G Wireless Intelligence</a></td>
  </tr>
  <tr>
    <td>2024.02.01</td>
    <td>Attack(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2402.00626' target='_blank'>Vision-LLMs Can Fool Themselves with Self-Generated Typographic Attacks</a></td>
  </tr>
  <tr>
    <td>2023.12.06</td>
    <td>Attack(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2312.03777' target='_blank'>On the Robustness of Large Multimodal Models Against Image Adversarial Attacks</a></td>
  </tr>
  <tr>
    <td>2023.12.07</td>
    <td>Attack(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2312.07553' target='_blank'>Hijacking Context in Large Multi-modal Models</a></td>
  </tr>
  <tr>
    <td>2023.12.04</td>
    <td>Attack(Robustness)</td>
    <td><a href='https://arxiv.org/abs/2312.01886' target='_blank'>InstructTA: Instruction-Tuned Targeted Attack for Large Vision-Language Models</a></td>
  </tr>
</table>
