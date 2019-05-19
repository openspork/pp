from ppapp.models import *


def get_group_params(group):
    active_params = (
        AvailParam.select()
        .join(GroupAvailParams)
        .where(GroupAvailParams.group == group)
        .order_by(AvailParam.base_param.name)
    )
    avail_params = (
        AvailParam.select()
        .join(GroupAvailParams, JOIN.LEFT_OUTER)
        .where(AvailParam.id.not_in(active_params))
        .order_by(AvailParam.base_param.name)
    )
    return (avail_params, active_params)


def get_phone_params(phone):
    active_params = (
        AvailParam.select()
        .join(PhoneAvailParams)
        .where(PhoneAvailParams.phone == phone)
        .order_by(AvailParam.base_param.name)
    )
    avail_params = (
        AvailParam.select()
        .join(PhoneAvailParams, JOIN.LEFT_OUTER)
        .where(AvailParam.id.not_in(active_params))
        .order_by(AvailParam.base_param.name)
    )
    return (avail_params, active_params)


def add_params_to_phone(new_param_ids, phone):
    for new_param_id in new_param_ids:
        avail_param = AvailParam.get(AvailParam.id == new_param_id)
        PhoneAvailParams.create(avail_param=avail_param, phone=phone)
        avail_param.save()


def remove_params_from_phone(prev_param_ids, phone):
    for prev_param_id in prev_param_ids:
        avail_param = AvailParam.get(AvailParam.id == prev_param_id)
        delete_query = PhoneAvailParams.delete().where(
            (PhoneAvailParams.phone == phone)
            & (PhoneAvailParams.avail_param == avail_param)
        )
        delete_query.execute()


def add_params_to_group(new_param_ids, group):
    for new_param_id in new_param_ids:
        avail_param = AvailParam.get(AvailParam.id == new_param_id)
        GroupAvailParams.create(avail_param=avail_param, group=group)
        avail_param.save()


def remove_params_from_group(prev_param_ids, group):
    for prev_param_id in prev_param_ids:
        avail_param = AvailParam.get(AvailParam.id == prev_param_id)
        delete_query = GroupAvailParams.delete().where(
            (GroupAvailParams.group == group)
            & (GroupAvailParams.avail_param == avail_param)
        )
        delete_query.execute()
