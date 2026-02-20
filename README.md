# QuantGPT

**AI-Powered Multimodal Investment Advisor**

QuantGPT is an open-source project that combines NLP, time-series forecasting and reinforcement learning to provide intelligent investment recommendations. The project is evolving into an **Agentic AI platform** with multi-agent systems, FastAPI, Kafka, and AgentOps.

## Documentation (Implementation & Learning)

| Document | Purpose |
|----------|---------|
| [Implementation Plan](docs/IMPLEMENTATION_PLAN.md) | Phased roadmap, branching strategy, phase checklists |
| [Architecture](docs/ARCHITECTURE.md) | System overview, diagrams, component descriptions |
| [Learning Log](docs/LEARNING_LOG.md) | Track learnings per phase |
| [Interview Prep](docs/INTERVIEW_PREP.md) | Project pitch, Q&A, tech one-liners |

## Features
- Real-time financial news and Twitter sentiment
- Stock price forecasting (LSTM, Prophet)
- Portfolio optimization (Reinforcement Learning)
- Interactive dashboard (Streamlit)

## Development

The codebase follows a simple `src/` layout. Core modules live under `src/quantgpt` and tests reside in `tests/`.

### Setup
1. Create a virtual environment and install the project in editable mode:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   ```
2. Run the unit tests with `pytest`:
   ```bash
   pytest
   ```

### Run the API (Phase 2+)
```bash
quantgpt-api
# or: uvicorn quantgpt.api.main:app --reload --host 0.0.0.0 --port 8000
```
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health
- Models: http://localhost:8000/api/v1/models
