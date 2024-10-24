from .routes import Routes

class MapsService:
    routes_service: Routes = None
    def __init__(self, routes_hostname: str, api_key: str):
        self.routes_service = Routes(routes_hostname, api_key)

    def get_route_details(self, slat: str, slong: str, dlat: str, dlong: str):
        return self.routes_service.__get_route_details__(slat, slong, dlat, dlong)