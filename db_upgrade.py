from migrate.versioning import api
from settings import SQLALCHEMY_DATABASE_URI
from settings import SQLALCHEMY_MIGRATE_REPO


api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('Current database version: ' + str(version))