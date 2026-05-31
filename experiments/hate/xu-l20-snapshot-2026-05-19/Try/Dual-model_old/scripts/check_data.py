import json
import os

DATA_DIR = "/data/chenjt/hate/DATA"

def check_dataset(name: str):
    path = os.path.join(DATA_DIR, name, "processed")
    for split in ["train", "valid", "test"]:
        f = os.path.join(path, f"{split}.json")
        if os.path.exists(f):
            data = json.load(open(f))
            toxic = sum(1 for d in data if d['class'] == 'toxic')
            print(f"{name}/{split}: {len(data)} samples, {toxic} toxic")
        else:
            print(f"{name}/{split}: FILE NOT FOUND")

if __name__ == "__main__":
    check_dataset("IHC")
    check_dataset("SBIC")