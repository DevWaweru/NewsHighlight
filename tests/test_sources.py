import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test case to test the behavior of the Sources class
    '''
    def setUp(self):
        '''
        Setup function that will run before every test
        '''
        self.new_source = Sources('mynews','My News','We have the latest updates','https://google.com','general','ke')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))