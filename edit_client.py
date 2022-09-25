import requests
import json

params = {
    "id":13,
    "name": "khan4567",
}
jsondata=json.dumps(params)
response = requests.put('http://127.0.0.1:8000/client/',
            data=jsondata)
print(response.json())
