from peewee import *

db = MySQLDatabase('pp', **{'charset': 'utf8', 'use_unicode': True, 'user': 'pp', 'password': 'password'})

class BaseModel(Model):
    class Meta:
        database = db

class Phone(BaseModel):
    name = CharField()
    mac_address = CharField()

class Client(BaseModel):
    name = CharField()

class PhoneClients(BaseModel):
    phone = ForeignKeyField(Phone)
    client = ForeignKeyField(Client)

class Site(BaseModel):
    name = CharField()

class PhoneSites(BaseModel):
    phone = ForeignKeyField(Phone)
    site = ForeignKeyField(Site)

class Extension(BaseModel):
    name = CharField()

class PhoneExtensions(BaseModel):
    phone = ForeignKeyField(Phone)
    extension = ForeignKeyField(Extension)

class ParamLevel(BaseModel):
    name = CharField(unique = True, null = True)

class BaseParam(BaseModel):
    param_level = ForeignKeyField(ParamLevel, backref = 'baseparams')
    name = CharField()
    default_value = CharField()
    note = CharField(null = True)

class AvailParam(BaseModel):
    base_param = ForeignKeyField(BaseParam, backref = 'avail_params', null = True)
    value = CharField()
    note = CharField(null = True)

class AvailParamPhones(BaseModel):
    avail_param = ForeignKeyField(AvailParam)
    phone = ForeignKeyField(Phone)

class AvailParamClients(BaseModel):
    avail_param = ForeignKeyField(AvailParam)
    client = ForeignKeyField(Client)

class AvailParamSites(BaseModel):
    avail_param = ForeignKeyField(AvailParam)
    site = ForeignKeyField(Site)

class AvailParamExtensions(BaseModel):
    avail_param = ForeignKeyField(AvailParam)
    extension = ForeignKeyField(Extension)
