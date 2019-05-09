import pymysql

# db=pymysql.connect('localhost','pp','password','pp')

# cursor = db.cursor()

# cursor.execute('select user from user;')

# data = cursor.fetchone()

# for row in data:
#     print(data)

import xmltodict

with open('./configs/site.cfg') as fd:
	content = fd.read()
	doc = xmltodict.parse(content)

	def find_leaf(d):
		# search children
		for key, value in d.items():
			if ( isinstance(value,dict) ):
				print('found a dict!')
				print('searching child: %s' % key )
				find_leaf(value)
			else:	
				print('found leaf: key: %s value: %s' % (key, value))

	find_leaf(doc)