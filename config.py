import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "postgresql://local-db:local-db@localhost:5432/local-db"
S3_ENDPOINT = "http://localhost:4566"