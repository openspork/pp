from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *

@app.route('/new_param', methods=['GET', 'POST'])
def new_param():
    form = NewParamForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            base_param = BaseParam.get(BaseParam.id == form.param.data)
            flash('Parameter added: {}, Value: {}'.format(base_param.name, form.value.data))
            AvailParam.create(base_param = base_param, value = form.value.data, note = form.note.data)
        else:
            flash('Invalid Input!')
    return render_template('new_param.j2', form = form)

@app.route('/edit_param/<id>', methods=['GET', 'POST'])
def edit_param(id):
    query = AvailParam.select().where(AvailParam.id == id)
    if not query.exists():
        flash('Invalid ID!')
        return redirect('/')
    else:
        avail_param = query.get()

    form = EditParamForm()

    avail_params = (AvailParam
                    .select()
                    .order_by(AvailParam.base_param.name)
                    )

    if request.method == 'POST':
        if form.validate_on_submit():
            if ( form.delete.data ):
                flash('Deleted param: {}'.format(avail_param.base_param.name))
                avail_param.delete_instance()
            else:
                flash('Updated param: {}'.format(avail_param.base_param.name))
                # Handle base data
                avail_param.value = form.value.data
                avail_param.note = form.note.data
                avail_param.save()
            return redirect('/')
        else:
            flash('Invalid Input!')
        return render_template('edit_param.j2', form = form, avail_param = avail_param)
    elif request.method == 'GET':
        form.value.data = avail_param.value
        form.note.data = avail_param.note
        return render_template('edit_param.j2', form = form, avail_param = avail_param)