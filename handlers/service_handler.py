class ServiceHandler:

    def __init__(self, ssh):
        self.ssh = ssh

    async def analyze(
        self,
        host,
        service_name
    ):

        status = self.ssh.execute(
            host,
            f"systemctl status {service_name}"
        )

        logs = self.ssh.execute(
            host,
            f"journalctl -u {service_name} -n 30"
        )

        return {
            "status": status,
            "logs": logs
        }