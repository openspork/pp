import xmltodict
import pymysql

db = pymysql.connect('localhost','pp','password','pp')
cursor = db.cursor()

# key is table name, value is [(key, value), (key, value)]
data = {}

def create_tables(data):
    # Define static tables
    create_strings = [
    'CREATE TABLE IF NOT EXISTS Phone (ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(ID), `Name` VARCHAR(255) NOT NULL, MACAddress VARCHAR(255) NOT NULL)',
    'CREATE TABLE IF NOT EXISTS Client (ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(ID), `Name` VARCHAR(255) NOT NULL)',
    'CREATE TABLE IF NOT EXISTS Site (ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(ID), `Name` VARCHAR(255) NOT NULL)',
    'CREATE TABLE IF NOT EXISTS Model (ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(ID), `Name` VARCHAR(255) NOT NULL)',
    'CREATE TABLE IF NOT EXISTS Expansion (ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(ID), `Name` VARCHAR(255) NOT NULL)'
    ]
    # Create static tables
    for create_string in create_strings:
        cursor.execute(create_string)

    # Create our dynamic tables
    # Begin our creation string
    create_string = 'CREATE TABLE IF NOT EXISTS '
    primary_key = 'ID INT NOT NULL AUTO_INCREMENT,PRIMARY KEY (ID)'
    phone_key = 'PhoneID INT, FOREIGN KEY (PhoneID) REFERENCES Phone(ID)'
    client_key = 'ClientID INT, FOREIGN KEY (ClientID) REFERENCES Client(ID)'
    site_key = 'SiteID INT, FOREIGN KEY (SiteID) REFERENCES Site(ID)'
    expansion_key = 'ExpansionID INT, FOREIGN KEY (ExpansionID) REFERENCES Expansion(ID)'
    keys_string = '%s,%s,%s,%s,%s' % (primary_key, phone_key, client_key, site_key, expansion_key)

    # Begin our insertion string
    insert_string = 'REPLACE INTO '

    for table in data.keys():
        if ( table ):
            columns = []
            rows = []
            for leaf_pair in data[table]:
                columns.append(leaf_pair[0])
                rows.append(leaf_pair[1])

            # Only process if there are columns to create
            if ( len(columns) > 0 ):
                #print('creating table %s\ncolumns: %s' % (table, columns))
                create_string = 'CREATE TABLE IF NOT EXISTS '
                create_string += '`%s`(%s,' % (table, keys_string)
                for column in columns:
                    create_string += '`%s`TEXT,' % column
                create_string = create_string[:-1]
                create_string += ')'
                #print(create_string,'\n')
                cursor.execute(create_string)

                # Now input data into the freshly created tables
                # Define our columns
                column_string = '('
                for column in columns:
                    column_string += '`%s`,' % column
                column_string = column_string[:-1]
                column_string += ')'

                # Define our rows
                row_string = '('
                for row in rows:
                    if ( row == '' ):
                        row = 'NULL'
                    row_string += '\'%s\',' % row
                row_string = row_string[:-1]
                row_string += ')'

                replace_string = 'REPLACE INTO `%s` %s VALUES %s' % (table, column_string, row_string)
                #print(replace_string,'\n')
                cursor.execute(replace_string)

def find_leaf(parent, d):
    global data
    leaf_pairs = []
    for key, value in d.items():
        if ( isinstance(value,dict) ):
            # Create an intermediate node
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