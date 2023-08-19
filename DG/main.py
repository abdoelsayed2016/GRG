import argparse
import os
import json
from process import process_generate_document
from utils import load_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # Required parameters
    parser.add_argument("--dataset", default=None, type=str, required=True,
        help="dataset name: [nq, tqa, webq]",
    )
    parser.add_argument("--split", default=None, type=str, required=True,
        help="dataset split: [train, dev, test]",
    )
    
    parser.add_argument("--engine", default='text-davinci-003', type=str, required=False,
        help="text-davinci-003 (used in our experiments), code-davidnci-003",
    )
    parser.add_argument("--num_sequence", default=1, type=int, required=False)
    parser.add_argument("--temperature", default=0, type=float, required=False)
    parser.add_argument("--max_tokens", default=300, type=float, required=False)
    args = parser.parse_args()

    


    
    prompt_lines = load_data(f'inprompts/{args.dataset}.jsonl')

    for line in prompt_lines:
        if args.dataset != line.get('dataset'):
            continue 
        prompt, pid = line['prompt'], line['pid']
        process_generate_document(args.dataset, args.split, args.max_tokens, args.engine, prompt, pid, args.num_sequence, args.temperature)

        
        break
