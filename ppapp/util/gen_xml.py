from peewee import *
from playhouse.shortcuts import *
from ppapp.models import *

def get_dict():
	pass

def gen_xml(rsop):
	params = []
	for param in rsop:
		print(param)
		#params.append((param[0], param[1]))
	print(rsop)
	print(params)
