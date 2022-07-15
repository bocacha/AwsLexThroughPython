import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_bot_version(
    botId='C8RQQDJY6Y',
    description='Jala Lex bot create version',
    botVersionLocaleSpecification={
        'en_US': {
            'sourceBotVersion': 'DRAFT'
        }
    }
)