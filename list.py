import json
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Directly access the 'users' data from the event
        body = event  # The payload is directly passed in as the event

        # Ensure 'users' data is present in the request
        if 'users' not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Bad Request: "users" data not found in the request body'})
            }

        users = body['users']  # Get the user data from the 'users' key in the request

        # Ensure the users data is a list
        if not isinstance(users, list):
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Bad Request: "users" should be a list'})
            }

        result_data = [f'{user["userId"]},{user["name"]}\n' for user in users]

        # Define file path for temporary storage in Lambda
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
