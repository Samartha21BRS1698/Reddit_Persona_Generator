# code to generate persona from Huggingface free public LLM
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

model_name = "google/flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def call_llm(prompt: str) -> str:
    print("🧠 Generating persona with FLAN-T5 (CPU)...")

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    output = model.generate(
        **inputs,
        max_new_tokens=512,  # you can go up to ~1024
        do_sample=True,
        top_k=50,
        top_p=0.9
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)
