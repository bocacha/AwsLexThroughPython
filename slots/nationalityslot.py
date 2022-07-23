import boto3
import json


client = boto3.client('lexv2-models')

esponse = client.create_slot(
    slotName='Nationality',
    description='Bootcamp slot for query students intent',
    slotTypeId='RCFOM9NTEZ',
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
    botId='C8RQQDJY6Y',
    botVersion='DRAFT',
    localeId='en_US',
    intentId='7WNEOVEESK',
)