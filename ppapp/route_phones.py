from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *

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
    query = Phone.select().where(Phone.id == id)
    if not query.exists():
        flash('Invalid ID!')
        return redirect('/')
    else:
        phone = query.get()

    form = EditPhoneForm()
    
    # Populate our forms' dynamic data
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
    
    active_groups = (Group
            .select()
            .join(PhoneGroups, JOIN.LEFT_OUTER)
            .where(PhoneGroups.phone == phone)
            .order_by(Group.name)
            )

    avail_groups = (Group
            .select()
            .join(PhoneGroups, JOIN.LEFT_OUTER)
            .where(Group.id.not_in(active_groups))
            .order_by(Group.name)
            )

    form.avail_params.choices = get_form_choices(avail_params, AvailParam)
    form.active_params.choices = get_form_choices(active_params, AvailParam)
    form.avail_groups.choices = get_form_choices(avail_groups, Group)
    form.active_groups.choices = get_form_choices(active_groups, Group)

    if request.method == 'POST':
        if form.validate_on_submit():
            if ( form.delete.data ):
                flash('Deleted - Phone: {}, MAC address: {}, Note: {}'.format(
                    form.name.data, form.mac_address.data, form.note.data))
                phone.delete_instance()
            else:
                flash('Updated - Phone: {}, MAC address: {}, Note: {}'.format(
                    form.name.data, form.mac_address.data, form.note.data))
                # Handle base data
                phone.name = form.name.data
                phone.mac_address = form.mac_address.data
                phone.note = form.note.data
                phone.save()

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

                # Handle groups
                new_group_ids = form.avail_groups.data
                prev_group_ids = form.active_groups.data

                # Add new groups
                for new_group_id in new_group_ids:
                    group = Group.get(Group.id == new_group_id)
                    PhoneGroups.create(group = group, phone = phone)
                    group.save()
                # Remove old params
                for prev_group_id in prev_group_ids:
                    group = Group.get(Group.id == prev_group_id)
                    delete_query = (PhoneGroups
                            .delete()
                            .where((PhoneGroups.phone == phone) & (PhoneGroups.group == group))
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