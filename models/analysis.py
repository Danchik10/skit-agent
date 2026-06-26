from pydantic import BaseModel


class AnalysisResult(BaseModel):

    success: bool

    event_type: str

    host: str

    # raw_data: str

    summary: str