import boto3
import json


client = boto3.client('lexv2-models')

with open('config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()
    
with open('config.json', 'r') as f:
    welcomeIntentId = json.load(f)['welcomeIntentId']
    f.close()

with open('config.json', 'r') as f:
    queryIntentId = json.load(f)['queryIntentId']
    f.close()



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
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
)

nationalitySlotTypeId = response['slotTypeId']

with open('config.json', 'w') as f:
    json.dump({"botId": botIdData, "welcomeIntentId": welcomeIntentId,"queryIntentId":queryIntentId,"nationalitySlotTypeId":nationalitySlotTypeId}, f, indent=4)
    f.close()
