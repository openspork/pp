import os
from io import BytesIO
from flask import (
    abort,
    flash,
    send_file,
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
from ppapp.route_conf import *
from ppapp.util.rsop import *
from ppapp.util.gen_xml import *
from ppapp.util.parse_xml import build_params

@app.route("/")
def index():
    phones = Phone.select()
    avail_params = AvailParam.select().join(BaseParam).order_by(BaseParam.name)
    # TODO: It would be nice to order by type, then name"
    groups = Group.select().order_by(Group.name)
    group_types = GroupType.select().order_by(GroupType.precedence)
    cert_authorities = CertAuthority.select().order_by(CertAuthority.name)
    return render_template(
        "index.j2",
        phones=phones,
        avail_params=avail_params,
        groups=groups,
        group_types=group_types,
        cert_authorities = cert_authorities
    )


@app.route("/init")
def init():
    build_params()
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
            xml = gen_xml(rsop)
        except Exception as e:
            flash(str(e))
            return redirect("/")
    return render_template(
        "rsop.j2",
        mac_address=mac_address,
        rsop=rsop,
        BaseParam=BaseParam,
        Group=Group,
        Phone=Phone,
        xml=xml,
    )


@app.route("/favicon.ico")
def favicon():
    dir = os.path.join(app.root_path, "static")
    return send_from_directory(dir, "favicon.ico", mimetype="image/vnd.microsoft.icon")
