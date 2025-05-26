
# llama_cpp_benchmark.py

import time
from llama_cpp import Llama

# === Config ===
MODEL_PATH = "./shared/models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
PROMPT = "Q: What is Hugging Face?\nA:"
MAX_TOKENS = 32
N_GPU_LAYERS = 16  # Try 16, 24, 33
N_THREADS = 4
N_BATCH = 32

# === Load model ===
print(f"Loading model: {MODEL_PATH}")
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_gpu_layers=N_GPU_LAYERS,
    n_threads=N_THREADS,
    n_batch=N_BATCH,
    use_mmap=True,
    use_mlock=True,
    verbose=False
)

# === Run benchmark ===
print(f"\n>>> Running with n_gpu_layers={N_GPU_LAYERS}, max_tokens={MAX_TOKENS}")

start_time = time.time()
response = llm(PROMPT, max_tokens=MAX_TOKENS, echo=True, stream=False)
end_time = time.time()

tokens_generated = len(response["choices"][0]["text"].split())
total_time = end_time - start_time
tokens_per_sec = tokens_generated / total_time

# === Output result ===
print("\n>>> Output:")
print(response["choices"][0]["text"])

print("\n>>> Benchmark Results:")
print(f"  Total time:       {total_time:.2f} sec")
print(f"  Tokens generated: {tokens_generated}")
print(f"  Speed:            {tokens_per_sec:.2f} tokens/sec")
print(f"  Prompt length:    {len(PROMPT.split())} tokens")
