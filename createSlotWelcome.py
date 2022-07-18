import boto3
import json

client = boto3.client('lexv2-models')

with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

with open('config.json', 'r') as f:
    welcomeIntentId = json.load(f)['welcomeIntentId']
    f.close()

response = client.create_slot(
    slotName='username',
    description='Username slot for welcome intent',
    slotTypeId='AMAZON.FirstName',
    valueElicitationSetting={
        'slotConstraint': 'Required',
        'promptSpecification': {
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'PLease, tell me your name'
                        },
                        
                    },
                },
            ],
            'maxRetries': 3,
            'allowInterrupt': True,
            'messageSelectionStrategy': 'Random',
        },      
    },
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
    intentId=welcomeIntentId,
)