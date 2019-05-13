from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *

@app.route('/new_group', methods = ['GET', 'POST'])
def new_group():
    form = GroupForm()
    if request.method == 'POST':   
        if form.validate_on_submit():
            grouptype = GroupType.get(GroupType.id == form.type.data)
            group = Group.create(name = form.name.data, type = grouptype, note = form.note.data).save()
            flash('New Group - Name: {}, Type: {}'.format(form.name.data, grouptype.name))
            return redirect('/')
        else:
            flash('Invalid Input!')
            return render_template('new_group.j2', form = form)
    elif request.method == 'GET':
        return render_template('new_group.j2', form = form)

@app.route('/edit_group/<id>', methods = ['GET', 'POST'])
def edit_group(id):
    pass