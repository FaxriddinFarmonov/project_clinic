
import requests
import json

SCOPUS_API_KEY='2883c1a19ce507c0ced7b6487e35851b'

import requests
from pprint import pprint

url = 'https://api.elsevier.com/content/search/scopus'
headers = {
    'X-ELS-APIKey': '285fbb82ea7717b8bc6b7e0f9d2b422d',
}

params = {
    'query': 'AU-ID(57205465027)',

}

response = requests.get(url, headers=headers, params=params)
print(response, '====')
data = response.json()
pprint(data)
