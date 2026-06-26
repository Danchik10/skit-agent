from pydantic import BaseModel


class DiagnosticResult(BaseModel):
    event_type: str
    host: str
    diagnostics: str