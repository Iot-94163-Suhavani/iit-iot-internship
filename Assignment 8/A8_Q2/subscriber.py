import paho.mqtt.client as mqtt
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_home_control"
)
cursor = db.cursor()

def on_message(client, userdata, message):
    appliance = message.topic.split("/")[-1]
    status = message.payload.decode()

    print(f"{appliance.upper()} turned {status}")

    query = """
    INSERT INTO appliance_status (appliance_name, status)
    VALUES (%s, %s)
    """
    cursor.execute(query, (appliance, status))
    db.commit()

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message

subscriber.connect("localhost", 1883)
subscriber.subscribe("home/light")
subscriber.subscribe("home/fan")

print("Appliance controller running...")
subscriber.loop_forever()
