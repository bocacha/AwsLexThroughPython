import boto3
import json


client = boto3.client('lexv2-models')

with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

response = client.create_bot_version(
    botId=botIdData,
    description='Lex bot create version',
    botVersionLocaleSpecification={
        'en_US': {
            'sourceBotVersion': 'DRAFT'
        }
    }
)
