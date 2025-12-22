import paho.mqtt.client as mqtt
import mysql.connector

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_home_monitor"
)
cursor = db.cursor()

def on_message(client, userdata, message):
    topic = message.topic
    value = float(message.payload.decode())

    if topic == "sensor/ldr":
        sensor_name = "LDR"
        print("LDR data received:", value)

    elif topic == "sensor/lm35":
        sensor_name = "LM35"
        print("LM35 data received:", value)

    query = "INSERT INTO sensor_data (sensor_name, value) VALUES (%s, %s)"
    cursor.execute(query, (sensor_name, value))
    db.commit()
    print("Data stored in database\n")

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message

subscriber.connect("localhost", 1883)
subscriber.subscribe("sensor/ldr")
subscriber.subscribe("sensor/lm35")

print("Subscriber started... Waiting for data")
subscriber.loop_forever()
