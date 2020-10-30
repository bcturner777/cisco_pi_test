import requests
import json
from requests.packages import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://primeinfrasandbox.cisco.com/webacs/api/v3/data/RogueApAlarms.json?.full=true'
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

#Load the JSON data as a dictionary
dict = json.loads(response.text)
#print(json.dumps(dict, indent=4, sort_keys=True))

#Set counters
count1 = 0
count2 = 0

#Drop into first list of meaningful data which is the value of the key "entity"
data = dict['queryResponse']['entity']
#iterate through the "entity" list which contains dictionaries for each alarm set
for find_list in data:
    #iterate through the key/value pairs to find "rogueApAlarmsDTO" for meaningful alarm details
    for key, value in find_list.items():
        if key=='rogueApAlarmsDTO':
            #iterate through the key/value pairs to find and print meaningful alarm details
            for key1, value1 in value.items():
                #start counter for entire rogue alarm API count
                count1 = count1 + 1
                if key1=='alarmFoundAt':
                    print('\n' + key1, value1)
                elif key1=='message':
                    print('log message = ', value1)
                    #start counter for all alarm sets with a message detail
                    count2 = count2 + 1
                elif key1=='rogueApAlarmDetails':
                    for key2, value2 in value1.items():
                        #filter out details with null values
                        if value2 != False:
                            print(key2, '=', value2)

#print the count results
print('\nTotal event count = ', count1)
print('Total message count = ', count2)
