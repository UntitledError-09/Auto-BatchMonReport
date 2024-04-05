import paramiko
import datetime

def ssh_connect_and_get_logs(server_ip, username, password, log_path, local_output_path):
    try:
        # Establish SSH connection
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=server_ip, username=username, password=password)
        
        # Execute command to fetch logs
        stdin, stdout, stderr = ssh_client.exec_command(f"cat {log_path}")
        logs = stdout.read().decode("utf-8")
        
        # Save logs to local file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{local_output_path}/logs_{timestamp}.txt"
        
        with open(output_filename, "w") as f:
            f.write(logs)
        
        ssh_client.close()
        return True, output_filename
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return False, None

# Example usage:
server_ip = "remote_server_ip"
username = "your_username"
password = "your_password"
log_path = "/path/to/logs"
local_output_path = "/path/to/local/output"

success, log_filename = ssh_connect_and_get_logs(server_ip, username, password, log_path, local_output_path)

if success:
    print(f"Logs downloaded successfully: {log_filename}")
else:
    print("Failed to download logs.")
