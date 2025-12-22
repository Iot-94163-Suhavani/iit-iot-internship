import paho.mqtt.client as mqtt
import mysql.connector

# Thresholds
PULSE_MIN = 60
PULSE_MAX = 100
SPO2_MIN = 95

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="healthcare_monitor"
)
cursor = db.cursor()

def on_message(client, userdata, message):
    topic = message.topic
    value = float(message.payload.decode())

    status = "NORMAL"
    is_alert = False
    parameter = ""

    if topic == "patient/pulse":
        parameter = "Pulse"
        if value < PULSE_MIN or value > PULSE_MAX:
            status = "ABNORMAL"
            is_alert = True
            print(" ALERT: Abnormal Pulse =", value)

    elif topic == "patient/spo2":
        parameter = "SpO2"
        if value < SPO2_MIN:
            status = "ABNORMAL"
            is_alert = True
            print(" ALERT: Low SpO2 =", value)

    print(f"{parameter} received:", value)

    query = """
    INSERT INTO patient_monitoring
    (parameter, value, status, is_alert)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (parameter, value, status, is_alert))
    db.commit()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("patient/pulse")
client.subscribe("patient/spo2")

print("Healthcare Monitoring System started...")
client.loop_forever()
