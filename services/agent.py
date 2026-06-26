from models.analysis import AnalysisResult
from services.logger import logger
from services.prompt_builder import PromptBuilder

from handlers.cpu_handler import CPUHandler
from handlers.disk_handler import DiskHandler
from handlers.service_handler import ServiceHandler

from services.router import EventRouter


class Agent:

    def __init__(self, ssh, llm):

        self.router = EventRouter()

        self.ssh = ssh

        self.llm = llm

    async def process(self, event):

        logger.info(f"Получено событие: {event.message}")

        event_type = self.router.detect(event)

        logger.info(f"Тип события: {event_type}")

        if event_type == "cpu":
            handler = CPUHandler(self.ssh)

        elif event_type == "disk":
            handler = DiskHandler(self.ssh)

        elif event_type == "service":
            handler = ServiceHandler(self.ssh)

        else:

            return AnalysisResult(
                success=False,
                event_type="unknown",
                host=event.interface_ip,
                summary="Неизвестный тип события."
            )

        try:

            diagnostic = await handler.analyze(
                event.interface_ip
            )

            prompt = PromptBuilder.build(
                diagnostic
            )

            result = await self.llm.analyze(
                diagnostic,
                prompt
            )

            result.success = True

            logger.info("Анализ успешно завершен")

            return result

        except Exception as e:

            logger.exception(e)

            return AnalysisResult(
                success=False,
                event_type=event_type,
                host=event.interface_ip,
                summary=str(e)
            )