"""The vector database that stores our embeddings. Which one depends on APP_MODE.

    local  -> Chroma, a vector database that saves to a folder on your disk
"""

from functools import lru_cache
from langchain_core.vectorstores import VectorStore
from config.settings import settings
from exceptions import ConfigurationError
from logger import GLOBAL_LOGGER as log
from rag.embeddings import get_embeddings


def _local_store() -> VectorStore:
    from langchain_chroma import Chroma  # imported here so cloud images do not need it loaded

    log.info("Using local Chroma vector store", path=settings.chroma_dir)
    return Chroma(
        collection_name=settings.chroma_collection,
        embedding_function=get_embeddings(),
        persist_directory=settings.chroma_dir,
    )

@lru_cache(maxsize=1)
def get_vector_store() -> VectorStore:
    """Connect on first use, so the API can start (e.g. /api/health) before anything is configured."""
    return  _local_store()
