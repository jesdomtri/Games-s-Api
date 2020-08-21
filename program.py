import json

with open('api.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

api = {}
games = []

for x in obj:
    if x["isExpansion"] == False:
        games.append({"name": x["name"]})

api["Games"] = games
api["Users"] = {
    "VruO3Eol16MmqYsmoXCp2kgjnqB3": {
        "Games": {
            "-MFFJIAP3MbINxsPh5_Y": {
                "name": "10 Days in Africa"
            },
            "-MFFJKE-Vcv8b1hwpZSX": {
                "name": "Above and Below"
            },
            "-MFFJOm1a4oOI42qnJbe": {
                "name": "Ascension: Year One Collector's Edition"
            }
        }
    }
}

api["Matches"] = {
    "10 Days in Africa": [
        {
            "VruO3Eol16MmqYsmoXCp2kgjnqB3": {
                "score": 90,
                "winner" : True,
                "position" : 1
            },
            "IYDfG66zDNgiSyuGY8alAKihzUL2": {
                "score": 10,
                "winner" : False,
                "position" : 2
            }
        }
    ],
    "Above and Below": [
        {
            "VruO3Eol16MmqYsmoXCp2kgjnqB3": {
                "score": 5,
                "winner" : False,
                "position" : 2
            },
            "IYDfG66zDNgiSyuGY8alAKihzUL2": {
                "score": 10,
                "winner" : True,
                "position" : 1
            }
        }
    ]
}

with open('newApi.json', 'w') as json_file:
    json.dump(api, json_file)
