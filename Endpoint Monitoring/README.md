# Endpoint Monitoring

This folder contains a lightweight Endpoint Detection and Response (EDR) utility designed to monitor active system processes without causing performance degradation.
It mainly monitors the CPU usage and memory.

### `process_monitor.py`
A persistent background script that cross-references running processes against a predefined list of suspicious executables (e.g., `winlogon.exe, svchost.exe`). 

**Key Features:**
* Uses `psutil` for cross-platform, resource-efficient system polling.
* Implements persistent file logging (`security_alerts.log`) to ensure alerts are recorded even if the terminal is cleared or the analyst is away.
* Includes duplicate-alert suppression to prevent log fatigue.

**Usage:**
```bash
python process_monitor.py
```