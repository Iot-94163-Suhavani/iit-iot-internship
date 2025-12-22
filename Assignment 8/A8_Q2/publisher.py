import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

# Control commands
client.publish("home/light", "ON")
client.publish("home/fan", "OFF")

print("Commands sent to appliances")

client.disconnect()
