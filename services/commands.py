class LinuxCommands:

    CPU_PROCESSES = (
        "ps aux --sort=-%cpu | head -10"
    )

    DISK_USAGE = (
        "df -h"
    )

    LARGE_DIRECTORIES = (
        "du -h /var --max-depth=1 | sort -hr | head"
    )

    SERVICE_STATUS = (
        "systemctl status {service}"
    )

    SERVICE_LOGS = (
        "journalctl -u {service} -n 30"
    )