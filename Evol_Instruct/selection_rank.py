import json
import pandas as pd
import numpy as np
import os
import shutil
from sklearn.preprocessing import MinMaxScaler


folder_path = 'result_1_2'
json_filenames = []
new_folder_path = 'result_1_3'

if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):  # 检查文件扩展名是否为 .json
        json_filenames.append(filename)
        
def compute_score(perplexity,diversity):
    alpha = 1
    beta = 1
    return alpha*perplexity*beta*abs(1-diversity)

for name in json_filenames:
    with open(f'{folder_path}/{name}', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(name)
    
    for i,entry in enumerate(data):
        entry['score'] = compute_score(entry['perplexity_normalized'],entry['diversity_normalized'])
        
    json_data_sorted = sorted(data, key=lambda x: x['score'], reverse=True)
    
    new_file_path = os.path.join(new_folder_path, name)
    with open(new_file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data_sorted, f, ensure_ascii=False, indent=4)

    