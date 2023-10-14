from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data.decode('utf-8')
    print("Incoming request with the following body", request_body)

    new_todo = request.get_json()
    todos.append(new_todo)

    return 'Todo added successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)