import requests
import json

params = {
    'project_name': 'tata',
    'client_id':13,
    'user_id':1,
'project_createdby':'morejygvjhbiuyubuyvytc'
          }
jsondata=json.dumps(params)
response = requests.post('http://127.0.0.1:8000/project/',
            data=jsondata)
print(response.json())
