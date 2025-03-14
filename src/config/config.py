import os

diagnosis_url = 'http://localhost:5600/diagnosis_tool/get_prediction'
headers = {
    "Content-Type": "application/json"
}

PORT = os.environ.get('server_port', '5700')