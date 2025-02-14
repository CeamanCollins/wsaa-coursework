import requests
import json

# url = "https://rickandmortyapi.com/api/character"
# response = requests.get(url)
# data = response.json()
# # print(data)

# with open("rickandmortycharacters.json", "w") as fp:
#     json.dump(data, fp)

with open("rickandmortycharacters.json", "r") as fp:
    data = json.load(fp)

# print(data)

chars = data["results"]
for char in chars:
    print(char['name'])