import requests

class APIService(object):

    def __init__(self):
        self.url = 'localhost'
        self.port = 8000 


    def all_tasks(self):
        endpoint = 'http://{}:{}/tasks'.format(self, url, self.port)
        response = requests.get(endpoint)
        return True 

    def remove_task(self, task_id):
        if isinstance(task_id, int): 
            endpoint = 'http://{}:{}/tasks/{}'.format(self, url, self.port, task_id)
            response = requests.delete(endpoint)
            return True 
        raise ValueError('task_id must be an integer')

    def add_task(self, action):
        endpoint = 'http://{}:{}/tasks'.format(self, url, self.port)
        response = requests.post(endpoint, {
            'action': action 
        })
        return True 

    def update_task(self, task_id, action):
        if isinstance(task_id, int): 
            endpoint = 'http://{}:{}/tasks/{}'.format(self, url, self.port, task_id)
            response = requests.put(endpoint, {
                'action': action 
            })
            return True 
        raise ValueError('task_id must be an integer')
