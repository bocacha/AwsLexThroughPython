import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_slot(
    slotName='BootcampType',
    description='Bootcamp slot for query students intent',
    slotTypeId='GF5PQBWWK8',
    valueElicitationSetting={
        'slotConstraint': 'Required',
        'promptSpecification': {
            'messageGroups': [
                {
                    'message': {
                        'plainTextMessage': {
                            'value': 'Wich bootcamp do you want to query?'
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
                'utterance': 'DevOps',
            },
            {
                'utterance': 'Data Science',
            },
            {
                'utterance': 'FullStack',
            },
        ],    
    },
    botId='C8RQQDJY6Y',
    botVersion='DRAFT',
    localeId='en_US',
    intentId='7WNEOVEESK',
)

print(response)
# with open('bootcampslot.json', 'w') as f:
#     json.dump(response, f, indent=4)
#     f.close()
#     print('File saved!')
#     print('You can now import the file into AWS Lambda')
#     print('https://console.aws.amazon.com/lambda/home?region=us-east-1#/')
#     print('and then create a new function')
#     print('https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/new')
#     print('and then import the file into the function')
#     print('https://console.aws.amazon.com/lambda/home?region=us-east-1#/import/new')
#     print('and then deploy the function')
#     print('https://console.aws.amazon.com/lambda/home?region=us-east-1#/deploy/new')
#     print('and then invoke the function')
#     print('https://console.aws.amazon.com/lambda/home?region=us-east-1#/invocations/new')
#     print('and then you can use the function')
#     print('https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/')
#     print('to query the data')
   