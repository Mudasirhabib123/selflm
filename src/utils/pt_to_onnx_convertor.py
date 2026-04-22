import os
import json
import torch

from src.models.model import SelfLM
from src.models.config import ModelConfig


def load_config(checkpoint_path):
    """
    Load config from config.json or checkpoint
    """
    config_dir = os.path.dirname(os.path.abspath(checkpoint_path))
    config_path = os.path.join(config_dir, "config.json")

    if os.path.exists(config_path):
        with open(config_path) as f:
            cfg = json.load(f)

        return ModelConfig(
            max_seq_len=cfg.get("max_position_embeddings", cfg.get("max_seq_len", 128)),
            d_model=cfg.get("hidden_size", cfg.get("d_model", 384)),
            n_layers=cfg.get("num_hidden_layers", cfg.get("n_layers", 6)),
            n_heads=cfg.get("num_attention_heads", cfg.get("n_heads", 6)),
            ffn_hidden=cfg.get("intermediate_size", cfg.get("ffn_hidden", 768)),
            dropout=cfg.get("hidden_dropout_prob", cfg.get("dropout", 0.1)),
            pad_id=cfg.get("pad_token_id", cfg.get("pad_id", 0)),
            bos_id=cfg.get("bos_token_id", cfg.get("bos_id", 1)),
            eos_id=cfg.get("eos_token_id", cfg.get("eos_id", 2)),
        )

    return ModelConfig()


def load_model(checkpoint_path, device="cpu"):
    """
    Load PyTorch model
    """
    device = torch.device(device)

    ckpt = torch.load(checkpoint_path, map_location=device)

    if isinstance(ckpt, dict) and "model_state_dict" in ckpt:
        state_dict = ckpt["model_state_dict"]
    else:
        state_dict = ckpt

    config = load_config(checkpoint_path)

    model = SelfLM(config).to(device)
    model.load_state_dict(state_dict, strict=False)
    model.eval()

    return model, config


def export_onnx(model, config, output_path="model.onnx"):
    print("🚀 Exporting to ONNX...")

    dummy_input = torch.randint(
        low=0,
        high=1000,
        size=(1, config.max_seq_len),
        dtype=torch.long
    )

    torch.onnx.export(
        model,
        dummy_input,
        output_path,
        input_names=["input_ids"],
        output_names=["logits"],
        dynamic_axes={
            "input_ids": {1: "seq_len"},
            "logits": {1: "seq_len"}
        },
        opset_version=13,
        do_constant_folding=True,
    )


def verify_onnx(output_path):
    """
    Verify ONNX model
    """
    print("🔍 Verifying ONNX model...")

    import onnx

    model = onnx.load(output_path)
    onnx.checker.check_model(model)

    print("✅ ONNX model is valid!")


def convert():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", default="checkpoints/final_model.pt")
    parser.add_argument("--output", default="model.onnx")
    parser.add_argument("--device", default="cpu")

    args = parser.parse_args()

    model, config = load_model(args.checkpoint, args.device)

    export_onnx(model, config, args.output)

    verify_onnx(args.output)


if __name__ == "__main__":
    convert()
