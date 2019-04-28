from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Quote:
    '''
    quote class to define quote object
    '''
    def __init__(self,id,quote,author):
        self.id = id
        self.quote = quote
        self.author = author

class User:
    '''
    user class to define user objects
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    occupation_id = db.Column(db.Integer,db.ForeignKey('occupation.id'))

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
    users = db.relationship('User',backref = 'occupation',lazy="dynamic")
    
    def __repr__(self):
        return f'User{self.name}'


class Review:
    all_reviews = []

    def __init__(self,article_id,title,review):
        self.article_id = article_id
        self.title = title
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

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



