from restplus import API,db
from flask import jsonify, request,abort
from flask_restplus import Resource
from .models import User
from .serializers import user_request


NS = API.namespace('auth', description='Authentication')

@NS.route('/login/')
class Login(Resource):
    """Used to for Login Controller"""
    def get(self):
        user = User.query.all()
        return jsonify({"data":str(user),"success":True})


@NS.route('/signup/')
class Signup(Resource):
	"""Used to for User Registration Controller"""
	@API.expect(user_request)
	def post(self):
		data = request.json
		username = data['username']
		password = data['password']
		if username is None or password is None:
		    return {"data":"username and password required!"}, 200
		if User.query.filter_by(username = username).first() is not None:
		    return {"data":"user exists!!"}, 200
		user = User(username = username)
		user.hash_password(password)
		db.session.add(user)
		db.session.commit()
		return {"data":"successfully register!!"}, 201
