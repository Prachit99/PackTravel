from django.core.exceptions import ValidationError
from utils import get_client

userDB = None

def intializeDB():
    global userDB
    if(userDB == None):
        client = get_client()
        db = client.SEProject
        userDB = db.userData

def validate_email_domain(value):
    allowed_domain = 'ncsu.edu'
    domain = value.split('@')[-1]
    if domain != allowed_domain:
        raise ValidationError(f"Email must be from the {allowed_domain} domain.")
    
def validate_unique_unity_id(value):
    intializeDB()
    unity_user = userDB.find_one({"unityid": value})
    if(unity_user):
        raise ValidationError("Unity ID must be unique")