from peewee import *
#from ppapp.util import dicttoxml
from ppapp.models import *
#import xml.dom.minidom
import xmltodict

def get_branch_dict(params):
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

    # TODO: convert Models into strings
def sanitize_dict(param_branch):
    print(param_branch.name)
    # Fetch our edge param level
    #param_level = ParamLevel.get(ParamLevel == param_branch)
    # Print our avail params
    #print(param_level.name)



# "current" - is a ParamLevel
def build_dict(current, param_branch):
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
        temp_dict = {result.name: temp_dict}
        if i == 1:
            temp_dict[current] = sanitize_dict(current)
        query = (ParamLevel
            .select()
            # If we are looking for parents, we are matching on child
            .join(ParamLevelParamLevels, JOIN.LEFT_OUTER, on = (ParamLevelParamLevels.parent == ParamLevel.id))
            .where(ParamLevelParamLevels.child == result)
            )
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

        param_branches = get_branch_dict(params)

        
        # for each param level, build a pure dict
        for param_branch_key, param_branch in param_branches.items():
            # Create the surrounding dict with our branch appended
            branch_dict = build_dict(param_branch_key, param_branch) 

            #xml_string = dicttoxml(branch_dict['polycomConfig'], root=False, attr_type=False).decode('utf-8')
            #dom = xml.dom.minidom.parseString(xml_string).toprettyxml()
            #xml_string = xmltodict.unparse(branch_dict, pretty = True)
            xml_string = ''
            xmls.append(xml_string)
    return(xmls)