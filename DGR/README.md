## Code for Document Generator Retriever(DGR)


### Structure
    .
    ├── indatasets                   # input dataset (NQ,TQA,WEBQ)
    ├── outdatasets                   # output dataset (NQ,TQA,WEBQ)
    └──main.py                      


### retreive generated Documents

```
python main.py --file_path indatasets/nq/train.json --model_name [sentence-transformers/gtr-t5-large,sentence-transformers/all-MiniLM-L6-v2] --output_filename outdatasets/nq/train.json --top_k [3,5]
``` 