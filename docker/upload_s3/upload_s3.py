import boto3

s3 = boto3.client("s3")
s3.upload_file("/app/data/raw_data.csv", "your-s3-bucket", "raw/raw_data.csv")
print("Uploaded raw CSV to S3")
