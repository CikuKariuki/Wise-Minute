import unittest
from app.models import Writer

class WriterTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Writer class
    '''
    def setUp(self):
        '''
        will run before every test
        '''
        self.new_writer = Writer(1234,'Ciku','ciku@gmail.com','I love cats','list of my articles')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_writer,Writer))

if __name__ == '__main__':
    unittest.main()
        