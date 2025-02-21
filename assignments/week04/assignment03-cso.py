# cso.py
# author Céaman Collins
# script to download Exchequer Account (Historical Series) from CSO website
# and to store it as a file, cso.json

import requests
import json

response = requests.get('https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en')
data = response.json()

with open('cso.json', 'wt') as fp:
    json.dump(data, fp)