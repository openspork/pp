from os import listdir, path
import xmltodict
from ppapp.models import *


def find_node(parent, d):
    for key, value in d.items():

        # print('Evaluating %s : %s' % (key, str(value)[:32]))

        if isinstance(value, dict):
            # Check if our ParamLevel already exists
            query = ParamLevel.select().where(ParamLevel.name == key)
            if not query.exists():
                # print('Value is a dictionary!')
                new_param_level = ParamLevel.create(name=key)
                if parent == None:  # This is the root node
                    # print("Root node: %s" % key)
                    pass
                elif parent != None:
                    # print('Creating parent / child mapping! %s -> %s' % (parent.name, new_param_level.name))
                    ParamLevelParamLevels.create(parent=parent, child=new_param_level)
            else:
                # Define so as to continue recursion
                new_param_level = query.get()

            find_node(new_param_level, value)
        elif isinstance(value, list):
            # TODO would be nice to eventually build support for lists
            raise Exception("%s is defined as a list!  Parser failure!")

        else:
            # Check if our BaseParam already exists
            query = BaseParam.select().where(BaseParam.name == key)
            if not query.exists():
                # If value is not a dict, key[val] is a keypair itself
                # print('Value is not a dictionary: it is a: %s  Create a leaf: %s = %s ' % (type(value), key, value))
                BaseParam.create(
                    param_level=parent, name=key, default_value=value, note=None
                )


def import_file(file):
    print("importing %s" % file)
    with open("./configs/%s" % file) as fd:
        content = fd.read()
        doc = xmltodict.parse(content)
        try:
            find_node(None, doc)
        except Exception as e:
            print(e)


def build_params():
    print("building params")
    # import_file('client.cfg')
    for file in listdir("./configs/"):
        if file.endswith(".cfg"):
            import_file(file)
