from flask import render_template, Blueprint, request, redirect
from app import app
from app.model.todo import Todo
from datetime import datetime
import numpy as np



todo = Blueprint("todo", __name__, static_folder="static", template_folder="templates")

todos = Todo()
time = datetime.now() 
formatDateTime = time.strftime("%d"),'-',time.strftime("%m"),'-',time.strftime("%Y"), ' ',time.strftime("%H"),':',time.strftime("%M"),':',time.strftime("%S")



def all_the_args(*args):
    return args

@app.route("/", methods=['GET'])
@app.route("/todo", methods=['GET'])
def getAllTodo():
    x = todos.todo_list
    print("dataStorage: ", x)

    result = all_the_args(*x)

    filter = []
    for i in range(0,len(result)):
        y = result[i]
        if y['deleted_at'] == None:
            filter.append(y)

    return render_template('index.html', listTodo = filter)

@app.route("/todo", methods = ['POST'])
def add():
    format
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        created = formatDateTime
        
        if not title or description:
            todo = Todo(title=title, description=description, created_at=created)
            data = todo.setTodo(title=title, description=description, created_at=created)
            todo.todo_list.append(data)
    return redirect("/todo")

@app.route('/todo/get/<int:id>', methods = ['GET'])
def getTodoById(id):
    index = 0
    print("debugId: ", id)
    
    if not id or id != 0:
        entry = todos.todo_list[id-1] 
        index+1
        print("debugEntry: ",entry['title'])
                
        return render_template("update.html", entrys=entry)                
    return "<h1>Data Not Found!</h1>"
    
@app.route('/todo/<int:id>', methods = ['POST'])
def updateTodo(id):
    if not id or id != 0:
        entry = todos.todo_list[id-1]
        form = request.form
        entry['title'] = form.get('title')
        entry['description'] = form.get('description')
        entry['updated_at'] = formatDateTime
        return redirect('/')

    return "<h3>Gagal Update</h3>"
    

@app.route('/todo/finish/<int:id>')
def finishedTodo(id):
    if not id or id != 0:
        entry = todos.todo_list[id-1]
        if entry['finished_at'] == None:
            print("debugFinish: datamasuk")
            entry['finished_at'] = formatDateTime
        else:
            entry['finished_at'] = None;
        return redirect('/')
    
    return redirect('/todo')


@app.route('/todo/delete/<int:id>')
def deleteTodo(id):
    if not id or id != 0:
        entry = todos.todo_list[id-1]
        entry['deleted_at'] = formatDateTime
        return redirect('/')

    return redirect('/todo')