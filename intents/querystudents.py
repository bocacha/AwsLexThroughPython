import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_intent(
    intentName='QueryStudents',
    description='An intent to query students',
    sampleUtterances=[
        {
            'utterance': 'Show me all  Jalasoft Students',
           
        },
        {
            'utterance': 'Check Students',
        }
    ],
    # fullfillmentCodeHook={
    # slotPriorities=[
    #     {'priority': 1, 'slotName': 'BootcampType'},
    #     {'priority': 2, 'slotName': 'Nationality'}
        
    # ],
    intentClosingSetting={        
        'closingResponse': {
            'allowInterrupt': True,
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'Ok, i will query Jalasoft students from {BootcampType} Bootcamp from {Nationality}',
                        }
                    },
                }
            ]
        },    
    },
    # slotPriorities=[
    #     {'priority':1,'slotname':'BootcampType'},
    #     {'priority':2,'slotname':'Nationality'}
    # ],
    botId='C8RQQDJY6Y',
    botVersion='DRAFT',
    localeId='en_US',
)

print(response)