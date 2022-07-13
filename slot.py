import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_slot(
    slotName='Students',
    description='A slot for students intended for use with the LexWithBoto3 bot',
    slotTypeId='Students',
    valueElicitationSetting={        
        'slotConstraint': 'Required',
        'promptSpecification': {
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'I will check Jalasoft Students!'
                        },
                    },

                },
            ],
            'maxRetries': 4,
            'allowInterrupt': True,
            'messageSelectionStrategy': 'Random',
        },    
    },
   botId='UYDAFVYMVQ',
    botVersion='DRAFT',
    localeId='en_US',
    intentId='YHLH1N2DAH',
    
)