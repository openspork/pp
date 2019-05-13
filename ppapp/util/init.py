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
    if ( len(ParamLevel.select()) == 0 ):
        print('populating paramlevels')
        build_params()
    db.close()