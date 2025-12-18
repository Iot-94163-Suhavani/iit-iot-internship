import mysql.connector

connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agri_iot",
    use_pure=True
)

sensor_id=int(input("Enter sensor id: "))
moisture_level=int(input("Enter moisture level: "))
date=int(input("Enter date: "))
time=float(input("Enter time: "))

query=f"insert into soil_moisture value({sensor_id},'{moisture_level}','{date}','{time}');"

cursor=connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()