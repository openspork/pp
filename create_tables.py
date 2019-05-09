#import pymysql
# db=pymysql.connect('localhost','pp','password','pp')
# cursor = db.cursor()
# cursor.execute('select user from user;')
# data = cursor.fetchone()
from peewee import *
import xmltodict

mysql_db = MySQLDatabase('pp', user = 'pp', password = 'password', host = 'localhost', port = 3316)

class BaseModel(Model):
	class Meta:
		database = mysql_db

class Leaf(BaseModel)







def create_table():
	print('creating table')


with open('./configs/site.cfg') as fd:
	content = fd.read()
	doc = xmltodict.parse(content)

	def find_leaf(parent, d):
		# search children
		for key, value in d.items():
			if ( isinstance(value,dict) ):
				#print('found a dict!')
				#print('searching child: %s' % key )
				find_leaf(key, value)
			else:	
				print('found leaf -- parent: %s key: %s value: %s' % (parent, key, value))


	find_leaf(None, doc)

