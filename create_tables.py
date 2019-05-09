import xmltodict
import pymysql

db = pymysql.connect('localhost','pp','password','pp')
cursor = db.cursor()

# key is table name, value is [(key, value), (key, value)]
data = {}

def create_tables(data):
    for table in data.keys():
        if ( table ):
            columns = []
            rows = []
            for leaf_pair in data[table]:
                columns.append(leaf_pair[0])
                rows.append(leaf_pair[1])

            if ( len(columns) > 0 ):
                #print('creating table %s\ncolumns: %s' % (table, columns))
                create_string = 'CREATE TABLE IF NOT EXISTS `%s`(' % table
                for column in columns:
                    create_string += '`%s` TEXT,' % column
                create_string = create_string[:-1]
                create_string += ')'
                #print(create_string)
                cursor.execute(create_string)
                # Now input data into the freshly created tables

                # Define our columns
                column_string = '('
                for column in columns:
                    column_string += '`%s`,' % column
                column_string = column_string[:-1]
                column_string += ')'
                print(column_string)

                # Define our rows
                row_string = '('
                for row in rows:
                    # if ( row == '' ):
                    #     print('NULL ROW')
                    #     row = 'NULL'
                    row_string += '%s,' % row
                row_string = row_string[:-1]
                row_string += ')'
                print(row_string)
                insert_string = 'INSERT INTO `%s` %s VALUES %s' % (table, column_string, row_string)
                print(insert_string)
                cursor.execute(insert_string, )



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