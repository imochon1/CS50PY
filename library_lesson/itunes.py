import requests
import sys
import json

# check if the user has entered a search term
if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)

o = response.json()
for result in o["results"]:  # quotes are for the key
    print(result["trackName"])

# print(json.dumps(response.json(), indent=2))

# print("Result song name: " + response.json()["results"][0]["trackName"])
