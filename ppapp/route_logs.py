from flask import request
from ppapp import app

@app.route('/poly/<mac>-<type>.log', methods=["GET", "HEAD", "PUT", "POST"])
def put_log(mac, type):
	print(request.data)
	return '', 204

@app.route('/post')
def post(methods = ['PUT']):
	return ''