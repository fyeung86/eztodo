import requests
import logging

log = logging.getLogger(__name__)

class APIService(object):

    def __init__(self, url='localhost', port=5000):
        self.url = url
        self.port = port

    def all_tasks(self):
        endpoint = 'http://{}:{}/tasks'.format(self.url, self.port)
        response = requests.get(endpoint)
        json_response = response.json()
        if json_response:
            log.debug('Response body %s', json_response)
            return json_response['tasks']
        raise ValueError('no tasks found')

    def remove_task(self, task_id):
        if isinstance(task_id, int):
            endpoint = 'http://{}:{}/tasks/{}'.format(self.url, self.port, task_id)
            response = requests.delete(endpoint)
            return True
        raise ValueError('task_id must be an integer')

    def add_task(self, action):
        log.info('Adding task: %s', action)
        endpoint = 'http://{}:{}/tasks'.format(self.url, self.port)
        response = requests.post(endpoint, json={'action': action})
        log.info('Response from adding task: %s', response)
        if response.status_code in [200, 201]:
            json_body = response.json()
            return json_body 
        raise Exception('Server returned invalid status %s' % response.status_code)

    def update_task(self, task_id, action):
        if isinstance(task_id, int):
            endpoint = 'http://{}:{}/tasks/{}'.format(self.url, self.port, task_id)
            response = requests.put(endpoint, {
                'action': action
            })
            return True
        raise ValueError('task_id must be an integer')
