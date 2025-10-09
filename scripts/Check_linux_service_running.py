#2. Check if a Linux Service is Running
import subprocess

def check_service(service_name):
    result = subprocess.run(["systemctl", "is-active", service_name], capture_output=True, text=True)
    if result.stdout.strip() == "active":
        print(f"{service_name} is running ✅")
    else:
        print(f"{service_name} is not running ❌")

check_service("nginx")