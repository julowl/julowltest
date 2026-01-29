import os
from tqdm import tqdm
import hashlib

def get_file_hash(file_path: str) -> str:
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # Read file in chunks to avoid using too much memory
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

path = "/home/padre/yandex/Фотки"

all_files = []
for root, _ , files in os.walk(path):
    for file in files:
        all_files.append(os.path.join(root,file))

print(all_files[:5])

hash_2file = {}
for file in tqdm(all_files):
    key = get_file_hash(file)
    if key in hash_2file:
        hash_2file[key].append(file)
    else:
        hash_2file[key] = [file]

for value in hash_2file.values():
    if len(value) > 1:
        print(value)