import json
import requests

res = requests.get('')
response = json.loads(res.text)
