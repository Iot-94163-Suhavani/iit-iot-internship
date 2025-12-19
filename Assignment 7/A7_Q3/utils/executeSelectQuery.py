from utils.dbConnection import getBDConnection

def executeSelectQuery(query):
    connection=getBDConnection()
    cursor=connection.cursor()
    cursor.execute(query)
    data=cursor.fetchall()
    cursor.close()
    connection.close()
    return data
    