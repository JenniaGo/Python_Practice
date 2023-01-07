import boto3
import datetime

# Set up cloudwatch client
cloudwatch = boto3.client('cloudwatch')

# Set threshold values for alerts
cpu_threshold = 80
memory_threshold = 75
disk_threshold = 90

# Set time period for metrics to retrieve
end_time = datetime.datetime.now()
start_time = end_time - datetime.timedelta(minutes=60)

# Get metrics for all instances in the account
instance_ids = []
instances = boto3.client('ec2').describe_instances()
for instance in instances['Reservations']:
    instance_ids.append(instance['Instances'][0]['InstanceId'])

# Check CPU utilization for each instance
for instance_id in instance_ids:
    cpu_utilization = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
    )
    cpu_avg = cpu_utilization['Datapoints'][0]['Average']
    if cpu_avg > cpu_threshold:
        send_alert("CPU utilization for instance {} exceeded threshold of {}%".format(instance_id, cpu_threshold))

# Check memory utilization for each instance
for instance_id in instance_ids:
    memory_utilization = cloudwatch.get_metric_statistics(
        Namespace='System/Linux',
        MetricName='MemoryUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
    )
    memory_avg = memory_utilization['Datapoints'][0]['Average']
    if memory_avg > memory_threshold:
        send_alert("Memory utilization for instance {} exceeded threshold of {}%".format(instance_id, memory_threshold))

# Check disk space utilization for each instance
for instance_id in instance_ids:
    disk_utilization = cloudwatch.get_metric_statistics(
        Namespace='System/Linux',
        MetricName='DiskSpaceUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
    )
    disk_avg = disk_utilization['Datapoints'][0]['Average']
    if disk_avg > disk_threshold:
        send_alert("Disk space utilization for instance {} exceeded threshold of {}%".format(instance_id, disk_threshold))
 # Function to send alerts when thresholds are exceeded
def send_alert(message):
    # Set up SNS client
    sns = boto3.client('sns')

    # Set up alert topic and message
    topic_arn = "arn:aws:sns:us-east-1:123456789012:cloud_infrastructure_alerts"
    subject = "Cloud Infrastructure Alert"
    msg = message

    # Send alert
    sns.publish(TopicArn=topic_arn, Subject=subject, Message=msg)

# Set up CloudTrail client
cloudtrail = boto3.client('cloudtrail')

# Set thresholds for suspicious activity alerts
login_failure_threshold = 5
security_group_threshold = 10

# Get CloudTrail events for the past hour
end_time = datetime.datetime.now()
start_time = end_time - datetime.timedelta(hours=1)
events = cloudtrail.lookup_events(
    StartTime=start_time,
    EndTime=end_time
)

# Count number of failed logins
login_failures = 0
for event in events['Events']:
    if event['EventName'] == "ConsoleLogin":
        if event['ResponseElements']['ConsoleLogin']['AuthenticationResult'] == "Failure":
            login_failures += 1

# Send alert if threshold is exceeded
if login_failures > login_failure_threshold:
    send_alert("Number of failed login attempts exceeded threshold of {} in the past hour".format(login_failure_threshold))

# Count number of security group changes
security_group_changes = 0
for event in events['Events']:
    if event['EventName'] == "AuthorizeSecurityGroupIngress" or event['EventName'] == "RevokeSecurityGroupIngress":
        security_group_changes += 1

# Send alert if threshold is exceeded
if security_group_changes > security_group_threshold:
    send_alert("Number of security group changes exceeded threshold of {} in the past hour".format(security_group_threshold))

# Set up RDS client
rds = boto3.client('rds')

# Set threshold for RDS storage space
storage_threshold = 75

# Get list of RDS instances
instances = rds.describe_db_instances()

# Check storage space for each instance
for instance in instances['DBInstances']:
    storage_percent = instance['AllocatedStorage'] / instance['MaxAllocatedStorage'] * 100
    if storage_percent > storage_threshold:
        send_alert("RDS instance {} is using more than {}% of its storage space".format(instance['DBInstanceIdentifier'], storage_threshold))

# Set up ELB client
elb = boto3.client('elbv2')

# Set threshold for ELB error rate
error_rate_threshold = 5

# Get list of ELB load balancers
load_balancers = elb.describe_load_balancers()

# Check error rate for each load balancer
for load_balancer in load_balancers['LoadBalancers']:
    error_rate = cloudwatch.get_metric_statistics(
        Namespace='AWS/ApplicationELB',
        MetricName='HTTPCode_ELB_5XX_Count',
        Dimensions=[{'Name': 'LoadBalancer', 'Value': load_balancer['LoadBalancerName']}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average']
    )
    error_rate_avg = error_rate['Datapoints'][0]['Average']
    if error_rate_avg > error_rate_threshold:
        send_alert("ELB load balancer {} has an error rate above {}% in the past hour".format(load_balancer['LoadBalancerName'], error_rate_threshold))
# Set up S3 client
s3 = boto3.client('s3')

# Set threshold for S3 bucket size
bucket_size_threshold = 75

# Get list of S3 buckets
buckets = s3.list_buckets()

# Check size of each bucket
for bucket in buckets['Buckets']:
    size = 0
    objects = s3.list_objects(Bucket=bucket['Name'])
    for obj in objects['Contents']:
        size += obj['Size']
    size_percent = size / bucket['Quota'] * 100
    if size_percent > bucket_size_threshold:
        send_alert("S3 bucket {} is using more than {}% of its storage quota".format(bucket['Name'], bucket_size_threshold))

# Set up SNS client
sns = boto3.client('sns')

# Set up topic for alerts
topic_arn = "arn:aws:sns:us-east-1:123456789012:cloud_infrastructure_alerts"

# Subscribe to topic
sns.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint='alerts@example.com')

