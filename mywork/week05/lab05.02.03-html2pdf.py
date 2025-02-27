import requests
from config import keys
from urllib import parse

auth = keys['html2pdf']
apiurl =  'https://api.html2pdf.app/v1/generate'
source = 'http://google.com/'

params = {'html':source, 'apiKey':auth}
parsed_params = parse.urlencode(params)
request_url = apiurl + "?" + parsed_params

response = requests.get(request_url)
print(response.status_code)

result = response.content

with open('google.pdf', 'wb') as fp:
    fp.write(result)