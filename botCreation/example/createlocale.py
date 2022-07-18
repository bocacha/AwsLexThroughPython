import boto3
import json


client = boto3.client('lexv2-models')
#read the botId from the json file: config.json, and save it in the variable botIdData:
with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()


response = client.create_bot_locale(
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
    description='Create locale for Lex bot',
    nluIntentConfidenceThreshold=0.40,
    voiceSettings={
        'voiceId': 'Joanna',
        'engine': 'neural'
    }
    
)

print("botId loaded from config.json: ",response.get('botId'))