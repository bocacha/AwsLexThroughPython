import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_slot_type(
    slotTypeName='Nationality',
    description='Slot for bootcamp type',
    slotTypeValues=[
        {
            'sampleValue': {
                'value': 'Nationality',
            },
        },
    ],
    valueSelectionSetting={
        'resolutionStrategy': 'OriginalValue',
    },
    botId='C8RQQDJY6Y',
    botVersion='DRAFT',
    localeId='en_US',
)

print(response)