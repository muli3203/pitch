import os

class Config:
    '''
    General configuration parent class
    '''
    pass

    SECRET_KEY = os.environ.get('SECRET KEY')
    # Let's create the start.sh file i was saying itakuwa ya mwisho
    # It should rid us off exporting the environment variables all the time
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitcher'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SECRET_KEY = os.environ.get('SECRET KEY')
    # Let's create the start.sh file i was saying itakuwa ya mwisho
    # It should rid us off exporting the environment variables all the time
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitcher'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SECRET_KEY = os.environ.get('SECRET KEY')
    # Let's create the start.sh file i was saying itakuwa ya mwisho
    # It should rid us off exporting the environment variables all the time
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitcher'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}