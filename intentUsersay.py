
import pandas as pd
import json

entries = []
arrayIntentUserSay = []
f = False
df1 = pd.read_csv('csvFile/test.csv')
df1.to_json('agentName/intent/testing_usersays_en.json')

with open('agentName/intent/testing_usersays_en.json') as data_file:
    data = json.load(data_file)  # Loading json as dictionary

for i in data['question']:
    entries.append(data['question'][i])

for rec in entries:
    outputIntentUserSay = {
        "data": [
            {
                "text": rec,
                "userDefined": False,
            }
        ],
        "isTemplate": False,
        "count": 0,
        "update": 1530453117
    }
    arrayIntentUserSay.append(outputIntentUserSay)

# print(arrayIntentUserSay)

with open('agentName/intent/testing_usersays_en.json', 'w') as jsonfile:
    json.dump(arrayIntentUserSay, jsonfile)
    jsonfile.write('\n')
