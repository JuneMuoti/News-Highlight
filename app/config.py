class Config:
    
NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
 
SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey={}'   
class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True



