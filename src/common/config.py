import os

diagnosis_url = 'http://localhost:5600/diagnosis_tool/get_prediction'
headers = {
    "Content-Type": "application/json"
}

PORT = os.environ.get('server_port', '5700')

# LiteLLM variables
LITELLM_ENDPOINT = os.environ.get('LITELLM_ENDPOINT', 'http://localhost:4000')
LITELLM_APIKEY = os.environ.get('LITELLM_APIKEY', 'sk-1234')