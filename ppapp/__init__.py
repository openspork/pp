from ppapp.app import app
from ppapp.models import *
from ppapp.util.init import init_db

init_db()

from ppapp import routes
