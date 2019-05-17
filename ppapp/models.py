from peewee import *

db = MySQLDatabase('pp', **{'charset': 'utf8', 'use_unicode': True, 'user': 'pp', 'password': 'password'})

class BaseModel(Model):
    class Meta:
        database = db

class Phone(BaseModel):
    name = CharField()
    mac_address = CharField(unique = True)
    note = CharField()

class GroupType(BaseModel):
    name = CharField()
    precedence = IntegerField(unique = True)
    note = CharField()

class Group(BaseModel):
    type = ForeignKeyField(GroupType, backref = 'groups')
    name = CharField()
    note = CharField()

class GroupGroups(BaseModel):
    parent = ForeignKeyField(Group, null = True)
    child = ForeignKeyField(Group, null = True)

class PhoneGroups(BaseModel):
    phone = ForeignKeyField(Phone)
    group = ForeignKeyField(Group)

class ParamLevel(BaseModel):
    name = CharField(null = True)#, unique = True,)

class BaseParam(BaseModel):
    param_level = ForeignKeyField(ParamLevel, backref = 'base_params')
    name = CharField()
    default_value = CharField()
    note = CharField(null = True)

class ParamLevelParamLevels(BaseModel):
    parent = ForeignKeyField(ParamLevel)
    child = ForeignKeyField(ParamLevel)

class AvailParam(BaseModel):
    base_param = ForeignKeyField(BaseParam, backref = 'avail_params', null = True)
    value = CharField()
    note = CharField(null = True)

class PhoneAvailParams(BaseModel):
    avail_param = ForeignKeyField(AvailParam)
    phone = ForeignKeyField(Phone)

class GroupAvailParams(BaseModel):
    avail_param = ForeignKeyField(AvailParam)
    group = ForeignKeyField(Group)