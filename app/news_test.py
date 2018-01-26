import unittest
from.models import news
News = news.News

class NewsTest(unittest.TestCase):

    def setUp(self):
        self.new_news_article = News('bbc','ander','interesting news','we went and saw',url,urlToImage)
