from models.diagnostic import DiagnosticResult
from services.commands import LinuxCommands

class ServiceHandler:

    def __init__(self, ssh):
        self.ssh = ssh

    async def analyze(
        self,
        host,
        service_name: str = 'nginx'
    ):
        status = self.ssh.execute(
            host,
            LinuxCommands.SERVICE_STATUS.format(
                service=service_name
            )
        )

        logs = self.ssh.execute(
            host,
            LinuxCommands.SERVICE_LOGS.format(
                service=service_name
            )
        )

        return DiagnosticResult(
    event_type="service",
    host=host,
    diagnostics=f"""
=== STATUS ===

{status}

=== LOGS ===

{logs}
"""
)