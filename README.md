# QuantGPT

**AI-Powered Multimodal Investment Advisor**

QuantGPT is an open-source project that combines NLP, time-series forecasting and reinforcement learning to provide intelligent investment recommendations.

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
   pip install -e .
   ```
2. Run the unit tests with `pytest`:
   ```bash
   pytest
   ```
