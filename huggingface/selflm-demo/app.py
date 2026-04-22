import gradio as gr
from huggingface_hub import hf_hub_download

from self_inference import SelfInference

# -------------------------
# DOWNLOAD FROM HF
# -------------------------
REPO_ID = "Mudasir-Habib/selflm-tiny-v1"

checkpoint_path = hf_hub_download(
    repo_id=REPO_ID,
    filename="pytorch_model.bin"
)

tokenizer_path = hf_hub_download(
    repo_id=REPO_ID,
    filename="tokenizer.json"
)

# -------------------------
# LOAD ENGINE
# -------------------------
engine = SelfInference(
    checkpoint_path=checkpoint_path,
    tokenizer_path=tokenizer_path,
    device="cpu"
)


# -------------------------
# CHAT FUNCTION
# -------------------------
def chat(message, history):
    result = engine.chat_completion([{"role": "user", "content": message}])
    msg = result["choices"][0]["message"]
    return msg['content']


# -------------------------
# UI (ChatGPT style)
# -------------------------
demo = gr.ChatInterface(
    fn=chat,
    title="SelfLM Chat",
    description="Tiny LLM 8.7M params, Experiment",
    examples=[
        "What is your name?",
        "tell me a joke",
        "any advice",
        "whats your email"
    ]
)

demo.launch()
