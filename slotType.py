import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_slot_type(
    slotTypeName='Students',
    description='A slot for students intended for use with the LexWithBoto3 bot',
    slotTypeValues=[
        {
            'sampleValue': {
                'value': 'Students'
            },
        },
    ],
    valueSelectionSetting={
        'resolutionStrategy': 'OriginalValue',
    },
    botId='UYDAFVYMVQ',
    botVersion='DRAFT',
    localeId='en_US',
)