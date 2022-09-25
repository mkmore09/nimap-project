import requests
import json
params = {
    'id':2,
    }
jsondata=json.dumps(params)
response = requests.delete('http://127.0.0.1:8000/client/',
            data=jsondata)
print(response.json())
