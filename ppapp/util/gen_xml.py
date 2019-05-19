from peewee import *
#from ppapp.util import dicttoxml
from ppapp.models import *
#import xml.dom.minidom
import xmltodict

def get_branch_dict_by_model(params):
    # Create a dict of dicts with each ParamLevel as key
    param_levels = {}
    for param in params:
        param_level = param[0]
        base_param = param[1]
        avail_param_value = param[2]
        #print('\nProcessing param_level: "%s" base_param: "%s" avail_value: "%s"' % (param_level.name, base_param.name, avail_param_value))
        
        param_levels[param_level] = {} # Initiate empty dict
        #print('Array created for param level: "%s"' % param_level.name )
        # Populate the arrays
        for param2 in params:
            # if param level is the key, append it to the array
            param_level2 = param2[0]
            if param_level == param_level2:
                base_param = param2[1]
                param_value = param2[2]
                param_levels[param_level][base_param] = param_value # Add our value with base as key

    return param_levels

def get_branch_dict_by_name(params):
    # Create a dict of dicts with each ParamLevel name as key
    param_levels = {}
    for param in params:
        param_level = param[0].name
        base_param = param[1].name
        avail_param_value = param[2]
        #print('\nProcessing param_level: "%s" base_param: "%s" avail_value: "%s"' % (param_level, base_param, avail_param_value))
        
        param_levels[param_level] = {} # Initiate empty dict
        #print('Array created for param level: "%s"' % param_level.name )
        # Populate the arrays
        for param2 in params:
            # if param level is the key, append it to the array
            param_level2 = param2[0].name
            if param_level == param_level2:
                base_param = param2[1].name
                param_value = param2[2]
                param_levels[param_level][base_param] = param_value # Add our value with base as key

    return param_levels

# "current" - is a ParamLevel
def build_parent_tree(current):
    #print(f'Found root node {current.name}')
    temp_dict = {}
    query = (ParamLevel
            .select()
            # If we are looking for parents, we are matching on child
            .join(ParamLevelParamLevels, JOIN.LEFT_OUTER, on = (ParamLevelParamLevels.parent == ParamLevel.id))
            .where(ParamLevelParamLevels.child == current)
            )
    while query.exists():
        result = query.get()
        temp_dict = {result.name: temp_dict }
        query = (ParamLevel
            .select()
            # If we are looking for parents, we are matching on child
            .join(ParamLevelParamLevels, JOIN.LEFT_OUTER, on = (ParamLevelParamLevels.parent == ParamLevel.id))
            .where(ParamLevelParamLevels.child == result)
            )
    return temp_dict

def assemble_full_tree(parent_tree, raw_param_branch):
    position = parent_tree
    root = position
    while position:
        position = next(iter(position.values()))
    position.update(raw_param_branch)

    return root

def gen_xml(rsop):
    # Build an array of (ParamLevel, BaseParam, avail_param_value) tuples
    params = []
    xmls = []
    for base_param_id, param_value in rsop.items():
        base_param = BaseParam.get(BaseParam.id == base_param_id)
        param_level = base_param.param_level
        avail_param_value = param_value[0]
        tup = (param_level, base_param, avail_param_value)
        params.append(tup)

    param_branches = get_branch_dict_by_model(params)
    param_branches_by_name = get_branch_dict_by_name(params)
    
    for param_branch_key, param_branch in param_branches.items():
        #print('Processing branch: %s' % param_branch_key.name)
        # Get our raw branch (no Models)
        raw_param_branch = param_branches_by_name[param_branch_key.name]
        # rint('Raw param branch: %s' % raw_param_branch)
        # Create the surrounding dict

        # All this needs is the starting node -- should be able to replace with query based on name...
        parent_tree = build_parent_tree(param_branch_key) 
        #print('Parent tree: %s' % parent_tree)
        full_tree = assemble_full_tree(parent_tree, raw_param_branch)
        #print('Complete dict: %s' % full_tree)
        xml_string = xmltodict.unparse(full_tree, pretty = True)
        #xml_string = ''
        xmls.append(xml_string)
    return(xmls)