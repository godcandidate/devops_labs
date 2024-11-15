import os
import requests
import shutil
from datetime import datetime


# CREATE A CUSTOM DIRECTORY WITH NAME
dir_name = 'edward_dankwah'

# checks if directory exists and removes it
if os.path.exists(dir_name):
    try:
        shutil.rmtree(dir_name)
        print(f"Directory {dir_name} has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# create a new directory
os.makedirs(dir_name)
print(f"Directory: {dir_name} created.")

# define local path
local_file_path = os.path.join(dir_name, f"{dir_name}.txt")


# DOWNLOAD FILE
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

# Get url
response = requests.get(url)

# Check if file is accessible and download
if response.status_code == 200:
    print(f"File sucessfully downloaded.")
    
    with open(local_file_path, "wb") as file:
        file.write(response.content)
        print("File saved sucessfully.")

else:
    print(f"Failed to download file. Status code: {response.status_code}")



# MODIFY FILE CONTENT

# Get user input and date
user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Overwrite file
with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on : {current_time}")
    print("File successfully modified.")


# READING FILE CONTENT
with open(local_file_path, "r") as file:
    print("\n You Entered: ", end='')
    print(file.read())