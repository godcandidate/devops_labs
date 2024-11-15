# Python Cron Job Lab  

This lab shows how to create a Python script that restarts a service, clears a folder, and automates these tasks using cron.

## Objectives  
- Write a Python script to restart a service.  
- Clear a temporary folder with Python.  
- Set up a cron job to run the script automatically.

## Run the script:

    ``` bash
        python manage_service.py

## Set up cron job 
Set up a cron job to run the script at your desired time:

    ``` bash
        crontab -e


## Example
Example for running it daily at 2:00 AM:

  ```plaintext
    0 2 * * * /usr/bin/python3 /path/to/manage_service.py >> /path/to/cron_log.txt 2>&1


