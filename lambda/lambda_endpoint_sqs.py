import boto3
import json
import os

def lambda_handler(event, context):
    sqs = boto3.client('sqs')

    if not 'body' in event:
        return {'Error': 'No data sent in request'}

    response = sqs.send_message(
        QueueUrl=os.environ['SQS_ENDPOINT'],
        MessageBody=json.dumps(event['body']),
        DelaySeconds=0
    )

    print(response)

    result = {
        'Success': 'Data has been submitted for processing'
    }
    return result