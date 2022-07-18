import boto3
import json


client = boto3.client('lexv2-models')

with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

with open('config.json', 'r') as f:
    queryIntentId = json.load(f)['queryIntentId']
    f.close()

with open('config.json', 'r') as f:
    nationalitySlotTypeId = json.load(f)['nationalitySlotTypeId']
    f.close()

esponse = client.create_slot(
    slotName='Nationality',
    description='Nationality slot for query students intent',
    slotTypeId=nationalitySlotTypeId,
    valueElicitationSetting={
        'slotConstraint': 'Required',
        'promptSpecification': {
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'Wich nationality should the students have?'
                        },
                        
                    },
                },
            ],
            'maxRetries': 3,
            'allowInterrupt': True,
            'messageSelectionStrategy': 'Random',
        },  
        'sampleUtterances': [
            {
                'utterance': 'Argentina',
            },
            {
                'utterance': 'Bolivia',
            },
            {
                'utterance': 'Venezuela',
            },
            {
                'utterance': 'Any',
            }
        ],    
    },
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
    intentId=queryIntentId
)