import os
from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *
from ppapp.route_phones import *
from ppapp.route_params import *

@app.route('/')
def index():
    phones = Phone.select()
    avail_params = AvailParam.select().order_by(AvailParam.base_param.name)
    groups = Group.select().order_by(Group.type.name).order_by(Group.name)
    return render_template('index.j2', phones = phones, avail_params = avail_params, groups = groups)

@app.route('/config/<mac_address>')
def config(mac_address):
    query = Phone.select().where(Phone.mac_address == mac_address)
    if not query.exists():
        mac_address = 'not found!'
    return render_template('config.j2', mac_address = mac_address)

@app.route('/favicon.ico')
def favicon():
    dir = os.path.join(app.root_path, 'static')
    print(dir)
    return send_from_directory(dir ,'favicon.ico', mimetype = 'image/vnd.microsoft.icon')