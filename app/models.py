from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))

    pitches = db.relationship("Pitch", backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f"User {self.username}"


class Pitch(db.Model):
    """
    Pitch class to define Pitch Objects
    """

    __tablename__ = "pitches"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    comments = db.relationship("Comment", backref="pitch", lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_pitches(cls):
        """
        Function that queries the database and returns all the pitches
        """
        pitches = Pitch.query.all()

        return pitches

    @classmethod
    def get_pitches_by_category(cls, category):
        """
        Function that queries the database and returns pitches based on the
        category passed to it
        """
        return Pitch.query.filter_by(category=category)


class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id).all()

        return comments
