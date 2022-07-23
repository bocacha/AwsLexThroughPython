import boto3
import json


client = boto3.client('lexv2-models')

with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

with open('config.json', 'r') as f:
    intentId = json.load(f)['firstQueryIntentId']
    f.close()

with open('config.json', 'r') as f:
    slotTypeId = json.load(f)['slotTypeCalificationId']
    f.close()


response = client.create_slot(
    slotName='calificationSlot',
    description='Slot for calification response',
    slotTypeId=slotTypeId,
    valueElicitationSetting={
        'slotConstraint': 'Required',
        'promptSpecification': {
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'Wich Calification level do you need?'
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
                'utterance': 'Lowest',
            },
            {
                'utterance': 'Average',
            },
            {
                'utterance': 'Highest',
            },
        ],    
    },
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
    intentId=intentId
) 
