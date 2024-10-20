import json
from http import client

class Routes:
    hostname = ""
    api_key = ""
    def __init__(self, hostname: str, api_key = ""): 
        self.hostname = hostname
        self.api_key = api_key

    def __get_route_details__(self, slat: str, slong: str, dlat: str, dlong: str):
        conn = client.HTTPSConnection(self.hostname)
        payload = json.dumps({
            "origin": {
                "location": {
                "latLng": {
                    "latitude": slat,
                    "longitude": slong
                }
                }
            },
            "destination": {
                "location": {
                "latLng": {
                    "latitude": dlat,
                    "longitude": dlong
                }
                }
            },
            "routeModifiers": {
                "vehicleInfo": {
                "emissionType": "GASOLINE"
                }
            },
            "travelMode": "DRIVE",
            "routingPreference": "TRAFFIC_AWARE_OPTIMAL",
            "extraComputations": [
                "FUEL_CONSUMPTION"
            ]
        })

        headers = {
            'content-type': 'application/json',
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': self.api_key,
            'X-Goog-FieldMask': 'routes.distanceMeters,routes.duration,routes.routeLabels,routes.routeToken,routes.travelAdvisory.fuelConsumptionMicroliters'
        }

        conn.request("POST", "/directions/v2:computeRoutes", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        return {
            "distance": int(data.get("routes", [])[0].get("distanceMeters", 0))/1000,
            "fuel": int(data.get("routes", [])[0].get("travelAdvisory", {}).get("fuelConsumptionMicroliters", 0))/(1000*1000),
        }

