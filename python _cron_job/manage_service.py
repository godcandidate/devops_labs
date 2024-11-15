import os
import subprocess
import shutil

# Function to restart a service
def restart_service(service_name):
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', service_name], check=True)
        print(f"Service '{service_name}' restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting service '{service_name}': {e}")

# Function to clear the temp folder
def clear_temp_folder(temp_folder):
    try:
        shutil.rmtree(temp_folder)
        os.makedirs(temp_folder)
        print(f"Temporary folder '{temp_folder}' cleared successfully.")
    except Exception as e:
        print(f"Error clearing temporary folder '{temp_folder}': {e}")

if __name__ == "__main__":
# The cups service is for managing printers
    SERVICE_NAME = "cups"
    TEMP_FOLDER = "cron_temp"

    # Call functions (if needed)
    restart_service(SERVICE_NAME)
    if os.path.exists(os.path.expanduser(TEMP_FOLDER)):
    	clear_temp_folder(TEMP_FOLDER)
