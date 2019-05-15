from flask import flash, send_from_directory, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *
from ppapp.util.param_ops import *
from ppapp.util.group_ops import *

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
    form = EditGroupForm()
    query = Group.select().where(Group.id == id)
    if not query.exists():
        flash('Invalid ID!')
        return redirect('/')
    else:
        group = query.get()

    params = get_group_params(group)
    children = get_group_groups(group, 'children')
    parents = get_group_groups(group, 'parents')

    form.avail_params.choices = get_form_choices(params[0], AvailParam)
    form.active_params.choices = get_form_choices(params[1], AvailParam)

    form.avail_parents.choices = get_form_choices(parents[0], Group)
    form.active_parents.choices = get_form_choices(parents[1], Group)

    form.avail_children.choices = get_form_choices(children[0], Group)
    form.active_children.choices = get_form_choices(children[1], Group)

    if request.method == 'POST':
        if form.validate_on_submit():

            # Get data
            # Get Params
            new_param_ids = form.avail_params.data
            prev_param_ids = form.active_params.data

            # Get parents
            new_parent_ids = form.avail_parents.data
            prev_parent_ids = form.active_parents.data

            # Get children
            new_child_ids = form.avail_children.data
            prev_child_ids = form.active_children.data


            if ( form.delete.data ):
                flash('Deleted - Group: {}, Type: {}, Note: {}'.format(
                    form.name.data, GroupType.get(GroupType.id == form.type.data).name, form.note.data))
                # Recursive to delete foreign keys
                group.delete_instance(recursive = True)
            else:
                flash('Updated - Group: {}, Type: {}, Note: {}'.format(
                    form.name.data, GroupType.get(GroupType.id == form.type.data).name, form.note.data))

                # Handle base data
                group.name = form.name.data
                group.type = GroupType.get(GroupType.id == form.type.data)
                group.note = form.note.data
                group.save()

                # Process group's children
                add_params_to_group(new_param_ids, group)
                remove_params_from_group(prev_param_ids, group)

                add_groups_to_group(new_child_ids, group, 'children')
                add_groups_to_group(new_parent_ids, group, 'parents')

                remove_groups_from_group(prev_child_ids, group, 'children')
                remove_groups_from_group(prev_parent_ids, group, 'parents')

            return redirect('/')
        else:
            flash('Invalid Input!')
        return render_template('edit_group.j2', form = form)

    elif request.method == 'GET':
        form.name.data = group.name
        form.type.data = group.type.id
        form.note.data = group.note
        return render_template('edit_group.j2', form = form)