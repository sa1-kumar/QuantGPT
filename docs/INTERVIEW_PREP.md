# QuantGPT — Interview Preparation

> **Purpose:** Be ready to explain the project and tech stack confidently in interviews.

---

## 2-Minute Project Pitch

**What:** QuantGPT is an AI-powered investment advisor built as an Agentic AI platform.

**Why:** I built it to demonstrate production-grade Agentic AI: multi-agent systems, FastAPI, Kafka, and AgentOps—aligned with roles like Wells Fargo's Python & GenAI Engineer.

**How:** A multi-agent system with a Coordinator that routes to Research, Portfolio, and Risk agents. LangGraph for stateful agent workflows, Kafka for event-driven pipelines, FastAPI for the API, and structured logging + Prometheus for observability.

**Tech:** LangGraph, Ollama (local LLM), FastAPI, Kafka, structlog, Prometheus. All free/open source.

---

## Common Interview Questions & Answers

### Project Deep-Dive

| Question | Answer |
|----------|--------|
| Walk me through the architecture. | FastAPI receives requests → Coordinator agent routes to Research/Portfolio/Risk → each is a LangGraph workflow with tools → responses aggregated. Kafka emits/consumes market and recommendation events. AgentOps tracks invocations, latency, errors. |
| Why LangGraph over plain LangChain? | LangGraph gives explicit state machines—deterministic control flow, easier debugging, clear node/edge model. LangChain is great for chains; LangGraph for multi-step, branching agent workflows. |
| Why Kafka? | Decouples producers (e.g. market data) from consumers (agents). Async processing, replay capability, scalable. Fits event-driven AI pipelines. |
| How do you handle agent failures? | Structured logs with trace ID, retries with backoff, graceful degradation. Prometheus metrics for error rate and latency. |
| How do you prevent hallucinations? | Tools for factual data (news, prices). Chain-of-thought prompting. Ground responses in tool outputs. |
| Why abstract base classes for agents? | Common interface, pluggable implementations, easier testing. New agents extend BaseAgent and focus on their logic. |

### Technical Deep-Dive

| Topic | Key Points |
|-------|------------|
| **FastAPI** | Async, automatic OpenAPI, Pydantic validation, `Depends()` for DI |
| **LangGraph** | `StateGraph`, nodes, edges, state, conditional routing |
| **Kafka** | Topics, partitions, producers, consumers, consumer groups, offset management |
| **AgentOps** | Trace IDs, structured JSON logs, Prometheus counters/histograms, `/metrics` |
| **OOP/SOLID** | SRP (one agent = one domain), Open/Closed (extend via new agents), DI (inject LLM, tools) |

---

## Architecture Recall (Draw from Memory)

Practice drawing:

1. **High-level:** API → Coordinator → Research | Portfolio | Risk → Ollama; Kafka in the loop
2. **Research Agent:** fetch_news → analyze_sentiment → llm_summarize
3. **Kafka flow:** Producer → market-data topic → Consumer → Agent → recommendations topic

---

## Tech Stack One-Liners

- **LangGraph:** State machine for agent workflows; nodes and edges; deterministic control flow
- **Ollama:** Local LLM inference; no API cost; OpenAI-compatible endpoint
- **FastAPI:** Async Python API framework; auto OpenAPI; Pydantic validation
- **Kafka:** Distributed event streaming; producers, consumers, topics
- **structlog:** Structured logging; JSON; context (trace ID, agent name)
- **Prometheus:** Metrics; counters, histograms; scrape-based

---

## "Tell me about a challenge" Story

*"When building the multi-agent orchestrator, routing was tricky—I needed the Coordinator to decide which specialist to invoke based on query intent. I used a simple classifier prompt first, then refined with few-shot examples. LangGraph's conditional edges made it clean: one routing node, edges to each specialist based on the decision."*

---

## Checklist Before Interview

- [ ] Run full stack locally (API, Ollama, Kafka)
- [ ] Can demo one endpoint (e.g. `/api/v1/research`)
- [ ] Can explain each file in `src/quantgpt/`
- [ ] Reviewed `docs/ARCHITECTURE.md` diagrams
- [ ] Filled `docs/LEARNING_LOG.md` with phase learnings
- [ ] Practiced 2-minute pitch out loud
