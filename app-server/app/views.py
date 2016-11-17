from app import app
from app.service import APIService
from flask import render_template

service = APIService()

@app.route('/')
def home():
    #tasks = service.all_tasks()
    tasks = [
            {'action': 'Hit the gym'},
            {'action': 'Pay bills'},
            {'action': 'Meet George'},
            {'action': 'Buy Eggs'},
            {'action': 'Read a book'},
            {'action': 'Organize office'}
    ]
    return render_template('index.html', tasks=tasks)

@app.route('/remove_task')
def remove_task():
    service.remove_task()
    return  { 'op': True }

@app.route('/update_task')
def update_task():
    service.update_task()

@app.route('/add_task')
def add_task():
    service.add_task()

@app.route('/static/<directory:directory>/<path:path>')
def send_static(directory, path):
    return send_from_directory(directory, path)
