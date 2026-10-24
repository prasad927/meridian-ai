# Meridian AI

Meridian AI is an AI-powered web application that demonstrates two practical use cases: **Retrieval-Augmented Generation (RAG)** for document question answering and **multi-agent AI workflows** for purchase auditing.

The project is built incrementally to explore how to develop, test, and integrate Agentic AI applications using Python and modern web technologies.

## Features

### 1. Document Question Answering (RAG)
- Upload PDF documents such as policies, contracts, and reports.
- Split documents into smaller text chunks and generate embeddings.
- Retrieve relevant passages using vector similarity search.
- Generate answers grounded in the retrieved document content.

### 2. AI-Powered Purchase Auditing
- Submit a purchase request for analysis.
- Use specialized AI agents for risk, tax, and accounting/control reviews.
- Allow agents to invoke tools for specific checks.
- Combine the individual reports into a final CFO-style decision memo.

### 3. Application Infrastructure
- REST APIs built with FastAPI.
- React and TypeScript frontend.
- Structured logging and environment-based configuration.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI, Pydantic |
| LLM integration | Google Gemini, LangChain |
| RAG | Embeddings, document chunking, Chroma, vector search |
| Frontend | React, TypeScript, Vite |
| Configuration | Environment variables, Pydantic Settings |

## Architecture

```text
User
  |
  v
React Frontend
  |
  v
FastAPI Backend
  |
  +---------------------+
  |                     |
  v                     v
Document Q&A         Purchase Audit
(RAG Pipeline)       (AI Agents)
  |                     |
  v                     v
Vector Search        Agent Tools
  |                     |
  v                     v
Gemini LLM           Risk / Tax / Controls
                        |
                        v
                   CFO Summary
```

## Prerequisites

Install the following before running the application:

- Python 3.12
- Node.js 20 or later
- npm
- A Google Gemini API key for live AI functionality

Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/prasad927/meridian-ai.git
cd meridian-ai
```

### 2. Set up the Python environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install the backend dependencies:

```bash
pip install -r requirements-dev.txt
```

### 3. Configure environment variables

Create your local environment file:

```bash
cp .env.example .env
```

Add your Gemini API key to `.env`:

```dotenv
APP_MODE=local
GOOGLE_API_KEY=your-gemini-api-key
```

Keep `.env` private. Never commit API keys or other secrets to GitHub.

### 4. Start the backend

Run this command from the repository root:

```bash
uvicorn api.main:app --app-dir backend --reload --port 8080
```

Open the interactive API documentation:

http://localhost:8080/docs

Check the health endpoint:

`GET /api/health`

### 5. Start the frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the frontend:

http://localhost:3000

The frontend communicates with the backend API. Start the backend before testing features that require server responses.

## Important Disclaimer

Aldermoor Industries and the accompanying sample documents are fictional. The purchase auditing workflow is an educational demonstration, not a substitute for professional tax, accounting, legal, or regulatory compliance review.


## Working Examples

### RAG Retrieval Strategy (Normal)

![Retrieval Strategy (Normal)](working_samples/RAG-retrival-normal.png "Retrieval Strategy (Normal)")


### RAG Retrieval Strategy (Multi-Query)

![Retrieval Strategy (Multi-Query)](working_samples/RAG-retrival-multi-query-1.png "Retrieval Strategy (Multi-Query)")

![Retrieval Strategy (Multi-Query)](working_samples/RAG-retrival-multi-query-2.png "Retrieval Strategy (Multi-Query)")


### RAG Retrieval Strategy (Contextual Compression)

![Retrieval Strategy (Contextual Compression)](working_samples/RAG-retrival-contextual-compression.png "Retrieval Strategy (Contextual Compression)")

### RAG Out of Context Question

![Out of context question](working_samples/RAG-out-of-context-question.png "Out of context question)")



### Multi Agent AI Workflow (Purchase Request Approved To Pay)

#### Purchase Request

```text
Purchase Request - Aldermoor Industries Global Procurement:
- Vendor: Mitsubishi Electric (Japan)
- Item: 20 spare servo motors for the Aldermoor filling line
- Total Cost: 38,000 EUR
- Origin: JP (Japan)
- Destination: DE (Aldermoor Industries, Hamburg, Germany)
- FX Rate quoted: 1 EUR = 176.5 JPY
```

#### Output (CFO Audit Memorandum Synthesised output from all specialist agents)

> **ALDERMOOR INDUSTRIES — CFO AUDIT MEMORANDUM**<br>
> **RE:** Procurement Request Audit Summary

**EXECUTIVE SUMMARY:**

This memorandum synthesises the three-point pre-procurement audit for the acquisition of 20 replacement servo motors (€38,000.00 net; €45,220.00 landed) sourced from Japan for the Hamburg filling machinery line. Unanimous clearance has been granted across Risk & Compliance (sanctions cleared, low counterparty risk), Tax & Treasury (EPA preferential tariff verified, FX variance within hedge tolerance), and Financial Control (compliant OpEx treatment under IAS 16.12/IAS 2).

**KEY FINDINGS:**

- **Risk & Compliance:** APPROVED — Full clearance across all international sanctions lists (EU/OFAC/UN/HMT/BAFA); counterparty credit score 90/100 (Low Risk); flagged as a critical-path automation supplier requiring Hamburg buffer stock.
- **Tax & Treasury:** APPROVED — Total landed cost established at €45,220.00, leveraging EU-Japan EPA 0% customs duty with €7,220.00 (19%) recoverable German Import VAT; FX rate variance (+0.56%) is well within Group Treasury’s ±5% hedge band.
- **IFRS Financial Control:** APPROVED — Validated as OpEx under IAS 16.12 / IAS 2; transaction value sits below the €50,000 threshold and requires standard operational sign-off.

**FINAL DECISION: APPROVED TO PAY**

**Reason:** All three specialist audit reports returned affirmative verdicts (APPROVED/SUCCESS) with zero anomaly flags or treasury holds. Under the Aldermoor Delegation of Authority Matrix, commercial release is authorized against GL Account Range 5xxx (Material Costs: MRO Consumables & Spare Parts) under Cost Centre 4210 (Plant Maintenance & Filling Line Assembly).

**NEXT ACTIONS:**

1. **Global Procurement & Logistics** — Issue Purchase Order under Net-30/45 terms; ensure supplier includes compliant EPA Statement on Origin/REX reference and execute standard dual-use clearance — **Deadline:** 2 business days (28 May 2024)
2. **Accounts Payable & Financial Control** — Post commitment to GL 5xxx / Cost Centre 4210 and schedule payment release upon matching commercial invoice against customs documentation — **Deadline:** Standard payment run post-invoice verification
3. **Group Tax** — Log customs documentation upon Hamburg entry to execute full €7,220.00 input tax recovery (*Vorsteuerabzug*) on the next *Umsatzsteuer-Voranmeldung* — **Deadline:** Next statutory VAT filing (10 June 2024)
4. **Plant Maintenance (Hamburg)** — Intake and log the 20 servo motors into Hamburg critical spare inventory to safeguard line uptime — **Deadline:** Immediate upon customs receipt

**Signed,**<br>
CFO Office — Aldermoor Industries, Hamburg
