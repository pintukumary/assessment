import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Parse incoming data (expecting JSON with userId and name)
    try:
        body = json.loads(event['body'])  # Extract the request body (POST request)
        users = body.get('users', [])  # Expecting {"users": [{"userId": 1, "name": "John Doe"}, ...]}

        if not users:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'No users provided'})
            }

        # Prepare data to write (CSV format)
        result_data = [f'{user["userId"]},{user["name"]}\n' for user in users]
        
        # Define file path (Lambda’s writable directory)
        file_path = "/tmp/user_data.txt"
        with open(file_path, "w") as file:
            file.writelines(result_data)

        # Upload file to S3
        bucket_name = "rest-api-get-data"  # Replace with your actual S3 bucket name
        s3_key = "user_data.txt"  # This will be the file name in S3

        s3.upload_file(file_path, bucket_name, s3_key)

        # Return success response with S3 file location
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Data written and uploaded to S3 successfully',
                's3_file_url': f's3://{bucket_name}/{s3_key}'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error processing request', 'error': str(e)})
        }
