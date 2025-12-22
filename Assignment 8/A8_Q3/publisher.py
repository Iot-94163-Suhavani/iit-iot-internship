import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)


pulse = random.randint(55, 120)
spo2 = random.randint(88, 100)

client.publish("patient/pulse", pulse)
client.publish("patient/spo2", spo2)

print(f"Pulse: {pulse} bpm | SpO2: {spo2}%")
time.sleep(5)
