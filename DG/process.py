import os
import json
from utils import run_main, load_data
def process_generate_document(dataset, split, max_tokens, engine, prompt, pid, n, temp):
    input_file = f'indatasets/{dataset}/{dataset}-{split}.jsonl'
    input_data = load_data(input_file)

    
    output_folder = f'outdataset/{dataset}'
    os.makedirs(output_folder, exist_ok=True)
    output_file = f'{output_folder}/{dataset}-{split}.json'

    run_main(input_data, output_file, engine, prompt, max_tokens, n, temp)
