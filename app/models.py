from app import db
from hashlib import md5


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    nickname = db.Column('nickname', db.String(64), index=True, unique=True)
    email = db.Column('email', db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column('about_me', db.String(140))
    last_seen = db.Column(db.DateTime)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname

        version = 2

        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break

            version += 1
        
        return new_nickname

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/{}?d=mm&s={}'.format(
            md5(self.email.encode('utf-8')).hexdigest(), size)

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)


class Post(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    body = db.Column('body', db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
