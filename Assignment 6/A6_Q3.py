from flask import Flask
import os

server = Flask(__name__)

@server.get('/')
def home():
    return "Sensor Server Running"

@server.route('/temperature/<float:temp>', methods=['GET', 'POST'])
def post_temperature(temp):
    with open("temperature.txt", "a") as t:
        t.write(str(temp) + "\n")
    return f"Temperature {temp} stored"

@server.route('/light/<int:light>', methods=['GET', 'POST'])
def post_light(light):
    with open("light.txt", "a") as l:
        l.write(str(light) + "\n")
    return f"Light {light} stored"

@server.get('/get_temperature')
def get_temperature():
    if not os.path.exists("temperature.txt"):
        return "No temperature data"
    with open("temperature.txt", "r") as t:
        return "<br>".join(t.readlines())

@server.get('/get_light')
def get_light():
    if not os.path.exists("light.txt"):
        return "No light data"
    with open("light.txt", "r") as l:
        return "<br>".join(l.readlines())

server.run(host='0.0.0.0', port=4000, debug=True)

