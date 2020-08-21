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
    "VruO3Eol16MmqYsmoXCp2kgjnqB3": {
        "10 Days in Africa": [
            {
                "score": 90,
                "winner": True,
                "position": 1
            }
        ],
        "Above and Below": [
            {
                "score": 5,
                "winner": False,
                "position": 2
            }
        ]
    },
    "IYDfG66zDNgiSyuGY8alAKihzUL2": {
        "10 Days in Africa": [
            {
                "score": 10,
                "winner": False,
                "position": 2
            }
        ],
        "Above and Below": [
            {
                "score": 10,
                "winner": True,
                "position": 1
            }
        ]
    }
}

with open('newApi.json', 'w') as json_file:
    json.dump(api, json_file)
