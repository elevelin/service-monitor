# 🛡️ Service Uptime Monitor with Log Rotation (Python)

A lightweight Python CLI tool that checks if critical services (like `nginx`, `docker`, `sshd`) are running on your system, logs the status with timestamps, and automatically rotates logs when they grow too large.

---

## ✅ Features

- ✅ Check service status using `systemctl`
- ✅ Log results with timestamps to `logs/service-monitor.log`
- ✅ Auto-rotate logs >1MB with date-stamped backup
- ✅ Accepts one or more services via command line
- ✅ Zero dependencies – works with Python 3 built-ins
- ✅ GitHub-safe and ready for cron automation

---

## 🚀 Usage

### 1. Clone the repo

```bash
git clone https://github.com/elevelin/service-monitor.git
cd service-monitor
```
### 2. Run the monitor
```bash

python3 service_monitor.py --services nginx docker sshd
```
Output Example
```csharp

[OK] nginx is running
[OK] docker is running
[FAIL] sshd is not running
```
## 📁 Directory Structure
```bash

service-monitor/
├── service_monitor.py     # Main script
├── logs/                  # Log files (auto-rotated)
├── README.md
└── .gitignore             # Excludes logs/
```

##🔧 How Log Rotation Works

If logs/service-monitor.log exceeds 1MB, it is renamed with a timestamp (e.g. service-monitor.log.20250520-140305.bak)

A fresh log file is then started

## 🧠 Why This Project?

This tool is ideal for:

-Keeping tabs on critical services

-Running as a cron job on servers or Raspberry Pi

-Demonstrating Python automation, logging, and system control skills

## 🛠️ To-Do / Future Ideas
-Add alerting via email or Slack webhook

-Use ps as a fallback for macOS support

-Add CSV export or uptime reporting


