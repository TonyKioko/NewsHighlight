class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'
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