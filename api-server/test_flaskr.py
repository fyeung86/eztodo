import os
import json
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        # with flaskr.app.app_context():
        #     flaskr.init_db()

    def test_delete(self):
        rv = self.app.delete('/tasks')
        json_response = json.loads(rv.data)
        print json_response
        assert json_response["op"]

    def test_empty_db(self):
        rv = self.app.get('/tasks')
        json_response = json.loads(rv.data)
        assert not json_response["tasks"]

    def test_insert(self):
        rv = self.app.post(
            '/tasks',
            data=json.dumps({"action": "Go to Grocery Store"}),
            headers={'content-type':'application/json'}
        )
        print(rv)
        print(rv.data)
        json_response = json.loads(rv.data)
        assert json_response["task"]
        assert json_response["op"]

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
