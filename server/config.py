import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/app.db'
    SECRET_KEY = 'your_secret_key_here'
    JWT_SECRET_KEY = 'jwt_secret_key_here'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
