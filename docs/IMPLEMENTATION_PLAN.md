# QuantGPT Agentic — Implementation Plan

> **Purpose:** Build an Agentic AI investment advisor platform while learning each technology. Target: Wells Fargo Python & GenAI role. All resources free (Ollama, LangGraph, FastAPI, Kafka).

---

## Part 1: Skills Map

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     SKILLS MAP: EXISTING vs NEW                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│  YOU ALREADY KNOW (leverage this)                                                │
│  ├── Python, numpy, pandas, sklearn                                               │
│  ├── ML/DL concepts (models, training, evaluation)                               │
│  ├── Data pipelines, preprocessing                                               │
│  └── Mathematical intuition (optimization, probability)                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│  NEW – LEARN WHILE BUILDING                                                      │
│  ├── Agentic AI     → Agents, tools, planning, multi-agent orchestration         │
│  ├── LLM APIs       → Prompting, token limits, context windows                   │
│  ├── LangGraph      → State machines for agent workflows                         │
│  ├── FastAPI        → Async HTTP, OpenAPI, dependency injection                  │
│  ├── Kafka          → Producers, consumers, topics, event-driven design          │
│  ├── AgentOps       → Observability, structured logging, metrics                │
│  └── Python OOP     → SOLID, design patterns in production code                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Part 2: Branching Strategy

```
main (production-ready, always deployable)
  │
  ├── develop (integration branch, working state)
  │     │
  │     ├── feature/project-scaffolding    ← Phase 1
  │     ├── feature/fastapi-foundation     ← Phase 2
  │     ├── feature/single-agent           ← Phase 3
  │     ├── feature/multi-agent            ← Phase 4
  │     ├── feature/kafka-integration      ← Phase 5
  │     ├── feature/agentops               ← Phase 6
  │     └── feature/polish-docs            ← Phase 7
  │
  └── release/v1.0.0 (final QA before merge to main)
```

### Workflow

1. **Branch from `develop`:** `git checkout develop && git pull && git checkout -b feature/single-agent`
2. **Small commits:** One logical change per commit. Example: `feat(agents): add ResearchAgent with fetch_news tool`
3. **Merge:** Push, open PR into `develop`, merge when done.
4. **Release:** Branch `release/v1.0.0` from `develop`, test, merge to `main` and `develop`.

### Commit Convention (Conventional Commits)

```
feat(scope): add feature X
fix(scope): fix bug Y
docs: update README
refactor(agents): extract BaseAgent
test(api): add recommendation endpoint test
```

---

## Part 3: Phased Implementation

| Phase | Branch | Duration | Status |
|-------|--------|----------|--------|
| 0 | *(setup)* | 1-2 days | ⬜ |
| 1 | feature/project-scaffolding | 2-3 days | ✅ |
| 2 | feature/fastapi-foundation | 2-3 days | ✅ |
| 3 | feature/single-agent | 4-5 days | ⬜ |
| 4 | feature/multi-agent | 5-6 days | ⬜ |
| 5 | feature/kafka-integration | 4-5 days | ⬜ |
| 6 | feature/agentops | 3-4 days | ⬜ |
| 7 | feature/polish-docs | 2-3 days | ⬜ |

---

### Phase 0: Setup & Prerequisites (Before Coding)

**Duration:** 1-2 days

**Actions:**
- [ ] Create `develop` from `main`
- [ ] Install Ollama, pull `llama3.2` or `mistral`, test a prompt
- [ ] Ensure `docs/` exists and you've read this plan

**Learn:**
- **LLM basics:** Context window, tokens, temperature
- **Ollama:** Local inference, `http://localhost:11434/v1/chat/completions`
- **LangChain:** `ChatOllama`, messages format

**Checkpoint:** You can send a prompt to Ollama and get a response. You understand tokens and temperature.

---

### Phase 1: Project Scaffolding & OOP Foundation

**Duration:** 2-3 days | **Branch:** `feature/project-scaffolding`

**Goal:** Clean project structure and Python OOP for agents.

