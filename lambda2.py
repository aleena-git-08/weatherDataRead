import json
import boto3
import uuid

s3 = boto3.client('s3')

BUCKET_NAME = 'weather-project-bucket-001'

def lambda_handler(event, context):