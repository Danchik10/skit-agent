import asyncio

from services.agent import Agent
from services.event_loader import EventLoader

from services.fake_ssh import FakeSSHClient

from llm.ollama_client import OllamaClient


async def main():

    event = EventLoader.load(
        "examples/cpu.json"
    )

    ssh = FakeSSHClient()

    llm = OllamaClient()

    agent = Agent(
        ssh=ssh,
        llm=llm
    )

    result = await agent.process(
        event
    )

    print(result.model_dump_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())