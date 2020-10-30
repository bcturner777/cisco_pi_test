import requests
import json
from requests.packages import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
user_data = input('Enter device model you want to search for: ')
url = 'https://primeinfrasandbox.cisco.com/webacs/api/v3/data/Devices.json?.full=true&deviceType=contains(' + user_data + ')'
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
#print(dict['queryResponse']['entity'][0]['devicesDTO']['deviceName'])
