from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime

db = SQLAlchemy()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Quote:
    '''
    quote class to define quote object
    '''
    def __init__(self,id,quote,author):
        self.id = id
        self.quote = quote
        self.author = author

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    occupation_id = db.Column(db.Integer,db.ForeignKey('occupation.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError("You can't read the password attribute")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User{self.username}'

class Writer:
    '''
    class to define all writer objects
    '''
    def __init__(self,id,username,email,bio,articles):
        self.id = id
        self.username = username
        self.email = email
        self.bio = bio 
        self.articles = articles

class Occupation(db.Model):
    __tablename__='occupation'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    user = db.relationship('User',backref = 'occupation',lazy="dynamic")
    
    def __repr__(self):
        return f'Occupation{self.name}'


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

   def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews
        
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []


        for review in cls.all_reviews:
            if review.article_id == id:
                response.append(review)

        return response



