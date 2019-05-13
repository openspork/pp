from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *

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
    query = Phone.select().where(Phone.id == id)
    if not query.exists():
        flash('Invalid ID!')
        return redirect('/')
    else:
        phone = query.get()

    form = EditPhoneForm()
    
    # Populate our form's dynamic data
    active_params = (AvailParam
            .select()
            .join(AvailParamPhones)
            .where(AvailParamPhones.phone == phone)
            .order_by(AvailParam.base_param.name)
            )

    avail_params = (AvailParam
            .select()
            .join(AvailParamPhones, JOIN.LEFT_OUTER)
            .where(AvailParam.id.not_in(active_params))
            .order_by(AvailParam.base_param.name)
            )
    
    active_clients = (Client
            .select()
            .join(PhoneClients, JOIN.LEFT_OUTER)
            .where(PhoneClients.phone == phone)
            .order_by(Client.name)
            )

    avail_clients = (Client
            .select()
            .join(PhoneClients, JOIN.LEFT_OUTER)
            .where(Client.id.not_in(active_clients))
            .order_by(Client.name)
            )


    form.avail_params.choices = get_avail_param_form_choices(avail_params)
    form.active_params.choices = get_avail_param_form_choices(active_params)
    form.avail_clients.choices = get_form_choices(avail_clients)
    form.active_clients.choices = get_form_choices(active_clients)


    if request.method == 'POST':
        if form.validate_on_submit():
            if ( form.delete.data ):
                flash('Deleted phone: {}, MAC Address: {}'.format(
                    form.name.data, form.mac_address.data))
                phone.delete_instance()
            else:
                flash('Updated phone: {}, MAC Address: {}'.format(
                    form.name.data, form.mac_address.data))
                # Handle base data
                phone.name = form.name.data
                phone.mac_address = form.mac_address.data

                # Handle params
                new_param_ids = form.avail_params.data
                prev_param_ids = form.active_params.data

                # Add new params
                for new_param_id in new_param_ids:
                    avail_param = AvailParam.get(AvailParam.id == new_param_id)
                    AvailParamPhones.create(avail_param = avail_param, phone = phone)
                    avail_param.save()
                # Remove old params
                for prev_param_id in prev_param_ids:
                    avail_param = AvailParam.get(AvailParam.id == prev_param_id)
                    delete_query = (AvailParamPhones
                            .delete()
                            .where((AvailParamPhones.phone == phone) & (AvailParamPhones.avail_param == avail_param))
                            )
                    delete_query.execute()
            return redirect('/')
        else:
            flash('Invalid Input!')
        return render_template('edit_phone.j2', form = form)

    elif request.method == 'GET':
        form.mac_address.data = phone.mac_address
        form.name.data = phone.name
        return render_template('edit_phone.j2', form = form)