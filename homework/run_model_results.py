"""Reproducible CPU generation for homework Days 1 and 4.
Run with: python homework/run_model_results.py
Requires: transformers, sentencepiece, torch.
Outputs are generated from real FLAN-T5 inference, not predetermined text.
"""
import json
import time
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

OUTPUT = Path(__file__).resolve().parent / "results"
OUTPUT.mkdir(parents=True, exist_ok=True)
MODEL = "google/flan-t5-small"
CONTEXT = "You can check your application status using its reference number."
SETTINGS = {"do_sample": False, "num_beams": 1, "max_new_tokens": 48}
QUESTIONS = [
    "How can I check my application status?",
    "What do I need to check my application status?",
    "How can I find out the status of my application?",
]

torch.set_num_threads(2)
tokenizer = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=False)
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL, trust_remote_code=False, use_safetensors=True
).to("cpu").eval()

def generate(question):
    prompt = f"Answer the question using the context.\nContext: {CONTEXT}\nQuestion: {question}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=256)
    started = time.perf_counter()
    with torch.inference_mode():
        output = model.generate(**inputs, **SETTINGS)
    elapsed = time.perf_counter() - started
    answer = tokenizer.decode(output[0], skip_special_tokens=True).strip()
    if not answer:
        raise RuntimeError("Model returned empty output")
    return {
        "question": question,
        "answer": answer,
        "input_tokens": int(inputs["input_ids"].shape[-1]),
        "output_tokens_including_special": int(output.shape[-1]),
        "inference_seconds": round(elapsed, 3),
    }

def save(name, payload):
    path = OUTPUT / name
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Saved {path}")

first = generate(QUESTIONS[0])
save("live_demo_result.json", {
    "mode": "real_local_model",
    "model": MODEL,
    "device": "cpu",
    "context": CONTEXT,
    "generation": SETTINGS,
    **first,
    "external_inference_api_calls": 0,
    "semantic_review": "Confirm the reply is supported by the context; check for invented claims.",
})

rows = []
for index, question in enumerate(QUESTIONS, 1):
    generated = first if index == 1 else generate(question)
    answer = generated["answer"].lower()
    rows.append({
        "id": f"E{index:02d}",
        **generated,
        "reference_keyword_hit": "reference" in answer and "number" in answer,
        "automatic_semantic_heuristic": (
            "Supported by synthetic context"
            if "reference number" in answer
            and not any(term in answer for term in ("fee", "cost", "tomorrow", "approved", "rejected"))
            else "Needs manual inspection: possibly incomplete or unsupported"
        ),
    })
save("evaluation_result.json", {
    "mode": "real_local_model",
    "model": MODEL,
    "device": "cpu",
    "context": CONTEXT,
    "generation": SETTINGS,
    "metric": "reference+number keyword indicator, not semantic accuracy",
    "keyword_hits": sum(row["reference_keyword_hit"] for row in rows),
    "total": len(rows),
    "external_inference_api_calls": 0,
    "billed_api_cost_usd": 0,
    "cases": rows,
    "limitation": "Three synthetic English examples cannot measure general accuracy or security.",
    "improvement": "Add diverse questions, answer-grounding checks, and negative cases.",
})
