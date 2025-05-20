import argparse
import datetime
import os
import shutil
import subprocess

LOG_DIR = "logs"
MAX_LOG_SIZE_MB = 1

def log_status(message):
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, "service-monitor.log")
    
    if os.path.exists(log_file) and os.path.getsize(log_file) > MAX_LOG_SIZE_MB * 1024 * 1024:
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.move(log_file, f"{log_file}.{timestamp}.bak")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def check_service(service):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stdout.strip() == "active":
            return True
    except Exception:
        pass
    return False

def main():
    parser = argparse.ArgumentParser(description="Check if services are running")
    parser.add_argument('--services', nargs='+', required=True, help='List of service names to check')
    args = parser.parse_args()

    for service in args.services:
        status = check_service(service)
        msg = f"[OK] {service} is running" if status else f"[FAIL] {service} is not running"
        print(msg)
        log_status(msg)

if __name__ == "__main__":
    main()

