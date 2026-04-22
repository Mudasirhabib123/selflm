import os
from datasets import load_dataset
from dotenv import load_dotenv
load_dotenv('.env')
dataset = load_dataset(
    "json",
    data_files={
        "train": "dataset/train.jsonl",
        "validation": "dataset/eval.jsonl"
    }
)
huggingface_username = os.getenv('huggingface_username')
dataset_name = os.getenv('dataset_name')
dataset.push_to_hub(f"{huggingface_username}/{dataset_name}")