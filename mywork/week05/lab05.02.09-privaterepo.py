import requests
from config import keys
from urllib import parse
import json

# url = "https://api.github.com/repos/CeamanCollins/aprivateone/commits"
url = "https://api.github.com/repos/CeamanCollins/aprivateone/git/blobs/5549a93d3a94fbaa03a3d216d6383405d557fa68"
# url = 'https://api.github.com/repos/CeamanCollins/aprivateone/README.md'
key = keys['github']

response = requests.get(url, auth=('token',key))
print(response.status_code)

repo_response = response.json()

with open('blob.json', 'w') as fp:
    json.dump(repo_response, fp, indent=4)
