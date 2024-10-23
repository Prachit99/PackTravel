from .cloud_storage import CloudStorage
from .credentials import Credentials

class GoogleCloud:
    credentials: Credentials = None
    StorageService: CloudStorage = None
    
    def __init__(self, credentials_path: str = "credentials.json", bucket_path: str = 'ptravel-pfp'):
        self.credentials = Credentials(credentials_path)
        self.StorageService = CloudStorage(self.credentials, '')

    def upload_file(self, file, file_name: str = ""):
        return self.StorageService.__upload_file__(file, destination_blob_name=file_name)