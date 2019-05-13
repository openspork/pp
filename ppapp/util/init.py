from ppapp.util.parse_xml import build_params
from ppapp.models import *

def init_db():
    print('db init')
    db.connect()

    desired_tables = [Phone,
                Client,
                Site,
                Extension,
                PhoneClients,
                PhoneSites,
                PhoneExtensions,
                ParamLevel,
                BaseParam,
                AvailParam,
                AvailParamPhones,
                AvailParamClients,
                AvailParamSites,
                AvailParamExtensions]

    for desired_table in desired_tables:
        db.create_tables(desired_table)

    if ( len(ParamLevel.select()) == 0 ):
        print('populating paramlevels')
        build_params()
    db.close()