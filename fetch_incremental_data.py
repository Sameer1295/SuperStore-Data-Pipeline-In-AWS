import os
import pandas as pd
import boto3


aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_s3_bucket = os.getenv('AWS_S3_BUCKET')
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

superstore_data = pd.read_csv("Sample-Superstore.csv", encoding='unicode_escape')
superstore_data['Order Date'] = pd.to_datetime(superstore_data['Order Date'])

# Filter data for the year 2017
superstore_data_2017 = superstore_data[(superstore_data['Order Date'] >= '2017-01-01') & (superstore_data['Order Date'] < '2018-01-01')]

# Create CSV files for each month
for month in range(1, 13):
    month_data = superstore_data_2017[
        (superstore_data_2017['Order Date'].dt.month == month)
    ]
    output_folder = f'orders_data\snapshot_data=2017_{month:02d}'
    os.makedirs(output_folder, exist_ok=True)

    output_filename = os.path.join(output_folder, f'superstore_data_2017_{month:02d}.csv')
    csv_buffer = month_data.to_csv(output_filename,  sep='\t', index=False)

    s3_key = f'orders/snapshot_data=2017-{month:02d}/superstore_data_2017_{month:02d}.csv'
    # s3_client.put_object(Body=csv_buffer.getvalue(), Bucket=aws_s3_bucket, Key=s3_key)

    local_file_path = os.path.join(output_folder, f'superstore_data_2017_{month:02d}.csv')

    # Upload to S3
    s3_client.upload_file(output_filename, aws_s3_bucket, s3_key)
