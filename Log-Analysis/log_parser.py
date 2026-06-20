import re
import sys
import os


def parse_logs(log_file):
    ssh_pattern = r"Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)"

    http_403_pattern = r"(\d+\.\d+\.\d+\.\d+) .*? \"(?:GET|POST) .*?\" 403"

    if not os.path.exists(log_file):
        print(f"[-] ERROR: The file '{log_file} does not exist.")
        return
    print(f"[*] Scanning '{log_file}' for security events...\n ")

    with open(log_file, 'r') as file:
        for line_num, line in enumerate(file,1):

            ssh_match = re.search(ssh_pattern, line)
            if ssh_match:
                user = ssh_match.group(1)
                ip = ssh_match.group(2)
                print(f"[Line {line_num}] SSH Failed Login - User: {user}, IP: {ip}")

            http_match = re.search(http_403_pattern, line)
            if http_match:
                ip = http_match.group(1)
                print(f"[Line {line_num}] Web 403 Forbidden Alert - IP: {ip}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        parse_logs(target_file)
    else:
        print("You forgot to give the path!")
        print("Usage: python log_parser.py <path _to_log_file>")
        sys.exit(1)         
