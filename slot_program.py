import boto3
import json


client = boto3.client('lexv2-models')

with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

with open('config.json', 'r') as f:
    instentId = json.load(f)['firstQueryIntentId']
    f.close()

with open('config.json', 'r') as f:
    slotTypeId = json.load(f)['slotTypeProgramId']
    f.close()


response = client.create_slot(
    slotName='programSlot',
    description='Slot for program response',
    slotTypeId=slotTypeId,
    valueElicitationSetting={
        'slotConstraint': 'Required',
        'promptSpecification': {
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'Wich Program do you need?'
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
                'utterance': 'English',
            },
            {
                'utterance': 'PsichoTest',
            },
            {
                'utterance': 'CodingSkills',
            },
        ],    
    },
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
    intentId=instentId
) 