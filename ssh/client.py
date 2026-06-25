# import paramiko
#
#
# class SSHClient:
#
#     def __init__(
#         self,
#         username,
#         password
#     ):
#         self.username = username
#         self.password = password
#
#     def execute(
#         self,
#         host,
#         command
#     ):
#
#         ssh = paramiko.SSHClient()
#
#         ssh.set_missing_host_key_policy(
#             paramiko.AutoAddPolicy()
#         )
#
#         ssh.connect(
#             host,
#             username=self.username,
#             password=self.password
#         )
#
#         stdin, stdout, stderr = ssh.exec_command(
#             command
#         )
#
#         result = stdout.read().decode()
#
#         ssh.close()
#
#         return result

class SSHClient:

    def __init__(self, username, password):

        self.username = username

        self.password = password

    def execute(self, host, command):

        print(f"SSH {host}: {command}")

        if "ps aux" in command:

            return """

    USER PID %CPU %MEM COMMAND

    root 1001 95.2 3.1 java

    root 1002 30.1 1.2 python3

    root 1003 12.5 0.8 nginx

    """

        return "command executed"