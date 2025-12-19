import mysql.connector

def getBDConnection():
    connection=mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="smart_home_db",
        use_pure=True
    )
    return connection