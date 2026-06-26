from models.diagnostic import DiagnosticResult
from services.commands import LinuxCommands

class CPUHandler:

    def __init__(self, ssh):
        self.ssh = ssh

    async def analyze(self, host):

        processes = self.ssh.execute(
            host,
            LinuxCommands.CPU_PROCESSES
        )

        return DiagnosticResult(event_type="cpu", host=host,diagnostics=processes)