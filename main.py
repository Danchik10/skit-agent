# import asyncio
#
# from kafka.consumer import KafkaConsumer
# from kafka.producer import KafkaProducer
#
# from services.router import EventRouter
#
# async def main():
#
#     consumer = KafkaConsumer()
#     producer = KafkaProducer()
#
#     await consumer.start()
#     await producer.start()
#
#     async for event in consumer.listen():
#
#         event_type = EventRouter.detect(
#             event
#         )
#
#         print(event_type)
#
# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio

from models.event import MonitoringEvent

from services.router import EventRouter

from handlers.cpu_handler import CPUHandler

from ssh.client import SSHClient

from llm.ollama_client import OllamaClient

TEST_EVENT = { "event_id": "019ee995",

"object_id": 157,

"object_name": "Test Server",

"interface_id": 265,

"interface_name": "eth0",

"interface_ip": "127.0.0.1",

"app_name": "monitoring",

"message": "CPU usage is high",

"summary": "status",

"severity": "critical",

"timestamp": "2026-06-21T09:48:45Z" }

async def main():

    event = MonitoringEvent.model_validate(TEST_EVENT)

    event_type = EventRouter.detect(event)

    ssh = SSHClient(

        username="root",

        password="password"

        )

    if event_type == "cpu":

        handler = CPUHandler(ssh)

        result = await handler.analyze(event.interface_ip)

        print(result)

        llm = OllamaClient()
        res = await llm.summarize(result)
        print(res)

if __name__ == "__main__":

    asyncio.run(main())