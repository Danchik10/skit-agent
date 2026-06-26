import asyncio

from services.agent import Agent
from services.event_loader import EventLoader

from services.fake_ssh import FakeSSHClient

from llm.ollama_client import OllamaClient


async def main():

    events = [
        EventLoader.load("examples/cpu.json"),
        EventLoader.load("examples/disk.json"),
        EventLoader.load("examples/service.json"),
    ]

    ssh = FakeSSHClient()

    llm = OllamaClient()

    agent = Agent(
        ssh=ssh,
        llm=llm
    )

    for event in events:
        result = await agent.process(event)

        print(result.model_dump_json(indent=4))



if __name__ == "__main__":
    asyncio.run(main())