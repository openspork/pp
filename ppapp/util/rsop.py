from ppapp.models import *
from ppapp.util.group_ops import *
from ppapp.util.param_ops import *

def drill(group, rsop, depth):
    depth += 1
    print('processing %s' % group.name)
    params = get_group_params(group)[1]

    for param in params:
        # If this is not a duplicate
        if param.base_param.name not in rsop.keys():
            # Add to our dict
            rsop[param.base_param.name] = (param.value, group, depth, [])
        else:
            # TODO: add logic to prefer based on type
            # Compare depth of saved param to current
            if depth > rsop[param.base_param.name][2] :
                # If deeper, add as an override
                print('Deeper dupe!')
                rsop[param.base_param.name][3].append((param.value, group.id, depth))
            elif rsop[param.base_param.name][2] == depth:
                # If equal, prefer based on group type precedence
                existing_group = Group.get(Group.id == rsop[param.base_param.name][1])
                # If the new type is greater than previous, update
                if group.type.precedence > existing_group.type.precedence:
                    print('Higher priority dupe!')
                    overridden_param_overrides = rsop[param.base_param.name][3] # Save existing overrides
                    overridden_param = (rsop[param.base_param.name][0], rsop[param.base_param.name][1].id, rsop[param.base_param.name][2])
                    overridden_param_overrides.append(overridden_param) # Concatenate previously overridden params with current
                    rsop[param.base_param.name] = (param.value, group, depth, overridden_param_overrides) # Update param
                elif group.type.precedence == existing_group.type.precedence:
                    raise Exception('Duplicate param of equal precedence!  Cannot resolve!')

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