from datetime import datetime
from flask import abort, request
from ppapp import app
from ppapp.models import *
from ppapp.util.misc import format_mac


@app.route('/poly/<mac_address>-<type>.<ext>', methods=['GET', 'HEAD', 'PUT'])
def put_log(mac_address, type, ext):
    formatted_mac_address = format_mac(mac_address)
    if request.method =='PUT':
        query = Phone.select().where(Phone.mac_address == formatted_mac_address)
        if query.exists():
            phone = Phone.get(Phone.mac_address == formatted_mac_address)
            if type == 'boot':
                BootLog.create(phone = phone, date_time = datetime.now(), data=request.data)
            elif type == 'app':
                AppLog.create(phone = phone, date_time = datetime.now(), data=request.data)
            elif type == 'calls':
                CallLog.create(phone = phone, date_time = datetime.now(), data=request.data)
        else:
            app.logger.warn('Failed to find phone: %s' % formatted_mac_address)
            return abort(403)
    return '', 204
