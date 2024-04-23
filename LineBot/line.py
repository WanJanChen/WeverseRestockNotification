import requests
import os
from dotenv import load_dotenv
load_dotenv()
def line_notify(msg):
    token = os.getenv('LINE_TOKEN') 
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + token
    }
    data = {
        'message': msg
    }
    requests.post(url, headers=headers, data=data)