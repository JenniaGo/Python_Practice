import boto3
import os
import time

# Retrieve the AWS access keys from the environment variables
ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
SECRET_KEY = os.environ['AWS_SECRET_KEY']

# Create a boto3 client for interacting with AWS
client = boto3.client(
    'codepipeline',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

# Define the name of the pipeline and the name of the CloudFormation stack
# that will be created as part of the pipeline
pipeline_name = 'MyCloudAppPipeline'
stack_name = 'MyCloudAppStack'

# Define the location of the source code and the buildspec file
# Replace with the location of your source code and buildspec file
source_location = 'https://github.com/JenniaGo/Movie_Posters_Webapp.git'
buildspec_location = 'https://s3.amazonaws.com/mybucket/buildspec.yml'

# Define the pipeline structure
pipeline_structure = {
    'name': pipeline_name,
    'roleArn': 'arn:aws:iam::123456789012:role/AWSCodePipelineServiceRole',
    'artifactStore': {
        'type': 'S3',
        'location': 'my-pipeline-artifacts'
    },
    'stages': [
        {
            'name': 'Source',
            'actions': [
                {
                    'name': 'Source',
                    'actionTypeId': {
                        'category': 'Source',
                        'owner': 'ThirdParty',
                        'provider': 'GitHub',
                        'version': '1'
                    },
                    'runOrder': 1,
                    'configuration': {
                        'Owner': 'myusername',
                        'Repo': 'mycloudapp',
                        'Branch': 'master',
                        'OAuthToken': 'my-oauth-token'
                    },
                    'outputArtifacts': [
                        {
                            'name': 'MyApp'
                        }
                    ]
                }
            ]
        },
        {
            'name': 'Build',
            'actions': [
                {
                    'name': 'Build',
                    'actionTypeId': {
                        'category': 'Build',
                        'owner': 'AWS',
                        'provider': 'CodeBuild',
                        'version': '1'
                    },
                    'runOrder': 1,
                    'configuration': {
                        'ProjectName': 'MyCloudAppBuild',
                        'EnvironmentVariables': [
                            {
                                'Name': 'S3_BUCKET',
                                'Value': 'my-pipeline-artifacts'
                            }
                        ]
                    },
                    'inputArtifacts': [
                        {
                            'name': 'MyApp'
                        }
                    ],
                    'outputArtifacts': [
                        {
                            'name': 'MyAppBuild'
                        }
                    ]
                }
            ]
        },
        {
            'name': 'Deploy',
            'actions': [
                               {
                    'name': 'CreateChangeSet',
                    'actionTypeId': {
                        'category': 'Deploy',
                        'owner': 'AWS',
                        'provider': 'CloudFormation',
                        'version': '1'
                    },
                    'runOrder': 1,
                    'configuration': {
                        'ActionMode': 'CREATE_UPDATE',
                        'StackName': stack_name,
                        'Capabilities': 'CAPABILITY_NAMED_IAM',
                        'TemplatePath': 'MyAppBuild::template.yml',
                        'RoleArn': 'arn:aws:iam::123456789012:role/CloudFormationRole',
                        'ChangeSetName': 'MyCloudAppChangeset'
                    },
                    'inputArtifacts': [
                        {
                            'name': 'MyAppBuild'
                        }
                    ]
                },
                {
                    'name': 'ExecuteChangeSet',
                    'actionTypeId': {
                        'category': 'Deploy',
                        'owner': 'AWS',
                        'provider': 'CloudFormation',
                        'version': '1'
                    },
                    'runOrder': 2,
                    'configuration': {
                        'ActionMode': 'EXECUTE_CHANGESET',
                        'StackName': stack_name,
                        'ChangeSetName': 'MyCloudAppChangeset'
                    }
                }
            ]
        }
    ],
    'version': 1
}

# Create the pipeline
client.create_pipeline(pipeline=pipeline_structure)

# Wait for the pipeline to be created
while True:
    response = client.get_pipeline_state(name=pipeline_name)
    status = response['stageStates'][0]['latestExecution']['status']
    if status == 'Succeeded':
        print(f'Pipeline {pipeline_name} successfully created')
        break
    elif status == 'Failed':
        raise Exception('Pipeline creation failed')
    time.sleep(30)

# Wait for the CloudFormation stack to be created
cf_client = boto3.client(
    'cloudformation',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
while True:
    response = cf_client.describe_stacks(StackName=stack_name)
    status = response['Stacks'][0]['StackStatus']
    if status == 'CREATE_COMPLETE':
        print(f'CloudFormation stack {stack_name} successfully created')
        break
    elif 'CREATE_FAILED' in status:
            raise Exception(f'CloudFormation stack creation failed: {status}')
    time.sleep(30)

# Create a CodePipeline trigger
response = client.create_webhook(
    pipelineName=pipeline_name,
    targetAction='Source',
    targetPipelineVersion=1,
    targetPipelineLocation={
        'type': 'CODEPIPELINE',
        'repositoryName': 'MyCloudAppPipeline'
    }
)
webhook_url = response['webhook']['url']
print(f'Webhook URL: {webhook_url}')

# Register the webhook URL as a webhook in your GitHub repository
# Replace with the URL of your GitHub repository
repository_url = 'https://github.com/myusername/mycloudapp'

# Set up a boto3 client for interacting with the GitHub API
# Make sure you have the necessary permissions and have authorized the
# GITHUB_PAT environment variable with a personal access token
gh_client = boto3.client(
    'codepipeline-github',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='us-east-1'
)

# Register the webhook
gh_client.register_webhook_url(
    webhookUrl=webhook_url,
    repositoryUrl=repository_url
)
print('Webhook successfully registered')

# Define a function for deploying the pipeline
def deploy_pipeline(event, context):
    # Extract the commit ID from the event data
    commit_id = event['detail']['commitId']

    # Start a new execution of the pipeline
    response = client.start_pipeline_execution(name=pipeline_name)
    execution_id = response['pipelineExecutionId']
    print(f'Started pipeline execution {execution_id}')

    # Wait for the pipeline execution to complete
    while True:
        response = client.get_pipeline_state(name=pipeline_name)
        execution = response['stageStates'][-1]['latestExecution']
        status = execution['status']
        if status == 'Succeeded':
            print(f'Pipeline execution {execution_id} completed successfully')
            break
        elif status == 'Failed':
            raise Exception(f'Pipeline execution {execution_id} failed')
        time.sleep(30)

# Define a function for deleting the pipeline
def delete_pipeline(event, context):
    # Delete the pipeline
    client.delete_pipeline(name=pipeline_name)

    # Wait for the pipeline to be deleted
    while True:
        try:
            client.get_pipeline(name=pipeline_name)
        except client.exceptions.PipelineNotFoundException:
            print(f'Pipeline {pipeline_name} successfully deleted')
            break
        time.sleep(30)

    # Delete the CloudFormation stack
    cf_client.delete_stack(StackName=stack_name)

    # Wait for the CloudFormation stack to be deleted
    while True:
        try:
            cf_client.describe_stacks(StackName=stack_name)
        except cf_client.exceptions.StackNotFoundException:
            print(f'CloudFormation stack {stack_name} successfully deleted')
            break
        time.sleep(30)

