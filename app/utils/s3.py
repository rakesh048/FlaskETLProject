from io import BytesIO
from uuid import uuid4
import os
import boto3
import botocore
from botocore.config import Config
from botocore.exceptions import ClientError

session = boto3.session.Session(profile_name='boto3user')
dev_s3_client = session.resource('s3')


def s3_parse(url):
    assert url.startswith('s3://')
    bucket, _, path = url[5:].partition('/')
    return bucket, path


def s3_create_bucket(s3_conn, bucket_name, directory_name):
    """
    Creates an S3 Bucket
    :param bucket_name: Name of the bucket to be created
    :param config: (optional) Boto3 configuration to use when connecting
    """
    s3_conn.put_object(Bucket=bucket_name, Key=(directory_name + '/'))


def s3_upload_file(s3_conn, local_file, bucket, s3_file):
    """
    Creates an S3 Bucket
    :param bucket_name: Name of the bucket to be created
    :param config: (optional) Boto3 configuration to use when connecting
    """
    try:
        my_bucket = s3_conn.Bucket(bucket)
        my_bucket.upload_file(local_file, '%s/%s' % ('dev_input', 'pipeline.xlsx'))
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False


# s3_create_bucket(dev_s3_client,'local-dev-flask','dev_input')

# s3_upload_file(dev_s3_client, 'C:/Users/rakeshsharma03/Downloads/pipeline.xlsx', 'local-dev-flask','pipeline.xlsx')

def s3_download(s3_conn, download_path, url):
    bucket, path = s3_parse(url)
    # s3_conn.download_file(bucket, path, download_path)
    if download_path is None:
        download_path = os.path.basename(path)
    s3_conn.Bucket(bucket).download_file(path, download_path)
    return download_path


s3_download(dev_s3_client, None , 's3://local-dev-flask/dev_input/pipeline.xlsx')