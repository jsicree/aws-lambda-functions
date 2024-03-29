
import boto3
import json

print('Loading function')
# dynamo = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    operation = event['httpMethod']
    if operation == 'GET':
        return respond(None, 'Goodbye!')
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
