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
    item_key = {"id":'count'}

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
           "id": "count",
           "count": messagecount + currentcount
         }
    )
    def put_message_id_using_resource():
        dynamodb_resource = boto3.resource("dynamodb")
        table = dynamodb_resource.Table(table_name)
        response = table.put_item(
            Item={
                "id": message_id,
                "message_count": messagecount
            })

    # grab input data and count words
    message_id = event.get('id')
    print('message id = ', message_id)
    print('current count =', currentcount)
    message_string = event.get('message')
    message_id = event.get('id')
    data = json.dumps(message_string)
    messagecount = len(data.split())
    print('new count =', messagecount)
    put_item_using_resource()
    put_message_id_using_resource()
    totalcount = currentcount + messagecount
    print('total count =', totalcount)
    return str(totalcount)