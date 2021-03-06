from ppapp.util.parse_xml import build_params
from ppapp.models import *


def init_db():
    print("db init")
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
        ],
        safe=True,
    )

    # Create our group types
    query = GroupType.select().where(GroupType.name == "Client")

    if not query.exists():
        GroupType.create(
            name="Client", precedence=0, note="Group for client level config"
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

    if len(ParamLevel.select()) == 0:
        print("populating paramlevels")
        build_params()

    build_params()
    db.close()
