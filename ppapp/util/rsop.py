from ppapp.models import *
from ppapp.util.group_ops import *
from ppapp.util.param_ops import *

def drill(group, rsop, depth):
    depth += 1
    print('processing %s' % group.name)
    params = get_group_params(group)[1]

    for param in params:
        if param.base_param.name not in rsop.keys():
            rsop[param.base_param.name] = (param.value, group, depth, [])
        else:
            print('dupe!  Appending override!', (param.value, group.id, depth))
            rsop[param.base_param.name][3].append((param.value, group.id, depth))
            

    groups = get_group_groups(group,'parents')[1]
    if len(groups) == 0:
        print('final group found')
    else:
        for group in groups:
            drill(group, rsop, depth)
    return rsop

def gen_rsop(phone):
    rsop = {}
    overrides = []
    params = get_phone_params(phone)[1]

    for param in params:
        rsop[param.base_param.name] = (param.value, phone, 0, [])

    groups = get_phone_groups(phone)[1]
    for group in groups:
        rsop = drill(group, rsop, 0)

    return rsop