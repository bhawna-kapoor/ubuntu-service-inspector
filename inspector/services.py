import subprocess
import json

def list_services(failed_only=False):
    """Fetches a list of services from systemctl."""
    command = ["systemctl", "list-units", "--type=service", "--all", "--output=json", "--no-legend"]

    if failed_only:
        command.append("--state=failed")

    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def get_service_status(service_name):
    """Fetches the status of a service from systemctl"""
    command = ["systemctl", "status", service_name]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout