import os
import time
import datetime
import smtplib
import requests
import json

# Set the API endpoint for retrieving cloud infrastructure performance data
API_ENDPOINT = "https://example.com/api/v1/performance"

# Set the thresholds for triggering alerts (e.g. 90th percentile for CPU usage must be above 80%)
THRESHOLDS = {
    "cpu_usage": 80,
    "memory_usage": 75,
    "disk_usage": 85
}

# Set the email address for sending alerts
ALERT_EMAIL = "alerts@example.com"

# Set the SMTP server and port for sending email
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

# Set the username and password for authenticating with the SMTP server
SMTP_USERNAME = "alerts@example.com"
SMTP_PASSWORD = "secret"

def send_email(subject, body):
    """Send an email with the specified subject and body to the alert email address."""
    msg = "Subject: {}\n\n{}".format(subject, body)
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(ALERT_EMAIL, ALERT_EMAIL, msg)
    server.quit()

def check_performance():
    """Retrieve cloud infrastructure performance data and check against thresholds."""
    # Make an API request to get the performance data
    response = requests.get(API_ENDPOINT)
    data = json.loads(response.text)
    
    # Check the performance data against the thresholds
    for metric, value in data.items():
        if metric in THRESHOLDS and value > THRESHOLDS[metric]:
            # Send an alert if a threshold is exceeded
            subject = "ALERT: {} threshold exceeded".format(metric)
            body = "The {} threshold of {}% was exceeded with a value of {}%.".format(metric, THRESHOLDS[metric], value)
            send_email(subject, body)

if __name__ == "__main__":
    check_performance()
