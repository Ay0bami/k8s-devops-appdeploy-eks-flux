import os
import boto3
from botocore.exceptions import NoCredentialsError

BGIMAGE = os.environ.get("BGIMAGE")

s3 = boto3.client("s3")
split_str = ""

try:
    if '/' in BGIMAGE:
        split_str = BGIMAGE.split('/')
except (AttributeError) as e:
    print(e)

try:
    if len(split_str) > 0:
        s3.download_file(split_str[2], split_str[-1], '/app/static/img/bgimg.jpg')
except (NoCredentialsError) as e:
    print(e)                    