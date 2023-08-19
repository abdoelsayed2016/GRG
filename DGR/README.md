

## Code for Document Generator Retriever (DGR)

### Repository Structure

```plaintext
.
├── indatasets              # Input dataset (NQ, TQA, WEBQ)
├── outdatasets             # Output dataset (NQ, TQA, WEBQ)
└── main.py                 # Main code file

### retreive generated Documents
Use the following command to retrieve generated documents using the Document Generator Retriever (DGR):

```bash
python main.py --dataset [nq, tqa, webq] --split [train, dev, test] --model_name [sentence-transformers/gtr-t5-large, sentence-transformers/all-MiniLM-L6-v2] --top_k [3, 5]
``` 
Feel free to customize the parameters according to your needs.

