from models.diagnostic import DiagnosticResult

class CPUHandler:

    def __init__(self, ssh):
        self.ssh = ssh

    async def analyze(self, host):

        processes = self.ssh.execute(
            host,
            "ps aux --sort=-%cpu | head -10"
        )

        return DiagnosticResult(event_type="cpu", host=host,diagnostics=processes)