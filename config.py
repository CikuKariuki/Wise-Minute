import os

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class Config:
    '''
    general configuration parent class
    '''
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json' 
    SECRET_KEY =os.environ.get('hjh635dhru584/hf55')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanjiku:mySql003@localhost/blogger'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanjiku:mySql003@localhost/blog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanjiku:mySql003@localhost/blog_test'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
}