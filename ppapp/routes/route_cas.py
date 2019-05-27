from flask import (
    flash,
    send_from_directory,
    render_template,
    request,
    redirect,
    url_for,
)
import base36
from ppapp import app
from ppapp.forms import *
from ppapp.models import *
from ppapp.util.param_ops import *
from ppapp.util.group_ops import *
from ppapp.util.view_ops import *
from ppapp.rsop.ca_rsop import *
from ppapp.crypto.revoke import build_crl
from ppapp.crypto.issue import create_cert


@app.route("/crl/<thumbprint>")
def get_cert_revocation_list(thumbprint):
    pass


@app.route("/new_ca", methods=["GET", "POST"])
def new_ca():
    form = NewCertAuthorityForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # Build a new CA:
            cert_pem, cert_key_pem, thumbprint = create_cert(
                form.cert.data, form.private_key.data, "https://fq.dn/crl/global"
            )  # CRL URI should probably be inputtable...
            # Build our empty CRL
            cert_revocation_list_pem = build_crl(form.cert.data, form.private_key.data)
            cert_authority = CertAuthority.create(
                name=form.name.data,
                cert=cert_pem,
                thumbprint=thumbprint,
                private_key=cert_key_pem,
                cert_revocation_list=cert_revocation_list_pem,
                note=form.note.data,
            ).save()
            flash("New CA - Name: {}".format(form.name.data))
            return redirect("/")
        else:
            flash_errors(form)
    return render_template("ca.j2", form=form)


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
                # Allow blanking input to regen CRL
                if form.cert_revocation_list.data == "":
                    cert_authority.cert_revocation_list = build_crl(
                        form.cert.data, form.private_key.data
                    )
                else:
                    cert_authority.cert_revocation_list = form.cert_revocation_list.data
                cert_authority.note = form.note.data
                cert_authority.save()
            return redirect("/")
        else:
            flash_errors(form)
    elif request.method == "GET":
        form.name.data = cert_authority.name
        form.private_key.data = cert_authority.private_key
        form.cert.data = cert_authority.cert
        form.cert_revocation_list.data = cert_authority.cert_revocation_list
        form.note.data = cert_authority.note
    return render_template("ca_edit.j2", form=form, cert_authority=cert_authority)
