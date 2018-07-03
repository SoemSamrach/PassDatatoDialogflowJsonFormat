import pandas as pd
import json
entries = []

df1 = pd.read_csv('csvFile/test.csv')
df1.to_json('agentName/intent/testing.json')


with open('agentName/intent/testing.json') as data_file:
    data = json.load(data_file)  # Loading json as dictionary
for i in data['answer']:
    entries.append(data['answer'][i])

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
                entries
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

with open('agentName/intent/testing.json', 'w') as jsonfile:

    # testJson =json.dumps(outputIntentAnswer, indent=4, sort_keys=True)
    json.dump(outputIntentAnswer,jsonfile)
    jsonfile.write('\n')
