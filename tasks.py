name = "Task manager"
if len(name) > 5:
	print("long name")

for i in range(3):
	print("Task", i)

def greet(user):
	return f"hello {user}"
print(greet("Alice"))

tasks =  ["Buy milk", "Clean desk"]
tasks.append("Read book")
print(tasks)

task = {"ID": 1, "Title": "Buy Milk", "done": False}
print(task["Title"])
