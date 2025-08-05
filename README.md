# llama-cpp-python-benchmark

# 🧠 Mistral 7B Python Benchmark on MacBook M1 (8GB RAM)

**Run and tweak Mistral-7B-Instruct locally using `llama-cpp-python` — no CLI, no cloud, just Python.**

---

## ⚡ Why This Approach?

This repo uses [`llama-cpp-python`](https://github.com/santhoshnumberone/llama-cpp-python-benchmark/tree/main), a Pythonic wrapper over `llama.cpp`, instead of the C++ CLI. Why?

- ✅ Simpler to install and run (especially on macOS)
- ✅ No CMake build or CLI argument hassle
- ✅ Python-native scripting = easier benchmarking, tweaking, automation
- ✅ Full Metal (GPU) acceleration support on Apple Silicon

---

## 🛠️ Installation

> Tested on MacBook Pro M1 (8GB RAM), macOS Ventura, Python 3.10+

1. **Install Python + pip** (if not already)

2. **Install llama-cpp-python with Metal support**:

```bash
CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python
```
## Download the model (Q4_K_M 4-bit quantized)

Get the .gguf model from TheBloke on Hugging Face:
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF

Example:
```
mkdir models/
# Place your downloaded .gguf model here, e.g.:
mv mistral-7b-instruct-v0.1.Q4_K_M.gguf models/
```
## 🚀 How to Run the Benchmark
Inside 
```
# === Config ===
MODEL_PATH = "./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf" #Your local .gguf path
PROMPT = "Q: What is Hugging Face?\nA:"
MAX_TOKENS = 32
N_GPU_LAYERS = 16  # Try 16, 24, 33
N_THREADS = 4
N_BATCH = 32
```
Run the script with desired `n_gpu_layers` and `max_tokens`:

```
python llama_cpp_benchmark.py
```
## 📤 What the Output Means
After running, you'll see:
```
>>> Output:
Q: What is Hugging Face?
A: Hugging Face is a company...

>>> Benchmark Results:
  Total time:       6.28 sec
  Tokens generated: 33
  Speed:            5.25 tokens/sec
  Prompt length:    6 tokens
```

### How to Interpret:
 - **Total time:** End-to-end generation time (wall clock)
 - **Tokens generated:** New tokens produced by the model
 - **Speed:** Tokens/sec → Higher = faster
 - **Prompt length:** Number of tokens in your input prompt

> ✅ Speeds >10 tokens/sec feel reasonably responsive
> 
> 🧠 Higher gpu_layers = better quality, but more memory usage

## 🔧 Tweak & Test

Edit the script or pass different arguments to:
 - Benchmark different max_tokens values (e.g. 32 vs 64)
 - See how n_gpu_layers affects speed vs quality
 - Try your own prompts





