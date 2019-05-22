from peewee import *
from ppapp.models import *
import xmltodict
from collections import OrderedDict
from ppapp.util.misc import AlphaDict

def get_branch_dict_by_name(params):
    # Create a dict of dicts with each ParamLevel name as key
    param_levels = {}
    for param in params:
        param_level = param[0].name
        base_param = param[1].name
        avail_param_value = param[2]
        # print('\nProcessing param_level: "%s" base_param: "%s" avail_value: "%s"' % (param_level, base_param, avail_param_value))

        param_levels[param_level] = {}  # Initiate empty dict
        # print('Array created for param level: "%s"' % param_level.name )
        # Populate the arrays
        for param2 in params:
            # if param level is the key, append it to the array
            param_level2 = param2[0].name
            if param_level == param_level2:
                base_param = param2[1].name
                param_value = param2[2]
                param_levels[param_level][
                    base_param
                ] = param_value  # Add our value with base as key
    return param_levels


# "current" - is a ParamLevel
def build_parent_tree(current):
    #print('Current: %s' % current.name)
    temp_dict = { current.name: {} }
    query = (
        # If we are looking for parents, we are matching on child
        ParamLevel.select()
        .join(
            ParamLevelParamLevels,
            JOIN.LEFT_OUTER,
            on=(ParamLevelParamLevels.parent == ParamLevel.id),
        ).where(ParamLevelParamLevels.child == current)
    )
    while query.exists():
        # While we have a parent
        result = query.get()
        #print('Parent: %s' % result.name)
        temp_dict = {result.name: temp_dict}

        query = (
            ParamLevel.select()
            # If we are looking for parents, we are matching on child
            .join(
                ParamLevelParamLevels,
                JOIN.LEFT_OUTER,
                on=(ParamLevelParamLevels.parent == ParamLevel.id),
            ).where(ParamLevelParamLevels.child == result)
        )
    return temp_dict


def assemble_full_tree(parent_tree, raw_param_branch):
    #print('assemble parent tree')
    position = parent_tree
    root = position
    while position:
        print(position)
        position = next(iter(position.values()))
    position.update(raw_param_branch)
    print(root)
    return root

# Merge A into B
def merge_dict(a, b, path=None):
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dict(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass  # same leaf value
            else:
                raise Exception("Conflict at %s" % ".".join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a


def gen_xml(rsop):
    # Build an array of (ParamLevel, BaseParam, avail_param_value) tuples from RSoP
    params = []
    dicts = []
    for base_param_id, param_value in rsop.items():
        base_param = BaseParam.get(BaseParam.id == base_param_id)
        param_level = base_param.param_level
        avail_param_value = param_value[0]
        tup = (param_level, base_param, avail_param_value)
        params.append(tup)

    param_branches_by_name = get_branch_dict_by_name(params)

    current_dict = {}

    for param_branch_name, param_branch in param_branches_by_name.items():
        parent_tree = build_parent_tree(
            ParamLevel.get(ParamLevel.name == param_branch_name)
        )

        full_tree = assemble_full_tree(parent_tree, param_branch)
        #print('\nParent ', parent_tree)
        #print('Branch: ', param_branch)
        #print('Full: ', full_tree, '\n')

        merge_dict(current_dict, full_tree)

    xml_string = xmltodict.unparse(AlphaDict(current_dict), pretty=True)

    return xml_string
