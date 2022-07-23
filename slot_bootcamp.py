import boto3
import json


client = boto3.client('lexv2-models')

with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

with open('config.json', 'r') as f:
    IntentId = json.load(f)['firstQueryIntentId']
    f.close()

with open('config.json', 'r') as f:
    slotTypeId = json.load(f)['slotTypeBootcampId']
    f.close()


response = client.create_slot(
    slotName='bootcampSlot',
    description='Slot for query intent',
    slotTypeId=slotTypeId,
    valueElicitationSetting={
        'slotConstraint': 'Required',
        'promptSpecification': {
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'Wich bootcamp do you want to query?'
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
                'utterance': 'Latam001',
            },
            {
                'utterance': 'Latam002',
            },
            {
                'utterance': 'Latam003',
            },
        ],    
    },
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
    intentId=IntentId
) 