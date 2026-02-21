#!/usr/bin/env bash
# Start QuantGPT API. Ensure Ollama is running first (ollama serve, ollama pull llama3.2).

set -e
cd "$(dirname "$0")/.."
source .venv/bin/activate
exec uvicorn quantgpt.api.main:app --reload --host 0.0.0.0 --port 8000
