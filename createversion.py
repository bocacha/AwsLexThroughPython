import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_bot_version(
    botId='UYDAFVYMVQ',
    description='Lex bot create version',
    botVersionLocaleSpecification={
        'en_US': {
            'sourceBotVersion': 'DRAFT'
        }
    }
)
