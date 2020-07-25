import logging
from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

LOG = logging.getLogger(__name__)
API = Api(version='1.0', title='REST Endpoints', description='REST Endpoints')

app = Flask(__name__)
db = SQLAlchemy(app)