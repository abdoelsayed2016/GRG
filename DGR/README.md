## Code for Document Generator Retriever(DGR)


### Structure
    .
    ├── indatasets                   # input dataset (NQ,TQA,WEBQ)
    ├── outdatasets                   # output dataset (NQ,TQA,WEBQ)
    └── main.py                      


### retreive generated Documents

```
python main.py --dataset [nq, tqa, webq] --split [train, dev, test] --model_name [sentence-transformers/gtr-t5-large,sentence-transformers/all-MiniLM-L6-v2]  --top_k [3,5]
``` 