from ppapp.models import Phone, Group

class EffectiveParam():

	param = None
	owner = None
	depth = None
	overrides = []

class ParamRSoP():
	effective_params = [] # Keep an array of EffectiveParams

# Define an RSoP object that will be extensible for additional future RSoPs
class RSoP_:
	i =123
	def __init__(self, phone):
		print(phone.name)
	pass




