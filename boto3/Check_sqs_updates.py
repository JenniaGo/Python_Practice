import boto3

# Set up the SQS client
sqs = boto3.client('sqs')

# Create a new queue
response = sqs.create_queue(QueueName='request_queue')
queue_url = response['QueueUrl']

# Send a message to the queue
sqs.send_message(QueueUrl=queue_url, MessageBody='{"request_id": 123, "user_id": 456, "request_data": "some data"}')

# Poll the queue for new messages
while True:
    # Receive up to 10 messages
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)

    # If there are no messages, the response will be empty
    if 'Messages' not in response:
        continue

    # Process each message
    for message in response['Messages']:
        request_id = message['Body']
        # Do some work with the request data...
        # Update the database, call an external API, etc.

        # Delete the message from the queue to mark it as processed
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message['ReceiptHandle'])
