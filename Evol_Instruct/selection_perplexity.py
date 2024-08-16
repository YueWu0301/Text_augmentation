from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from multiprocessing import Pool, cpu_count
import concurrent.futures
from tqdm import tqdm  # 导入 tqdm 库
import json
import os

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B")

def getp (sentence):
    encodings = tokenizer(sentence, return_tensors='pt')
    stride = 512
    seq_len = encodings.input_ids.size(1)
    max_length = 512
    prev_end_loc = 0
    nlls = []
    prev_end_loc = 0
    for begin_loc in range(0, seq_len, stride):
        end_loc = min(begin_loc + max_length, seq_len)
        trg_len = end_loc - prev_end_loc  # may be different from stride on last loop
        input_ids = encodings.input_ids[:, begin_loc:end_loc]
        target_ids = input_ids.clone()
        target_ids[:, :-trg_len] = -100

        with torch.no_grad():
            outputs = model(input_ids, labels=target_ids)

            # loss is calculated using CrossEntropyLoss which averages over valid labels
            # N.B. the model only calculates loss over trg_len - 1 labels, because it internally shifts the labels
            # to the left by 1.
            neg_log_likelihood = outputs.loss

        nlls.append(neg_log_likelihood)

        prev_end_loc = end_loc
        if end_loc == seq_len:
            break
    ppl = float(torch.exp(torch.stack(nlls).mean()))
    print(ppl)
    return ppl


folder_path = 'result_1'
json_filenames = []
def process_item(item):
    item['sentence_length'] = len(item['evol_prompt'])
    item['perplexity'] = getp(item['evol_prompt'])
    return item

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):  # 检查文件扩展名是否为 .json
        json_filenames.append(filename)

for name in json_filenames:
    print(name)
    with open(f'{folder_path}/{name}', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(process_item, data), total=len(data)))
    with open(f'{folder_path}/{name}', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    