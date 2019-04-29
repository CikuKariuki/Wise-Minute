import unittest
from app.models import User

class UserTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the User class
    '''
    def setUp(self):
        '''
        will run before every test
        '''
        self.new_user = user(1234,'Ciku','ciku@gmail.com','I love cats','list of my articles')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

if __name__ == '__main__':
    unittest.main()
        