from flask import Flask, request, jsonify
from datetime import datetime
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

THUNDER_THRESHOLD = 30  # 🌩️ temperature limit

@server.get('/')
def home():
    return jsonify({"message": "Smart Home Thunder Server"})

# --------------------------------------------------
# CREATE / UPDATE SENSOR DATA (POST)
# --------------------------------------------------
@server.route('/smart_home', methods=['POST'])
def create_update():
    data = request.get_json()

    device_id = data.get("device_id")
    light = data.get("light_status")
    fan = data.get("fan_status")
    temp = data.get("temperature")

    if None in (device_id, light, fan, temp):
        return jsonify({"error": "Missing fields"}), 400

    query = f"""
    INSERT INTO smart_home (device_id, light_status, fan_status, temperature, date_time)
    VALUES ({device_id}, '{light}', '{fan}', {temp}, '{datetime.now()}')
    ON DUPLICATE KEY UPDATE
        light_status='{light}',
        fan_status='{fan}',
        temperature={temp},
        date_time='{datetime.now()}';
    """
    executeQuery(query)

    return jsonify({"message": "Data stored successfully"})

# --------------------------------------------------
# READ STATUS (GET)
# --------------------------------------------------
@server.route('/smart_home/status', methods=['GET'])
def status():
    query = """
    SELECT light_status, fan_status, temperature
    FROM smart_home
    ORDER BY date_time DESC
    LIMIT 1;
    """
    data = executeSelectQuery(query)

    if not data:
        return jsonify({"message": "No data found"}), 404

    light, fan, temp = data[0]

    return jsonify({
        "light_status": light,
        "fan_status": fan,
        "temperature": temp,
        "thunder_alert": temp > THUNDER_THRESHOLD
    })

# --------------------------------------------------
# UPDATE DEVICE STATUS ONLY (PUT)
# --------------------------------------------------
@server.route('/smart_home', methods=['PUT'])
def update_status():
    data = request.get_json()

    device_id = data.get("device_id")
    light = data.get("light_status")
    fan = data.get("fan_status")

    if device_id is None:
        return jsonify({"error": "device_id required"}), 400

    query = f"""
    UPDATE smart_home
    SET light_status='{light}', fan_status='{fan}'
    WHERE device_id={device_id};
    """
    executeQuery(query)

    return jsonify({"message": "Device updated"})

# --------------------------------------------------
# DELETE DEVICE (DELETE)
# --------------------------------------------------
@server.route('/smart_home', methods=['DELETE'])
def delete_device():
    data = request.get_json()
    device_id = data.get("device_id")

    if device_id is None:
        return jsonify({"error": "device_id required"}), 400

    query = f"DELETE FROM smart_home WHERE device_id={device_id};"
    executeQuery(query)

    return jsonify({"message": "Device deleted"})

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
