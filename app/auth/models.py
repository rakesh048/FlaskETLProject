from restplus import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True, nullable=False, server_default='user')
    password = db.Column(db.String(128), nullable=False, server_default='password')
    email = db.Column(db.String(120), nullable=False, server_default='abc@gmail.com')
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<User %r>' % self.email




