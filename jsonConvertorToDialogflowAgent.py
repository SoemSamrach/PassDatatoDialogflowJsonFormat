
import pandas as pd
import json

entries_answer = []
entries_question = []
arrayIntentUserSay = []
df1 = pd.read_csv('csvFile/test.csv')
df1.to_json('agentName/intent/file.json')

with open('agentName/intent/file.json') as data_file:
    data = json.load(data_file)  # Loading json as dictionary

for i in data['question']:
    entries_question.append(data['question'][i])


for i in data['answer']:
    entries_answer.append(data['answer'][i])

for rec in entries_question:
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

outputIntentAnswer = {
    "name": "testing",
    "auto": True,
    "contexts": [],
    "responses": [{
        "resetContexts": False,
        "affectedContexts": [],
        "parameters": [],
        "message": [{
            "type": 0,
            "lang": "en",
            "speech":
                entries_answer
        }
        ],
        "defaultResponsePlatform": {},
        "speech": []
    }
    ],
    "priority": 500000,
    "webhookUsed": False,
    "webhookForSlotFilling": False,
    "lastUpdate": 1530453117,
    "fallbackItent": False,
    "events": []

}

with open('agentName/intent/testing.json', 'w') as jsonfile_answer:
    json.dump(outputIntentAnswer, jsonfile_answer)
    jsonfile_answer.write('\n')
with open('agentName/intent/testing_usersays_en.json', 'w') as jsonfile_question:
    json.dump(arrayIntentUserSay, jsonfile_question)
    jsonfile_question.write('\n')