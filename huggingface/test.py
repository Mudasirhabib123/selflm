import torch
from src.models.model import SelfLM
from src.models.config import ModelConfig
from transformers import PreTrainedTokenizerFast

model = SelfLM(ModelConfig())
checkpoint = torch.load("checkpoints/best_model.pt", map_location="cpu")
model.load_state_dict(checkpoint["model_state_dict"])
model.eval()

tokenizer = PreTrainedTokenizerFast(tokenizer_file="dataset/tokenizer.json")

# simple test
input_ids = tokenizer("Hello", return_tensors="pt")["input_ids"]

with torch.no_grad():
    output = model(input_ids)

print(type(output))
print(len(output))