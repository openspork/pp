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
from ppapp.util.rsop import *


@app.route("/new_ca", methods=["GET", "POST"])
def new_ca():
	form = NewCAForm()
	return render_template("new_ca.j2", form=form)