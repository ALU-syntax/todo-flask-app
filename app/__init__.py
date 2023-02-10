from flask import Flask, render_template

SECRET_KEY = "some secret key"
app = Flask("app")

from app.controller.todo_controller import todo
app.register_blueprint(todo)
app.config['SECRET_KEY'] = SECRET_KEY
