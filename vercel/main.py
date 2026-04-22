from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from inference.onnx_engine import ONNXInference

app = FastAPI()

engine = ONNXInference(
    model_path="assets/model.onnx",
    tokenizer_path="assets/tokenizer.json"
)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 64
    top_k: Optional[int] = 50


@app.post("/chat_completions")
def chat(req: ChatRequest):
    return engine.chat_completion(
        messages=[m.dict() for m in req.messages],
        temperature=req.temperature,
        max_tokens=req.max_tokens,
        top_k=req.top_k
    )


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)