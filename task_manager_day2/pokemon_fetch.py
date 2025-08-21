## requests pokemon names from api, write to file

import json
import requests
'''
task1 = {"id": 1, "title": "Title", "done": False}
print(task1) #dict
task1 = json.dumps(task1)
print(task1) #json
task1 = json.loads(task1)
print(task1) #back to dict
'''

# request = requests.get("https://pokeapi.co/api/v2/pokemon/1")
# parsedResponse = request.json()3
pokeList = []

for i in range(1, 6):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
    parsedResponse = response.json()
    pokeList.append(parsedResponse["forms"][0]["name"])
with open("pokemon_names.txt", "w") as file:
    for item in pokeList:
        file.write(f"{item}\n")

print(pokeList)