from flask import Flask, request, abort, redirect, url_for, jsonify, make_response
from flask.ext.sqlalchemy import SQLAlchemy, DeclarativeMeta
from json import JSONEncoder

class ProductJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return obj.to_dict()
        return super(ProductJSONEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = ProductJSONEncoder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    action = db.Column(db.String(80), nullable=False)

    def __init__(self, action):
        self.action = action 

    def __repr__(self):
        return '<User %r>' % self.name

    def to_dict(self):
        return dict(action=self.action, id=self.id)


@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    print 'getting'
    return jsonify(dict(tasks=Task.query.all()))


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    prods=Task.query.filter(id=id)
    if len(prods) == 0:
        abort(404)
    return jsonify({'task': prods.first()})


@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'action' not in request.json:
        abort(400)
    print("Creating Task", request.json)
    prod = Task(action=request.json['action'])
    db.session.add(prod)
    db.session.commit()
    return jsonify({'op': 'OK', 'task': prod}), 201

@app.route('/tasks/<int:sku>', methods=['PUT'])
def update_task(sku):
    print('deleting tasks', sku)
    if not request.json or 'action' not in request.json:
        abort(400)

    tasks =Task.query.filter(id=sku)
    if len(tasks) == 0:
        abort(404)
    for task in tasks:
        task.action = request.json['action']
    db.session.commit()

@app.route('/tasks/<int:sku>', methods=['DELETE'])
def remove_task(sku):
    print('deleting tasks', sku)
    tasks =Task.query.filter(id=sku)
    if len(tasks) == 0:
        abort(404)
    for task in tasks:
        db.session.delete(task)
    db.session.commit()
    return jsonify({'op': 'OK'})

@app.route('/tasks', methods=['DELETE'])
def remove_all_tasks():
    print('deleting all tasks')
    tasks = Task.query.all()
    for task in tasks:
        db.session.delete(task)
    db.session.commit()
    return jsonify({'op': 'OK'})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    db.create_all()
    app.run()
