import os
from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID
from flask_sqlalchemy import SQLAlchemy
from settings import BASE_DIR


app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(BASE_DIR, 'tmp'))

from app import views
from app import models
