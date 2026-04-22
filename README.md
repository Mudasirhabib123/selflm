## ✨ Project Overview

This project demonstrates that building a language model is far simpler than it often appears. Using just a single Colab notebook, you can go from raw text to a working model in minutes—covering data creation, tokenization, architecture design, training, and inference.

The goal here isn’t massive scale, but genuine understanding. By implementing each component yourself, you gain clear insight into how everything fits together—removing the “black box” mystery behind modern large language models.

## 🤖 About SelfLM

SelfLM is a compact language model designed to simulate a personal information assistant. It generates concise responses about identity-related details such as contact information, professional background, social links, hobbies, preferences, and skills.

Trained from scratch on **60K synthetic conversations**, the entire pipeline can be executed in a Colab environment with a T4 GPU in approximately **5 minutes (~270 seconds)**. Despite its simplicity, the resulting model is lightweight enough to run efficiently even in browser-based environments.


# 🤖 SelfLM — Tiny LLM from Scratch

SelfLM is a **lightweight language model (LLM)** built from scratch using PyTorch and trained on a **synthetic instruction dataset**.

This project demonstrates the **full LLM pipeline**:

* Dataset generation
* Tokenization
* Model architecture
* Training
* Inference (CLI + Web)
* Hugging Face deployment
* ONNX export for production

---

# 🚀 Features

* Custom Transformer-based LLM
* Synthetic instruction dataset
* Chat-style prompt formatting
* CLI + Gradio + ONNX inference
* Hugging Face Model + Dataset + Space
* Vercel deployment support

---

# 📁 Project Structure

```
.
├── checkpoints/        # Trained model checkpoints
├── dataset/            # Training + evaluation data
├── hf_model/           # Hugging Face formatted model
├── huggingface/        # Scripts for HF export + Space
├── src/                # Core ML pipeline
├── vercel/             # ONNX deployment (serverless)
├── requirements.txt
└── README.md
```

---

# 🧠 Core Modules Explained

---

## 📊 `dataset/`

Contains training and evaluation data.

```
dataset/
├── train.jsonl
├── eval.jsonl
├── train_openai.jsonl
├── eval_openai.jsonl
├── tokenizer.json
```

### Files:

* `train.jsonl` → Main training dataset
* `eval.jsonl` → Validation dataset
* `*_openai.jsonl` → Chat-format datasets
* `tokenizer.json` → Tokenizer used by model

---

## 🧱 `src/models/`

Defines the LLM architecture.

```
src/models/
├── config.py
└── model.py
```

### Components:

* `ModelConfig` → Hyperparameters (layers, heads, etc.)
* `SelfLM` → Transformer-based model

  * Embeddings
  * Attention layers
  * Feed-forward blocks

---

## 🏋️ `src/training/`

Handles model training.

```
src/training/
├── config.py
└── train.py
```

### Features:

* Training loop
* Loss computation
* Checkpoint saving
* Evaluation

---

## 📦 `src/dataset/`

Data processing pipeline.

```
src/dataset/
├── config.py
├── data.py
├── data_loader.py
├── generate.py
└── prepare.py
```

### Responsibilities:

* Dataset generation
* Cleaning & formatting
* Tokenization
* Data loading

---

## 💬 `src/inference/`

CLI-based chat interface.

```
src/inference/
└── console_chat.py
```

### Features:

* Interactive chat loop
* Structured prompts
* Uses `model.generate()`

---

## 🔧 `src/utils/`

Utility tools.

```
src/utils/
└── pt_to_onnx_convertor.py
```

### Purpose:

* Convert PyTorch model → ONNX
* Used for deployment (Vercel)

---

# 🧪 Checkpoints

```
checkpoints/
├── best_model.pt
├── final_model.pt
├── config.json
```

* `best_model.pt` → best validation checkpoint
* `final_model.pt` → final trained model
* `config.json` → model configuration

---

# 🤗 Hugging Face Integration

```
huggingface/
├── export_dataset.py
├── export_model.py
├── test.py
└── selflm-demo/   # Space app
```

### Includes:

* Dataset upload script
* Model export script
* Gradio Space demo

---

## 🌐 Space (Demo App)

```
huggingface/selflm-demo/
├── app.py
├── self_inference.py
├── model.py
├── config.py
├── requirements.txt
```

### Features:

* Chat UI (Gradio)
* Uses `SelfInference`
* Loads model from HF repo

---

# ⚡ Vercel Deployment (Free, ONNX Optimized)

SelfLM can be deployed on **Vercel** using a **quantized ONNX model**, enabling fast and cost-efficient inference on the free tier.


