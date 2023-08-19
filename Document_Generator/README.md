## Code for Document Generator(DG)

### Introduction & Setup


- Add your OpenAI API key at `openai.api_key` (line 12) in `utils.py`

### Structure
    .
    ├── indatasets                   # input dataset (NQ,TQA,WEBQ)
    ├── inprompts                    # input prompts (NQ,TQA,WEBQ)
    ├── outdataset                   # output dataset (NQ,TQA,WEBQ)
    ├── main.py                      
    ├── process.py                   
    └── utils.py

### Few-shot Learning to generate Documents

```
python main.py --dataset [nq,tqa,webq] --split [train, dev, test] --engine [text-davinci-003,text-davinci-002] --num_sequence [10,50] --temperature 0.5  --max_tokens [100,200,300]
``` 