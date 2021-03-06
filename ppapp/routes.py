import os
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
from ppapp.route_phones import *
from ppapp.route_params import *
from ppapp.route_groups import *
from ppapp.util.rsop import *
from ppapp.util.gen_xml import *
from ppapp.util.init import init_db


@app.route("/")
def index():
    phones = Phone.select()
    avail_params = AvailParam.select().order_by(AvailParam.base_param.name)
    # TODO: It would be nice to order by type, then name"
    groups = Group.select().order_by(Group.name)
    group_types = GroupType.select().order_by(GroupType.precedence)
    return render_template(
        "index.j2",
        phones=phones,
        avail_params=avail_params,
        groups=groups,
        group_types=group_types,
    )


@app.route("/init")
def init():
    init_db()
    flash("DB Init Performed")
    return redirect("/")


@app.route("/rsop/<mac_address>")
def rsop(mac_address):
    query = Phone.select().where(Phone.mac_address == mac_address)
    if not query.exists():
        mac_address = "not found!"
    else:
        phone = query.get()
        try:
            rsop = gen_rsop(phone)
            xmls = gen_xml(rsop)
        except Exception as e:
            flash(str(e))
            return redirect("/")
    return render_template(
        "config.j2",
        mac_address=mac_address,
        rsop=rsop,
        BaseParam=BaseParam,
        Group=Group,
        Phone=Phone,
        xmls=xmls,
    )


@app.route("/favicon.ico")
def favicon():
    dir = os.path.join(app.root_path, "static")
    return send_from_directory(dir, "favicon.ico", mimetype="image/vnd.microsoft.icon")
