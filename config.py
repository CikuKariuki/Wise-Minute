import os

class Config:
    '''
    general configuration parent class
    '''
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json' 
    SECRET_KEY =os.environ.get('hjh635dhru584/hf55')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}