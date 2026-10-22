"""REST endpoints. Each route is thin: validate input, call the real logic, return JSON.

    /api/health        - is the server up?
    /api/status        - configuration summary shown on the System Status tab

Errors: our own exceptions (exceptions/) are turned into clear HTTP answers in api/main.py,
so the routes only catch what they can explain better themselves.
"""

import platform
import sys
from datetime import datetime, timezone
from functools import lru_cache

from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool

from config.settings import settings
from exceptions import MeridianError
from logger import GLOBAL_LOGGER as log
from rag import document_store

health_router = APIRouter(prefix="/api", tags=["Health"])
status_router = APIRouter(prefix="/api", tags=["Status"])


_server_start_time = datetime.now(timezone.utc)
_upload_history: list[dict] = []




@health_router.get("/health")
def health():
    return {"status": "ok", "mode": settings.app_mode}


@status_router.get("/status")
def system_status():
    """Return system configuration and health information (makes no calls to Google)."""
    uptime_seconds = int((datetime.now(timezone.utc) - _server_start_time).total_seconds())
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    cloud = settings.is_cloud

    return {
        "mode": settings.app_mode,
        "backend": {
            "status": "healthy",
            "uptime": f"{hours:02d}h {minutes:02d}m {seconds:02d}s",
            "python_version": sys.version.split()[0],
            "platform": platform.system(),
        },
        "storage": {
            "location": document_store.location(),
        },
        "vector_search": {
            "backend": "Chroma (local disk)",
            "index_id": settings.chroma_dir,
            "endpoint_id": "-",
            "stream_update": cloud,
        },
        "models": {
            "embedding": settings.local_embedding_model_name,
            "llm": settings.llm_model_name,
            "llm_framework": (
                "Gemini API (chat + embeddings) via LangChain v1"
            ),
        },
        "ingestion": {
            "uploads_this_session": len(_upload_history),
        },
    }

