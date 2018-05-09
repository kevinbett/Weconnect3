from api import db

class User(db.Model):
    """This class represents the users table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    businesses = db.relationship("Business")
    reviews = db.relationship("Review")


    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        db.session.add(self)
        db.session.commit()

class Business(db.Model):


    """This Class represents Business Table"""

    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    reviews = db.relationship("Review")


    def __init__(self, name, type):
        self.name = name
        self.type = type

    def save(self):
        db.session.add(self)
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

