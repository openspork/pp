from flask import send_from_directory, render_template, redirect, url_for

from ppapp import app

from ppapp.models import *

@app.route('/')
def index():
	return 'index'