import boto3
import json

bedrock = boto3.client('bedrock-runtime')

def determine_task(user_input):
    # Uses a lightweight model to decide what the user wants
    return "generation" # Simplified for orchestration logic

def lambda_handler(event, context):
    user_input = event.get('userInput', '')
    task = determine_task(user_input)
    
    model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
    if task == 'classification':
        model_id = 'amazon.titan-text-express-v1'

    return {
        "statusCode": 200,
        "selectedModel": model_id,
        "status": "Ready for multi-model execution"
    }