

class Todo:

    count = 0

    todo_list = []
    data = {}


    def __init__(self, title="", description="", finished_at=None, created_at=None, updated_at = None, deleted_at= None):
        self.id = Todo.count
        Todo.count += 1
        self.title = title
        self.description = description
        self.finished_at = finished_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def setTodo(self, title, description, finished_at=None, created_at=None, updated_at = None, deleted_at= None):
        data = {"id" : self.id, "title" : title, "description" : description,
            "finished_at" : finished_at, "created_at" : created_at,
            "updated_at" : updated_at, "deleted_at" : deleted_at}

        return data
    
    def listTodo(self):
        print("List Todo: ", self.todo_list)
        return self.data
