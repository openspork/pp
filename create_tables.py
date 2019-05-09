import xmltodict
import pymysql

db = pymysql.connect('localhost','pp','password','pp')
cursor = db.cursor()

# key is table name, value is [(key, value), (key, value)]
data = {}



def create_tables(data):
	for table in data.keys():
		columns = []
		for leaf_pair in data[table]:

			columns.append(leaf_pair[0])

		print('creating table %s\ncolumns: %s' % (table, columns))




def find_leaf(parent, d):
	global data
	leaf_pairs = []
	for key, value in d.items():
		if ( isinstance(value,dict) ):
			find_leaf(key, value)
		else:	
			#print('found leaf -- parent: %s key: %s value: %s' % (parent, key, value))
			leaf_pairs.append((key, value))

	data[parent] = leaf_pairs

with open('./configs/site.cfg') as fd:
	content = fd.read()
	doc = xmltodict.parse(content)

	find_leaf(None, doc)

create_tables(data)