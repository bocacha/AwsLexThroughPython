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




response = client.create_slot_type(
    slotTypeName='ProgramType',
    description='Slot for Program type',
    slotTypeValues=[
        {
            'sampleValue': {
                'value': 'English',
            },
        },
        {
            'sampleValue': {
                'value': 'PsichoTest',
            },
        },
        {
            'sampleValue': {
                'value': 'CV',
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
slotTypeProgramId = response['slotTypeId']

with open('config.json', 'w') as f:
    json.dump(
        {
        "botId": botIdData, 
        "welcomeIntentId": welcomeIntentId,
        "firstQueryIntentId":intentId,
        "slotTypeBootcampId":slotTypeBootcampId,
        "slotTypeProgramId": slotTypeProgramId
        }, f, indent=4
    )
    f.close()