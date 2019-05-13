from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *

@app.route('/new_group', methods=['GET', 'POST'])
def new_group():
    form = GroupForm()
    if request.method == 'POST':   
        if form.validate_on_submit():
            flash('New group: {}, MAC Address: {}'.format(
                form.name.data, form.mac_address.data))
            group.create(name = form.name.data, mac_address = form.mac_address.data).save()
            return redirect('/')
        else:
            flash('Invalid Input!')
            return render_template('new_group.j2', form = form)
    elif request.method == 'GET':
        return render_template('new_group.j2', form = form)