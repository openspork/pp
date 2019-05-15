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
    	GroupType.create(name = 'Client', precedence = 0, note = 'Group for client level config')

    query = GroupType.select().where(GroupType.name == 'Site')

    if not query.exists():
    	GroupType.create(name = 'Site', precedence = 5, note = 'Group for site level config')

    query = GroupType.select().where(GroupType.name == 'Model')

    if not query.exists():
    	GroupType.create(name = 'Model', precedence = 10, note = 'Group for phone model level config')

    query = GroupType.select().where(GroupType.name == 'Addon')

    if not query.exists():
    	GroupType.create(name = 'Addon', precedence = 15, note = 'Group for addon unit level config')

    if ( len(ParamLevel.select()) == 0 ):
        print('populating paramlevels')
        build_params()
    db.close()