import psutil
import logging
from datetime import datetime

# Configuration
CPU_THRESHOLD = 80  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage
DISK_THRESHOLD = 80  # Disk usage percentage
LOG_FILE = 'system_health.log'

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_alert(message):
    """Log an alert message to the log file."""
    logging.warning(message)
    print(message)

def check_cpu_usage():
    """Check the CPU usage and log an alert if it exceeds the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    """Check the memory usage and log an alert if it exceeds the threshold."""
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High memory usage detected: {memory_usage}%")

def check_disk_usage():
    """Check the disk usage and log an alert if it exceeds the threshold."""
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        log_alert(f"High disk usage detected: {disk_usage.percent}% on /")

def check_running_processes():
    """Check the running processes and log an alert if any process exceeds the threshold."""
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            cpu_percent = proc.info['cpu_percent']
            memory_percent = proc.info['memory_percent']
            if cpu_percent > CPU_THRESHOLD or memory_percent > MEMORY_THRESHOLD:
                log_alert(f"High resource usage detected: PID={proc.info['pid']}, "
                          f"Name={proc.info['name']}, CPU={cpu_percent}%, Memory={memory_percent}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def main():
    logging.info("Starting system health monitoring...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    logging.info("System health check completed.")

if __name__ == '__main__':
    main()
