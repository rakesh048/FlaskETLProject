
from restplus import API
from flask_restplus import fields



user_request = API.model('User Request', {
    'username': fields.String(description='Login username required!!'),
    'password': fields.String(description='Password for username!!'),
    })