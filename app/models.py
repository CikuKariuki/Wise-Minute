class User:
    '''
    user class to define user objects
    '''
    def __init__(self,id):
        self.id =id

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

class Review:
    all_reviews = []

    def __init__(self,user_id,title,review):
        self.user_id = user_id
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
            if review.user_id == id:
                response.append(review)

        return response



