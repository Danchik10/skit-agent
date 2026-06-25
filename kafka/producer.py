# import json
#
# from aiokafka import AIOKafkaProducer
# from config import settings
#
# class KafkaProducer:
#
#     def __init__(self):
#         self.producer = AIOKafkaProducer(
#             bootstrap_servers=settings.kafka_bootstrap
#         )
#
#     async def start(self):
#         await self.producer.start()
#
#     async def stop(self):
#         await self.producer.stop()
#
#     async def send(self, data: dict):
#
#         await self.producer.send_and_wait(
#             "monitoring-output",
#             json.dumps(data).encode()
#         )