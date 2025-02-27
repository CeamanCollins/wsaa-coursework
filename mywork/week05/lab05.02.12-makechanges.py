import requests
from config import keys
from urllib import parse
import json
import base64

url = 'https://api.github.com/repos/CeamanCollins/aprivateone/contents/README.md'
key = keys['github']
content = base64.b64encode(bytes('# Private Repo \n \n This is a private repo for test purposes. \n \n This is an additional test. \n \n And a further test.', 'utf-8'))
# print(content.decode('utf-8'))


# , auth=('token',key)
response = requests.put(url, headers={
    "Accept" : "application/vnd.github+json",
    "Authorization" : f"Bearer {key}"
    },
    json={
        "message":"updating README2.md",
        "committer":{
            "name":"Ceaman Collins",
            "email":"ceaman.collins@gmail.com"
            },
        "content":f"{content.decode('utf-8')}",
        "sha":"8703e0bd28ef63737d8147d6808003036e6d1e2a"
        }
    )
print(response.status_code, " ", response.json()['message'])