## 📦 ONNX Assets

```id="onnx_tree"
vercel/assets/
├── model.onnx
├── model.onnx.data
└── tokenizer.json
```

---

## ⚙️ How it works

* PyTorch model → converted to ONNX
* ONNX model → optimized / quantized
* Served via lightweight inference engine
* Deployed as serverless API on Vercel

---

## 🚀 Deploy to Vercel

### 1. Install Vercel CLI

```bash id="vercel_install"
npm i -g vercel
```

---

### 2. Navigate to Vercel folder

```bash id="vercel_cd"
cd vercel
```

---

### 3. Deploy

```bash id="vercel_deploy"
vercel
```

Follow prompts:

* Link project
* Choose settings (default works)

---

### 4. Done 🎉

You’ll get:

```id="vercel_url"
https://your-project.vercel.app
```

---

## ⚡ Inference Engine

```id="onnx_engine"
vercel/inference/onnx_engine.py
```

Handles:

* Tokenization
* ONNX runtime execution
* Decoding output

---

## 💡 Notes

* Quantized ONNX model enables **free-tier deployment**
* Cold start latency may exist
* Ideal for lightweight demos / APIs

---

# 🏃‍♂️ Full Pipeline (Step-by-Step)

Follow this to run the complete SelfLM pipeline from scratch.

---

## 1️⃣ Setup Environment

```bash id="env_setup"
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

---

## 2️⃣ Generate Dataset

```bash id="generate_data"
python -m src.dataset.generate
```

Creates synthetic instruction dataset.

---

## 3️⃣ Prepare Dataset

```bash id="prepare_data"
python -m src.dataset.prepare
```

* Cleans data
* Tokenizes dataset
* Prepares training format

---

## 4️⃣ Train Model

```bash id="train_model"
python -m src.training.train
```

Outputs:

```id="train_output"
checkpoints/best_model.pt
checkpoints/final_model.pt
```

---

## 5️⃣ Run CLI Chat

```bash id="cli_chat"
python -m src.inference.console_chat
```

Interactive terminal chat with SelfLM.

---

## 6️⃣ Export to Hugging Face

```bash id="export_hf"
python -m huggingface.export_model
python -m huggingface.export_dataset
```

Uploads:

* Model
* Dataset

---

## 7️⃣ Run Web Demo (Gradio)

```bash id="run_space"
cd huggingface/selflm-demo
python app.py
```

---

## 8️⃣ Convert to ONNX (Optional)

```bash id="onnx_convert"
python -m src.utils.pt_to_onnx_convertor
```

---

## 9️⃣ Deploy to Vercel

```bash id="deploy_vercel"
cd vercel
vercel
```

---

# 🎯 End-to-End Flow

```id="pipeline_flow"
Dataset → Tokenization → Training → Checkpoints
        → Inference (CLI / Gradio)
        → ONNX Conversion
        → Vercel Deployment
```

---

# 🚀 Result

You now have:

* ✅ Local training pipeline
* ✅ CLI chat
* ✅ Hugging Face model + Space
* ✅ Serverless deployment on Vercel

---

🔥 SelfLM is now a **complete production-ready mini LLM system**


# 🌐 Run Hugging Face Space Locally

```bash
cd huggingface/selflm-demo
pip install -r requirements.txt
python app.py
```

---

# 🚀 Hugging Face Deployment

### Model

Upload using:

```
huggingface/export_model.py
```

### Dataset

Upload using:

```
huggingface/export_dataset.py
```

### Space

Push code to Space repo:

```bash
git add .
git commit -m "update"
git push
```

---

# 🧠 How It Works

1. Input → Tokenized
2. Tokens → Transformer model
3. Model → Next token prediction
4. Loop → Generate sequence
5. Decode → Text output

---

# ⚠️ Limitations

* Small model size
* Synthetic dataset
* Limited reasoning ability
* CPU inference is slow

---

# 🚀 Future Improvements

* Larger dataset
* Better tokenizer
* Beam search / top-p sampling
* Streaming responses
* Full Hugging Face `PreTrainedModel` support

---

# 👨‍💻 Author

**Mudasir Habib**

---

# ⭐ Contributing

Feel free to:

* Improve model
* Optimize training
* Enhance UI
* Add features

---

# 📜 License

Apache 2.0

---

# 🎯 Summary

SelfLM demonstrates:

✔ Build LLM from scratch
✔ Train on custom dataset
✔ Deploy to Hugging Face
✔ Serve via API / UI / ONNX

---

🚀 This is a complete **end-to-end LLM system**
