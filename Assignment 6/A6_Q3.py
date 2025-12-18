from flask import Flask

server = Flask(__name__)

@server.get('/')
def homepage():
    return "This is a home page"

@server.get('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Student Management System</h1></body></html>"




@server.post('/temperature/<float:temp>')
def post_temperature(temp):
    print(f"temp = {temp}")
    return f"{temp} is received"

@server.post('/light_intensity/<float:intensity>')
def post_light_intensity(intensity):
    print(f"light intensity = {intensity}")
    return f"{intensity} is received"



@server.get('/temperature/<float:temp>')
def get_temperature(temp):
    return f"<h2>Temperature = {temp}</h2>"

@server.get('/light_intensity/<float:intensity>')
def get_light_intensity(intensity):
    return f"<h2>Light Intensity = {intensity}</h2>"


server.run(host='0.0.0.0', port=4000, debug=True)
