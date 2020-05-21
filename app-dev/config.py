import os
from datetime import timedelta
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # Creation of secret key for WTForms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-agile-key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'db/unicode.db')

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # PERMANENT_SESSION_LIFETIME = timedelta(minutes=120)

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'Tests/test.db')

    