import xmltodict

from ppapp.models import *

def create_intermediate_node(parent, key):
    try:
        print('found intermediate -- parent: %s key: %s' % (parent, key))
        query = ParamLevel.select().where(ParamLevel.name == parent)

        if ( not query.exists() ):
            #print('%s is unique!' % parent)
            param_level = ParamLevel.create(name = parent)
        else:
            #print('%s is duplicate!' % parent)
            param_level = query.get()
        return param_level

    except Exception as e:
        print(e)

def create_leaf_node(parent, key, value):
    try:
        print('found leaf -- parent: %s key: %s value: %s' % (parent, key, value))
        param_level = create_intermediate_node(parent, key)
        BaseParam.create(param_level = param_level, name = key, default_value = value, note = None)
    except Exception as e:
        print(e)

def find_node(parent, d):
    try:
        for key, value in d.items():
                if ( isinstance(value,dict) ):
                    if (parent):
                        create_intermediate_node(parent, key)
                    find_node(key, value)
                else:   
                    create_leaf_node(parent, key, value)
    except Exception as e:
        print(e)

def build_params():
    print('building params')
    with open('./configs/site.cfg') as fd:
        content = fd.read()
        doc = xmltodict.parse(content)
        find_node(None, doc)