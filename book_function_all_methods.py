import json
import logging

# AWS Lambda Function Logging in Python - https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    '''Demonstrates Amazon API Gateway Lambda proxy integration. You have full
    access to the request and response payload, including headers and
    status code.
    https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    '''
    logger.debug(event) # Mind logger.setLevel at line 6. Check Event printed at CloudWatch

    
    BOOKS = [
     {
          "id": "1",
          "title": "Harry Potter",
          "author": "Hawkings",
     },
     {
          "id": "2",
          "title": "Pan Tadeusz",
          "author": "Mickiewicz",
     },
     {
          "id": "3",
          "title": "Biblia",
          "author": "Bog",
     },

]
    
    # Input Format https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    resource = event['resource']
    # Uncomment to print the event
    # print("Received event: " + json.dumps(event, indent=2))

    err = None
    # /books List all books
    response_body = {}
    if (resource == "/books"):
        response_body = {
            "success": True,
            "books": BOOKS
        }
    # /books/bookId find book by Id    
    elif (resource == "/books/{id}"):
        bookId = event['pathParameters']['id']
        value = next((item for item in BOOKS if item["id"] == str(bookId)), False)
        if( value == False ):
            err = "book not found"
        else:
            response_body = {
                "success": True,
                "book": value
            }
    # /books create new book
    elif (resource == "/books"):
        pass
    response =  response_payload(err, response_body)

    return response
  
  
    
'''
In Lambda proxy integration, API Gateway sends the entire request as input to a backend Lambda function. 
API Gateway then transforms the Lambda function output to a frontend HTTP response.
Output Format: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format
'''
def response_payload(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }