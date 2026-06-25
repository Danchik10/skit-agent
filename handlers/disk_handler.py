class DiskHandler:

    def __init__(self, ssh):
        self.ssh = ssh

    async def analyze(self, host):

        df = self.ssh.execute(
            host,
            "df -h"
        )

        du = self.ssh.execute(
            host,
            "du -h /var --max-depth=1 | sort -hr | head"
        )

        return {
            "df": df,
            "du": du
        }