**Learn:**
- **SOLID:** Single Responsibility, Open/Closed, Dependency Inversion
- **ABC:** Abstract base classes (`ABC`, `abstractmethod`)
- **Dependency injection:** Inject `LLM` into agents, don't hardcode

**Build:**
- [x] `src/quantgpt/agents/base.py` — `BaseAgent`, `BaseTool` ABCs
- [x] `src/quantgpt/tools/` — directory, implement `CalculatorTool` as example
- [x] Unit tests for base classes and tools

**Flow:** `BaseTool (protocol) → BaseAgent (calls tools) → Concrete Agent (implements logic)`

**Document:** Add "Agent Layer Design" to `docs/ARCHITECTURE.md` with a class diagram. ✅

**Interview angle:** *"I used abstract base for agents so any new agent (Research, Portfolio, Risk) simply extends it. Tools are pluggable via dependency injection."*

---

### Phase 2: FastAPI Foundation

**Duration:** 2-3 days | **Branch:** `feature/fastapi-foundation`

**Goal:** REST API with OpenAPI, understand async.

**Learn:**
- **FastAPI:** Decorators, `Depends()`, Pydantic request/response models
- **OpenAPI:** Auto-generated docs at `/docs`, `/openapi.json`
- **Async:** When to use `async def` vs `def`, `await`

**Build:**
- [x] `src/quantgpt/api/main.py` — FastAPI app
- [x] `GET /health` — liveness
- [x] `GET /api/v1/models` — returns available models (from config)
- [x] Pydantic schemas for responses

**Flow:** `Request → FastAPI Router → Pydantic validation → Handler → Response`

**Document:** Add API section to `docs/ARCHITECTURE.md`; draw a sequence diagram for one endpoint. ✅

**Interview angle:** *"I chose FastAPI for automatic OpenAPI, Pydantic validation, and `Depends()` for injection."*

---

### Phase 3: Single Agent with LangGraph

**Duration:** 4-5 days | **Branch:** `feature/single-agent`

**Goal:** One agent (Research) with LangGraph and tools.

**Learn:**
- **LangGraph:** Nodes, edges, state, `StateGraph`
- **Prompts:** System vs user, role-based, chain-of-thought
- **Tools:** LangChain `@tool`, function calling, schema

**Build:**
- [ ] `ResearchAgent` with LangGraph:
  - Node 1: Fetch/parse news (tool)
  - Node 2: Analyze sentiment (tool)
  - Node 3: LLM summarize and produce insight
- [ ] Two tools: `fetch_market_news`, `analyze_sentiment`
- [ ] Integrate with FastAPI: `POST /api/v1/research` → run agent → return insight

**Flow:** `[START] → fetch_news → analyze_sentiment → llm_summarize → [END]`

**Document:** LangGraph state machine diagram for Research Agent in `docs/ARCHITECTURE.md`.

**Interview angle:** *"Research Agent is a 3-node graph: fetch news, analyze sentiment, LLM synthesis. LangGraph gives deterministic control flow and state."*

---

### Phase 4: Multi-Agent Orchestration

**Duration:** 5-6 days | **Branch:** `feature/multi-agent`

**Goal:** Coordinator + multiple specialist agents.

**Learn:**
- **Multi-agent:** Routing, handoffs, shared state
- **LangGraph subgraphs** or `RunnableParallel`
- **When single vs multi-agent:** Complexity vs modularity

**Build:**
- [ ] `CoordinatorAgent` — routes to Research, Portfolio, Risk
- [ ] `PortfolioAgent` — allocation suggestions
- [ ] `RiskAgent` — basic risk checks
- [ ] Orchestrator graph: Coordinator → choose agent → run subgraph → aggregate

**Flow:** `[User Query] → Coordinator (route) → Research | Portfolio | Risk → Aggregate → Response`

**Document:** Multi-agent flowchart in `docs/ARCHITECTURE.md`.

**Interview angle:** *"Coordinator decides which specialist runs. Each specialist is a subgraph. Aggregation happens at top level."*

