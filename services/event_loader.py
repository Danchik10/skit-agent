import json

from pathlib import Path

from models.event import MonitoringEvent


class EventLoader:

    @staticmethod
    def load(path: str) -> MonitoringEvent:

        with open(Path(path), encoding="utf-8") as f:
            data = json.load(f)

        return MonitoringEvent.model_validate(data)