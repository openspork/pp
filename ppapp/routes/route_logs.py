from io import BytesIO
from datetime import datetime
from flask import abort, render_template, request, send_file
from ppapp import app
from ppapp.models import *
from ppapp.util.misc import format_mac


@app.route("/logs/<id>")
def list_logs(id):
    query = Phone.select().where(Phone.id == id)
    if not query.exists():
        flash("Invalid ID!")
        return redirect("/")
    else:
        phone = query.get()
        boot_logs = (
            BootLog.select()
            .where(BootLog.phone == phone)
            .order_by(BootLog.date_time.desc())
        )
        app_logs = (
            AppLog.select()
            .where(AppLog.phone == phone)
            .order_by(AppLog.date_time.desc())
        )
        call_logs = (
            CallLog.select()
            .where(CallLog.phone == phone)
            .order_by(CallLog.date_time.desc())
        )
        return render_template(
            "logs.j2",
            phone=phone,
            boot_logs=boot_logs,
            app_logs=app_logs,
            call_logs=call_logs,
        )


@app.route("/log/<type>/<id>")
def get_log(type, id):
    if type == "boot":
        log_type = BootLog
    elif type == "app":
        log_type = AppLog
    elif type == "call":
        log_type = CallLog
    else:
        flash("Invalid Log Type!")
        return redirect("/")
    log = log_type.get(log_type.id == id)

    byte_io = BytesIO()
    byte_io.write(log.data.encode())
    byte_io.seek(0)

    return send_file(
        byte_io,
        attachment_filename="phone_%s_%s_%s.log" % (log.phone.id, type, id),
        as_attachment=True,
    )


@app.route("/poly/<dir>/<mac_address>-<type>.<ext>", methods=["GET", "HEAD", "PUT"])
def put_log(dir, mac_address, type, ext):
    formatted_mac_address = format_mac(mac_address)
    if request.method == "PUT":
        query = Phone.select().where(Phone.mac_address == formatted_mac_address)
        if query.exists():
            phone = Phone.get(Phone.mac_address == formatted_mac_address)
            if dir == "logs":
                if type == "boot":
                    BootLog.create(
                        phone=phone, date_time=datetime.now(), data=request.data
                    )
                elif type == "app":
                    AppLog.create(
                        phone=phone, date_time=datetime.now(), data=request.data
                    )
                # elif type == "calls":
                #     CallLog.create(
                #         phone=phone, date_time=datetime.now(), data=request.data
                #     )
            elif dir == "calls":
                if type == "calls":
                    CallLog.create(
                        phone=phone, date_time=datetime.now(), data=request.data
                    )
        else:
            app.logger.warn("Failed to find phone: %s" % formatted_mac_address)
            return abort(403)
    return "", 204
