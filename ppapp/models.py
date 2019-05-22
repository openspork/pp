from peewee import *

db = MySQLDatabase("pp", user="pp", password="password", host="localhost", port=3306)

class LongTextField(TextField):
    field_type = 'LONGTEXT'

class NameNoteField(Model):
    name = CharField()
    note = CharField(null=True)


class BaseModel(Model):
    class Meta:
        database = db

class Cert(BaseModel):
    public_key = TextField()

class CertAuthority(Cert, NameNoteField):
    private_key = TextField()


class ClientCert(Cert):
    cert_authority = ForeignKeyField(CertAuthority)

class Phone(BaseModel, NameNoteField):
    mac_address = CharField(unique=True)
    client_cert = ForeignKeyField(
        ClientCert, backref="phones", null=True
    )  # Change this back to False default later


class GroupType(BaseModel, NameNoteField):
    precedence = IntegerField(unique=True)

class Group(BaseModel, NameNoteField):
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


class BaseParam(BaseModel, NameNoteField):
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
    phone = ForeignKeyField(Phone, backref = 'logs')
    date_time = DateTimeField()
    data = LongTextField()

class AppLog(Log):
    pass

class BootLog(Log):
    pass

class CallLog(Log):
    pass