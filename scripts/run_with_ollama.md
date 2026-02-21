# Run QuantGPT API with Ollama

## 1. Install Ollama (if not installed)

**macOS:**
```bash
# Download from https://ollama.com/download
# Or via Homebrew:
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 2. Start Ollama

In **Terminal 1**:
```bash
ollama serve
```

## 3. Pull a model (first time only)

In **Terminal 2**:
```bash
ollama pull llama3.2
```

## 4. Stop any existing API server

If the API is already running (e.g. from a previous session), stop it with `Ctrl+C` in that terminal.

## 5. Start the QuantGPT API

In **Terminal 2** (or a new terminal):
```bash
cd /Users/sawankumar/Repositories/QuantGPT/QuantGPT
source .venv/bin/activate
quantgpt-api
```

Or:
```bash
uvicorn quantgpt.api.main:app --reload --host 0.0.0.0 --port 8000
```

## 6. Test the research endpoint

**Via curl:**
```bash
curl -X POST http://localhost:8000/api/v1/research \
  -H "Content-Type: application/json" \
  -d '{"query":"AAPL"}'
```

**Via Swagger UI:**  
Open http://localhost:8000/docs and try `POST /api/v1/research` with `{"query": "AAPL"}`.

## Expected responses

| Ollama status | HTTP status | Response |
|---------------|-------------|----------|
| Running       | 200         | `{"insight": "..."}` (LLM-generated insight) |
| Not running   | 503         | `{"detail": "Ollama is not available..."}` |
