from utils.dbConnection import getBDConnection

# To execute SELECT query

def executeSelectQuery(query):
    # create connection with mysql server
    connection = getBDConnection()

    # create cursor to execute a query
    cursor = connection.cursor()

    # execute query with cursor
    cursor.execute(query)

    # fetch data from cursor
    data = cursor.fetchall()

    # close the cursor
    cursor.close()

    # close the connection with mysql server
    connection.close()

    # return data
    return data