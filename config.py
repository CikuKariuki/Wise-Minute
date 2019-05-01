import os

class Config:
    '''
    general configuration parent class
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanjiku:mySql003@localhost/pitcher'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanjiku:mySql003@localhost/pitch_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanjiku:mySql003@localhost/pitcher'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
    # 'test': TestConfig
}