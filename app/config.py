import os

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///assistant-speech.db'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig()
    else:
        return DevelopmentConfig()
