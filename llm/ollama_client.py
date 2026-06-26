from ollama import AsyncClient

from models.analysis import AnalysisResult
from models.diagnostic import DiagnosticResult


class OllamaClient:

    def __init__(self):

        self.client = AsyncClient(
            host="http://localhost:11434"
        )

    async def analyze(
        self,
        diagnostic: DiagnosticResult,
        prompt: str
    ) -> AnalysisResult:

        response = await self.client.chat(

            model="smollm2",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return AnalysisResult(
            success=True,
            event_type=diagnostic.event_type,
            host=diagnostic.host,
            summary=response["message"]["content"]
        )