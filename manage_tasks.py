 # simple task management script

taskList = [
    {"id": 1, "title": "Task 1", "done": False},
    {"id": 2, "title": "Task 2", "done": False},
    {"id": 3, "title": "Task 3", "done": False}
]
# marks a task as done if given id is matched
def mark_done(task_id):
    for task in taskList:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Task {task_id} is {task['done']}")
            break
# removes task containing given id
def remove_task(task_id):
    for task in taskList:
        if task["id"] == task_id:
            taskList.remove(task)
            print(f"Task {task_id} is removed")
            break

remove_task(3)

for task in taskList:
    mark_done(task["id"])
   


