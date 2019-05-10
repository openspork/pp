from flask import Flask
from peewee import MySQLDatabase
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = MySQLDatabase('pp', user='pp', password='password', host='localhost', port=3306)