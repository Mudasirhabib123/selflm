## 🔗 Quick Links

[![HF Model](https://img.shields.io/badge/HF%20Model-SelfLM-blue)](https://huggingface.co/Mudasir-Habib/selflm-tiny-v1)
[![HF Dataset](https://img.shields.io/badge/HF%20Dataset-selflm--dataset-blue)](https://huggingface.co/datasets/Mudasir-Habib/selflm-dataset)
[![HF Demo](https://img.shields.io/badge/HF%20Demo-selflm--demo-blue)](https://huggingface.co/spaces/Mudasir-Habib/selflm-demo)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EyR5mFuHupJWdnJWazvdjU1Bre2rF2RD?usp=sharing)
[![Vercel Demo](https://img.shields.io/badge/Vercel%20Demo-selflm--swagger-blue)](https://selflm.vercel.app/docs)


## ✨ SelfLM — From Raw Text to a Working LLM in Minutes

Building a language model may seem complex, but it doesn’t have to be.

**SelfLM** is a compact language model built from scratch to demonstrate how the entire LLM pipeline—data generation, tokenization, architecture, training, and inference—works end-to-end. Instead of focusing on scale, this project emphasizes **clarity and understanding**, breaking down the “black box” behind modern LLMs.

Trained on **60K synthetic conversations**, the model can be built in ~**5 minutes (~270 seconds)** on a Colab T4 GPU and is lightweight enough to run even in browser-based environments.

---

## 🚀 Features

* Custom Transformer-based LLM (PyTorch)
* Synthetic instruction dataset
* Chat-style prompt formatting
* CLI + Web (Gradio) inference
* Hugging Face model, dataset & live demo
* ONNX export for fast, serverless deployment (Vercel)


# 📁 Project Structure

```
.
├── checkpoints/        # Trained model checkpoints
├── dataset/            # Training + evaluation data
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
## ⚡ Vercel Deployment (Free, ONNX Optimized)

Deploy **SelfLM** on Vercel using a quantized ONNX model for fast, low-cost inference.

**Assets**

```
vercel/assets/
├── model.onnx
├── model.onnx.data
└── tokenizer.json
```

**Flow**
PyTorch → ONNX → Quantized → Serverless API

**Deploy**

```bash
npm i -g vercel
cd vercel
vercel
```

**Output**

```
https://your-project.vercel.app
```

**Engine**
`vercel/inference/onnx_engine.py` (tokenization + ONNX runtime + decoding)

**Note**
Free-tier friendly, but expect cold starts.

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



# 🎯 Summary

SelfLM demonstrates:

✔ Build LLM from scratch
✔ Train on custom dataset
✔ Deploy to Hugging Face
✔ Serve via API / UI / ONNX

---

🚀 This is a complete **end-to-end LLM system**
