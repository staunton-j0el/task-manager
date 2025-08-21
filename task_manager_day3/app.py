from flask import Flask, jsonify
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

            

if __name__ == "__main__":
    app.run(debug=True)