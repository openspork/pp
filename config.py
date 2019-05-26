import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "SECRET_KEY"
    SERVER_NAME = "localhost:5000"
