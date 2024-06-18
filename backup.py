import os
import paramiko
from scp import SCPClient
import logging
from datetime import datetime

# Configuration - need to change the placeholders
SOURCE_DIR = '/path/to/source/directory'  
REMOTE_HOST = 'remote.server.com'         
REMOTE_PORT = 22                          
REMOTE_USER = 'username'                 
REMOTE_PASS = 'password'                 
REMOTE_DIR = '/path/to/remote/directory'  
LOG_FILE = 'backup.log'

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_ssh_client(host, port, user, password):
    """Create and return an SSH client connected to the remote host."""
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, user, password)
    return client

def backup_directory(source_dir, remote_dir, ssh_client):
    """Backup the specified directory to the remote directory."""
    try:
        with SCPClient(ssh_client.get_transport()) as scp:
            scp.put(source_dir, recursive=True, remote_path=remote_dir)
        return True
    except Exception as e:
        logging.error(f"Failed to backup directory: {e}")
        return False

def main():
    logging.info("Starting backup process...")
    start_time = datetime.now()

    try:
        ssh_client = create_ssh_client(REMOTE_HOST, REMOTE_PORT, REMOTE_USER, REMOTE_PASS)
        logging.info("SSH connection established.")
    except Exception as e:
        logging.error(f"SSH connection failed: {e}")
        return

    if backup_directory(SOURCE_DIR, REMOTE_DIR, ssh_client):
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        logging.info(f"Backup completed successfully in {duration:.2f} seconds.")
    else:
        logging.error("Backup failed.")

    ssh_client.close()
    logging.info("SSH connection closed.")

if __name__ == '__main__':
    main()
