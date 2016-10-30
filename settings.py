import os
from decouple import config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Port
PORT = config('PORT', default=8000, cast=int)

# Forms configuration
WTF_CSRF_ENABLED = config('WTF_CSRF_ENABLED', default=False, cast=bool)

# Database
DEFAULT_DBURL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default=DEFAULT_DBURL)
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'migrations')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Open ID configuration
OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
