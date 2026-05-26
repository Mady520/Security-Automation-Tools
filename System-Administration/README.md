# System Administration

This folder contains automated operational scripts to maintain infrastructure health and secure configurations.

#### `log_mover.py`
An automated archiving tool that rotates old log files based on modification dates. 
* **Features:** Includes directory collision protection (prevents overwriting existing backups) and graceful exception handling for file locks or `PermissionError`.
* **Usage:** `python log_mover.py <source_dir> <dest_dir> [days_old]`

#### `ssl_checker.py`
A certificate health monitor that checks external domains over port 443 to calculate exact days remaining until SSL certificate expiration.
* **Features:** Utilizes Python's native `ssl` and `socket` libraries with built-in timeouts and DNS resolution error handling.
* **Usage:** `python ssl_checker.py google.com`