import requests
import json

url = 'http://127.0.0.1:5002/service1'
data = 'hello'

response = requests.get(url, data=data)
json_data = json.loads(response.text)
print(json_data)
