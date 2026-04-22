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





# @dataclass
# class DatasetConfig:
#     f_name = "Muhammad"
#     m_name = "Mudasir"
#     l_name = "Habib"
#     email = "mudasirhebeb@gmail.com"
#     website = " https://mudasir-habib.web.app"
#     github = "https://github.com/Mudasirhabib123"
#     linkedIn = "https://www.linkedin.com/in/mudasir-habib-2b27b71a3"
#     stackoverflow = "https://stackoverflow.com/users/12890258/mudasir-habib"
#
#     role = ["software engineer", "backend engineer", "full-stack engineer", "ai engineer", "machine learning engineer"]
#     phone_number = "+923000044164"
#     age = "26 years"
#     locations = ["Lahore, Pakistan", "Bahawalpur, Pakistan", "Pakistan"]
#     experience = "5+ years in software development"

