from flask import Flask,request
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery
server=Flask(__name__)

@server.get('/')
def gomepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/soil_moisture')
def create_soil_moisture():
    sensor_id=request.form.get('sensor_id')
    moisture_level=request.form.get('moisture_level')
    date=request.form.get('date')
    time=request.form.get('time')
    query=f"insert into soil_moisture values({sensor_id},'{moisture_level}','{date}','{time}');"
    executeQuery(query=query)
    return " soil_moisture is added successfully "

@server.get('/soil_moisture')
def retrieve_soil_moisture():
    query ="select * from soil_moisture ;"
    data=executeSelectQuery(query=query)
    return f"soil_moisture :{data}"


@server.put('/soil_moisture')
def update_soil_moisture():
    sensor_id=request.form.get('sensor_id')
    moisture_level=request.form.get('moisture_level')
    query=f"update soil_moisture SET moisture_level='{moisture_level}' where sensor_id='{sensor_id}';"
    executeQuery(query=query)  
    return "soil_moisture is updated successfully"

@server.delete('/soil_moisture')
def delete_soil_moisture():
    sensor_id=request.form.get('sensor_id')
    query=f"delete from soil_moisture where sensor_id='{sensor_id}';"
    executeQuery(query=query)  
    return "soil_moisture is deleted successfully" 

@server.get('/soil_moisture/below_moisture_level')
def below_moisture_level():
    moisture_level = request.args.get('moisture_level')
    query = f"""select * from soil_moisture
    where moisture_level < {moisture_level};
    """
    data = executeSelectQuery(query)
    return f"Below moisture_level readings: {data}"

if __name__ =='_main_':
   server.run(host='0.0.0.0',port=4000,debug=True)