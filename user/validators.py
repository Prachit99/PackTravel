from django.core.exceptions import ValidationError

def validate_email_domain(value):
    allowed_domain = 'ncsu.edu'
    domain = value.split('@')[-1]
    if domain != allowed_domain:
        raise ValidationError(f"Email must be from the {allowed_domain} domain.")