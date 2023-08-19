<a id="contents"></a>
# Contents
<!-- MarkdownTOC -->
<!--
- [Requirements](#Requirements)
- [Downloading Data and Checkpoints](#downloading-data-and-checkpoints)
- [Usage](#usage)
- [Training](#training)-->
- [Introduction](#Introduction)
- [Citation](#Citation)
<!-- /MarkdownTOC -->

# Introduction
[GRG Generator-Retriever-Generator: A Novel Approach to Open-domain Question Answering](https://arxiv.org/abs/2307.11278). 

## Abstract
Open-domain question answering (QA) tasks usually require the retrieval of relevant information from a large corpus to generate accurate answers. We propose a novel approach called Generator-Retriever-Generator (GRG) that combines document retrieval techniques with a large language model (LLM), by first prompting the model to generate contextual documents based on a given question. In parallel, a dual-encoder network retrieves documents that are relevant to the question from an external corpus. The generated and retrieved documents are then passed to the second LLM, which generates the final answer. By combining document retrieval and LLM generation, our approach addresses the challenges of open-domain QA, such as generating informative and contextually relevant answers. GRG outperforms the state-of-the-art generate-then-read and retrieve-then-read pipelines (GENREAD and RFiD) improving their performance at least by +5.2, +4.2, and +1.6 on TriviaQA, NQ, and WebQ datasets, respectively.

**GRG approach**
<p align="center">
  <img src="images/GRG.png">
</p>

**Comparison with other approaches**
<p align="center">
  <img src="images/result.png">
</p>
<a id="Requirements"></a>

# Requirements

<a id="Citation"></a>
# Citation

If you find these codes or data useful, please consider citing our paper as:

```
@article{abdallah2023generator,
  title={Generator-Retriever-Generator: A Novel Approach to Open-domain Question Answering},
  author={Abdallah, Abdelrahman and Jatowt, Adam},
  journal={arXiv preprint arXiv:2307.11278},
  year={2023}
}
```

