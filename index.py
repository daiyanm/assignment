import boto3
import os

ssm = boto3.client('ssm')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Retrieve parameter from SSM
    response = ssm.get_parameter(Name='UserName')
    user_name = response['Parameter']['Value']
    
    # Write parameter to a file in S3
    bucket_name = os.environ['BUCKET_NAME']
    file_content = f'UserName: {user_name}'
    s3.put_object(Bucket=bucket_name, Key='username.txt', Body=file_content)
    
    return {
        'statusCode': 200,
        'body': f'Successfully wrote to {bucket_name}/username.txt'
    }
