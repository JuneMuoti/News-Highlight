class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'    
class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True



