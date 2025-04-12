import unittest

from user_service.app import create_app, db


# from ./app
# from ./app.models import db

class UserServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        response = self.client.post('/users/register', json={'username': 'testuser', 'email': 'testuser@example.com', 'password': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json)
        self.assertIn('username', response.json)
        self.assertIn('email', response.json)
        self.assertIn('password', response.json)
