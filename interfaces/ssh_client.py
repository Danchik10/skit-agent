from abc import ABC, abstractmethod


class SSHClient(ABC):

    @abstractmethod
    def execute(
        self,
        host: str,
        command: str
    ) -> str:
        pass