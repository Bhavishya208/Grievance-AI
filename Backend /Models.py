from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    description = db.Column(db.String(200))
    location = db.Column(db.String(100))
    status = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    complaints = db.relationship('Complaint', backref='user', lazy=True)
