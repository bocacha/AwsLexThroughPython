import boto3
import json


client = boto3.client('lexv2-models')

with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

response = client.create_bot_locale(
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
    description='Create locale for Jala query bot',
    nluIntentConfidenceThreshold=0.40,
    voiceSettings={
        'voiceId': 'Joanna',
        'engine': 'neural'
    }
    
)

print("botId loaded from config.json: ",response.get('botId'))