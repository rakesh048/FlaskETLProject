
from restplus import API
from app.auth.views import NS as AUTH_NS
from restplus import db,app
from settings import test_db as DB_URL
from app.auth.models import User
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy_utils import database_exists,drop_database

# Configurations
app.config.from_object('settings.DevConfig')
db.init_app(app)
migrate = Migrate(app, db)
API.init_app(app)

#add namespaces
API.add_namespace(AUTH_NS)
#drop_database(DB_URL)