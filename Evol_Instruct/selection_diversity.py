from multiprocessing import Pool, cpu_count
import concurrent.futures
from tqdm import tqdm  # 导入 tqdm 库
import json
import os
from sentence_transformers import SentenceTransformer, SimilarityFunction

model = SentenceTransformer("all-MiniLM-L6-v2")
model.similarity_fn_name = SimilarityFunction.COSINE

real_sentence = '优点：爱学习，看书，1000~2000本书，90%都看过。市场，销售财务。看书比较杂，人文。国家形式，全球的形式\
1. 对商业的趋势判断，很感兴趣。\
2. 安静的时候，能量更大。\
----中----\
多把学到应用出来，不能再看书了。要开始读无字书（人）\
卢总前两-三年都是在反腐，我管辖范围内也有出问题的。\
---待提升---\
心理素质：有时候沉不住气\
更喜欢一个人待着\
'
real_embedding = model.encode(real_sentence)

def getsimilarity(sentence):
    embedding = model.encode(sentence)
    similarities = float(model.similarity(real_embedding, embedding))
    return similarities


with open(f'result_1/one_1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def process_item(item):
    item['diversity'] = getsimilarity(item['evol_prompt'])
    return item

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(tqdm(executor.map(process_item, data), total=len(data)))

with open(f'updated_data_1.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)