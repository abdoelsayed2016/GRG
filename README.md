<a id="contents"></a>
# Table of Contents
<!-- MarkdownTOC -->
<!-- 
- [Requirements](#Requirements)
- [Downloading Data and Checkpoints](#downloading-data-and-checkpoints)
- [Usage](#usage)
- [Training](#training) -->
- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Document Generator (DG)](./DG)
- [Document Generator Retriever (DGR)](./DGR)
- [Citation](#Citation)
<!-- /MarkdownTOC -->

## Introduction
Welcome to the repository for [Generator-Retriever-Generator: A Novel Approach to Open-domain Question Answering](https://arxiv.org/abs/2307.11278). In this work, we present the GRG approach for tackling open-domain question answering challenges.

**GRG Approach**
<div align="center">
  <img src="images/GRG.png" alt="GRG Approach Diagram">
</div>

<!--**Comparison with Other Approaches**
<div align="center">
  <img src="images/result.png" alt="Comparison with Other Approaches">
</div>
<a id="Requirements"></a>-->

## Requirements
Make sure you have the required environment set up to run the GRG project:

```bash
$ conda create -n grg
$ conda activate grg
$ pip install -r requirements.txt
```


## [Document Generator(DG)](./DG)
In the Document Generator (DG) directory you'll encounter code designed to create documents using few-shot learning methodologies
## [Document Generator Retriever(DGR)](./DGR)
In the Document Generator (DG) directory, you'll uncover a retriever specifically crafted for the document generator, employing sentence transformers for enhanced performance.

## [Document  Retriever(DR)](./DGR)
Will be available soon................

## [LLaMA Generator](./DGR)
Will be available soon................



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
