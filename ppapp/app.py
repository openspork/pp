import logging
from flask import Flask
from peewee import MySQLDatabase
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

db = MySQLDatabase('pp', user='pp', password='password', host='localhost', port=3306)