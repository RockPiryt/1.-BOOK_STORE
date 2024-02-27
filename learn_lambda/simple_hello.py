import json

def lambda_handler(event, context):
    # TODO implement
    user=event["user"]
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'message': f"Hello {user}"
    }
