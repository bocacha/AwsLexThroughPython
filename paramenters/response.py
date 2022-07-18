{'ResponseMetadata': {
    'RequestId': '7f2ae81d-0dd1-453a-8799-1cf0ce84975a', 
    'HTTPStatusCode': 200, 
    'HTTPHeaders': {
        'date': 'Sat, 16 Jul 2022 17:33:39 GMT', 
        'content-type': 'application/json', 
        'content-length': '768', 
        'connection': 'keep-alive', 
        'x-amzn-requestid': '7f2ae81d-0dd1-453a-8799-1cf0ce84975a', 
        'strict-transport-security': 'max-age=31536000; includeSubDomains', 
        'x-amz-apigw-id': 'VXtx-GKmPHcFhHw=', 
        'x-content-type-options': 'nosniff', 
        'x-amzn-trace-id': 'Root=1-62d2f672-306a2f1e610688a1041a54b3'
    }, 'RetryAttempts': 0
}, 
'intentId': 'HWGRLDZXTI',
'intentName': 'Welcome', 
'description': 'A greeting intent test', 
'sampleUtterances': [
    {'utterance': 'Hi'}, 
    {'utterance': 'Hello'}, 
    {'utterance': 'Good Morning'}, 
    {'utterance': 'I need Help'}
], 
'intentClosingSetting': {
    'closingResponse': {
        'messageGroups': [
            {'message': 
            {
                'plainTextMessage': {
                    'value': 'Good day {username}! on wich query do you want to start?'
                }
                }
            }
        ], 'allowInterrupt': True
    }, 
    'active': True
}, 
'botId': 'DALKJYVLDO', 
'botVersion': 'DRAFT', 
'localeId': 'en_US', 
'creationDateTime': datetime.datetime(2022, 7, 16, 13, 33, 38, 966000, tzinfo=tzlocal())}