---

### Phase 5: Kafka Event Pipeline

**Duration:** 4-5 days | **Branch:** `feature/kafka-integration`

**Goal:** Event-driven architecture with Kafka.

**Learn:**
- **Kafka:** Topics, partitions, producers, consumers, consumer groups
- **aiokafka** or **confluent-kafka-python**
- **Event-driven design:** Why vs request-response

**Build:**
- [ ] `docker-compose.yml` — Kafka + Zookeeper (or KRaft)
- [ ] Producer: Market data events → topic `market-data`
- [ ] Consumer: Listen `market-data` → trigger agent (e.g. Risk) → emit `recommendation` event
- [ ] One end-to-end flow working

**Flow:** `[External/Simulated Data] → Producer → market-data topic → Consumer → Agent → recommendation topic`

**Document:** Kafka topology diagram in `docs/ARCHITECTURE.md`.

**Interview angle:** *"Market data is produced to Kafka. Consumers trigger agents asynchronously. Recommendations go to another topic for downstream."*

---

### Phase 6: AgentOps (Observability)

**Duration:** 3-4 days | **Branch:** `feature/agentops`

**Goal:** Logging, metrics, traceability.

**Learn:**
- **Structured logging:** JSON, trace IDs, correlation
- **Prometheus:** Counters, histograms, `/metrics`
- **Debugging agents in production**

**Build:**
- [ ] `structlog` with JSON output, agent name, trace ID
- [ ] Prometheus metrics: `agent_invocations_total`, `agent_latency_seconds`, `agent_errors_total`
- [ ] `/metrics` endpoint for Prometheus scrape

**Document:** Observability diagram in `docs/ARCHITECTURE.md`.

**Interview angle:** *"Every request gets a trace ID. Logs are structured. I track invocations, latency, errors per agent."*

---

### Phase 7: Polish, Docs & Interview Prep

**Duration:** 2-3 days | **Branch:** `feature/polish-docs`

**Goal:** Professional finish, clear story.

**Build:**
- [ ] README: Purpose, setup, run instructions, architecture summary
- [ ] `docs/ARCHITECTURE.md` — Complete, with all diagrams
- [ ] `docs/INTERVIEW_PREP.md` — Update with your answers
- [ ] Docker instructions for full stack

---

## Part 4: Learning-First Workflow (Per Phase)

1. **Read first:** Short docs or tutorials for the tech (e.g., LangGraph quickstart).
2. **Minimal POC:** Build a tiny isolated example (e.g., one LangGraph node).
3. **Integrate:** Add it to QuantGPT in a clean way.
4. **Reflect:** Update `docs/LEARNING_LOG.md` — what clicked, what didn't.
5. **Explain:** Pretend you're teaching a colleague.

---

## Part 5: Estimated Timeline

| Phase | Duration | Cumulative |
|-------|----------|------------|
| 0. Setup | 1-2 days | Day 2 |
| 1. Scaffolding | 2-3 days | Day 5 |
| 2. FastAPI | 2-3 days | Day 8 |
| 3. Single Agent | 4-5 days | Day 13 |
| 4. Multi-Agent | 5-6 days | Day 19 |
| 5. Kafka | 4-5 days | Day 24 |
| 6. AgentOps | 3-4 days | Day 28 |
| 7. Polish | 2-3 days | **Day 31** |

**Total: ~4-5 weeks** at 2-3 hours/day.

---

## Quick Reference: Branch → Phase

| Branch | Phase |
|--------|-------|
| `feature/project-scaffolding` | 1. OOP Foundation |
| `feature/fastapi-foundation` | 2. FastAPI |
| `feature/single-agent` | 3. LangGraph + Research Agent |
| `feature/multi-agent` | 4. Multi-Agent Orchestration |
| `feature/kafka-integration` | 5. Kafka Pipeline |
| `feature/agentops` | 6. Observability |
| `feature/polish-docs` | 7. Polish & Interview Prep |
