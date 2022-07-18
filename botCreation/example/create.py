import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_bot(
    botName='ExampleBot',
    description='My first bot created with boto3',
    roleArn='arn:aws:iam::077492956248:role/lambda-invoke-role',
    dataPrivacy={
        'childDirected': False
    },
    idleSessionTTLInSeconds=300,
)


botIdData = response.get('botId')
#create a json file with the botId:
with open('config.json', 'w') as f:
    json.dump({"botId": botIdData}, f, indent=4)
