'''
databasePlayCx.py
This file is to show the basic use of cx_Oracle import
to access oracle database. This will not run as it has many
placeholder information since I do not have an oracle DB.
'''
import cx_Oracle as orac

try:
    # create a connection to Oracle database
    connection = orac.connect("username/password@localhost")

    # create a cursor to execute queries
    cursor = connection.cursor()

    # variable to track end of input
    flag = True

    # while we are still inputting queries
    while flag:
        # prompt user for a query
        input_query = input("Insert query would you like to run (type quit to exit): ")

        # if the user types quit, end input cycle
        if input_query.lower() == "quit":
            flag = False

        # if not execute the query
        else:
            cursor.execute(input_query)
            print("Success.")

# if there is an error, throw an exception
except orac.DatabaseError as execpetion:
    print("There is an error with Oracle", execpetion)

# once done, close the cursor and the connection.
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
