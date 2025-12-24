from flask import Flask, request

app = Flask(__name__)

@app.route('/sensor', methods=['POST'])
def receive_data():
    temp = request.form.get('temperature')
    hum = request.form.get('humidity')
    return f"Temperature: {temp}, Humidity: {hum}"

app.run(host='0.0.0.0', port=5000)
