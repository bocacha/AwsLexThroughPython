import boto3
import json


client = boto3.client('lexv2-models')

response = client.create_bot_locale(
    botId='C8RQQDJY6Y',
    botVersion='DRAFT',
    localeId='en_US',
    description='Create locale for Jala query bot',
    nluIntentConfidenceThreshold=0.40,
    voiceSettings={
        'voiceId': 'Joanna',
        'engine': 'neural'
    }
    
)