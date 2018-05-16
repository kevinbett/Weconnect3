from flask_sqlalchemy import SQLAlchemy
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from instance.config import Config
import datetime

db = SQLAlchemy()


class User(db.Model):
    """This class represents the users table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    businesses = db.relationship("Business", backref="owner")
    reviews = db.relationship("Review")


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, plaintext):
        self.password = generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return check_password_hash(self.password, plaintext)

    def encode_auth_token(self, user_id):

        try:
            payload = {

                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=30),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                Config.SECRET,
                algorithm="HS256"
            )
        except Exception as e:
            return e

    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, Config.SECRET)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



class Business(db.Model):


    """This Class represents Business Table"""

    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    location = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    reviews = db.relationship("Review")


    def __init__(self, name, type, location, category):
        self.name = name
        self.type = type
        self.location = location
        self.category = category

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Review(db.Model):


    """This class represents Reviews Table"""

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    business_id = db.Column(db.Integer, db.ForeignKey("businesses.id"))

    def __init__(self, feedback):
        self.feedback = feedback

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

