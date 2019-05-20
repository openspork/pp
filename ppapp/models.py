from peewee import *

db = MySQLDatabase("pp", user="pp", password="password", host="localhost", port=3306)
# db = SQLLite


class BaseModel(Model):
    class Meta:
        database = db


class Cert(BaseModel):
    cert = TextField()


class CertAuthority(Cert):
    pass


class ClientCert(Cert):
    ca = ForeignKeyField(CertAuthority)
    # phone = ForeignKeyField(Phone, backref="client_cert")


class Phone(BaseModel):
    name = CharField()
    mac_address = CharField(unique=True)
    client_cert = ForeignKeyField(ClientCert, backref="phones", null=True) # Change this back to False default later
    note = CharField(null=True)


class GroupType(BaseModel):
    name = CharField()
    precedence = IntegerField(unique=True)
    note = CharField()


class Group(BaseModel):
    type = ForeignKeyField(GroupType, backref="groups")
    name = CharField()
    note = CharField()


class GroupGroups(BaseModel):
    parent = ForeignKeyField(Group, null=True)
    child = ForeignKeyField(Group, null=True)


class PhoneGroups(BaseModel):
    phone = ForeignKeyField(Phone)
    group = ForeignKeyField(Group)


class ParamLevel(BaseModel):
    name = CharField(null=True)


class BaseParam(BaseModel):
    param_level = ForeignKeyField(ParamLevel, backref="base_params")
    name = CharField()
    default_value = CharField()
    note = CharField(null=True)


class ParamLevelParamLevels(BaseModel):
    parent = ForeignKeyField(ParamLevel)
    child = ForeignKeyField(ParamLevel)


class AvailParam(BaseModel):
    base_param = ForeignKeyField(BaseParam, backref="avail_params", null=True)
    value = CharField()
    note = CharField(null=True)


class PhoneAvailParams(BaseModel):
    avail_param = ForeignKeyField(AvailParam)
    phone = ForeignKeyField(Phone)


class GroupAvailParams(BaseModel):
    avail_param = ForeignKeyField(AvailParam)
    group = ForeignKeyField(Group)
