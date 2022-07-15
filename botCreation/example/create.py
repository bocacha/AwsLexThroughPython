import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_bot(
    botName='LexWithBoto3',
    description='My first bot created with boto3',
    roleArn='arn:aws:iam::077492956248:role/lambda-invoke-role',
    dataPrivacy={
        'childDirected': False
    },
    idleSessionTTLInSeconds=300,
)
   


