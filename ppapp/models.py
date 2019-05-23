from peewee import *

db = MySQLDatabase("pp", user="pp", password="password", host="localhost", port=3306)

class LongTextField(TextField):
    field_type = 'LONGTEXT'

class BaseModel(Model):
    class Meta:
        database = db

class NameNoteField(BaseModel):
    name = CharField()
    note = CharField(null=True)

class Phone(NameNoteField):
    mac_address = CharField()

class Cert(BaseModel):
    public_key = TextField()

class CertAuthority(Cert, NameNoteField):
    private_key = TextField()


class ClientCert(Cert):
    phone = ForeignKeyField(Phone, backref = 'client_certs')
    cert_authority = ForeignKeyField(CertAuthority, null=True) # Change this back to False default later


class GroupType(NameNoteField):
    precedence = IntegerField(unique=True)

class Group(NameNoteField):
    pass
    type = ForeignKeyField(GroupType, backref="groups")
    cert_authority = ForeignKeyField(CertAuthority, backref="groups", null=True)


class GroupGroups(BaseModel):
    parent = ForeignKeyField(Group, null=True)
    child = ForeignKeyField(Group, null=True)


class PhoneGroups(BaseModel):
    phone = ForeignKeyField(Phone)
    group = ForeignKeyField(Group)


class ParamLevel(BaseModel):
    name = CharField(null=True)


class BaseParam(NameNoteField):
    param_level = ForeignKeyField(ParamLevel, backref="base_params")
    default_value = CharField()


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

class Log(BaseModel):
    phone = ForeignKeyField(Phone, backref = 'logs', null=True)
    date_time = DateTimeField()
    data = LongTextField()

class AppLog(Log):
    pass

class BootLog(Log):
    pass

class CallLog(Log):
    pass