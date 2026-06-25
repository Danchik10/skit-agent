# import json
#
# from aiokafka import AIOKafkaConsumer
#
# from models.event import MonitoringEvent
# from config import settings
#
# class KafkaConsumer:
#
#     def __init__(self):
#         self.consumer = AIOKafkaConsumer(
#             "monitoring-input",
#             bootstrap_servers=settings.kafka_bootstrap,
#             group_id="skit-agent-group",
#         )
#
#     async def start(self):
#         await self.consumer.start()
#
#     async def stop(self):
#         await self.consumer.stop()
#
#     async def listen(self):
#         async for msg in self.consumer:
#             yield MonitoringEvent.model_validate_json(
#                 msg.value.decode()
#             )