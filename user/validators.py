from django.core.exceptions import ValidationError
from utils import get_client
import re

userDB = None

def intializeDB():
    global userDB
    if(userDB == None):
        client = get_client()
        db = client.SEProject
        userDB = db.userData

def validate_email_domain(value):
    pattern = re.compile("^[a-zA-Z0-9]+$")
    allowed_domain = 'ncsu.edu'
    email_parts = value.split('@')
    domain = email_parts[-1]
    if len(email_parts) != 2:
        raise ValidationError(f"Invalid email")
    if not pattern.match(email_parts[0]):
        raise ValidationError(f"Invalid email")
    if domain != allowed_domain:
        raise ValidationError(f"Email must be from the {allowed_domain} domain.")
    
def validate_unique_unity_id(value):
    intializeDB()
    unity_user = userDB.find_one({"unityid": value})
    if(unity_user):
        raise ValidationError("Unity ID must be unique")