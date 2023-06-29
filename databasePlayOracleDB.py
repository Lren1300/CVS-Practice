'''
databasePlayOracleDB.py
This file shows the use of python-oracledb import to connect
to an oracle database.
'''

import getpass
import oracledb

password = getpass.getpass("Enter password: ")

connection = oracledb.connect(
    user="username",
    password=password,
    dsn="localhost")
print("Successfully connected to Oracle Database")

cursor = connection.cursor()

'''
GIVEN QUERIES FROM ORACLE WEBSITE
'''
#drop table if it exists
cursor.execute("""
    begin
        execute immediate 'drop table todoitem';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

#create a new table
cursor.execute("""
    create table todoitem (
        id number generated always as identity,
        description varchar2(4000),
        creation_ts timestamp with time zone default current_timestamp,
        done number(1,0),
        primary key (id))""")

# Insert some data
rows = [ ("Task 1", 0 ),
         ("Task 2", 0 ),
         ("Task 3", 1 ),
         ("Task 4", 0 ),
         ("Task 5", 1 ) ]

cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
print(cursor.rowcount, "Rows Inserted")
'''
END 
'''

connection.commit()

# Now query the rows back to test if the data persisted
for row in cursor.execute('select description, done from todoitem'):
    if (row[1]):
        print(row[0], "is done")
    else:
        print(row[0], "is NOT done")


