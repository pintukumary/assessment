import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all the S3 buckets
response = s3.list_buckets()

# Extract and print only the bucket names
bucket_names = [bucket['Name'] for bucket in response['Buckets']]

file_content = "This is test content inside of test file"
bucket_name=bucket_names[0]

s3.put_object(Bucket=bucket_name, Key="test.txt", Body=file_content)

# Output the bucket names
print(f"File have been uploaded to bucket {bucket_name}")
