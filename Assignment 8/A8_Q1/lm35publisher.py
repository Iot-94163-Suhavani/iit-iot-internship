import paho.mqtt.client as mqtt
import time

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.connect("localhost", 1883)

temperature = 58.5
publisher.publish("sensor/lm35", temperature)
print("Published Temperature:", temperature)

publisher.disconnect()
