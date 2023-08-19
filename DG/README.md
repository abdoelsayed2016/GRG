
## Code for Document Generator (DG)

### Introduction & Setup

To get started with the Document Generator (DG) code, follow these steps:

1. Add your OpenAI API key to `openai.api_key` (line 12) in the `utils.py` file.

### Repository Structure

```plaintext
.
├── indatasets              # Input dataset (NQ, TQA, WEBQ)
├── inprompts               # Input prompts (NQ, TQA, WEBQ)
├── outdataset              # Output dataset (NQ, TQA, WEBQ)
├── main.py                 # Main code file
├── process.py              # Processing utilities
└── utils.py                # Utility functions
### Few-shot Learning to generate Documents
Use the following command to execute the few-shot learning process for document generation:


```bash
$ python main.py --dataset [nq, tqa, webq] --split [train, dev, test] --engine [text-davinci-003, text-davinci-002] --num_sequence [10, 50] --temperature 0.5 --max_tokens [100, 200, 300]
``` 
Feel free to customize the parameters according to your needs.

