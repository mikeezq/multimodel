import os

import boto3

from config import S3_ENDPOINT

bucket_name = "tv-serials"


def get_s3():
    return boto3.client(
        's3',
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id='12',
        aws_secret_access_key='12',
        region_name='us-east-1'
    )


def get_presigned_url(key):
    return get_s3().generate_presigned_url(
        'get_object',
        Params={
            "Bucket": bucket_name,
            "Key": key
        },
        ExpiresIn=60000000
    )


def fill_s3_if_not_filled():
    buckets = [b["Name"] for b in get_s3().list_buckets()["Buckets"]]
    if bucket_name in buckets:
        return

    get_s3().create_bucket(Bucket=bucket_name)

    media_dir = os.path.join(os.getcwd(), "static", "img")

    for flag in os.listdir(media_dir):
        s3 = get_s3()
        flag_path = os.path.join(media_dir, flag)
        s3.upload_file(flag_path, bucket_name, flag)
    print("flags ok")
