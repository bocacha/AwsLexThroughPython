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
    slotTypeId = json.load(f)['slotTypeId']
    f.close()


response = client.create_slot(
    slotName='BootcampType',
    description='Bootcamp slot for query students intent',
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
                'utterance': 'DevOps',
            },
            {
                'utterance': 'Data Science',
            },
            {
                'utterance': 'FullStack',
            },
        ],    
    },
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
    intentId=queryIntentId
) 