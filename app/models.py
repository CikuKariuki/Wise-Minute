from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime
from flask_login import UserMixin
from app import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String()) 
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitches',backref = 'author',lazy = 'dynamic') 

    @property
    def password(self):
        raise AttributeError("You can't read the password attribute")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'

class Pitches(db.Model):
    __tablename__='pitches'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(2550))
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Reviews', backref = 'author', lazy = True) 

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'Pitches{self.name}'


class Reviews(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    review = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,  db.ForeignKey("pitches.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Review{self.review}'


    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(pitches_id=id).all()
        return reviews
        
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []


        for review in cls.all_reviews:
            if review.pitch_id == id:
                response.append(review)

        return response
