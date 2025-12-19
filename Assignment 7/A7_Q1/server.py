from flask import Flask, request
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server=Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is a homepage</h1></body></html>"

@server.post('/sensor')
def create_sensor_readings():
    id=request.form.get('id')
    temperature=request.form.get('temperature')
    humidity=request.form.get('humidity')
    timestamp=request.form.get('timestamp')
    query=f"insert into sensor_readings values({id},'{temperature}','{humidity}','{timestamp}');"    
    executeQuery(query=query)
    return "sensor readings is added successfully"

@server.get('/sensor')
def retrieve_sensor_readings():
    query="select * from sensor_readings;"
    data=executeSelectQuery(query=query)
    return f"sensor_readings: {data}"

@server.put('/sensor')
def update_sensor_readings():
    id=request.form.get('id')
    temperature=request.form.get('temperature')
    query=f"update sensor_readings SET temperature= {temperature} where id={id};"
    executeQuery(query=query)
    return "temperature is updated successfully"

@server.delete('/sensor')
def delete_sensor_readings():
    id=request.form.get('id')
    query=f"delete from sensor_readings where id= {id} ;"
    executeQuery(query=query)
    return "sensor_readings is deleted successfully"

@server.post('/sensor_readings/below_threshold')
def below_threshold_post():
    threshold = request.form.get('threshold')

    if threshold is None:
        return "Threshold value is required"

    query = f"SELECT * FROM sensor_readings WHERE temperature < {threshold};"
    data = executeSelectQuery(query=query)

    return f"Sensor readings below threshold {threshold}: {data}"

@server.get('/sensor_readings/below_threshold')
def below_threshold_get():
    threshold = request.args.get('threshold')

    if threshold is None:
        return "Threshold value is required"

    query = f"SELECT * FROM sensor_readings WHERE temperature < {threshold};"
    data = executeSelectQuery(query=query)

    return f"Sensor readings below threshold {threshold}: {data}"

    


if __name__=='__main__':
    server.run(host='0.0.0.0',port=4000,debug=True)