#!/usr/bin/env python

import boto3

BUCKET = "your-bucket-name"
s3 = boto3.client('s3')

def lambda_handler(event, context):
    key = 'test/bbbb' # directory-name/file-name
    content = "test content" # file content
    s3.put_object(Bucket=BUCKET, Key=key, Body=content)