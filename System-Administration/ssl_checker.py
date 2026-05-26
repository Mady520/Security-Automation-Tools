# Check SSl certificate expiry and days left 
import ssl
import socket
import sys
from datetime import datetime, timezone

def check_ssl(domain):
    context = ssl.create_default_context()
    print(f"[*] Checking SSL certificate for: {domain}")

    try:
        with socket.create_connection((domain, 443), timeout=5) as s:
           with context.wrap_socket(s, server_hostname = domain) as sock:
             cert = sock.getpeercert()
             expiry = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
             expiry = expiry.replace(tzinfo =timezone.utc)
            
             now = datetime.now(timezone.utc)
             days_left = (expiry -now).days
             if days_left <0:
                 print(f"[-]Expired : Was valid until {expiry.date()} ({abs(days_left)} days ago)")
             elif days_left <30:
                print(f"[!] WARNING: Expired in {days_left} days! (Date : {expiry.date()})")
             else:
                print(f"[+] HEALTHY: {days_left} days left (Expires: {expiry.date()})")

    except socket.gaierror:
     print("[-] ERROR: Invalid domain or DNS resolution failed.")
    except socket.timeout:
            print("[-] ERROR: Connection timed out.")
    except ssl.SSLError as e:
            print(f"[-] SSL ERROR: {e}")
    except Exception as e:
            print(f"ERROR: {e}")                
if __name__ == "__main__":
    if len(sys.argv) >1:
        target_domain =sys.argv[1]
        check_ssl(target_domain)
    else:
        print("Usage :python ssl_checker.py <domain_name>")  
        print("Example: python ssl_checker.py google.com")             