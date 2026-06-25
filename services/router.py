class EventRouter:

    @staticmethod
    def detect(event):

        msg = event.message.lower()

        if "disk" in msg:
            return "disk"

        if "cpu" in msg:
            return "cpu"

        if "down" in msg:
            return "service"

        return "unknown"