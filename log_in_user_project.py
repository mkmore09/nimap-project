import requests
import json
params = {
    'id':1,
    }
jsondata=json.dumps(params)
response = requests.get('http://127.0.0.1:8000/user/',
            data=jsondata)
print(response.json())
