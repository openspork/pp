from os import listdir
import xmltodict
from ppapp.models import *

def find_node(parent, d):
    for key, value in d.items():

        # Hackily avoid dupes
        query = ParamLevel.select().where(ParamLevel.name == key)
        if not query.exists():

            #print('Evaluating %s : %s' % (key, str(value)[:32]))

            if ( isinstance(value, dict) ):
                #print('Value is a dictionary!')
                
                new_param_level = ParamLevel.create( name = key )
                if parent == None: # This is the root node
                    print('Root node: %s' % key)

                elif parent != None:
                    #print('Creating parent / child mapping! %s -> %s' % (parent.name, new_param_level.name))
                    ParamLevelParamLevels.create(parent = parent, child = new_param_level)

                find_node(new_param_level, value)
            else:
                # If value is not a dict, key[val] is a keypair itself
                #print('Value is not a dictionary!  Create a leaf: %s = %s ' % (key, value))
                BaseParam.create(param_level = parent, name = key, default_value = value, note = None)

def build_params():
    print('building params')

    for file in listdir('./configs/'):
        if file.endswith('.cfg'):
            with open('./configs/site.cfg') as fd:
                content = fd.read()
                doc = xmltodict.parse(content)
            #try:
                find_node(None, doc)
            #except Exception as e:
                #print(e)