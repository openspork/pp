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
from ppapp.rsop.ca_rsop import *


@app.route("/new_ca", methods=["GET", "POST"])
def new_ca():
    form = NewCertAuthorityForm()
    if request.method == "POST":
        if form.validate_on_submit():
            cert_authority = CertAuthority.create(
                name=form.name.data,
                cert=form.cert.data,
                private_key=form.private_key.data,
                note=form.note.data,
            ).save()
            flash("New CA - Name: {}".format(form.name.data))
            return redirect("/")
        else:
            flash_errors(form)
    return render_template("new_ca.j2", form=form)


@app.route("/edit_ca/<id>", methods=["GET", "POST"])
def edit_ca(id):
    query = CertAuthority.select().where(CertAuthority.id == id)
    if not query.exists():
        flash("Invalid ID!")
        return redirect("/")
    else:
        cert_authority = query.get()

    form = EditCertAuthorityForm()

    if request.method == "POST":
        if form.validate_on_submit():
            if form.delete.data:
                flash("Deleted - CA: {}".format(cert_authority.name))
                cert_authority.delete_instance(recursive=True)
            else:
                flash("Updated - CA: {}".format(cert_authority.name))
                # Handle base data
                cert_authority.name = form.name.data
                cert_authority.private_key = form.private_key.data
                cert_authority.cert = form.cert.data
                cert_authority.note = form.note.data
                cert_authority.save()
            return redirect("/")
        else:
            flash_errors(form)
    elif request.method == "GET":
        form.name.data = cert_authority.name
        form.private_key.data = cert_authority.private_key
        form.cert.data = cert_authority.cert
        form.note.data = cert_authority.note
    return render_template("edit_ca.j2", form=form, cert_authority=cert_authority)
