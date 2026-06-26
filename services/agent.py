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

        self.llm = llm

        self.handlers = {
            "cpu": CPUHandler(ssh),
            "disk": DiskHandler(ssh),
            "service": ServiceHandler(ssh)
        }

    async def process(self, event) -> AnalysisResult:

        logger.info(f"Получено событие: {event.message}")

        event_type = self.router.detect(event)

        logger.info(f"Тип события: {event_type}")

        handler = self.handlers.get(event_type)

        if handler is None:
            logger.warning("Не найден обработчик события.")

            return AnalysisResult(
                success=False,
                event_type=event_type,
                host=event.interface_ip,
                summary=f"Для события '{event_type}' обработчик отсутствует."
            )

        try:

            logger.info("Запуск диагностики...")

            diagnostic = await handler.analyze(
                event.interface_ip
            )

            logger.info("Диагностика завершена.")

            prompt = PromptBuilder.build(
                diagnostic
            )

            logger.info("Отправка данных в LLM...")

            analysis = await self.llm.analyze(
                diagnostic,
                prompt
            )

            logger.info("Ответ от LLM получен.")

            return analysis

        except Exception as e:

            logger.exception(e)

            return AnalysisResult(
                success=False,
                event_type=event_type,
                host=event.interface_ip,
                summary=str(e)
            )