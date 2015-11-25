import json
import base64
import boto3

print('Loading function')

def lambda_handler(event, context):
    try:
        print('Reading in file info from JSON blob')
        for fileinfo in event['putfile']:
            region = fileinfo['region']
            bucketname = fileinfo['bucketname']
            key = fileinfo['key']
            contenttype = fileinfo['contenttype']
            acl = fileinfo['acl']
            decodedbody = base64.b64decode(fileinfo['body'])
            print('Body decoded')
            print('S3 upload started')
            s3 = boto3.client('s3', region_name=region)
            response = s3.put_object(Bucket=bucketname, Key=key, ContentType=contenttype, ACL=acl, Body=decodedbody)
            print('S3 upload complete')
            print(response)
        print('All S3 uploads completed')
    except Exception as e:
        print(e)
        print('Error')
        raise e
