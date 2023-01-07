# Import the required libraries
import boto3
import time

# Set the AWS region and service
AWS_REGION = "us-east-1"
EC2_SERVICE = "ec2"

# Set the thresholds for the monitoring
CPU_UTILIZATION_THRESHOLD = 80
MEMORY_UTILIZATION_THRESHOLD = 70

# Set the email address to send the alerts to
ALERT_EMAIL_ADDRESS = "alerts@example.com"

# Connect to the EC2 service
ec2 = boto3.client(EC2_SERVICE, region_name=AWS_REGION)

while True:
    # Get a list of all the instances in the region
    instances = ec2.describe_instances()["Reservations"]
    for reservation in instances:
        for instance in reservation["Instances"]:
            # Get the instance's ID and state
            instance_id = instance["InstanceId"]
            instance_state = instance["State"]["Name"]
            
            # Only check running instances
            if instance_state == "running":
                # Get the instance's metrics
                instance_metrics = ec2.get_metric_statistics(
                    Namespace="AWS/EC2",
                    MetricName="CPUUtilization",
                    Dimensions=[
                        {
                            "Name": "InstanceId",
                            "Value": instance_id
                        }
                    ],
                    StartTime=time.time() - 3600,
                    EndTime=time.time(),
                    Period=300,
                    Statistics=["Average"]
                )
                
                # Check if the CPU utilization is above the threshold
                if instance_metrics["Datapoints"][0]["Average"] > CPU_UTILIZATION_THRESHOLD:
                    # Send an alert email
                    ses = boto3.client("ses", region_name=AWS_REGION)
                    ses.send_email(
                        Source=ALERT_EMAIL_ADDRESS,
                        Destination={
                            "ToAddresses": [
                                ALERT_EMAIL_ADDRESS
                            ]
                        },
                        Message={
                            "Subject": {
                                "Data": "High CPU Utilization Alert"
                            },
                            "Body": {
                                "Text": {
                                    "Data": f"The CPU utilization of instance {instance_id} is currently above the threshold of {CPU_UTILIZATION_THRESHOLD}%."
                                }
                            }
                        }
                    )
                
                # Get the instance's memory metrics
                instance_metrics = ec2.get_metric_statistics(
                    Namespace="System/Linux",
                    MetricName="MemoryUtilization",
                    Dimensions=[
                        {
                            "Name": "InstanceId",
                            "Value": instance_id
                        }
                    ],
                    StartTime=time.time() - 3600,
                    EndTime=time.time(),
                    Period=300,
                    Statistics=["Average"]
                )
                
                # Check if the CPU utilization is above the threshold
                if instance_metrics["Datapoints"][0]["Average"] > CPU_UTILIZATION_THRESHOLD:
                    # Send an alert email
                    ses = boto3.client("ses", region_name=AWS_REGION)
                    response = ses.send_email(
                        Source=ALERT_EMAIL_ADDRESS,
                        Destination={
                            "ToAddresses": [
                                ALERT_EMAIL_ADDRESS
                            ]
                        },
                        Message={
                            "Subject": {
                                "Data": "High CPU Utilization Alert"
                            },
                            "Body": {
                                "Text": {
                                    "Data": f"The CPU utilization of instance {instance_id} is currently above the threshold of {CPU_UTILIZATION_THRESHOLD}%."
                                }
                            }
                        }
                    )
                
