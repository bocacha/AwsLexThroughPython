import boto3
import json


client = boto3.client('lexv2-models')

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
    botId='C8RQQDJY6Y',
    botVersion='DRAFT',
    localeId='en_US',
)