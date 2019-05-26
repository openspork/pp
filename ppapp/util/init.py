from ppapp.models import *


def init_db():
    try:
        db.connect()
    except Exception as e:
        print(str(e))

    db.create_tables(
        [
            Phone,
            Group,
            GroupType,
            GroupGroups,
            PhoneGroups,
            ParamLevel,
            ParamLevelParamLevels,
            BaseParam,
            AvailParam,
            PhoneAvailParams,
            GroupAvailParams,
            CertAuthority,
            ClientCert,
            PhoneActiveClientCert,
            BootLog,
            AppLog,
            CallLog,
        ],
        safe=True,
    )

    db.close()
    print("db init")
