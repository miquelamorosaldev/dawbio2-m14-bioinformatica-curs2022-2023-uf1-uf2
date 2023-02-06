'''Requests example: GET method to access an API.'''

import requests
from   requests.models import Response

url:       str      = 'https://animechan.vercel.app/api/random'
response:  Response = requests.get(url)
content:   dict     = response.json()

print(content)
