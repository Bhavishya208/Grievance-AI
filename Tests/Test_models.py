import unittest
from models import db, User, Complaint

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def test_user_creation(self):
        with self.app.app_context():
            user0
