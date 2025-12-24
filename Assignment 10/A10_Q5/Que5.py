from flask import Flask
import mysql.connector
import paho.mqtt.publish as publish

app = Flask(__name__)

# MySQL configuration (USE YOUR DB)
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "smart_agri_iot"
}

# MQTT details
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "alert/moisture"

# Threshold value
THRESHOLD = 30


# Insert data into YOUR table
def insert_data(sensor_id, moisture_level, date, time):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = """
    INSERT INTO soil_moisture (sensor_id, moisture_level, date, time)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (sensor_id, moisture_level, date, time))
    conn.commit()
    conn.close()


@app.route('/moisture/<int:sensor_id>/<int:moisture>/<int:date>/<string:time>', methods=['POST'])
def receive_moisture(sensor_id, moisture, date, time):


    insert_data(sensor_id, moisture, date, time)

    # Threshold check
    if moisture < THRESHOLD:
        alert = f"ALERT! Moisture LOW: {moisture} (Sensor {sensor_id})"
        publish.single(MQTT_TOPIC, alert, hostname=MQTT_BROKER)
        return alert

    return f"Moisture stored successfully: {moisture}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)