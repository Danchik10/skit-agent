from pydantic import BaseModel
from datetime import datetime


class MonitoringEvent(BaseModel):
    event_id: str
    object_id: int
    object_name: str
    interface_id: int
    interface_name: str
    interface_ip: str

    app_name: str
    message: str
    summary: str
    severity: str

    timestamp: datetime