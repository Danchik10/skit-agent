from models.diagnostic import DiagnosticResult


class DiskHandler:

    def __init__(self, ssh):
        self.ssh = ssh

    async def analyze(self, host):

        disk = self.ssh.execute(host, "df -h")

        folders = self.ssh.execute(
            host,
            "du -h /var --max-depth=1 | sort -hr | head"
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