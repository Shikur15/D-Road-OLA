from mainapp import db






class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)