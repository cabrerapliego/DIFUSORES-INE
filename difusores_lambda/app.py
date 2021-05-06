from time import time
import json
import boto3
from botocore.exceptions import ClientError
# import requests
import zipfile
import os


def lambda_handler(event, context): 
    with zipfile.ZipFile("file.zip", 'r') as zip_ref:
        zip_ref.extractall("/tmp")
    arr = os.listdir("/tmp")
     # Upload the file
    s3_client = boto3.client('s3')
    bucket='ine-difusores-aws'
    print(arr)
    for s in arr:
        try:
            if '.' in s:
                s3_client.upload_file("/tmp/"+s, bucket, s)
        except ClientError as e:
            logging.error(e)
    
   

   
        
    clientCF = boto3.client('cloudfront')
    response = clientCF.create_invalidation(
    #DistributionId=get_id(sys.argv[1]),
    DistributionId='EGR12FIAAYULY',
    InvalidationBatch={
        'Paths': {
            'Quantity': 1,
            'Items': [
                '/*'
                ],
            },
        'CallerReference': "Proceso INE"
        }
    )

    return  {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world" 
        }),
    }
