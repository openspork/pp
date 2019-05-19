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

    # TODO: convert Models into strings
def sanitize_dict(param_branch):
    pass

# "current" - is a ParamLevel
def build_dict(current, raw_param_branch):
    #print(f'Found root node {current.name}')
    temp_dict = {}
    query = (ParamLevel
            .select()
            # If we are looking for parents, we are matching on child
            .join(ParamLevelParamLevels, JOIN.LEFT_OUTER, on = (ParamLevelParamLevels.parent == ParamLevel.id))
            .where(ParamLevelParamLevels.child == current)
            )
    i = 0
    while query.exists():
        i += 1
        result = query.get()
        temp_dict = {result.name: raw_param_branch}
        query = (ParamLevel
            .select()
            # If we are looking for parents, we are matching on child
            .join(ParamLevelParamLevels, JOIN.LEFT_OUTER, on = (ParamLevelParamLevels.parent == ParamLevel.id))
            .where(ParamLevelParamLevels.child == result)
            )
    print('our parent tree: %s' % temp_dict)
    return temp_dict

def gen_xml(rsop):
    # Build an array of (ParamLevel, BaseParam, avail_param_value) tuples
    params = []
    xmls = []
    #print(rsop)
    for base_param_id, param_value in rsop.items():
        base_param = BaseParam.get(BaseParam.id == base_param_id)
        param_level = base_param.param_level
        avail_param_value = param_value[0]
        tup = (param_level, base_param, avail_param_value)
        params.append(tup)

        param_branches = get_branch_dict_by_model(params)
        param_branches_by_name = get_branch_dict_by_name(params)
        
        # for each param level, build a pure dict
        for param_branch_key, param_branch in param_branches.items():
            print('processing branch: %s' % param_branch_key.name)
            
            # get our raw branch (no Models)
            raw_param_branch = param_branches_by_name[param_branch_key.name]
            
            print('our raw param branch: %s' % raw_param_branch)

            # Create the surrounding dict with our raw branch appended
            full_branch_dict = build_dict(param_branch_key, raw_param_branch) 

            print('our complete dict: %s' % full_branch_dict)

            #xml_string = xmltodict.unparse(branch_dict, pretty = True)
            xml_string = ''
            xmls.append(xml_string)
    return(xmls)