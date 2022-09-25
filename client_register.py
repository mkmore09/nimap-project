import requests
import json

params = {"name": "junaid",
"createdby":"more"}
jsondata=json.dumps(params)
response = requests.post('http://127.0.0.1:8000/client/',
            data=jsondata)
print(response.json())
