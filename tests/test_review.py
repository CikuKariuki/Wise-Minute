import unittest
from app.models import Review,User,Pitches
from app import db

class ReviewTest(unittest.TestCase):
        
        def setUp(self):
                self.user_Wanjiku = User(id = 1,username = 'Wanjiku',password = 'potato', email = 'sheekokariuki@gmail.com',bio="Time is abstract")
                self.new_review = Review(pitch_id=12,pitch_title='Review for pitches',pitch_review='This is the best story I have ever read ',user = self.user_Wanjiku )

        def tearDown(self):
                Review.query.delete()
                User.query.delete()

        def test_check_instance_variables(self):
                self.assertEquals(self.new_review.pitch_id,12)
                self.assertEquals(self.new_review.pitch_review,'This is the best story I have ever read')
                self.assertEquals(self.new_review.user,self.user_Wanjiku)

        def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)

        def test_get_review_by_id(self):

                self.new_review.save_review()
                got_reviews = Review.get_reviews(12)
                self.assertTrue(len(got_reviews) == 1)    