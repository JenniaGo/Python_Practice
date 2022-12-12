import boto3

# Chose a resource
ec2_client = boto3.client("ec2", region_name="us-east-1")
# get list of vpcs
all_available_vpcs = ec2_client.describe_vpcs()
vpcs = all_available_vpcs["Vpcs"]

# loop to get id and state of each vpc
for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"])
