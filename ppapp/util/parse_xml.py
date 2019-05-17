import xmltodict

from ppapp.models import *

def create_intermediate_node(parent, key):
    # try:
    print('found intermediate -- parent: %s key: %s' % (parent.name, key))
    query = ParamLevel.select().where(ParamLevel.name == parent)

    # Avoids dupes between multiple source files -- not XML generic
    # TODO: Need to handle dupes
    #if ( not query.exists() ):
        #print('%s is unique!' % parent)
    #    param_level = ParamLevel.create(name = parent)
    #else:
        #print('%s is duplicate!' % parent)
    #    param_level = query.get()

    new_param_level = ParamLevel.create( name = parent.name )
    ParamLevelParamLevels.create(parent = parent, child = new_param_level)


    return new_param_level

    # except Exception as e:
    #     print(e)

def create_leaf_node(parent, key, value):
    # try:
        print('found leaf -- parent: %s key: %s value: %s' % (parent.name, key, value))
        param_level = create_intermediate_node(parent, key)
        BaseParam.create(param_level = param_level, name = key, default_value = value, note = None)
    # except Exception as e:
    #     print(e)

def find_node(parent, d):
    # try:
        for key, value in d.items():
            # If value is a dict, it has sub-items
            if ( isinstance(value,dict) ):
                # If parent exists, we are not the root node
                if parent:
                    new_param_level = create_intermediate_node(parent, key) # I just added
                elif parent == None:
                    # We are the rot node
                    new_param_level = ParamLevel.create( name = None )
                    print('new param level created: %s' % new_param_level)

                #find_node(key, value) # Key is the next parent
                find_node(new_param_level, value)

            else:   
                # If value is not a dict, key[val] is a keypair itself
                create_leaf_node(parent, key, value)
    # except Exception as e:
    #     print(e)

def build_params():
    print('building params')
    with open('./configs/site.cfg') as fd:
        content = fd.read()
        doc = xmltodict.parse(content)
        find_node(None, doc)