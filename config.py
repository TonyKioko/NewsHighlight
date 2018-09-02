import os

class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'
    # ARTICLES_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    HEADLINES_URL ='https://newsapi.org/v2/top-headlines?language={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    # SECRET_KEY = os.environ.get('SECRET_KEY')

    # https://newsapi.org/v2/top-headlines?language=en&apiKey=3f7ad7ad6ae546a28feead545feea3c4
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2?sources={}&apiKey={}'
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/?sources={}&apiKey={}'
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?sources={}&apiKey={}'
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?language=en&category={}&sources={}&q={}&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}