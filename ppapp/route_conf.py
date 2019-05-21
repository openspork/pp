from io import BytesIO
from flask import abort, request, send_file
from ppapp import app
from ppapp.models import *
from ppapp.util.rsop import gen_rsop
from ppapp.util.gen_xml import gen_xml
from ppapp.util.misc import format_mac

@app.route("/poly/<mac_address>.cfg")
def get_conf(mac_address):
    formatted_mac_address = format_mac(mac_address)
    query = Phone.select().where(Phone.mac_address == formatted_mac_address)
    if not query.exists():
        app.logger.warn('Failed to find phone: %s' % formatted_mac_address)
        return abort(403)
    else:
        phone = query.get()
    try:
        rsop = gen_rsop(phone)
        xml = gen_xml(rsop)
        print()
    except Exception as e:
        app.logger.error('Failed to generate XML for phone  #%s: %s (%s): %s ' % (phone.id, phone.name, formatted_mac_address, e))
        return abort(500)

    byte_io = BytesIO()
    byte_io.write(xml.encode())
    byte_io.seek(0)

    return send_file(byte_io,
        attachment_filename="%s.cfg" % mac_address,
        as_attachment=True)
