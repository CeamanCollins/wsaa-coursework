import requests
import json
from urllib import parse

# request_url = 'https://api.github.com/users/CeamanCollins/repos'
# request_url = 'https://api.github.com/repos/CeamanCollins/pands-mywork'
# request_url = 'https://api.github.com/repos/CeamanCollins/pands-mywork/commits'

# response = requests.get(url=request_url,headers={"HTTP":"Accept: application/vnd.github+json"})

# print(response.status_code)

# response_json = response.json()

# with open('repos.json', 'w') as fp:
#     json.dump(response_json, fp, indent=4)

with open('repos.json', 'r') as fp:
    data = json.load(fp)

# print(data[0]['commit']['message'])

for commit in data:
    print(commit['commit']['message'])



