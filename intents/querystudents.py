import boto3
import json


client = boto3.client('lexv2-models')

with open('../botCreation/querybot/config.json', 'r') as f:
    botIdData = json.load(f)['botId']
    f.close()

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
    botId=botIdData,
    botVersion='DRAFT',
    localeId='en_US',
)
intentData = response.get('intentId')
#create a json file with the intentId:
with open('config.json', 'w') as f:
    json.dump({"queryIntentId": intentData}, f, indent=4)


