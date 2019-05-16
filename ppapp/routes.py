import os
from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *
from ppapp.route_phones import *
from ppapp.route_params import *
from ppapp.route_groups import *
from ppapp.util.rsop import *

@app.route('/')
def index():
    phones = Phone.select()
    avail_params = AvailParam.select().order_by(AvailParam.base_param.name)
    # TODO: It would be nice to order by type, then name"
    groups = Group.select().order_by(Group.name)
    group_types = GroupType.select().order_by(GroupType.precedence)
    return render_template('index.j2', phones = phones, avail_params = avail_params, groups = groups, group_types = group_types)

@app.route('/config/<mac_address>')
def config(mac_address):
    query = Phone.select().where(Phone.mac_address == mac_address)
    if not query.exists():
        mac_address = 'not found!'
    else:
        phone = query.get()
        # TODO: Introduce try statement
        try:
            rsop = gen_rsop(phone)
        except Exception as e:
            flash(str(e))
            return redirect('/')
    return render_template('config.j2', mac_address = mac_address, rsop = rsop, Group = Group)

@app.route('/favicon.ico')
def favicon():
    dir = os.path.join(app.root_path, 'static')
    print(dir)
    return send_from_directory(dir ,'favicon.ico', mimetype = 'image/vnd.microsoft.icon')