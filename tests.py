import os
import unittest
from app import app
from app import db
from app.models import User
from settings import BASE_DIR


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True 
        app.config['WTF_CSRF_ENABLED'] = False 
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
            BASE_DIR, 'test.sqlite3')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_avatar(self):
        user = User(nickname='john', email='john@example.com')
        avatar = user.avatar(120)
        expected = 'http://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
        assert avatar[0:len(expected)] == expected

    def test_make_unique_nickname(self):
        user = User(nickname='john', email='john@example.com')
        db.session.add(user)
        db.session.commit()
        nickname = User.make_unique_nickname('john')
        assert nickname != 'john'
        user = User(nickname=nickname, email='susan@example.com')
        db.session.add(user)
        db.session.commit()
        nickname2 = User.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname


if __name__ == '__main__':
    unittest.main()
    