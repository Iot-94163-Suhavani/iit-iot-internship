from flask import Flask
import mysql.connector
import paho.mqtt.publish as publish

app = Flask(__name__)

# MySQL configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "smart_agri_iot"
}

# MQTT details
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "alert/moisture"

# Threshold
THRESHOLD = 30


# Insert data into MySQL
def insert_data(sensor_id, moisture_level,date,time):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = """
    INSERT INTO moisture_data (sensor_id, moisture_level, date,time)
    VALUES (%s, %s, %s,%s)
    """

    cursor.execute(query, (
        sensor_id,
        moisture_level,
        date,
        time
    ))

    conn.commit()
    conn.close()


# API to receive moisture data
@app.route('/moisture/<sensor_id>/<int:moisture>', methods=['POST'])
def receive_moisture(sensor_id, moisture_level,date,time):

    insert_data(sensor_id, moisture_level,date,time)

    # Threshold check
    if moisture_level < THRESHOLD:
        alert = f"ALERT! Moisture LOW: {moisture_level} (Sensor {sensor_id})"
        publish.single(MQTT_TOPIC, alert, hostname=MQTT_BROKER)
        return alert

    return f"Moisture stored successfully: {moisture_level}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
