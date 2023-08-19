import json
import openai
import os
import time
import threading
import json
import _thread
from tqdm import tqdm
import regex
import json
import string
import unicodedata
from typing import List
import numpy as np
from collections import Counter
from rouge import Rouge
from contextlib import contextmanager
from collections import defaultdict


openai.api_key = "ADD YOUR API KEY HERE"



class TimeoutException(Exception):
    def __init__(self, msg=''):
        self.msg = msg


@contextmanager
def time_limit(seconds, msg=''):
    
    timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt:
        raise TimeoutException("Timed out for operation {}".format(msg))
    finally:
        # if the action ends in specified time, timer is canceled
        timer.cancel()


def _normalize(text):
    return unicodedata.normalize('NFD', text)



class SimpleTokenizer(object):
    ALPHA_NUM = r'[\p{L}\p{N}\p{M}]+'
    NON_WS = r'[^\p{Z}\p{C}]'

    def __init__(self):
        """
        Args:
            annotators: None or empty set (only tokenizes).
        """
        self._regexp = regex.compile(
            '(%s)|(%s)' % (self.ALPHA_NUM, self.NON_WS),
            flags=regex.IGNORECASE + regex.UNICODE + regex.MULTILINE
        )

    def tokenize(self, text, uncased=False):
        matches = [m for m in self._regexp.finditer(text)]
        if uncased:
            tokens = [m.group().lower() for m in matches]
        else:
            tokens = [m.group() for m in matches]
        return tokens


def load_data(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        if file_path.endswith('.json'):
            data = json.load(file)
        elif file_path.endswith('.jsonl'):
            data = [json.loads(line) for line in file]
        else:
            raise NotImplementedError
    if isinstance(data[0], dict) and len(data[0]) == 1 and 'prompt' in data[0]:
        data = data[1:]
    return data
def add_prompt(item, prompt):

    def rmreturn(s):
        s = s.replace('\n\n', ' ')
        s = s.replace('\n', ' ')
        return s.strip()

    query = item['question']
    prompt = prompt.replace('{query}', query)

    if item.get('output'): # background info
        backinfo = rmreturn(item['output'][0])
        prompt = prompt.replace('{background}', backinfo)

    return prompt
def run_inference(inputs_with_prompts, engine, max_tokens, num_sequence=1, temp=0):

    completions = {"choices": []}
    for _ in range(200):
        try:
            with time_limit(20, 'run gpt-3'):
                completions = openai.Completion.create(
                    engine=engine, 
                    max_tokens=max_tokens, 
                    prompt=inputs_with_prompts, 
                    temperature=temp, 
                    n=num_sequence, # num of returned sequence
                    )
                break
        except Exception as e:
            print(f"Exception caught: {str(e)}")
            time.sleep(2)

    outputs = [c["text"] for c in completions["choices"]]
    return outputs

def has_answer(answers, text, tokenizer=SimpleTokenizer()) -> bool:
    """Check if a document contains an answer string."""
    text = _normalize(text)
    text = tokenizer.tokenize(text, uncased=True)

    for answer in answers:
        answer = _normalize(answer)
        answer = tokenizer.tokenize(answer, uncased=True)
        for i in range(0, len(text) - len(answer) + 1):
            if answer == text[i: i + len(answer)]:
                return True
    return False

def run_main(inlines, outfile, engine, prompt, max_tokens, n=1, temp=0):


    data=[]
    pbar = tqdm(total = len(inlines))
    index = 0
    pbar.update(index)
    while index < len(inlines):
        inputs, answers = [], []
        inputs_with_prompts = []
        for _ in range(20):
            if index >= len(inlines): break
            input_with_prompt = add_prompt(inlines[index], prompt)
            inputs.append(inlines[index]['question']) ## a string
            answers.append(inlines[index]['answer']) ## a list of strings
            inputs_with_prompts.append(input_with_prompt)
            index += 1

        samples = defaultdict(list)
        outputs = run_inference(inputs_with_prompts, 
            engine, max_tokens, n, temp)
        for j, output in enumerate(outputs):
            samples[j//n].append(output)

        
        for i in range(len(inputs_with_prompts)):
            print()
            x = {
                    "idx": i + 1,
                    "question": inputs[i],
                    "answers": answers[i],
                    "ctxs": [{"id": f"text-davinci-{k+1:03}:001", "title": "GPT Context", "text": output, "score": 1000, "has_answer": has_answer(answers[i],output)} for k, output in enumerate(samples[i])]
            }
            data.append(x)
        
        pbar.update(len(inputs_with_prompts))
    with open(outfile, 'w', encoding='utf-8') as output_file:
            json.dump(data, output_file, indent=4, ensure_ascii=False)
    pbar.close()

