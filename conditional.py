import boto3

def get_volume_id_from_arn(arn):
    # Split the ARN string by ':' delimiter
    parts = arn.split(':')
    
    # Extract the volume ID from the last part of the ARN
    volume_id = parts[-1].split('/')[-1]
    
    return volume_id

def lambda_handler(event, context):
    # Extract the volume ARN from the event
    volume_arn = event['resources'][0]
    
    # Get the volume ID from the ARN
    volume_id = get_volume_id_from_arn(volume_arn)
    
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2')
    
    try:
        # Modify the volume type to gp3
        response = ec2_client.modify_volume(
            VolumeId=volume_id,
            VolumeType='gp3'
        )
        
        print(f"EBS volume {volume_id} converted to gp3 successfully.")
        return {
            'statusCode': 200,
            'body': f"EBS volume {volume_id} converted to gp3 successfully."
        }
    except Exception as e:
        print(f"Error converting EBS volume {volume_id} to gp3: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Failed to convert EBS volume {volume_id} to gp3."
        }
### On the creation of EBS volume it automatically changes from ebs volume gp2 to gp3 