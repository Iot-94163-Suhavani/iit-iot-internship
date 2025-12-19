from utils.dbConnection import getBDConnection

# To execute CREATE, UPDATE and DELETE query

def executeQuery(query):
    # create connection with mysql server
    connection = getBDConnection()

    # create cursor to execute a query
    cursor = connection.cursor()

    # execute query with cursor
    cursor.execute(query)

    # commit your changes to mysql server
    connection.commit()

    # close the cursor
    cursor.close()

    # close the connection with mysql server
    connection.close()
