from ollama import AsyncClient


class OllamaClient:

    async def summarize(
        self,
        raw_data
    ):

        client = AsyncClient(
            host="http://ollama:11434"
        )

        response = await client.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content":
                    f"""
                    Ты DevOps инженер.

                    Проанализируй данные:

                    {raw_data}

                    Верни краткий отчет.
                    """
                }
            ]
        )

        return response["message"]["content"]