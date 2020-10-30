import requests
import json
from requests.packages import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://primeinfrasandbox.cisco.com/webacs/api/v3/data/Devices.json"
basic_token = "Basic", os.getenv('token')

headers = {
    'Authorization': basic_token,
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "primeinfrasandbox.cisco.com",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, verify=False)

#print(type(response))
dict = json.loads(response.text)
print(json.dumps(dict, indent=4, sort_keys=True))
