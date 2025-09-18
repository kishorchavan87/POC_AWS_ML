import pandas as pd
import boto3

df = pd.read_csv("/app/data/clean_data.csv")
df.to_parquet("/app/data/final_results.parquet")

s3 = boto3.client("s3")
s3.upload_file("/app/data/final_results.parquet", "your-s3-bucket", "results/final_results.parquet")
print("Final results saved as Parquet to S3")
