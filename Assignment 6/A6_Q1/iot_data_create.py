import mysql.connector

connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data",
    use_pure=True
)

id=int(input("Enter id: "))
temp=int(input("Enter temperature: "))
humidity=int(input("Enter humidity: "))
timestamp=int(input("Enter timestamp: "))

query=f"insert into sensor_readings value({id},'{temp}','{humidity}','{timestamp}');"

cursor=connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()