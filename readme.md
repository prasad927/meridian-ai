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
