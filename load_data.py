import json

def get_vehicle_tariffs():
    with open("mk_tarifa_app_static/vehicle_tariffs.json", "r", encoding="utf-8") as f:
        return json.load(f)
