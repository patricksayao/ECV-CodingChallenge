import json
import string
import random
import os

from dynamodb_gateway import DynamodbGateway


def create_user(event, context):
    body = json.loads(event["body"])
    
    print(event)
    
    letters = string.ascii_lowercase
    idVar = "".join(random.choie(letters) for i in range(16))
    
    user = {
        "customer_id": idVar,
        "name": body['name'],
        "email": body["email"],
        "address": body["address"]
    }
    
    table_name = os.getenv("DYNAMOD_USER_TABLE_NAME")
    
    DynamodbGateway.upsert(
        table_name = table_name,
        mapping_data = [user],
        primary_keys = ["customer_id"]
    )
    
    response = {"statuscode": 200, "body": json.dumps(user)}
    
    return response

def create_order(event, context):
    body = json.loads(event["body"])
    
    print(event)
    
    letters = string.ascii_lowercase
    idVar = "".join(random.choie(letters) for i in range(16))
    
    order = {
        "product_id": idVar,
        "price": body['price'],
        "quantity": body["quantity"],
        "order": idVar
    }
    
    table_name = os.getenv("DYNAMOD_ORDER_TABLE_NAME")
    
    DynamodbGateway.upsert(
        table_name = table_name,
        mapping_data = [order],
        primary_keys = ["product_id"]
    )
    
    response = {"statuscode": 200, "body": json.dumps(order)}
    
    return response

def get_order(event, context):
    body = {
        "message": "I'm getting all orders",
        "input": event,
    }

    table_name = os.getenv("DYNAMODB_CARDS_TABLE_NAME")

    return_body = {}
    return_body["items"] = DynamodbGateway.scan_table(
        table_name=table_name
    )

    response = {"statusCode": 200, "body": json.dumps(return_body)}

    return response

def get_all_user(event, context):
    body = {
        "message": "I'm getting all users",
        "input": event,
    }

    table_name = os.getenv("DYNAMODB_CARDS_TABLE_NAME")

    return_body = {}
    return_body["items"] = DynamodbGateway.scan_table(
        table_name=table_name
    )

    response = {"statusCode": 200, "body": json.dumps(return_body)}

    return response