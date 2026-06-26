class EventRouter:

    CPU_KEYWORDS = (
        "cpu",
        "processor",
        "load"
    )

    DISK_KEYWORDS = (
        "disk",
        "space",
        "filesystem"
    )

    SERVICE_KEYWORDS = (
        "down",
        "inactive",
        "failed"
    )

    @classmethod
    def detect(cls, event):

        message = event.message.lower()

        if any(word in message for word in cls.CPU_KEYWORDS):
            return "cpu"

        if any(word in message for word in cls.DISK_KEYWORDS):
            return "disk"

        if any(word in message for word in cls.SERVICE_KEYWORDS):
            return "service"

        return "unknown"