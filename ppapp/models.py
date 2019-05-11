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

class ActiveParam(BaseModel):
    phone_params = ForeignKeyField(Phone, backref = 'active_params')
    client_params = ForeignKeyField(Client, backref = 'active_params')
    site_params = ForeignKeyField(Site, backref = 'active_params')
    extension_params = ForeignKeyField(Extension, backref = 'active_params')
    base_param = ForeignKeyField(BaseParam, backref = 'active_params')
    value = CharField()
    note = CharField(null = True)

