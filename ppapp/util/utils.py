import xmltodict

from ppapp.models import *

def init_db():
    print('db init')
    db.connect()
    db.create_tables([Phone, Client, Site, Extension, ParamLevel, Param], safe = True)
    # if ( len(ParamLevel.select()) == 0 ):
    #     print('populating paramlevels')
    #     build_params()
    build_params()
    db.close()

def create_intermediate_node(parent, key):
    try:
        print('found intermediate -- parent: %s key: %s' % (parent, key))
        query = ParamLevel.select().where(ParamLevel.name == parent)

        if ( not query.exists() ):
            print('%s is unique!' % parent)
            ParamLevel.create(name = parent)
        else:
            print('%s is duplicate!' % parent)

    except Exception as e:
        print(e)

def create_leaf_node(parent, key, value):
    try:
        print('found leaf -- parent: %s key: %s value: %s' % (parent, key, value))
        #param_level = ParamLevel.select().where(ParamLevel.name == parent).get()
        #Param.create(param_level = param_level, name = key, default_value = value, note = None)
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