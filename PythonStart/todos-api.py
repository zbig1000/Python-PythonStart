from flask import Flask, request
from flask_restful import abort, Api, Resource

from dataclasses import dataclass, asdict

app = Flask(__name__)
api = Api(app)


@dataclass
class Todo:
    task: str
    id: int = None
        
    _last_id = 0
    
    def __post_init__(self):
        if self.id is None:
            Todo._last_id += 1
            self.id = Todo._last_id


todos = [
    Todo(task='build an API'),
    Todo(task='something else'),
    Todo(task='bla bla'),
]
todos = {todo.id: todo for todo in todos}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos:
        abort(404, message=f"Todo {todo_id} doesn't exist")

# Todo
# shows a single todo item and lets you delete a todo item
class TodoResource(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return asdict(todos[todo_id])

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del todos[todo_id]
        return '', 204

    def put(self, todo_id):        
        abort_if_todo_doesnt_exist(todo_id)
        task_name = request.json.get('task', None)
        if task_name is None or task_name == '':
            return {'message': 'Task name cannot be empty'}, 400
        todo = Todo(task_name, id=todo_id)
        todos[todo.id] = todo
        return asdict(todo), 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return [asdict(todo) for todo in todos.values()]

    def post(self):
        task_name = request.json.get('task', None)
        if task_name is None or task_name == '':
            return {'message': 'Task name cannot be empty'}, 400
        todo = Todo(task_name)
        todos[todo.id] = todo
        return asdict(todo), 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(TodoResource, '/todos/<int:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)