# Log Analysis

This folder contains utilities for threat hunting and incident response via log parsing. 

### `log_parser.py`
A memory-efficient Python script that utilizes regular expressions to scan massive text-based server logs for security events. 

**Key Features:**
* **Memory-Safe:** Uses line-by-line file iteration, allowing it to process multi-gigabyte log files without exhausting system RAM.
* **Threat Detection:** Specifically targets SSH brute-force attempts (from Linux `auth.log`) and 403 Forbidden HTTP errors.
* **CLI Integrated:** Accepts target files dynamically via command-line arguments.

**Usage:**
```bash
python log_parser.py /path/to/your/access_log.txt
```