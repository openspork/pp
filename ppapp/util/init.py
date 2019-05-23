from ppapp.models import *


def init_db():
    try:
        db.connect()
    except Exception as e:
        print(str(e))

    db.create_tables([
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
            BootLog,
            AppLog,
            CallLog
            ], safe=True)


    # Create our group types
    query = GroupType.select().where(GroupType.name == "Client")

    if not query.exists():
        GroupType.create(
            name="Client", precedence=1, note="Group for client level config"
        )

    query = GroupType.select().where(GroupType.name == "Site")

    if not query.exists():
        GroupType.create(name="Site", precedence=5, note="Group for site level config")

    query = GroupType.select().where(GroupType.name == "Model")

    if not query.exists():
        GroupType.create(
            name="Model", precedence=10, note="Group for phone model level config"
        )

    query = GroupType.select().where(GroupType.name == "Addon")

    if not query.exists():
        GroupType.create(
            name="Addon", precedence=15, note="Group for addon unit level config"
        )

    db.close()
    print("db init")
