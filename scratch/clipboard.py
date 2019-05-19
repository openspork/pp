path_dict = {}

def build_dict(current, wip_dict):
	print(wip_dict)
	query = (ParamLevel
			.select()
			# If we are looking for parents, we are matching on child
			.join(ParamLevelParamLevels, JOIN.LEFT_OUTER, on = (ParamLevelParamLevels.parent == ParamLevel.id))
			.where(ParamLevelParamLevels.child == current)
			)

	# If we have a parent node, recurse further
	if query.exists():
		parent = query.get()

		print('Current ParamLevel "%s" parent: "%s"' % ( current.name, parent.name ))

		wip_dict[parent.name][current.name] = wip_dict

		build_dict(parent, wip_dict)

	else:
		print('Found root node: %s' % current.name)
		path_dict = wip_dict