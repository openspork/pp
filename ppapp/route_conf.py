from io import BytesIO
from ppapp import app

from flask import (
    abort,
    send_file,
)

@app.route("/poly/<mac>.cfg")
def get_conf(mac):
    formatted_mac = ':'.join(mac[i:i+2] for i in range(0,12,2))
    try:
        phone = Phone.get(Phone.mac_address == formatted_mac)
    except Exception as e:
        app.logger.warn('Failed to find phone: %s' % formatted_mac)
        return abort(403)

    try:
        rsop = gen_rsop(phone)
        xml = gen_xml(rsop)
        print()
    except Exception as e:
        app.logger.error('Failed to generate XML for phone  #%s: %s (%s) ' % (phone.id, phone.name, formatted_mac))
        return abort(500)

    byte_io = BytesIO()
    byte_io.write(xml.encode())
    byte_io.seek(0)

    return send_file(byte_io,
        attachment_filename="%s.cfg" % mac,
        as_attachment=True)
