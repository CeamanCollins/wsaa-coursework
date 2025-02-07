#from file

import json
filename = "wsaa2.4-json.json"

#fp = file pointer
with open(filename, "r") as fp:
    jsonobject = json.load(fp)
# print(jsonobject)
for employee in jsonobject["employees"]:
    print(employee["firstName"])

# from url

# import requests
# url = "https://someurl.com"
# response = requests.get(url)
# data = response.json()
# print(data)