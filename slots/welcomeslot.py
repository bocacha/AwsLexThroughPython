import boto3
import json


client = boto3.client('lexv2-models')

esponse = client.create_slot(
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
    botId='C8RQQDJY6Y',
    botVersion='DRAFT',
    localeId='en_US',
    intentId='A5Q2KLJ830',
)