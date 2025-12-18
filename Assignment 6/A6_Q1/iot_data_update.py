import mysql.connector

connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data",
    use_pure=True
)

id=int(input("Enter id whose temperature to be updated: "))
temp=int(input("Enter new temperature: "))


query=f"update sensor_readings SET temperature='{temp}' where id='{id}';"

cursor=connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()