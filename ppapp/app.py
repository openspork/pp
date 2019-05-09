from flask import Flask
from peewee import MySQLDatabase

app = Flask(__name__)

db = MySQLDatabase('pp', user='pp', password='password', host='localhost', port=3306)