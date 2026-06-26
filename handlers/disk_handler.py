from models.diagnostic import DiagnosticResult
from services.commands import LinuxCommands

class DiskHandler:

    def __init__(self, ssh):
        self.ssh = ssh

    async def analyze(self, host):

        disk = self.ssh.execute(host, LinuxCommands.DISK_USAGE)

        folders = self.ssh.execute(
            host,
            LinuxCommands.LARGE_DIRECTORIES
        )

        diagnostics = f"""
=== Disk ===

{disk}

=== Large folders ===

{folders}
"""

        return DiagnosticResult(
            event_type="disk",
            host=host,
            diagnostics=diagnostics
        )