# 🚀 SelfLM ONNX Deployment (Vercel)

This project contains a lightweight transformer-based LLM (SelfLM) exported to ONNX and deployed on Vercel as a serverless API.

---

# 📦 Project Flow

```
Train PyTorch Model
        ↓
Export to ONNX
        ↓
Move ONNX files to Vercel project
        ↓
Deploy FastAPI Server on Vercel
```

---

# 🧠 1. Convert PyTorch Model to ONNX

Run the following command to export the trained model:

```bash
python -m src.utils.pt_to_onnx_convertor
```

This will generate:

```
dataset/model.onnx
dataset/model.onnx.data
```

---

# 📁 2. Copy Model Files to Vercel Project

Move exported files into the Vercel deployment folder:

```bash
cp dataset/model.onnx vercel/
cp dataset/model.onnx.data vercel/
cp dataset/tokenizer.json vercel/
```

Your Vercel folder should now contain:

```
vercel/
├── model.onnx
├── model.onnx.data
├── tokenizer.json
├── main.py
├── inference/
├── requirements.txt
├── vercel.json
```

---

# ⚙️ 3. Install Vercel CLI

Install Vercel globally:

```bash
npm install -g vercel
```

---

# 🔐 4. Login to Vercel

Authenticate your account:

```bash
vercel login
```

Follow the browser login process.

---

# 🚀 5. Deploy to Vercel

Navigate to the Vercel project folder:

```bash
cd vercel
```

Deploy the project:

```bash
vercel
```

For production deployment:

```bash
vercel --prod
```

---

# 🌐 6. API Endpoints

After deployment, your API will be available at:

## Health Check

```
GET /health
```

## Chat Completion

```
POST /chat_completions
```

### Example Request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 64,
  "top_k": 50
}
```

---

# 📌 Example Response

```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you?"
      }
    }
  ]
}
```

---

# ⚠️ Notes & Limitations

* ONNX model is loaded on cold start (serverless limitation)
* Large models may increase cold start latency
* Vercel has execution time limits (~10s–30s depending on plan)
* Best for lightweight inference only

---

# 🧠 Recommended Architecture

```
Frontend (Vercel)
        ↓
FastAPI ONNX Server (VPS / Ubuntu)
        ↓
SelfLM ONNX Model
```

---

# 🏁 Summary

✔ PyTorch → ONNX conversion
✔ Model copied to Vercel
✔ Serverless API deployed
✔ Chat completion endpoint working

---

# 🎯 Author

Built with ❤️ using:

* PyTorch
* ONNX Runtime
* FastAPI
* Vercel Serverless
