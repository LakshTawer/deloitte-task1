from datetime import datetime

def convert_to_milliseconds(iso_time):
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

def transform_model_1(data):
    result = {}
    result["device_id"] = data["deviceID"]
    result["temperature"] = data["temperature"]
    result["humidity"] = data["humidity"]
    result["timestamp"] = data["timestamp"]
    return result

def transform_model_2(data):
    result = {}
    result["device_id"] = data["id"]
    result["temperature"] = data["temp"]
    result["humidity"] = data["humidity"]
    result["timestamp"] = convert_to_milliseconds(data["timestamp"])
    return result
