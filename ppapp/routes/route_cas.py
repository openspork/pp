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
from ppapp.rsop.rsop import *


@app.route("/new_ca", methods=["GET", "POST"])
def new_ca():
    form = NewCAForm()

    if request.method == "POST":
        if form.validate_on_submit():
            cert_authority = CertAuthority.create(
                name=form.name.data,
                public_key=form.public_key.data,
                private_key=form.private_key.data,
                note=form.note.data,
            ).save()
            flash("New CA - Name: {}".format(form.name.data))
            return redirect("/")
        else:
            flash_errors(form)
    return render_template("new_ca.j2", form=form)