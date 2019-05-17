from peewee import *
from playhouse.shortcuts import *
from ppapp.models import *

def get_dict():
	pass

def gen_xml(rsop):
	# Build an array of (ParamLevel, BaseParam, avail_param_value) tuples
	params = []
	#print(rsop)
	for base_param_id, param_value in rsop.items():
		base_param = BaseParam.get(BaseParam.id == base_param_id)
		param_level = BaseParam.param_level
		avail_param_value = param_value[0]
		tup = (param_level, base_param, avail_param_value)
		params.append(tup)

	# Create a dict of arrays with each ParamLevel as key
	param_levels = {}
	for param in params:
		param_level = param[0]
		base_param = param[1]
		avail_param_value = param[2]
		print('\nProcessing param_level: %s base_param: %s avail_value: %s' % (param_level.name, base_param.name, avail_param_value))
		
		param_levels[param_level] = [] # Initiate empty array
		print('Array created for param level: %s' % param_level.name )
		# Populate the arrays
		for param2 in params:
			# if param level is the key, append it to the array
			param_level2 = param2[0]
			if param_level == param_level2:
				base_param = param2[1]
				param_value = param2[2]
				param_levels[param_level].append(param_value)

	print(param_levels.keys())