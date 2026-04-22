from dataclasses import dataclass


@dataclass
class ModelConfig:
    vocab_size: int = 4096
    max_seq_len: int = 128
    d_model: int = 384
    n_layers: int = 6
    n_heads: int = 6
    ffn_hidden: int = 768
    dropout: float = 0.1

    # Special tokens
    pad_id: int = 0
    bos_id: int = 1  # <|slm_start|>
    eos_id: int = 2  # <|slm_end|>




class Config:
    dataset_dir = 'dataset'
    training_file_name = 'train.jsonl'
    eval_file_name = 'eval.jsonl'

    training_openai_file_name = 'train_openai.jsonl'
    eval_openai_file_name = 'eval_openai.jsonl'

    start_token = "<|slm_start|>"
    end_token = "<|slm_end|>"
    pad_token = "<pad>"