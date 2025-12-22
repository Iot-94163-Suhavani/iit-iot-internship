import paho.mqtt.client as mqtt
import time

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.connect("localhost", 1883)

intensity = 3050.5
publisher.publish("sensor/ldr", intensity)
print("Published Light Intensity:", intensity)

publisher.disconnect()
