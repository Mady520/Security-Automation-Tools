import psutil
import logging

logging.basicConfig(
    filename = "Security_alerts.log",
    level = logging.WARNING,
    format = "%(asctime)s - %(levelname)s - %(message)s")

def monitor_system():
    suspicious_process =["......."] #Programs you will here here will be monitored for alerts! and should be written in lower case!
    alerted_pids =set()

    print("Starting System Monitor .... Alerts will be saved to 'Security_alerts.log'. ")

    try:
       while True:
          CPU_usage = psutil.cpu_percent(interval=1)
          memory = psutil.virtual_memory().percent
        
        
          print(f"CPU: {CPU_usage}%,|Memory : {memory}%")

          for proc in psutil.process_iter(['pid','name']):
            try:
               proc_name = proc.info['name'].lower() if proc.info['name'] else ""
               pid =  proc.info['pid']

               if proc_name in suspicious_process and pid not in alerted_pids:
                alert_msg = f"Suspicious process :{proc.info['name']}(PID : {pid})"
                print(f"[!] ALERT! {alert_msg}")

                logging.warning(alert_msg)

                alerted_pids.add(pid)


            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
               pass

    except KeyboardInterrupt:
          print("\nMOnitoring stopped by user.")

if __name__ == "__main__":
   monitor_system()          
              
                

