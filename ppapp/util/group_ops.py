from ppapp.models import *

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

def get_group_groups(group, relationship):
    if relationship == 'parents':
        active_groups = (Group
                .select()
            # If we are looking for parents, we are matching on child
            .join(GroupGroups, JOIN.LEFT_OUTER, on=(GroupGroups.parent == Group.id))
            .where(GroupGroups.child == group)
            .order_by(Group.name)
                )
    elif relationship == 'children':
        active_groups = (Group.select()
            # If we are looking for children, we are joining children
            .join(GroupGroups, JOIN.LEFT_OUTER, on=(GroupGroups.child == Group.id))
            # We are matching on parent
            .where(GroupGroups.parent == group)
            .order_by(Group.name)
            )
    # Avail is the inverse of whatever is the above
    # Need to check for circular dependency here or elsewhere

    avail_groups = (Group
            .select()
            .join(GroupGroups, JOIN.LEFT_OUTER, on=(GroupGroups.parent == Group.id))
            # Omit siblings, children & ourselves
            .where((Group.id != group.id) & # Omit ourselves
                    Group.id.not_in(active_groups) & # Omit children
                    Group.id.not_in( # Omit parents
                        GroupGroups.select().where(GroupGroups.child == group.id)) # (Where we are not a child)
                )
            .order_by(Group.name)
            )    
    return(avail_groups, active_groups)

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

def add_groups_to_group(new_group_ids, group, relationship):
	if relationship == 'children':
		for new_child_group_id in new_group_ids:
			new_child_group = Group.get(Group.id == new_child_group_id)
			GroupGroups.create(parent = group, child = new_child_group)
			group.save()
	elif relationship =='parents':
		for new_parent_group_id in new_group_ids:
			new_parent_group = Group.get(Group.id == new_parent_group_id)
			GroupGroups.create(parent = new_parent_group, child = group)
			group.save()

def remove_groups_from_group(prev_group_ids, group, relationship):
	if relationship == 'children':
		for child_group_id in prev_group_ids:
			child_group = Group.get(Group.id == child_group_id)
			delete_query =(GroupGroups
					.delete()
					.where((GroupGroups.parent == group) & (GroupGroups.child == child_group))
					)
			delete_query.execute()
	elif relationship == 'parents':
		for parent_group_id in prev_group_ids:
			parent_group = Group.get(Group.id == parent_group_id)
			delete_query =(GroupGroups
					.delete()
					.where((GroupGroups.child == group) & (GroupGroups.parent == parent_group))
					)
			delete_query.execute()