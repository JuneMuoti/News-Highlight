import unittest
from .models import sources
Source=sources.Source

class ArticleTest(unittest.TestCase):

    def setUp(self):
        self.new_source = Source('bbc','bbcnews','bbc news is news','http://bbc.com','all','en','uk')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()