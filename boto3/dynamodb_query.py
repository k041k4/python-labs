import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('e-company')

response = table.query(
    KeyConditionExpression=Key('company-name').eq('a3825853-05af-4ffd-85ed-b91fd8e48b3a')
)
items = response['Items']
print(items)