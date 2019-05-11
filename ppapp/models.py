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

class Site(BaseModel):
    name = CharField()

class Extension(BaseModel):
    name = CharField()

class ParamLevel(BaseModel):
    name = CharField(unique = True, null = True)

class BaseParam(BaseModel):
    param_level = ForeignKeyField(ParamLevel, backref = 'baseparams')
    name = CharField()
    default_value = CharField()
    note = CharField(null = True)

class AvailParam(BaseModel):
    phone_params = ForeignKeyField(Phone, backref = 'avail_params', null = True)
    client_params = ForeignKeyField(Client, backref = 'avail_params', null = True)
    site_params = ForeignKeyField(Site, backref = 'avail_params', null = True)
    extension_params = ForeignKeyField(Extension, backref = 'avail_params', null = True)
    base_param = ForeignKeyField(BaseParam, backref = 'avail_params', null = True)
    value = CharField()
    note = CharField(null = True)

