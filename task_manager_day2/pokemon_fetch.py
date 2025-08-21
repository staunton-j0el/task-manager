import json
task1 = {"id": 1, "title": "Title", "done": False}
print(task1) #dict
task1 = json.dumps(task1)
print(task1) #json
task1 = json.loads(task1)
print(task1) #back to dict
