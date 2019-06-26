import os
from flask import abort, flash, send_file, render_template, request, redirect, url_for
from ppapp import app
from ppapp.forms import *
from ppapp.models import *
from ppapp.routes.route_phones import *
from ppapp.routes.route_params import *
from ppapp.routes.route_groups import *
from ppapp.routes.route_logs import *
from ppapp.routes.route_conf import *
from ppapp.routes.route_cas import *
from ppapp.rsop.param_rsop import gen_param_rsop
from ppapp.util.gen_xml import *
from ppapp.util.parse_xml import build_params
from ppapp.util.misc import AlphaDict
from ppapp.rsop.ca_rsop import *


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
        cert_authorities=cert_authorities,
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
        flash("Can't display RSoP - phone not found!")
        return redirect("/")
    else:
        phone = query.get()
        try:
            cert_authority_rsop = CertAuthorityRSoP(phone)
            param_rsop = gen_param_rsop(phone)
            # If we got RSOP back, gen xml
            if not param_rsop == {}:
                xml = gen_xml(param_rsop)
            else:
                xml = ""
        except Exception as e:
            flash(str(e))
            return redirect("/")
    return render_template(
        "rsop.j2",
        mac_address=mac_address,
        rsop=param_rsop,
        cert_authority_rsop=cert_authority_rsop,
        Group=Group,
        Phone=Phone,
        xml=xml,
    )


@app.route("/favicon.ico")
def favicon():
    file = os.path.join(app.root_path, "static", "favicon.ico")
    return send_file(file, mimetype="image/vnd.microsoft.icon")
