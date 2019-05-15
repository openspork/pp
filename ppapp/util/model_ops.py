from ppapp.models import *

def get_group_params(group):
    active_params = (AvailParam
            .select()
            .join(GroupAvailParams)
            .where(GroupAvailParams.group == group)
            .order_by(AvailParam.base_param.name)
            )
    avail_params = (AvailParam
            .select()
            .join(GroupAvailParams, JOIN.LEFT_OUTER)
            .where(AvailParam.id.not_in(active_params))
            .order_by(AvailParam.base_param.name)
            )
    return (avail_params, active_params)

def get_phone_params(phone):
    active_params = (AvailParam
            .select()
            .join(PhoneAvailParams)
            .where(PhoneAvailParams.phone == phone)
            .order_by(AvailParam.base_param.name)
            )
    avail_params = (AvailParam
            .select()
            .join(PhoneAvailParams, JOIN.LEFT_OUTER)
            .where(AvailParam.id.not_in(active_params))
            .order_by(AvailParam.base_param.name)
            )
    return (avail_params, active_params)

def get_phone_groups(phone):
    active_groups = (Group
            .select()
            .join(PhoneGroups, JOIN.LEFT_OUTER)
            .where(PhoneGroups.phone == phone)
            .order_by(Group.name)
            )

    avail_groups = (Group
            .select()
            .join(PhoneGroups, JOIN.LEFT_OUTER)
            .where(Group.id.not_in(active_groups))
            .order_by(Group.name)
            )    
    return(avail_groups, active_groups)

def add_params_to_phone(new_param_ids, phone):
    for new_param_id in new_param_ids:
        avail_param = AvailParam.get(AvailParam.id == new_param_id)
        PhoneAvailParams.create(avail_param = avail_param, phone = phone)
        avail_param.save()

def remove_params_from_phone(prev_param_ids, phone):
    for prev_param_id in prev_param_ids:
        avail_param = AvailParam.get(AvailParam.id == prev_param_id)
        delete_query = (PhoneAvailParams
                .delete()
                .where((PhoneAvailParams.phone == phone) & (PhoneAvailParams.avail_param == avail_param))
                )
        delete_query.execute()

def add_params_to_group(new_param_ids, group):
    for new_param_id in new_param_ids:
        avail_param = AvailParam.get(AvailParam.id == new_param_id)
        GroupAvailParams.create(avail_param = avail_param, group = group)
        avail_param.save()

def remove_params_from_group(prev_param_ids, group):
    for prev_param_id in prev_param_ids:
        avail_param = AvailParam.get(AvailParam.id == prev_param_id)
        delete_query = (GroupAvailParams
                .delete()
                .where((GroupAvailParams.group == group) & (GroupAvailParams.avail_param == avail_param))
                )
        delete_query.execute()

def add_groups_to_phone(new_group_ids, phone):
    for new_group_id in new_group_ids:
        group = Group.get(Group.id == new_group_id)
        PhoneGroups.create(group = group, phone = phone)
        group.save()

def remove_groups_from_phone(prev_group_ids, phone):
    for prev_group_id in prev_group_ids:
        group = Group.get(Group.id == prev_group_id)
        delete_query = (PhoneGroups
                .delete()
                .where((PhoneGroups.phone == phone) & (PhoneGroups.group == group))
                )
        delete_query.execute()