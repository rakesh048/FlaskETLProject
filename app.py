from app import app
app.run(host='0.0.0.0', port=8000, debug=True)

##### for db migrations ###
#flask db init
#flask db migrate -m "Initial migration."
#flask db upgrade -- apply migrations to database
