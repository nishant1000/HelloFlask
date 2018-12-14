import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1/bus_transport"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
