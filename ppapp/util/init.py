from ppapp.util.parse_xml import build_params
from ppapp.models import *

def init_db():
    print('db init')
    db.connect()

    db.create_tables([Phone,
    				Group,
                    GroupType,
                    PhoneGroups,
    				ParamLevel,
    				BaseParam,
    				AvailParam,
    				AvailParamPhones,
    				AvailParamGroups],
    				safe = True)

    # Create our group types
    query = GroupType.select().where(GroupType.name == 'Client')

    if not query.exists():
    	GroupType.create(name = 'Client', note = 'Group for client level config')

    query = GroupType.select().where(GroupType.name == 'Site')

    if not query.exists():
    	GroupType.create(name = 'Site', note = 'Group for site level config')

    query = GroupType.select().where(GroupType.name == 'Model')

    if not query.exists():
    	GroupType.create(name = 'Model', note = 'Group for phone model level config')

    query = GroupType.select().where(GroupType.name == 'Addon')

    if not query.exists():
    	GroupType.create(name = 'Addon', note = 'Group for addon unit level config')

    if ( len(ParamLevel.select()) == 0 ):
        print('populating paramlevels')
        build_params()
    db.close()