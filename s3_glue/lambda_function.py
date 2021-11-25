import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('glue')

    print('starting crawler...')
    response = client.start_crawler(Name='new-crawler-58')
    print(json.dumps(response, indent=4))