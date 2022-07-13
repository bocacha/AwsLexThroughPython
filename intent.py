import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_intent(
    intentName='QueryStudents',
    description='An intent to query students',
    # parentIntentSignature='string',
    sampleUtterances=[
        {
            'utterance': 'Show me the Students',
           
        },
        {
            'utterance': 'Check Students',
        }
    ],
    dialogCodeHook={
        'enabled': False
    },
    fulfillmentCodeHook={
        'enabled': True|False,
        'postFulfillmentStatusSpecification': {
            'successResponse': {
                'messageGroups': [
                    {
                        'message': {
                            'plainTextMessage': {
                                'value': 'string'
                            },
                            'customPayload': {
                                'value': 'string'
                            },
                            'ssmlMessage': {
                                'value': 'string'
                            },
                            'imageResponseCard': {
                                'title': 'string',
                                'subtitle': 'string',
                                'imageUrl': 'string',
                                'buttons': [
                                    {
                                        'text': 'string',
                                        'value': 'string'
                                    },
                                ]
                            }
                        },
                        'variations': [
                            {
                                'plainTextMessage': {
                                    'value': 'string'
                                },
                                'customPayload': {
                                    'value': 'string'
                                },
                                'ssmlMessage': {
                                    'value': 'string'
                                },
                                'imageResponseCard': {
                                    'title': 'string',
                                    'subtitle': 'string',
                                    'imageUrl': 'string',
                                    'buttons': [
                                        {
                                            'text': 'string',
                                            'value': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                ],
                'allowInterrupt': True|False
            },
            'failureResponse': {
                'messageGroups': [
                    {
                        'message': {
                            'plainTextMessage': {
                                'value': 'string'
                            },
                            'customPayload': {
                                'value': 'string'
                            },
                            'ssmlMessage': {
                                'value': 'string'
                            },
                            'imageResponseCard': {
                                'title': 'string',
                                'subtitle': 'string',
                                'imageUrl': 'string',
                                'buttons': [
                                    {
                                        'text': 'string',
                                        'value': 'string'
                                    },
                                ]
                            }
                        },
                        'variations': [
                            {
                                'plainTextMessage': {
                                    'value': 'string'
                                },
                                'customPayload': {
                                    'value': 'string'
                                },
                                'ssmlMessage': {
                                    'value': 'string'
                                },
                                'imageResponseCard': {
                                    'title': 'string',
                                    'subtitle': 'string',
                                    'imageUrl': 'string',
                                    'buttons': [
                                        {
                                            'text': 'string',
                                            'value': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                ],
                'allowInterrupt': True|False
            },
            'timeoutResponse': {
                'messageGroups': [
                    {
                        'message': {
                            'plainTextMessage': {
                                'value': 'string'
                            },
                            'customPayload': {
                                'value': 'string'
                            },
                            'ssmlMessage': {
                                'value': 'string'
                            },
                            'imageResponseCard': {
                                'title': 'string',
                                'subtitle': 'string',
                                'imageUrl': 'string',
                                'buttons': [
                                    {
                                        'text': 'string',
                                        'value': 'string'
                                    },
                                ]
                            }
                        },
                        'variations': [
                            {
                                'plainTextMessage': {
                                    'value': 'string'
                                },
                                'customPayload': {
                                    'value': 'string'
                                },
                                'ssmlMessage': {
                                    'value': 'string'
                                },
                                'imageResponseCard': {
                                    'title': 'string',
                                    'subtitle': 'string',
                                    'imageUrl': 'string',
                                    'buttons': [
                                        {
                                            'text': 'string',
                                            'value': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                ],
                'allowInterrupt': True|False
            }
        },
        'fulfillmentUpdatesSpecification': {
            'active': True|False,
            'startResponse': {
                'delayInSeconds': 123,
                'messageGroups': [
                    {
                        'message': {
                            'plainTextMessage': {
                                'value': 'string'
                            },
                            'customPayload': {
                                'value': 'string'
                            },
                            'ssmlMessage': {
                                'value': 'string'
                            },
                            'imageResponseCard': {
                                'title': 'string',
                                'subtitle': 'string',
                                'imageUrl': 'string',
                                'buttons': [
                                    {
                                        'text': 'string',
                                        'value': 'string'
                                    },
                                ]
                            }
                        },
                        'variations': [
                            {
                                'plainTextMessage': {
                                    'value': 'string'
                                },
                                'customPayload': {
                                    'value': 'string'
                                },
                                'ssmlMessage': {
                                    'value': 'string'
                                },
                                'imageResponseCard': {
                                    'title': 'string',
                                    'subtitle': 'string',
                                    'imageUrl': 'string',
                                    'buttons': [
                                        {
                                            'text': 'string',
                                            'value': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                ],
                'allowInterrupt': True|False
            },
            'updateResponse': {
                'frequencyInSeconds': 123,
                'messageGroups': [
                    {
                        'message': {
                            'plainTextMessage': {
                                'value': 'string'
                            },
                            'customPayload': {
                                'value': 'string'
                            },
                            'ssmlMessage': {
                                'value': 'string'
                            },
                            'imageResponseCard': {
                                'title': 'string',
                                'subtitle': 'string',
                                'imageUrl': 'string',
                                'buttons': [
                                    {
                                        'text': 'string',
                                        'value': 'string'
                                    },
                                ]
                            }
                        },
                        'variations': [
                            {
                                'plainTextMessage': {
                                    'value': 'string'
                                },
                                'customPayload': {
                                    'value': 'string'
                                },
                                'ssmlMessage': {
                                    'value': 'string'
                                },
                                'imageResponseCard': {
                                    'title': 'string',
                                    'subtitle': 'string',
                                    'imageUrl': 'string',
                                    'buttons': [
                                        {
                                            'text': 'string',
                                            'value': 'string'
                                        },
                                    ]
                                }
                            },
                        ]
                    },
                ],
                'allowInterrupt': True|False
            },
            'timeoutInSeconds': 123
        }
    },
    botId='UYDAFVYMVQ',
    botVersion='DRAFT',
    localeId='en_US',
)