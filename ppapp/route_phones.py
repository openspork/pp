from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *
from ppapp.util.model_ops import *

@app.route('/new_phone', methods = ['GET', 'POST'])
def new_phone():
    form = NewPhoneForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('New - Phone: {}, MAC Address: {}, Note: {}'.format(
                    form.name.data, form.mac_address.data, form.note.data))
            Phone.create(name = form.name.data, mac_address = form.mac_address.data, note = form.note.data).save()
            return redirect('/')
        else:
            flash('Invalid Input!')
            return render_template('new_phone.j2', form = form)
    elif request.method == 'GET':
        return render_template('new_phone.j2', form = form)

@app.route('/edit_phone/<id>', methods = ['GET', 'POST'])
def edit_phone(id):
    form = EditPhoneForm()
    query = Phone.select().where(Phone.id == id)
    if not query.exists():
        flash('Invalid ID!')
        return redirect('/')
    else:
        phone = query.get()
    
    params = get_phone_params(phone)
    groups = get_phone_groups(phone)

    form.avail_params.choices = get_form_choices(params[0], AvailParam)
    form.active_params.choices = get_form_choices(params[1], AvailParam)
    form.avail_groups.choices = get_form_choices(groups[0], Group)
    form.active_groups.choices = get_form_choices(groups[1], Group)

    if request.method == 'POST':
        if form.validate_on_submit():

            # Get data
            new_param_ids = form.avail_params.data
            prev_param_ids = form.active_params.data
            new_group_ids = form.avail_groups.data
            prev_group_ids = form.active_groups.data

            if ( form.delete.data ):
                flash('Deleted - Phone: {}, MAC address: {}, Note: {}'.format(
                    form.name.data, form.mac_address.data, form.note.data))
                # Recursive to delete foreign keys
                phone.delete_instance(recursive = True)
            else:
                flash('Updated - Phone: {}, MAC address: {}, Note: {}'.format(
                    form.name.data, form.mac_address.data, form.note.data))

                # Handle base data
                phone.name = form.name.data
                phone.mac_address = form.mac_address.data
                phone.note = form.note.data
                phone.save()

                # Process phone's children
                add_params_to_phone(new_param_ids, phone)
                add_groups_to_phone(new_group_ids, phone)
                remove_params_from_phone(prev_param_ids, phone)
                remove_groups_from_phone(prev_group_ids, phone)
                
            return redirect('/')
        else:
            flash('Invalid Input!')
        return render_template('edit_phone.j2', form = form)

    elif request.method == 'GET':
        form.mac_address.data = phone.mac_address
        form.name.data = phone.name
        form.note.data = phone.note
        return render_template('edit_phone.j2', form = form)