import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get all instances with required tags
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Environment',
                'Values': ['Development']
            },
            {
                'Name': 'tag:AutoStart',
                'Values': ['true']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['stopped']
            }
        ]
    )
    
    instances_to_start = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances_to_start.append(instance['InstanceId'])
    print(instances_to_start)
    if instances_to_start:
        ec2.start_instances(InstanceIds=instances_to_start)
        print(f"Started instances: {instances_to_start}")
    else:
        print("No instances to start")
