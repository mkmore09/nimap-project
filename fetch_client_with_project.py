import requests
import json
params = {
    'id':13,
    }
jsondata=json.dumps(params)
response = requests.get('http://127.0.0.1:8000/project/',
            data=jsondata)
print(response.json())
