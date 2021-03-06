import logging
from flask import Flask
from peewee import MySQLDatabase
from config import Config
from ppapp.util.group_ops import get_phone_groups, get_group_groups

app = Flask(__name__)
app.config.from_object(Config)
app.add_template_global(get_phone_groups)
app.add_template_global(get_group_groups)

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

db = MySQLDatabase("pp", user="pp", password="password", host="localhost", port=3306)

# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@app.before_request
def _db_connect():
    db.connect()


# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()


@app.after_request
def after_request(response):
    db.close()
    return response


# @app.template_filter('type')
# def type(value):
#     return type(value)

# @app.template_filter('datetimeformat')
# def datetimeformat(value, format='%Y-%m-%d'):
#     return value.strftime(format)

# @app.template_filter('google_search')
# def google_search(value):
# 	query = sub(r'\s+', '+', value)
# 	url = 'http://www.google.com/search?q=' + query
# 	return url
