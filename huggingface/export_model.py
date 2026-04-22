import os
import torch
from transformers import PreTrainedTokenizerFast

from src.models.config import ModelConfig
from src.models.model import SelfLM

from huggingface_hub import HfApi, login

# -------------------------
# STEP 4: LOAD MODEL
# -------------------------

HF_USERNAME = "Mudasir-Habib"
HF_TOKEN = os.getenv("huggingface_token")
repo_id = f"{HF_USERNAME}/selflm-tiny-v1"

api = HfApi()
api.create_repo(repo_id=repo_id, repo_type="model", exist_ok=True)

MODEL_PATH = "checkpoints/best_model.pt"
TOKENIZER_PATH = "dataset/tokenizer.json"

print("Loading model...")

model = SelfLM(ModelConfig())

checkpoint = torch.load(MODEL_PATH, map_location="cpu")

state_dict = checkpoint["model_state_dict"]

model.load_state_dict(state_dict)

model.eval()

# -------------------------
# STEP 5: LOAD TOKENIZER
# -------------------------

tokenizer = PreTrainedTokenizerFast(tokenizer_file=TOKENIZER_PATH)

# -------------------------
# STEP 6: SAVE IN HF FORMAT
# -------------------------

SAVE_DIR = "hf_model"
os.makedirs(SAVE_DIR, exist_ok=True)

print("Saving model in Hugging Face format...")

import os
import torch

os.makedirs(SAVE_DIR, exist_ok=True)

# Save model weights
torch.save(
    {
        "model_state_dict": model.state_dict(),
    },
    f"{SAVE_DIR}/pytorch_model.bin"
)

# Save config if you have it
import json

with open(f"{SAVE_DIR}/config.json", "w") as f:
    json.dump({}, f)

# Save tokenizer
tokenizer.save_pretrained(SAVE_DIR)

# Add a simple README
readme_content = """
---
license: apache-2.0
datasets:
- Mudasir-Habib/selflm-dataset
---

# 🤖 SelfLM (Tiny LLM)

SelfLM is a lightweight language model trained on a **synthetic instruction dataset**.  
It is designed for experiments, learning, and small-scale NLP tasks.

---

## 📦 Model Info

- Model Type: Tiny Causal Language Model
- Training Data: Synthetic dataset (instruction-based)
- Framework: PyTorch / Transformers
- Goal: Fast experimentation with small LLMs

---

## 📊 Dataset

This model is trained on:

👉 https://huggingface.co/datasets/Mudasir-Habib/selflm-dataset

Dataset includes:
- Instruction-style samples
- Synthetic generated conversations
- Cleaned and deduplicated records

---

## ⚙️ Installation

Install required libraries:

```bash
pip install transformers torch
"""

with open(f"{SAVE_DIR}/README.md", "w") as f:
    f.write(readme_content)

print("Uploading to Hugging Face...")

api.upload_folder(
    repo_id=repo_id,
    folder_path=SAVE_DIR
)

print(f"✅ Upload complete: https://huggingface.co/{repo_id}")
