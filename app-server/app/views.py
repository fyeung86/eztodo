import logging
from app import app
from app.service import APIService
from flask import render_template
from flask import Flask, request, abort, redirect, url_for, jsonify, make_response

log = logging.getLogger(__name__)
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
    return jsonify({'op': True}), 201

@app.route('/update_task')
def update_task():
    service.update_task()
    return jsonify({'op': True}), 201

@app.route('/add_task', methods=['POST'])
def add_task():
    log.debug('Adding task')
    if not request.json or 'action' not in request.json:
        abort(400)
    else:
        action = request.json['action']
        json_response = service.add_task(action)
        log.debug('Response: %s', json_response)
        return jsonify(json_response), 201

@app.route('/static/<string:directory>/<path:path>')
def send_static(directory, path):
    return send_from_directory(directory, path)
