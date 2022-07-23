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
    intentId= json.load(f)['firstQueryIntentId']
    f.close()

with open('config.json', 'r') as f:
    slotTypeBootcampId= json.load(f)['slotTypeBootcampId']
    f.close()

with open('config.json', 'r') as f:
    slotTypeProgramId= json.load(f)['slotTypeProgramId']
    f.close()




response = client.create_slot_type(
    slotTypeName='CalificationType',
    description='Slot for Program type',
    slotTypeValues=[
        {
            'sampleValue': {
                'value': 'Lowest',
            },
        },
        {
            'sampleValue': {
                'value': 'Average',
            },
        },
        {
            'sampleValue': {
                'value': 'Highest',
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
slotTypeCalificationId = response['slotTypeId']

with open('config.json', 'w') as f:
    json.dump(
        {
        "botId": botIdData, 
        "welcomeIntentId": welcomeIntentId,
        "firstQueryIntentId":intentId,
        "slotTypeBootcampId":slotTypeBootcampId,
        "slotTypeProgramId": slotTypeProgramId,
        "slotTypeCalificationId": slotTypeCalificationId
        }, f, indent=4
    )
    f.close()