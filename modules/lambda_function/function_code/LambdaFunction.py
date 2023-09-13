import boto3
import json

# define the DynamoDB table that Lambda will connect to
tableName = "lambda-apigateway"

# create the DynamoDB resource
dynamo = boto3.resource('dynamodb').Table(tableName)

print('Loading function')

def handler(event, context):
    dynamodb_resource = boto3.resource("dynamodb")
    table_name = "lambda-apigateway"
    table = dynamodb_resource.Table(table_name)
    item_key = {"id":'1234'}

    # fetch current value in count
    def get_single_item(item_key):
        response = table.get_item(Key=item_key)
        return response
        global currentcount
    # check for value
    try:
       response = get_single_item(item_key=item_key)
       currentcount = response["Item"]["count"]
    except:
       print("An exception occurred")

# update value in count
    def put_item_using_resource():
       dynamodb_resource = boto3.resource("dynamodb")
       table = dynamodb_resource.Table(table_name)
       response = table.put_item(
         Item={
           "id": "1234",
           "count": messagecount + currentcount
         }
    )

    # grab input data and count words
    print('current count =', currentcount)
    message_string = event.get('message')
    data = json.dumps(message_string)
    messagecount = len(data.split())
    print('new count =', messagecount)
    put_item_using_resource()
    totalcount = currentcount + messagecount
    print('total count =', totalcount)
    return str(totalcount)