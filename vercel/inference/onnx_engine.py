import os
import json
import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer

from model_config import ModelConfig


class ONNXInference:
    def __init__(self, model_path, tokenizer_path):
        self.session = ort.InferenceSession(model_path)
        self.tokenizer = Tokenizer.from_file(tokenizer_path)

        # load config (VERY IMPORTANT for consistency)
        config_path = os.path.join(os.path.dirname(model_path), "config.json")

        if os.path.exists(config_path):
            with open(config_path) as f:
                cfg = json.load(f)

            self.config = ModelConfig(
                max_seq_len=cfg.get("max_position_embeddings", cfg.get("max_seq_len", 128)),
                pad_id=cfg.get("pad_token_id", 0),
                bos_id=cfg.get("bos_token_id", 1),
                eos_id=cfg.get("eos_token_id", 2),
            )
        else:
            self.config = ModelConfig()

        self.eos_id = self.config.eos_id

    # -----------------------------
    # SAME FORMAT AS PYTORCH VERSION
    # -----------------------------
    def format_prompt(self, messages):
        parts = []
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")

            parts.append(f"<|slm_start|>{role}\n{content}<|slm_end|>")

        parts.append("<|slm_start|>assistant\n")
        return "\n".join(parts)

    # -----------------------------
    # TOP-K SAMPLING (MATCH PT)
    # -----------------------------
    def sample(self, logits, temperature=0.7, top_k=50):
        logits = logits / max(temperature, 1e-6)

        # top-k filtering
        idx = np.argpartition(logits, -top_k)[-top_k:]
        top_logits = logits[idx]

        # softmax
        probs = np.exp(top_logits - np.max(top_logits))
        probs = probs / np.sum(probs)

        return np.random.choice(idx, p=probs)

    # -----------------------------
    # GENERATION LOOP (CRITICAL FIX)
    # -----------------------------
    def generate(self, input_ids, max_tokens=64, temperature=0.7, top_k=50):
        for _ in range(max_tokens):
            outputs = self.session.run(
                None,
                {"input_ids": input_ids}
            )

            logits = outputs[0]

            next_logits = logits[:, -1, :][0]

            next_token = self.sample(
                next_logits,
                temperature=temperature,
                top_k=top_k
            )

            if next_token == self.eos_id:
                break

            input_ids = np.concatenate(
                [input_ids, np.array([[next_token]], dtype=np.int64)],
                axis=1
            )

        return input_ids

    # -----------------------------
    # CHAT COMPLETION (MATCH PT OUTPUT)
    # -----------------------------
    def chat_completion(self, messages, temperature=0.7, max_tokens=64, top_k=50):
        prompt = self.format_prompt(messages)

        input_ids = self.tokenizer.encode(prompt).ids
        prompt_len = len(input_ids)

        input_ids = np.array([input_ids], dtype=np.int64)

        output_ids = self.generate(
            input_ids,
            max_tokens=max_tokens,
            temperature=temperature,
            top_k=top_k
        )

        # decode ONLY new tokens (same as PT version)
        new_tokens = output_ids[0][prompt_len:]

        text = self.tokenizer.decode(new_tokens.tolist())

        # cleanup (same logic as PyTorch version)
        if "<|slm_end|>" in text:
            text = text.split("<|slm_end|>")[0]

        if "<|slm_start|>" in text:
            text = text.split("<|slm_start|>")[0]

        return {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": text.strip()
                    }
                }
            ]
        }
