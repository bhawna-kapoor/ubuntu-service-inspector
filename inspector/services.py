import subprocess
import json
from inspector.errors import SystemctlError

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
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        # systemctl status returns 4 if the service is not found
        if e.returncode == 4:
            return f"Service `{service_name}` not found."

        # if service is inactive (code 3), it still prints useful info to stdout.
        # returning stdout instead of crashing!
        if e.stdout:
            return e.stdout


        # for any other error
        raise SystemctlError(f"Failed to check status: {e.stderr}")