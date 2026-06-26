from interfaces.ssh_client import SSHClient


class FakeSSHClient(SSHClient):

    def execute(self, host, command):

        if command == "ps aux --sort=-%cpu | head -10":
            return """
USER       PID %CPU COMMAND
root      1453 95.2 java
root      1234 30.1 python3
"""

        if command == "df -h":
            return """
Filesystem      Size Used Avail Use%
/dev/sda1       50G 48G 2G 96%
"""

        return ""