# Set up CloudWatch Events client
cloudwatch_events = boto3.client('events')

# Set up event rule to run script every hour
rule_name = "cloud_infrastructure_monitoring"
schedule_expression = "rate(1 hour)"
cloudwatch_events.put_rule(Name=rule_name, ScheduleExpression=schedule_expression, State='ENABLED')

# Set up event target to run script
function_name = "cloud_infrastructure_monitoring"
cloudwatch_events.put_targets(Rule=rule_name, Targets=[{'Id': function_name, 'Arn': 'arn:aws:lambda:us-east-1:123456789012:function:cloud_infrastructure_monitoring'}])

# Set up CloudFormation client
cloudformation = boto3.client('cloudformation')

# Set threshold for number of stack updates
stack_update_threshold = 3

# Get list of CloudFormation stacks
stacks = cloudformation.list_stacks()

# Count number of stacks with updates
stack_updates = 0
for stack in stacks['StackSummaries']:
    if stack['StackStatus'] == "UPDATE_IN_PROGRESS":
        stack_updates += 1

# Send alert if threshold is exceeded
if stack_updates > stack_update_threshold:
    send_alert("Number of stacks with updates in progress exceeded threshold of {}".format(stack_update_threshold))

# Set up Auto Scaling client
autoscaling = boto3.client('autoscaling')

# Set threshold for number of instances in failed state
failed_instance_threshold = 1

# Get list of Auto Scaling groups
groups = autoscaling.describe_auto_scaling_groups()

# Count number of instances in failed state
failed_instances = 0
for group in groups['AutoScalingGroups']:
    instances = autoscaling.describe_auto_scaling_instances()
    for instance in instances['AutoScalingInstances']:
        if instance['LifecycleState'] == "Unhealthy":
            failed_instances += 1

# Send alert if threshold is exceeded
if failed_instances > failed_instance_threshold:
    send_alert("Number of instances in failed state exceeded threshold of {}".format(failed_instance_threshold))

# Set up DynamoDB client
dynamodb = boto3.client('dynamodb')

# Set threshold for DynamoDB throughput
throughput_threshold = 75

# Get list of DynamoDB tables
tables = dynamodb.list_tables()

# Check throughput for each table
for table in tables['TableNames']:
    throughput = dynamodb.describe_table(TableName=table)
    throughput_percent = throughput['Table']['ProvisionedThroughput']['ReadCapacityUnits'] / throughput['Table']['ProvisionedThroughput']['MaxCapacityUnits'] * 100
    if throughput_percent > throughput_threshold:
        send_alert("DynamoDB table {} is using more than {}% of its provisioned throughput".format(table, throughput_threshold))

# Set up Lambda client
lambda_client = boto3.client('lambda')

# Set threshold for number of throttled Lambda invocations
throttled_invocation_threshold = 5

# Get list of Lambda functions
functions = lambda_client.list_functions()

# Check number of throttled invocations for each function
for function in functions['Functions']:
    throttled_invocations = cloudwatch.get_metric_statistics(
        Namespace='AWS/Lambda',
        MetricName='Throttles',
        Dimensions=[{'Name': 'FunctionName', 'Value': function['FunctionName']}],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Sum']
    )
    throttled_invocations_sum = throttled_invocations['Datapoints'][0]['Sum']
    if throttled_invocations_sum > throttled_invocation_threshold:
        send_alert("Lambda function {} has been throttled more than {} times in the past hour".format(function['FunctionName'], throttled_invocation_threshold))

# Set up ECS client
ecs = boto3.client('ecs')

# Set threshold for number of running tasks
running_task_threshold = 10

# Get list of ECS clusters
clusters = ecs.list_clusters()

# Check number of running tasks for each cluster
for cluster in clusters['clusterArns']:
    tasks = ecs.list_tasks(cluster=cluster)
    running_tasks = 0
    for task in tasks['taskArns']:
        task_details = ecs.describe_tasks(cluster=cluster, tasks=[task])
        if task_details['tasks'][0]['lastStatus'] == "RUNNING":
            running_tasks += 1
    if running_tasks > running_task_threshold:
        send_alert("ECS cluster {} has more than {} running tasks".format(cluster, running_task_threshold))

# Set up EKS client
eks = boto3.client('eks')

# Set threshold for number of unresponsive worker nodes
unresponsive_node_threshold = 3

# Get list of EKS clusters
clusters = eks.list_clusters()

# Check number of unresponsive worker nodes for each cluster
for cluster in clusters['clusters']:
    nodes = eks.list_nodegroups(clusterName=cluster)
    unresponsive_nodes = 0
    for node in nodes['nodegroups']:
        node_details = eks.describe_nodegroup(clusterName=cluster, nodegroupName=node)
        if node_details['nodegroup']['status'] == "Unhealthy":
            unresponsive_nodes += 1
    if unresponsive_nodes > unresponsive_node_threshold:
        send_alert("EKS cluster {} has more than {} unresponsive worker nodes".format(cluster, unresponsive_node_threshold))
