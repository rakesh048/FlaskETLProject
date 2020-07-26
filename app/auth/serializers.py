from restplus import API
from flask_restplus import fields, reqparse
import re

EMAIL_REGEX = re.compile(r"\S+@\S+\.\S+")


def email_validation(value):
    if not EMAIL_REGEX.match(value):
        raise ValueError('Invalid email format ex: abc@domain.com')
    return value


""" user registration """
registration_parser = reqparse.RequestParser()
email_validation.__schema__ = {"type": "string", "format": "email_validation"}
registration_parser.add_argument('username', required=True)
registration_parser.add_argument('password', required=True)
registration_parser.add_argument('email', type=email_validation, required=True)

""" user login """
login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=email_validation, required=True)
login_parser.add_argument('password', required=True)