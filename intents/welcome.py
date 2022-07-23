import boto3
import json


client = boto3.client('lexv2-models')

with open('../botCreation/querybot/config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

response = client.create_intent(
    intentName='Welcome',
    description='A greeting intent test',
    sampleUtterances=[
        {
            "utterance": "Hi"
        },
        {
            "utterance": "Hello"
        },
        {
            "utterance": "Good Morning"
        },
        {
            "utterance": "I need Help"
        }
    ],
     intentClosingSetting={
        'closingResponse': {
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'Good day {username}! on wich query do you want to start?'
                        },
                    },
                },
            ],
            'allowInterrupt': True
        },
        'active': True
    },
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
)
intentData = response.get('intentId')
#create a json file with the intentId:
with open('config.json', 'w') as f:
    json.dump({"welcomeIntentId": intentData}, f, indent=4)