from io import BytesIO
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from flask import flash, send_file, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *
from ppapp.util.misc import format_thumbprint
from ppapp.util.param_ops import *
from ppapp.util.group_ops import *
from ppapp.util.view_ops import *
from ppapp.rsop.ca_rsop import *
from ppapp.crypto.revoke import build_crl
from ppapp.crypto.issue import create_cert


@app.route("/view_ca/<id>")
def view_ca(id):
    query = CertAuthority.select().where(CertAuthority.id == id)
    if not query.exists():
        flash("Invalid ID!")
        return redirect("/")
    else:
        cert_authority = query.get()

    # Gather information:
    # Get CA
    cert_authority_load = x509.load_pem_x509_certificate(
        cert_authority.cert.encode("ascii"), default_backend()
    )
    # TODO: Fully package CA info and display via GUI
    # Create a tuple of CA information
    # 0 = friendly (pp) name
    # 1 = thumbprint
    # 2 = serial number
    # Add here
    cert_authority_info = (
        cert_authority.name,
        format_thumbprint(cert_authority.thumbprint),
        cert_authority_load.serial_number,
    )

    # Get CRL
    cert_revocation_list = x509.load_pem_x509_crl(
        cert_authority.cert_revocation_list.encode("ascii"), default_backend()
    )

    # Get client certs
    client_certs = ClientCert.select().where(
        ClientCert.cert_authority == cert_authority
    )

    # Create a tuple of client cert information
    # 0 = thumbprint
    # 1 = serial number
    # 2 = active (False or Phone)
    # 3 = revoked date (False or datetime)

    client_cert_info = []
    for client_cert in client_certs:
        # Determine if this cert is in our active certs table
        query = PhoneActiveClientCert.select().where(
            PhoneActiveClientCert.active_client_cert == client_cert.id
        )
        if not query.exists():
            active = False
        else:
            active = query.get().phone

        loaded_cert = x509.load_pem_x509_certificate(
            client_cert.cert.encode("ascii"), default_backend()
        )
        thumbprint = format_thumbprint(loaded_cert.fingerprint(hashes.SHA1()).hex())
        serial_number = loaded_cert.serial_number
        revoked_cert = cert_revocation_list.get_revoked_certificate_by_serial_number(
            serial_number
        )
        if not revoked_cert:
            revoked = False
        else:
            revoked = revoked_cert.revocation_date
        client_cert_info.append((thumbprint, serial_number, active, revoked))

    return render_template(
        "ca_view.j2",
        cert_authority=cert_authority,
        cert_authority_info=cert_authority_info,
        cert_revocation_list=cert_revocation_list,
        client_certs_info=client_cert_info,
    )

@app.route("/ca/<id>")
def get_ca(id):
    cert_authority = CertAuthority.get(CertAuthority.id == id)
    byte_io = BytesIO()
    byte_io.write(cert_authority.cert.encode())
    byte_io.seek(0)

    return send_file(
        byte_io, attachment_filename="%s_%s.pem" % (cert_authority.name, cert_authority.id), as_attachment=True
    )

@app.route("/crl/<thumbprint>")
def get_crl(thumbprint):
    cert_authority = CertAuthority.get(CertAuthority.thumbprint == thumbprint)
    byte_io = BytesIO()
    byte_io.write(cert_authority.cert_revocation_list.encode())
    byte_io.seek(0)

    return send_file(
        byte_io, attachment_filename="%s.pem" % thumbprint, as_attachment=True
    )


@app.route("/new_ca", methods=["GET", "POST"])
def new_ca():
    form = NewCertAuthorityForm()
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                x509.load_pem_x509_certificate(
                    form.cert.data.encode("ascii"), default_backend()
                )
                serialization.load_pem_private_key(
                    form.private_key.data.encode("ascii"),
                    password=None,
                    backend=default_backend(),
                )
            except ValueError as e:
                flash(e)
                return render_template("ca_new.j2", form=form)

            # Build a new CA:
            cert_revocation_list_uri = form.cert_revocation_list_uri.data
            if cert_revocation_list_uri == "":
                cert_revocation_list_uri = None

            cert_pem, cert_key_pem, thumbprint = create_cert(
                cert_authority_pem=form.cert.data,
                private_key_pem=form.private_key.data,
                common_name=form.name.data,
                is_ca=True,
                cert_revocation_list_uri=cert_revocation_list_uri,
                country_name=form.country_name.data,
                state_or_province_name=form.state_or_province_name.data,
                locality_name=form.locality_name.data,
                organization_name=form.organization_name.data,
            )
            # Build our empty CRL
            cert_revocation_list_pem = build_crl(form.cert.data, form.private_key.data)
            # Save our CA in DB
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
    return render_template("ca_new.j2", form=form)


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
                # Only alow delete if unused (no groups)
                groups = Group.select().where(Group.cert_authority == cert_authority)

                if groups.exists():
                    group_string = ""
                    for group in groups:
                        group_string += '"%s", ' % group.name
                    group_string = group_string[:-2]
                    flash(
                        'Cannot delete CA "%s" due to active groups: %s.  Please remove the CA from all groups before trying again.'
                        % (cert_authority.name, group_string)
                    )
                    return redirect("/")

                cert_authority.delete_instance(recursive=True)
                flash("Deleted - CA: {}".format(cert_authority.name))

            else:
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
                flash("Updated - CA: {}".format(cert_authority.name))
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
