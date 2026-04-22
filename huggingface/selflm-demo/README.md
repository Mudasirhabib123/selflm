# 🤖 SelfLM Chat (Hugging Face Space)

An interactive demo for **SelfLM**, a tiny language model trained on a synthetic dataset.
This Space allows you to chat with the model in real time.

---

## 🚀 Live Demo

👉 https://huggingface.co/spaces/Mudasir-Habib/selflm-demo

---

## 📦 Model

👉 https://huggingface.co/Mudasir-Habib/selflm-tiny-v1

---

## 📊 Dataset

👉 https://huggingface.co/datasets/Mudasir-Habib/selflm-dataset

---

# 🛠️ Setup Locally

## 1. Clone the Space repository

```bash
git clone https://huggingface.co/spaces/Mudasir-Habib/selflm-demo
cd selflm-demo
```

---

## 2. (Optional) Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run locally

```bash
python app.py
```

App will start at:

```
http://127.0.0.1:7860
```

---

# 🔄 Make Changes & Push

## 1. Modify files

Edit:

* `app.py`
* `requirements.txt`
* UI or inference logic

---

## 2. Add changes

```bash
git add .
```

---

## 3. Commit

```bash
git commit -m "update: improved UI / model logic"
```

---

## 4. Push to Hugging Face

```bash
git push
```

---

## ⚡ What happens after push?

* Hugging Face automatically rebuilds the Space
* Installs dependencies
* Runs `app.py`
* Deploys updated app

---

# 📁 Project Structure

```
selflm-demo/
├── app.py                 # Main Gradio app
├── requirements.txt       # Dependencies
├── self_inference.py      # Inference engine
├── src/
│   ├── models/
│   └── dataset/
```

---

# 🧠 Features

* Chat-based interface
* Custom inference pipeline
* Temperature & token control
* Uses structured prompt format

---

# ⚠️ Notes

* First load may be slow (model download)
* Runs on CPU (free tier)
* Model is experimental

---

# 🧑‍💻 Author

**Mudasir Habib**

---

# ⭐ Contribute

Feel free to:

* Fork the Space
* Improve UI
* Optimize model
* Add features

---

# 🚀 Future Improvements

* Streaming responses (typing effect)
* Chat history persistence
* Better decoding strategies
* Hugging Face native model conversion

---

Enjoy experimenting with SelfLM! 🚀
