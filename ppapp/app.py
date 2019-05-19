from flask import Flask
from peewee import MySQLDatabase
from config import Config
from ppapp.util.group_ops import get_phone_groups, get_group_groups

app = Flask(__name__)
app.config.from_object(Config)
app.add_template_global(get_phone_groups)
app.add_template_global(get_group_groups)

db = MySQLDatabase('pp', user='pp', password='password', host='localhost', port=3306)