class CPUHandler:

    def __init__(self, ssh):
        self.ssh = ssh

    async def analyze(self, host):

        top_processes = self.ssh.execute(
            host,
            "ps aux --sort=-%cpu | head -10"
        )

        return {
            "processes": top_processes
        }