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
                'Name': 'tag:AutoStop',
                'Values': ['true']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )
    
    instances_to_stop = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances_to_stop.append(instance['InstanceId'])

    print(instances_to_stop)
    
    if instances_to_stop:
        ec2.stop_instances(InstanceIds=instances_to_stop)
        print(f"Stopped instances: {instances_to_stop}")
    else:
        print("No instances to stop")
