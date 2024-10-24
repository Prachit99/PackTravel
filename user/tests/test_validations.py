from ..validators import validate_email_domain
from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

class UserValidationTests(SimpleTestCase):
    def test_valid_email(self):
        email = "student@ncsu.edu"
        try:
            validate_email_domain(email)
        except ValidationError:
            self.fail("Raised validation error on a valid email")

    def test_invalid_email_domain(self):
        email = "asd@gmail.com"
        with self.assertRaises(ValidationError):
            validate_email_domain(email)

    def test_invalid_email_address(self):
        email = "@ncsu.edu"
        with self.assertRaises(ValidationError):
            validate_email_domain(email)

    def test_invalid_email_address_no_domain(self):
        email = "bkbhayan"
        with self.assertRaises(ValidationError):
            validate_email_domain(email)

    def test_invalid_email_address_no_domain_2(self):
        email = "bkbhayan@"
        with self.assertRaises(ValidationError):
            validate_email_domain(email)