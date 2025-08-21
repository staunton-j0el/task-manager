from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Clean desk", "done": False},
    {"id": 3, "title": "Read book", "done": True},
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)
#visitng path /tasks/<id> returns specifc task 
@app.route("/tasks/<int:id>", methods=["GET"])
def get_task_id(id):
    for task in tasks:
        if task["id"] == id:
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json() # read json body
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title", "Untitled task"),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


'''
POST example
curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title":"Learn Flask"}'
      #      
'''
if __name__ == "__main__":
    app.run(debug=True)