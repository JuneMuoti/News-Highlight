import unittest
from .models import news_article
Article=news_article.Article

class NewsArticleTest(unittest.TestCase):

    def setUp(self):
        self.new_news_article = Article('bbc','andy','news is news','now this happened','http://www.foxnews.com/','//a57.foxnews.com/images','1-3-2018')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article,Article))

if __name__ == '__main__':
    unittest.main()