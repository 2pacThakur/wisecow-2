# System Health Monitoring Script

This script monitors the health of a Linux system by checking CPU usage, memory usage, disk space, and running processes. Alerts are logged if any metrics exceed predefined thresholds.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/system-health-monitor.git
    cd system-health-monitor
    ```

2. **Install Dependencies**:
    ```sh
    pip install psutil
    ```

## Configuration

Edit `system_health_monitor.py` to set thresholds and log file path:

```python
CPU_THRESHOLD = 80  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage
DISK_THRESHOLD = 80  # Disk usage percentage
LOG_FILE = 'system_health.log'
