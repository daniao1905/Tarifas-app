import json

def get_vehicle_tariffs():
    with open("vehicle_tariffs.json", "r", encoding="utf-8") as f:
        return json.load(f)
