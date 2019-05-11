import os
from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp.forms import *

from ppapp import app

from ppapp.models import *

@app.route('/')
def index():
    phones = Phone.select()
    return render_template('index.j2', phones = phones)





@app.route('/params', methods=['GET', 'POST'])
def params():
    form = ParamForm()
    #form.param_level.choices = form_choices
    if request.method == 'POST':
        if form.validate_on_submit():

            base_param = BaseParam.get(BaseParam.id == form.param.data)

            flash('Parameter added: {}, Value: {}'.format(base_param.name, form.value.data))

            ActiveParam.create(base_param = base_param, value = form.value.data, note = form.note.data)

        else:
            flash('Invalid Input!')
    return render_template('params.j2', form = form)

@app.route('/new_phone', methods=['GET', 'POST'])
def new_phone():
    form = PhoneForm()
    if request.method == 'POST':   
        if form.validate_on_submit():
            flash('New phone: {}, MAC Address: {}'.format(
                form.name.data, form.mac_address.data))
            Phone.create(name = form.name.data, mac_address = form.mac_address.data).save()
            return redirect('/')
        else:
            flash('Invalid Input!')
            return render_template('new_phone.j2', form = form)
    elif request.method == 'GET':
        return render_template('new_phone.j2', form = form)

@app.route('/edit_phone/<id>', methods=['GET', 'POST'])
def edit_phone(id):
    form = EditPhoneForm()
    query = Phone.select().where(Phone.id == id)
    if not query.exists():
        flash('Invalid ID!')
        return redirect('/')
    else:
        phone = query.get()
    if request.method == 'GET':



        form.mac_address.data = phone.mac_address
        form.name.data = phone.name
        active_params = ActiveParam.select().where(ActiveParam.phone_params == phone )

        return render_template('edit_phone.j2', form = form, active_params = active_params)

    elif request.method == 'POST':
        if form.validate_on_submit():
            if ( form.delete.data ):
                flash('Deleted phone: {}, MAC Address: {}'.format(
                    form.name.data, form.mac_address.data))
                phone.delete_instance()
            else:
                flash('Updated phone: {}, MAC Address: {}'.format(
                    form.name.data, form.mac_address.data))
                phone.name = form.name.data
                phone.mac_address = form.mac_address.data

            phone.save()
            return redirect('/')
        else:
            flash('Invalid Input!')
        return render_template('edit_phone.j2', form = form)

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