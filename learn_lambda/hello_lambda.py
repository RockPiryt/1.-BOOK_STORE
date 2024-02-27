import boto3
import os

def lambda_handler(event:any, context: any):
    user = event["user"]
    visit_count: int = 0

    #Create a DynamoDB client
    dynamodb = boto3.resource("dynamodb")
    # table_name = "visit-count-table"
    table_name = os.environ["TABLE_NAME"]
    table = dynamodb.Table(table_name)

    #Get the current visit count
    response = table.get_item(Key = {"user":user})
    if "Item" in response:
        visit_count = response["Item"]["count"]
        print(visit_count)
    
    #Increment the number of visits
    visit_count+=1

    #Put the new visit count into the table
    table.put_item(Item={
        "user": user,
        "count": visit_count 
    })

    message= f"Hi {user} ! You have visited this page {visit_count} times"
    return{"message": message}

if __name__ == "__main__":
    os.environ["TABLE_NAME"] = "visit-count-table"
    event= {"user": "Jack"}
    print(lambda_handler(event,None))