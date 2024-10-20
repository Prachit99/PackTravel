from dotenv import load_dotenv
import os

class Secrets: 
    GoogleMapsAPIKey = ""
    MongoConnectionURL = ""
    def __init__(self):
        load_dotenv()
        self.MongoConnectionURL = os.getenv("MONGO_CONNECTION_URL")
        self.GoogleMapsAPIKey = os.getenv("GOOGLE_MAPS_API_KEY")

class URLConfig: 
    RoutesHostname=""
    def __init__(self):
        load_dotenv
        self.RoutesHostname = os.getenv("ROUTES_HOSTNAME")


