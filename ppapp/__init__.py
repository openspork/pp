#from re import sub
from ppapp.app import app
from ppapp.models import *
from ppapp.util.utils import init_db, build_params

init_db()

@app.before_request
def before_request():
    db.connect()

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

from ppapp import routes