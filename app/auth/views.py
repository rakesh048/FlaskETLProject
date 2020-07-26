from restplus import API, db
from flask import jsonify, request, abort
from flask_restplus import Resource,reqparse
from .models import User
from .serializers import registration_parser, login_parser

NS = API.namespace('auth', description='Authentication')


@NS.route('/login/')
class Login(Resource):
    """Used to for Login Controller"""

    @API.expect(login_parser, validate=True)
    def post(self):
        args = login_parser.parse_args()
        email = args.email
        password = args.password
        user = User.query.filter(User.email == email, User.password == password).first()
        if user:
            return {"data": str(user.username)+" Logged in successfully !!", "success": True}, 200
        else:
            return {"data": "User not found in database !!", "success": True}, 200


@NS.route('/signup/')
class Signup(Resource):
    """Used to for User Registration Controller"""

    @API.expect(registration_parser, validate=True)
    def post(self):
        args = registration_parser.parse_args()
        username = args.username
        password = args.password
        email = args.email

        if username is None or password is None:
            return {"data": "username and password required!"}, 200
        if User.query.filter_by(email=email).first() is not None:
            return {"data": "user exists!!"}, 200
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return {"data": "successfully register!!"}, 201
