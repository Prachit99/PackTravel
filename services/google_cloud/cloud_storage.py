from .credentials import Credentials
from google.cloud import storage

class CloudStorage:
    credentials: Credentials = None
    PfpBucket: str = ""

    def __init__(self, credentials: Credentials, pfp_bucket: str = ""):
        self.credentials = credentials
        self.PfpBucket = pfp_bucket

    def __upload_file__(self, file, destination_blob_name: str) -> str:
        client = storage.Client(credentials=self.credentials.credentials)
        bucket = client.bucket('ptravel-pfp')
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_file(file)
        return blob.public_url  
