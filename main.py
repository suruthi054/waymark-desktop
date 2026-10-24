import os
import sys
import json

def load_config(path):
    if not os.path.exists(path): return {}
    with open(path, 'r', encoding='utf-8') as f: return json.load(f)

if __name__ == '__main__':
    print('Loaded', len(load_config('config.json')))
