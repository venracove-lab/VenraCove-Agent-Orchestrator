import boto3
import json
from botocore.exceptions import ClientError

# Initialize Bedrock client
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime')

def lambda_handler(event, context):
    user_input = event.get('userInput', 'How can I help you?')
    session_id = event.get('sessionId', 'new-session')
    
    try:
        response = bedrock_agent_runtime.invoke_agent(
            agentId='your-agent-id',
            agentAliasId='your-agent-alias-id',
            sessionId=session_id,
            inputText=user_input
        )
        
        # Stream the response
        full_response = ""
        for event in response['completion']:
            if 'chunk' in event:
                full_response += event['chunk']['bytes'].decode('utf-8')
        
        return {
            "statusCode": 200,
            "body": json.dumps({"response": full_response, "sessionId": session_id})
        }
    except ClientError as e:
        return {"statusCode": 500, "body": str(e)}