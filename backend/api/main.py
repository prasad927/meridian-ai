"""
FastAPI backend — Procurement Audit & RAG Document Intelligence
================================================================
Run locally (from the project root):
    uvicorn api.main:app --app-dir backend --reload --port 8080
Interactive API docs: http://localhost:8080/docs

Exposes REST endpoints for:
  1. Running multi-agent procurement audits       (agent/agents.py)
  2. Uploading documents into the vector store       (rag/data_ingestion.py)
     APP_MODE=local -> Chroma on disk, APP_MODE=cloud -> Vertex AI Vector Search
  3. Querying the RAG pipeline                    (rag/retrieval.py)
In Docker / Cloud Run the same server also serves the built React app.
"""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from api.endpoints import agent_router, health_router, rag_router, status_router
from config.settings import settings
from exceptions import ConfigurationError, IngestionError
from logger import _LOGGER_INSTANCE
from logger import GLOBAL_LOGGER as log


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Meridian AI starting", mode=settings.app_mode, llm=settings.llm_model_name)
    yield  # the app runs here



app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Multi-agent procurement audit & RAG document intelligence backend.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health_router)
app.include_router(status_router)
