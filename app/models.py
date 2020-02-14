from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref='user',lazy='dynamic')

    def __repr__(self): 
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key =True)
    title = db.Column(db.String(255),nullable=False)
    post = db.Column(db.Text(),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    time = db.Column(db.DateTime,default = datetime.utcnow)
    category = db.Column(db.String(255),index=True,nullable=False)