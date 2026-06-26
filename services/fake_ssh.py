from interfaces.ssh_client import SSHClient
from services.commands import LinuxCommands


class FakeSSHClient(SSHClient):

    RESPONSES = {

        LinuxCommands.CPU_PROCESSES:
"""
USER       PID %CPU COMMAND
root      1453 95.2 java
root      1234 30.1 python3
""",

        LinuxCommands.DISK_USAGE:
"""
Filesystem Size Used Avail Use%
/dev/sda1 50G 48G 2G 96%
""",

        LinuxCommands.LARGE_DIRECTORIES:
"""
25G /var/log
12G /var/lib/docker
"""
    }

    def execute(
        self,
        host,
        command
    ):

        return self.RESPONSES.get(
            command,
            ""
        )