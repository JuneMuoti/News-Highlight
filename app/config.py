class Config:
    NEWS_API_BASE_URL ='http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
 
    SOURCES_API_BASE_URL ='http://newsapi.org/v2/sources?language=en&category={}&apiKey={}'   
class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True



