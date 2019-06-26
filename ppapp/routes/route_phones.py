from flask import (
    flash,
    send_from_directory,
    render_template,
    request,
    redirect,
    url_for,
)
from ppapp import app
from ppapp.forms import *
from ppapp.models import *
from ppapp.util.param_ops import *
from ppapp.util.group_ops import *
from ppapp.util.view_ops import *
from ppapp.rsop.param_rsop import gen_param_rsop
from ppapp.crypto.issue import issue_client_cert, reissue_client_cert
from ppapp.crypto.revoke import revoke_client_cert


@app.route("/new_phone", methods=["GET", "POST"])
def new_phone():
    form = NewPhoneForm()

    params = AvailParam.select()
    groups = Group.select()

    form.avail_params.choices = get_form_choices(params, AvailParam)
    form.avail_parents.choices = get_form_choices(groups, Group)

    if request.method == "POST":
        if form.validate_on_submit():
            query = Phone.select().where(Phone.mac_address == form.mac_address.data)
            if query.exists():
                flash("Duplicate MAC Address!")
            else:
                flash(
                    "New - Phone: {}, MAC Address: {}:".format(
                        form.name.data, form.mac_address.data
                    )
                )
                phone = Phone.create(
                    name=form.name.data,
                    mac_address=form.mac_address.data,
                    note=form.note.data,
                )

                # Process phone's children
                add_params_to_phone(form.avail_params.data, phone)
                add_groups_to_phone(form.avail_parents.data, phone)

                # Validate RSoP
                try:
                    rsop = gen_param_rsop(phone)
                    # TODO: Validate CA RSoP
                except Exception as e:
                    flash(str(e))

                issue_client_cert(phone)
            return redirect("/")
        else:
            flash_errors(form)
            return render_template("new_phone.j2", form=form)
    elif request.method == "GET":
        return render_template("phone_new.j2", form=form)


@app.route("/edit_phone/<id>", methods=["GET", "POST"])
def edit_phone(id):
    form = EditPhoneForm()
    query = Phone.select().where(Phone.id == id)
    if not query.exists():
        flash("Invalid ID!")
        return redirect("/")
    else:
        phone = query.get()

    params = get_phone_params(phone)
    groups = get_phone_groups(phone)

    form.avail_params.choices = get_form_choices(params[0], AvailParam)
    form.active_params.choices = get_form_choices(params[1], AvailParam)
    form.avail_parents.choices = get_form_choices(groups[0], Group)
    form.active_parents.choices = get_form_choices(groups[1], Group)

    if request.method == "POST":
        if form.validate_on_submit():

            # Get data
            new_param_ids = form.avail_params.data
            prev_param_ids = form.active_params.data
            new_group_ids = form.avail_parents.data
            prev_group_ids = form.active_parents.data

            if form.reissue_cert.data:
                reissue_client_cert(phone)

            if form.delete.data:
                flash(
                    "Deleted - Phone: {}, MAC address: {}".format(
                        form.name.data, form.mac_address.data
                    )
                )
                # Find the current active client cert
                phone_active_client_cert = (
                    PhoneActiveClientCert.select()
                    .join(Phone)
                    .where(Phone.id == phone)
                    .get()
                )
                active_client_cert = phone_active_client_cert.active_client_cert
                # Revoke the current active client cert
                revoke_client_cert(phone)
                # Find auto-generated params
                avail_params_to_delete = (
                    AvailParam.select()
                    .join(PhoneAvailParams)
                    # .switch(AvailParam)
                    .join(Phone)
                    .where((Phone.id == phone) & (AvailParam.automatic == True))
                )
                # Recursive to delete foreign keys (due to constraint)
                for avail_param in avail_params_to_delete:
                    avail_param.delete_instance(recursive=True)
                phone.delete_instance(recursive=True)
            else:
                flash(
                    "Updated - Phone: {}, MAC address: {}".format(
                        form.name.data, form.mac_address.data
                    )
                )

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

                # Validate RSoP
                try:
                    rsop = gen_param_rsop(phone)
                except Exception as e:
                    flash(str(e))
            return redirect("/")
        else:
            flash_errors(form)
        return render_template("edit_phone.j2", form=form)

    elif request.method == "GET":
        form.mac_address.data = phone.mac_address
        form.name.data = phone.name
        form.note.data = phone.note
        return render_template("phone_edit.j2", form=form)
