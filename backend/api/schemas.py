
from pydantic import BaseModel, Field


# RAG  Schemas

class QueryRequest(BaseModel):
    query: str
    retriever_type: str = "similarity"

class QuerySource(BaseModel):
    source: str
    filename: str
    pages: list[int] = Field(default_factory=list)


class QueryResponse(BaseModel):
    answer: str
    sources: list[QuerySource] = Field(default_factory=list)


# Audit  Schemas

class AuditRequest(BaseModel):
    request_text: str

class AuditResponse(BaseModel):
    risk_result: str
    tax_result: str
    control_result: str
    cfo_memo: str
